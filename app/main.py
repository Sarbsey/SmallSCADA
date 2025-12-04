import sys
import asyncio
import signal
from qasync import QEventLoop
from PySide6.QtWidgets import QApplication
from FRAPS_Controller import DashboardController
from FRAPS_GUI import DashboardUI
from Win_main import MainWindow


def main():
    app = QApplication(sys.argv)
    loop = QEventLoop(app)

    # Create main window
    main_window = MainWindow()

    # Create controller
    controller = DashboardController(main_window=main_window)

    # Link main window to controller
    main_window.controller = controller
    controller.widget_requested.connect(main_window.add_new_widget)

    # Show main window
    main_window.show()

    with loop:
        loop.run_forever()

if __name__ == "__main__":
    main()
