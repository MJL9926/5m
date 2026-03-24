import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QTextEdit, QGridLayout
from PyQt5.QtCore import Qt, QTimer
import threading
import time

class BTC5MinApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('BTC 5分钟预测')
        self.setGeometry(100, 100, 400, 850)  # 手机屏幕尺寸
        
        # 创建中央部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # 主布局
        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(10)
        main_layout.setContentsMargins(10, 10, 10, 10)
        
        # 顶部状态栏
        top_layout = QHBoxLayout()
        self.price_label = QLabel('当前价格: $ --')
        self.price_label.setStyleSheet('font-size: 16px; font-weight: bold;')
        self.pred_label = QLabel('预测: 等待预测...')
        self.pred_label.setStyleSheet('font-size: 14px; font-weight: bold;')
        top_layout.addWidget(self.price_label)
        top_layout.addWidget(self.pred_label)
        main_layout.addLayout(top_layout)
        
        # 控制面板
        control_layout = QHBoxLayout()
        self.start_btn = QPushButton('开始预测')
        self.start_btn.setStyleSheet('background-color: #4CAF50; color: white; font-size: 12px;')
        self.stop_btn = QPushButton('停止')
        self.stop_btn.setStyleSheet('background-color: #F44336; color: white; font-size: 12px;')
        control_layout.addWidget(self.start_btn)
        control_layout.addWidget(self.stop_btn)
        main_layout.addLayout(control_layout)
        
        # 自动交易面板
        auto_trade_widget = QWidget()
        auto_trade_layout = QVBoxLayout(auto_trade_widget)
        auto_trade_title = QLabel('自动交易')
        auto_trade_title.setStyleSheet('font-size: 12px; font-weight: bold;')
        auto_trade_layout.addWidget(auto_trade_title)
        
        # 自动交易按钮网格
        auto_trade_buttons = QGridLayout()
        auto_trade_buttons.setSpacing(5)
        
        # 第一行
        self.auto_trade_btn = QPushButton('自动交易: 关闭')
        self.auto_trade_btn.setStyleSheet('background-color: #F44336; color: white; font-size: 10px;')
        auto_trade_buttons.addWidget(self.auto_trade_btn, 0, 0, 1, 2)
        
        # 第二行
        self.amount_btn = QPushButton('设置金额: 10000')
        self.amount_btn.setStyleSheet('background-color: #2196F3; color: white; font-size: 10px;')
        auto_trade_buttons.addWidget(self.amount_btn, 1, 0, 1, 2)
        
        # 第三行
        self.amount_coord_btn = QPushButton('设置金额坐标')
        self.amount_coord_btn.setStyleSheet('background-color: #00BCD4; color: white; font-size: 10px;')
        self.up_coord_btn = QPushButton('设置买涨坐标')
        self.up_coord_btn.setStyleSheet('background-color: #00BCD4; color: white; font-size: 10px;')
        auto_trade_buttons.addWidget(self.amount_coord_btn, 2, 0)
        auto_trade_buttons.addWidget(self.up_coord_btn, 2, 1)
        
        # 第四行
        self.down_coord_btn = QPushButton('设置买跌坐标')
        self.down_coord_btn.setStyleSheet('background-color: #00BCD4; color: white; font-size: 10px;')
        self.confirm_coord_btn = QPushButton('设置确认坐标')
        self.confirm_coord_btn.setStyleSheet('background-color: #00BCD4; color: white; font-size: 10px;')
        auto_trade_buttons.addWidget(self.down_coord_btn, 3, 0)
        auto_trade_buttons.addWidget(self.confirm_coord_btn, 3, 1)
        
        # 第五行
        self.save_coord_btn = QPushButton('保存坐标')
        self.save_coord_btn.setStyleSheet('background-color: #00BCD4; color: white; font-size: 10px;')
        self.test_amount_btn = QPushButton('测试金额')
        self.test_amount_btn.setStyleSheet('background-color: #FFEB3B; color: black; font-size: 10px;')
        auto_trade_buttons.addWidget(self.save_coord_btn, 4, 0)
        auto_trade_buttons.addWidget(self.test_amount_btn, 4, 1)
        
        # 第六行
        self.test_up_btn = QPushButton('测试买涨')
        self.test_up_btn.setStyleSheet('background-color: #FFEB3B; color: black; font-size: 10px;')
        self.test_down_btn = QPushButton('测试买跌')
        self.test_down_btn.setStyleSheet('background-color: #FFEB3B; color: black; font-size: 10px;')
        auto_trade_buttons.addWidget(self.test_up_btn, 5, 0)
        auto_trade_buttons.addWidget(self.test_down_btn, 5, 1)
        
        auto_trade_layout.addLayout(auto_trade_buttons)
        main_layout.addWidget(auto_trade_widget)
        
        # 日志输出
        log_widget = QWidget()
        log_layout = QVBoxLayout(log_widget)
        log_title = QLabel('日志输出')
        log_title.setStyleSheet('font-size: 12px; font-weight: bold;')
        log_layout.addWidget(log_title)
        
        self.log_text = QTextEdit()
        self.log_text.setReadOnly(True)
        self.log_text.setStyleSheet('font-size: 10px;')
        log_layout.addWidget(self.log_text)
        main_layout.addWidget(log_widget)
        
        # 状态栏
        status_layout = QHBoxLayout()
        self.status_label = QLabel('状态: 就绪')
        self.status_label.setStyleSheet('font-size: 12px;')
        status_layout.addWidget(self.status_label)
        main_layout.addLayout(status_layout)
        
        # 连接信号
        self.start_btn.clicked.connect(self.start_prediction)
        self.stop_btn.clicked.connect(self.stop_prediction)
        
        # 初始化状态
        self.is_running = False
        self.log_text.append('应用已启动，等待开始预测...')
    
    def start_prediction(self):
        self.is_running = True
        self.start_btn.setEnabled(False)
        self.stop_btn.setEnabled(True)
        self.status_label.setText('状态: 运行中')
        self.log_text.append('开始预测...')
        
        # 启动预测线程
        threading.Thread(target=self.prediction_loop, daemon=True).start()
    
    def stop_prediction(self):
        self.is_running = False
        self.start_btn.setEnabled(True)
        self.stop_btn.setEnabled(False)
        self.status_label.setText('状态: 就绪')
        self.log_text.append('停止预测...')
    
    def prediction_loop(self):
        while self.is_running:
            # 模拟预测过程
            time.sleep(5)
            # 在主线程中更新UI
            self.update_prediction()
    
    def update_prediction(self):
        # 模拟价格和预测
        import random
        price = 40000 + random.randint(0, 1000)
        prediction = '上涨' if random.random() > 0.5 else '下跌'
        
        self.price_label.setText(f'当前价格: ${price}')
        self.pred_label.setText(f'预测: {prediction}')
        self.log_text.append(f'价格: ${price}, 预测: {prediction}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BTC5MinApp()
    window.show()
    sys.exit(app.exec_())
