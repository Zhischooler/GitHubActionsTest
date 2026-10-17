from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QHBoxLayout,
    QSpinBox,
    QMessageBox,
)
from PySide6.QtCore import QTimer, Qt
import sys


class TimerWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PySide6 计时器")
        self.resize(320, 180)

        layout = QVBoxLayout(self)

        self.time_label = QLabel("00:00:00")
        self.time_label.setAlignment(Qt.AlignCenter)
        font = self.time_label.font()
        font.setPointSize(28)
        self.time_label.setFont(font)
        layout.addWidget(self.time_label)

        # Controls to set minutes / seconds
        set_layout = QHBoxLayout()
        self.spin_min = QSpinBox()
        self.spin_min.setRange(0, 999)
        self.spin_min.setSuffix(" min")
        self.spin_sec = QSpinBox()
        self.spin_sec.setRange(0, 59)
        self.spin_sec.setSuffix(" s")
        set_layout.addWidget(self.spin_min)
        set_layout.addWidget(self.spin_sec)
        layout.addLayout(set_layout)

        # Buttons
        btn_layout = QHBoxLayout()
        self.start_btn = QPushButton("开始")
        self.pause_btn = QPushButton("暂停")
        self.reset_btn = QPushButton("重置")
        btn_layout.addWidget(self.start_btn)
        btn_layout.addWidget(self.pause_btn)
        btn_layout.addWidget(self.reset_btn)
        layout.addLayout(btn_layout)

        # Connections
        self.start_btn.clicked.connect(self.start_timer)
        self.pause_btn.clicked.connect(self.pause_timer)
        self.reset_btn.clicked.connect(self.reset_timer)

        # QTimer 用于倒计时（100 ms 更平滑）
        self._timer = QTimer(self)
        self._timer.setInterval(100)
        self._timer.timeout.connect(self._tick)

        # internal state
        self._remaining_ms = 0
        self._running = False

    def _format_time(self, ms: int) -> str:
        total_seconds = ms // 1000
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

    def _tick(self):
        if self._remaining_ms <= 0:
            self._timer.stop()
            self._running = False
            self._on_finished()
            return
        self._remaining_ms -= 100
        if self._remaining_ms < 0:
            self._remaining_ms = 0
        self.time_label.setText(self._format_time(self._remaining_ms))

    def start_timer(self):
        # If not started and remaining time is zero, read from spin boxes
        if not self._running and self._remaining_ms == 0:
            mins = self.spin_min.value()
            secs = self.spin_sec.value()
            self._remaining_ms = (mins * 60 + secs) * 1000
            if self._remaining_ms == 0:
                QMessageBox.warning(self, "警告", "请设置一个大于 0 的时间。")
                return
            self.time_label.setText(self._format_time(self._remaining_ms))

        if not self._running and self._remaining_ms > 0:
            self._timer.start()
            self._running = True

    def pause_timer(self):
        if self._running:
            self._timer.stop()
            self._running = False

    def reset_timer(self):
        self._timer.stop()
        self._running = False
        self._remaining_ms = 0
        self.time_label.setText("00:00:00")

    def _on_finished(self):
        self.time_label.setText("00:00:00")
        QMessageBox.information(self, "计时结束", "时间到！")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = TimerWindow()
    w.show()
    sys.exit(app.exec())
