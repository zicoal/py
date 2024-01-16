import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QDesktopWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer, Qt
import  random

class Countdown(QWidget):
    result = 0
    caclation_time_left =5
    previous_number = -1
    all_numbers=[]
    def __init__(self):
        super().__init__()

        self.setWindowTitle('智多星V1.0')
        self.setWindowIcon(self.style().standardIcon(1))
        self.resize(self.width(), self.height())  # 默认大小
#        self.move((self,self.width() - self.width()) / 2, (self.height() - self.height()) / 2)
        # 窗口居中显示
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        #self.setFixedSize(500,500)

        # 垂直布局
        layout = QVBoxLayout()

        # 显示文字标签
        self.label = QLabel('欢迎Lucie小朋友\n你准备好了吗?', self)
        font_size = screen.width() // 20  # 字体大小设置为相对于屏幕宽度的比例
        font = QFont('Microsoft YaHei', font_size, QFont.Bold)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)  # 居中对齐
        layout.addWidget(self.label)

#        label = QLabel('最大和:')
#        layout.addWidget(label)

        # 水平布局
        h_layout = QHBoxLayout()

        # 开始按钮
        self.start_button = QPushButton('开始', self)
        self.start_button.clicked.connect(self.start_timer)
        h_layout.addWidget(self.start_button)

        # 重置按钮
        self.reset_button = QPushButton('重置', self)
        self.reset_button.clicked.connect(self.reset_timer)
        h_layout.addWidget(self.reset_button)

        # 重置按钮
        self.answer_button = QPushButton('答案', self)
        self.answer_button.clicked.connect(self.ask_answer)
        h_layout.addWidget(self.answer_button)

        layout.addLayout(h_layout)

        self.setLayout(layout)

        # 倒计时时间（秒）
        self.time_total = 3
        self.time_left = self.time_total

        # 倒计时器
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_timer)


    def ask_answer(self):
        texts=""
        for i in range(len(self.all_numbers)):
            texts = texts + str(self.all_numbers[i])
            if i !=len(self.all_numbers)-1:
                texts += "+"

        self.label.setText(f"正确答案是：\n{texts}={self.result}\n你答对了吗？")

    def start_timer(self):
        self.start_button.setEnabled(False)
        self.label.setText('欢迎Lucie小朋友\n你准备好了吗?')
        self.time_left = self.time_total + 1  # 显示“答辩开始”
        self.timer.start()

    def reset_timer(self):
        screen_width = QDesktopWidget().screenGeometry().width()
        font_size = screen_width // 20
        self.start_button.setEnabled(True)
        self.label.setText('欢迎Lucie小朋友\n你准备好了吗?')
        self.time_left = self.time_total
        self.all_numbers=[]
        self.caclation_time_left =5
        self.previous_number =-1
        self.result =0
        self.timer.stop()

    def update_timer(self):
        self.time_left -= 1

        # 获取屏幕的宽度
        screen_width = QDesktopWidget().screenGeometry().width()

        # 动态调整字体大小
        font_size = screen_width // 10
        font = QFont('Microsoft YaHei', font_size, QFont.Bold)
        self.label.setFont(font)

        # 更新时间标签
        minutes = self.time_left // 60
        seconds = self.time_left
#        self.label.setText(f'{minutes:02d}:{seconds:02d}')
        if (self.time_left > 0):
            self.label.setText(f'{seconds:01d}')
        elif (self.time_left == 0):
            self.label.setText('GO!')

        if self.time_left < 0:  # 倒计时结束，显示“答辩结束”
            self.label.setStyleSheet('')
            #self.label.setText('答题结束')
 #           self.timer.stop()
#            self.start_button.setEnabled(True)

            #self.caclation_time_left =5
            self.update_calculation_timer()
            #self.timer.timeout.connect(self.update_calculation_timer)


    def update_calculation_timer(self):
        self.caclation_time_left -= 1
        if (self.caclation_time_left < 0):
            screen_width = QDesktopWidget().screenGeometry().width()
            # 动态调整字体大小
            font_size = screen_width // 20
            font = QFont('Microsoft YaHei', font_size, QFont.Bold)
            self.label.setFont(font)

            self.label.setText('答题结束了哦^-^')
            self.label.setText(f"Lucie,你知道答案是多少？")
#            self.label.setText(f"Lucie，：{self.result}")
            self.start_button.setEnabled(True)
            self.timer.stop()
        else:
            number = random.randint(1, 5)
            if (number == self.previous_number):
                number = random.randint(1, 5)
            self.label.setText(str(number))
            self.all_numbers.append(number)
            self.result += number
            self.previous_number = number
            #print(number)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    countdown = Countdown()
    countdown.showMaximized()  # 全屏显示
    sys.exit(app.exec_())
