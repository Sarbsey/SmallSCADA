import asyncio
import random
from Win_experiment import ExperimentSettingsWindow as esw

from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QLabel,
    QProgressBar, QTableWidget, QTableWidgetItem, QTabWidget, QApplication, QMainWindow, 
    QComboBox, QSplitter, QTextEdit, QDockWidget, QTabBar
)
from PySide6.QtGui import (
    QAction, QKeySequence, QIcon
)
from PySide6.QtCore import Signal, Qt, QObject



class DashboardController(QObject):
    widget_requested = Signal(dict)

    def __init__(self, main_window=None, parent=None):
        super().__init__(parent)
        self.main_window = main_window
        self.settings_window = None

        print("[Controller] Initialized")

    def handle_file_command(self, command):
        """Handles commands coming from the main window."""
        print(f"[Controller] Received file command: {command}")
        if command == "New":
            self.open_settings_window()

    def open_settings_window(self):
        """Creates and shows the experiment settings window."""
        print("[Controller] Opening Experiment Settings Window...")
        self.settings_window = esw()
        self.settings_window.settings_submitted.connect(self.handle_settings_submitted)
        self.settings_window.show()

    def handle_settings_submitted(self, settings):
        """Receives settings and requests a new widget in the main window."""
        print(f"[Controller] Settings received: {settings}")
        self.widget_requested.emit(settings)


'''
    Old example functions
    async def run_task(self):
        self.ui.label.setText("Running task...")
        self.ui.progress.setValue(0)
        for i in range(1, 101):
            self.ui.progress.setValue(i)
            await asyncio.sleep(0.05)
        self.ui.label.setText("Task Complete!")

    async def live_plot_updater(self):
        while True:
            self.x_data.append(len(self.x_data))
            self.y_data.append(random.uniform(0, 1000))

            self.x_data = self.x_data[-200:]
            self.y_data = self.y_data[-200:]

            #self.ui.update_plot(self.x_data, self.y_data)
            await asyncio.sleep(0.05)

    async def table_updater(self):
        while True:
            self.ui.update_table(self.x_data, self.y_data)
            await asyncio.sleep(0.5)
    

    def ExperimentEditor(self, type, content=None):
        if content:
            # Extract data from file then pass into 
            pass
        else:
            content = QWidget()
            content.setWidget(QLabel('New Window'))



        return content



    def create_window(self, title, content, type, allowed_areas=Qt.AllDockWidgetAreas):
        """Helper to create a docked panel."""
        window = QMainWindow()
        window.setWindowTitle(title)
        window.setGeometry(300,300,300,300)

        central_widget = QWidget()
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        window.setCentralWidget(central_widget)

        # Add content if not provided
        # TODO figure out how to open experiment editor with content
        if content:
            pass
        else:
            self.ExperimentEditor(self, type='new')
            return content
        

        window.show()
        self.secondary_windows.append(window)

        return window


    def create_dock(self, title, content, type, allowed_areas=Qt.AllDockWidgetAreas):
        """Helper to create a docked panel."""
        dock = QDockWidget(title, self.right_panel)
        dock.setWidget(QLabel(content))
        dock.setAllowedAreas(allowed_areas)

        # Disable floating if you want docks to stay contained
        dock.setFeatures(
            QDockWidget.DockWidgetClosable |
            QDockWidget.DockWidgetMovable  |
            QDockWidget.DockWidgetFloatable 
        )

        return dock
    


    def FileCommands(self, command=None):
        if command == 'New':
            # Create new window to set up experiment
            #content = self.ExperimentEditor(self, type='new')
            self.create_window(self, title='Start New Experiment', type='New', content=None)
        return

'''