from PyQt5.QtWidgets import *
import sys

app = QApplication(sys.argv)

window = QWidget()
window.resize(300, 300)
btn = QPushButton(window)
btn.setText('按钮')

# 设置按钮为不可用
btn.setEnabled(False)
print(btn.isEnabled())  # 获取当前按钮是否可用的状态，并打印出来

window.show()

sys.exit(app.exec_())
