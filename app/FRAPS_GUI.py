import pyqtgraph as pg
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QLabel,
    QProgressBar, QTableWidget, QTableWidgetItem, QTabWidget, QApplication, QMainWindow, 
    QComboBox, QSplitter, QTextEdit, QDockWidget, QTabBar
)
from PySide6.QtGui import (
    QAction, QKeySequence, QIcon
)
from PySide6.QtCore import Signal, Qt
from FRAPS_Controller import DashboardController as dc
from functools import partial



class DashboardUI(QMainWindow):
    start_task_signal = Signal()  # GUI → Controller

    def __init__(self):
        super().__init__()
        self.setWindowTitle("BRAPS")
        logo = QIcon('flaherty_logo.png')
        self.setWindowIcon(logo)
 
        self.setGeometry(2500, 200, 800, 600)

        self.main_window = QWidget()
        self.setCentralWidget(self.main_window)
        self.layout = QVBoxLayout(self.main_window)



        # Initialize Menu Bar Items Individually
        
        #self.initSetup()
        #self.initView()
        #self.initAnalysis()


        ''' TODO Main Window design and functionality
        # Add split window
        splitter = QSplitter(Qt.Horizontal)
        splitter.setSizes([300, 300])
        left_panel = QTextEdit()
        left_panel.setPlaceholderText('Left Panel')
        splitter.addWidget(left_panel)


        # Right panel → QMainWindow to manage dock widgets internally
        self.right_panel = QMainWindow()
        self.right_panel.setDockOptions(
            QMainWindow.AllowTabbedDocks |
            QMainWindow.AnimatedDocks |
            #QMainWindow.ForceTabbedDocks  | # << KEY FIX: Force docks to show tabs
            QMainWindow.DockOption.VerticalTabs
        )
        splitter.addWidget(self.right_panel)

        # Add splitter to main layout
        self.layout.addWidget(splitter)

        # Add dock widgets to right panel
        self.add_dock_windows()

    def create_dock(self, title, content, allowed_areas=Qt.AllDockWidgetAreas):
        """Helper to create a docked panel."""
        dock = QDockWidget(title, self.right_panel)
        dock.setWidget(QLabel(content))
        dock.setAllowedAreas(allowed_areas)

        # Disable floating if you want docks to stay contained
        dock.setFeatures(
            QDockWidget.DockWidgetClosable |
            QDockWidget.DockWidgetMovable
            # No DockWidgetFloatable → prevents tearing out
        )

        return dock

    def add_dock_windows(self):
        dock1 = self.create_dock("Dockable Panel 1", "Content of Dock 1")
        dock2 = self.create_dock("Dockable Panel 2", "Content of Dock 2")
        dock3 = self.create_dock("Dockable Panel 3", "Content of Dock 3")

        # Add docks to the right panel
        self.right_panel.addDockWidget(Qt.RightDockWidgetArea, dock1)
        self.right_panel.addDockWidget(Qt.RightDockWidgetArea, dock2)
        self.right_panel.addDockWidget(Qt.RightDockWidgetArea, dock3)

        # Tabify them
        self.right_panel.tabifyDockWidget(dock1, dock2)
        self.right_panel.tabifyDockWidget(dock1, dock3)

        # Force dock1 to be active
        dock1.raise_()

        # Locate the internal QTabBar created by Qt
        tab_bars = self.right_panel.findChildren(QTabBar)
        if tab_bars:
            tab_bar = tab_bars[0]
            tab_bar.setShape(QTabBar.RoundedNorth)  # ⬅️ Forces tabs to top
  
    
    
      '''

        # file_action_new = QAction('New', self)
        # file_action_open = QAction('Open', self)


        # file_action_new.triggered.connect(lambda: dc.FileCommands(command='New'))
        # file_action_open.triggered.connect(lambda: print('Open Action Triggered'))
        
        
        # self.menu_file.addAction(file_action_open)
        # self.menu_file.addAction(file_action_new)
        

    def initSetup(self):
        layout = QVBoxLayout(self.tab_setup_content)
        label = QLabel('This is the Setup tab')
        layout.addWidget(label)


    def initView(self):
        layout = QVBoxLayout(self.tab_view_content)
        label = QLabel('This is the View tab')
        layout.addWidget(label)


    def initAnalysis(self):
        layout = QVBoxLayout(self.tab_analysis_content)
        label = QLabel('This is the Analysis tab')
        layout.addWidget(label)