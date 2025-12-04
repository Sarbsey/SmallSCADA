from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel
from PySide6.QtGui import QIcon, QAction, QKeySequence
from PySide6.QtCore import Signal, Qt
from functools import partial

class MainWindow(QMainWindow):
    file_command_requested = Signal(str)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")
        self.setGeometry(2500, 300, 300, 300)
        self.controller = None

        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.layout = QVBoxLayout()
        central_widget.setLayout(self.layout)

        # Menu bar
        menu = self.menuBar().addMenu("File")
        new_action = QAction("New", self)
        new_action.setShortcut(QKeySequence("Ctrl+N"))
        new_action.triggered.connect(self._on_new_triggered)
        menu.addAction(new_action)

        # Forward "New" to controller
        self.file_command_requested.connect(self._send_to_controller)

    def _on_new_triggered(self):
        print("[MainWindow] 'New' clicked")
        self.file_command_requested.emit("New")

    def _send_to_controller(self, command):
        """Call controller if available."""
        if self.controller:
            print(f"[MainWindow] Sending '{command}' to controller")
            self.controller.handle_file_command(command)
        else:
            print("[MainWindow] ERROR: No controller attached!")

    def add_new_widget(self, settings):
        """Adds a new widget when settings are submitted."""
        print(f"[MainWindow] Adding new widget with settings: {settings}")
        label = QLabel(f"Widget: A={settings['file_path']}")
        label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(label)
       # Main Menu Bar



        # self.menu_bar = self.menuBar()
        # self.menu_file = self.menu_bar.addMenu('File')
        # self.menu_setup = self.menu_bar.addMenu('Experiment')
        # self.menu_view = self.menu_bar.addMenu('View')
        # self.menu_analysis = self.menu_bar.addMenu('Analysis')

        # TODO Add basic items to menu bar inits
        # TODO Add funcitonality to menu bar items through FRAPS_Controller.py
        # print(f'Controller is {controller}')
        # if controller:
        #     print('yay')
        #     self.initFile()




    def initFile(self):
        # Action name : Shortcut mapping
        file_actions = {
            "New": "Ctrl+N",
            "Open": "Ctrl+O",
            "Save": "Ctrl+S",
            "Save As": "Ctrl+Shift+S",
        }

        for action_name, shortcut in file_actions.items():
            file_action = QAction(action_name, self)
            file_action.setShortcut(QKeySequence(shortcut))
            file_action.triggered.connect(partial(self.controller.FileCommands, command=action_name))

            self.menu_file.addAction(file_action)

