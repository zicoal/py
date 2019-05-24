import numpy as np
import tensorflow as tf
import os
import sys
import time

LEARNING_RATE_BASE = 0.0001
LEARNING_RATE_DECAY = 0.99
BATCH_SIZE = 32
STEPS = 30000


class PreSize:
    """
    用于预测的类
    """
    def __init__(self, data_type, data_file, feature_index, label_index):
        """
        进行一些初始化的操作
        :param data_type: 是算微博还是推特的数据
        :param data_file: 决定是算那个文件，Preiction_Data_Updata_MS_{5,6,7~10}.txt
        :param feature_index: 使用哪个/些特征，特征的下标
        :param label_index: 预测哪个size
        """
        self.__data_type = data_type
        self.__top_path = "./data/Compare_Data/" + self.__data_type + "/Size_Prediction"
        self.__file_name = data_file
        self.data_path = self.__top_path + "/" + self.__file_name
        self.__features_index = list(map(int, feature_index.split()))
        self.__label_index = int(label_index)
        self.__feature_size = len(self.__features_index)
        self.__map = {7: "1hour", 8: "2hour", 9: "12hour", 10: "1day", 11: "2day", 12: "10day", 13: "final"}

    def load_data(self):
        """
        加载数据，并划分训练集和测试集
        :return:
        """
        data = np.loadtxt(self.data_path, dtype=int)
        np.random.shuffle(data)
        print(self.__features_index)
        x = data[:, self.__features_index]
        y = data[:, self.__label_index]
        data_size = data.shape[0]

        test_set_size = int(data_size * 0.1)

        x_train, x_test = x[: -test_set_size], x[-test_set_size:]
        y_train, y_test = np.array(map(int, y[: -test_set_size])), np.array(map(int, y[-test_set_size:]))

        # def y_dist():
        #     result = Counter(y_train)
        #     norm = len(y_train)
        #     y_distribution = np.array([result[y] / norm for y in y_train])
        #     y_distribution = 1. / y_distribution
        #     y_distribution = y_distribution / np.sum(y_distribution)
        #     return y_distribution
        # y_prop = y_dist()

        return x_train, y_train.reshape(-1, 1), x_test, y_test.reshape(-1, 1)

    def train(self, x_train, y_train, x_test, y_test):
        """
        搭建网络进行train
        :param x_train:
        :param y_train:
        :param x_test:
        :param y_test:
        :return:
        """
        x_pl = tf.placeholder(dtype=tf.float32, shape=[None, self.__feature_size], name="X-input")
        y_pl = tf.placeholder(dtype=tf.float32, shape=[None, 1], name="Y-input")
        train_examples_n = x_train.shape[0]

        weight1 = self.__get_weight([self.__feature_size, 32], None)
        bias1 = self.__get_bias([1, 32])
        a1 = tf.nn.tanh(tf.matmul(x_pl, weight1) + bias1)
        weight2 = self.__get_weight([32, 64], None)
        bias2 = self.__get_bias([1, 64])
        a2 = tf.nn.relu(tf.matmul(a1, weight2) + bias2)
        weight3 = self.__get_weight([64, 128], None)
        bias3 = self.__get_bias([1, 128])
        a3 = tf.nn.tanh(tf.matmul(a2, weight3) + bias3)
        weight4 = self.__get_weight([128, 32], None)
        bias4 = self.__get_bias([1, 32])
        a4 = tf.nn.relu(tf.matmul(a3, weight4) + bias4)
        weight5 = self.__get_weight([32, 1], None)
        bias5 = self.__get_bias([1, 1])
        a = tf.matmul(a4, weight5) + bias5

        global_step = tf.Variable(0, trainable=False)

        loss_cem = tf.reduce_mean(tf.div(tf.abs(a - y_pl), y_pl))

        learning_rate = tf.train.exponential_decay(LEARNING_RATE_BASE,
                                                   global_step,
                                                   train_examples_n / BATCH_SIZE,
                                                   LEARNING_RATE_DECAY,
                                                   staircase=True)

        train_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss_cem, global_step)

        with tf.Session() as sess:
            init = tf.global_variables_initializer()
            sess.run(init)

            for i in range(STEPS):
                start = (i * BATCH_SIZE) % x_train.shape[0]
                end = min(x_train.shape[0], start + BATCH_SIZE)
                xs, ys = x_train[start: end], y_train[start: end]
                # xs, ys = self.__choice_feed(X_train, Y_train, y_p, BATCH_SIZE, train_examples_n)
                _, global_step_value, loss_value = sess.run([train_step, global_step, loss_cem],
                                                            feed_dict={x_pl: xs, y_pl: ys})
                if i % 10000 == 0:
                    _, loss_test = sess.run([train_step, loss_cem], feed_dict={x_pl: x_test, y_pl: y_test})
                    print("After %5d steps, the loss-train is %f, the loss-test is %f."
                          % (global_step_value, loss_value, loss_test))

            prediction = sess.run(a, feed_dict={x_pl: x_test, y_pl: y_test})

            print("./result/" + self.__data_type + "/size/" + self.__file_name.split(".")[0])
            if not os.path.exists("./result/" + self.__data_type + "/size/" + self.__file_name.split(".")[0]):
                os.makedirs("./result/" + self.__data_type + "/size/" + self.__file_name.split(".")[0])

            fe = [str(x) for x in self.__features_index]
            with open("./result/" + self.__data_type + "/size/" + self.__file_name.split(".")[0] + "/f" +
                      "f".join(fe) + "-" + self.__map[self.__label_index] + "-" + str(int(time.time())), "w") as f_out:
                for pre, size in zip(prediction, y_test):
                    f_out.write(str(pre[0]) + "\t" + str(size[0]) + "\n")

    @staticmethod
    def __get_weight(shape, regularize):
        """
        得到每一层的weight
        :param shape:
        :param regularize:
        :return:
        """
        w = tf.Variable(tf.truncated_normal(shape=shape, stddev=0.1))
        if regularize is not None:
            tf.add_to_collection("losses", tf.contrib.layers.l2_regularizer(regularize)(w))
        return w

    @staticmethod
    def __get_bias(shape):
        """
        得到每一层的bias
        :param shape:
        :return:
        """
        return tf.Variable(tf.zeros(shape))


class Run:
    """
    开放接口给shell脚本，方便并行计算各个文件
    """
    def __init__(self):
        """
        设置运行参数
        """
        self.data_type = sys.argv[1]
        self.file_name = sys.argv[2]
        self.x_index = sys.argv[3]
        self.y_index = sys.argv[4]

    def start_run(self):
        """
        调用PreSize对象进行计算
        :return:
        """
        print("info")
        print ("data type: ", self.data_type, ". file name: ", self.file_name, ", x_index: ", self.x_index, ". y_index: ", self.y_index)
        ps = PreSize(self.data_type, self.file_name, self.x_index, self.y_index)
        x_train, y_train, x_test, y_test = ps.load_data()
        for i in range(10):
            ps.train(x_train, y_train, x_test, y_test)


if __name__ == "__main__":
    # ps = PreSize(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    # print "info:"
    # print "data source: ", sys.argv[1], "file name: ", sys.argv[2], "x and y: ", sys.argv[3], sys.argv[4]
    # X_train, Y_train, X_test, Y_test = ps.load_data()
    # ps.train(X_train, Y_train, X_test, Y_test)
    run = Run()
    run.start_run()
