from PySide6.QtWidgets import QWidget, QDialog, QVBoxLayout, QLabel, QComboBox, QLineEdit, QPushButton, QTabWidget, QTextEdit, QFileDialog, QCheckBox
from PySide6.QtCore import Signal


class ExperimentSettingsWindow(QDialog):
    settings_submitted = Signal(dict)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Experiment Settings")
        self.setGeometry(2500, 300, 800, 500)
        print("[SettingsWindow] Initialized")

        layout = QVBoxLayout(self)


        # Create tab widget
        self.tabs = QTabWidget()
        self.tabs.setTabPosition(QTabWidget.North)  # Tabs at the top (default)

        # Add tabs
        #self.tabs.addTab(QLabel("This is panel 1"), "Panel 1")
        #self.tabs.addTab(QTextEdit("Editable text area in panel 2"), "Panel 2")
        self.initExperimentFile()
        self.initExperimentControllers() 
        self.tabs.addTab(QLabel("Panel 3 content"), "Panel 3")

        # Add tab widget to layout
        layout.addWidget(self.tabs)

        # Submit button
        submit_btn = QPushButton("Submit")
        submit_btn.clicked.connect(self.submit_settings)
        layout.addWidget(submit_btn)


    def initExperimentFile(self):
        tab_widget = QWidget()
        efile_layout = QVBoxLayout(tab_widget)
        tab_name = 'File'

        # File tab content
        self.file_path = QLineEdit()
        self.file_path.setPlaceholderText('Select path...')
        browse_btn = QPushButton('Browse...')
        browse_btn.clicked.connect(self.browse_file)

        # Add to main widget
        efile_layout.addWidget(self.file_path)
        efile_layout.addWidget(browse_btn)
        self.tabs.addTab(tab_widget, tab_name)


    def browse_file(self):
        chosen_file_path, _ = QFileDialog.getOpenFileName(
            self,
            'Select a File',
            '', # start directory
            'All Files (*);; Text Files (*.txt)'
        )
        if chosen_file_path:
            self.file_path.setText(chosen_file_path)


    def initExperimentControllers(self):
        tab_widget = QWidget()
        econtroller_layout = QVBoxLayout(tab_widget)
        tab_name = 'Contollers'

        # Contoller tab content
        self.cb_heater = QCheckBox('Enable Heater')
        self.cb_heater.stateChanged.connect(self.toggleHeaterOptions)
        self.cb_MFCs = QCheckBox('Enable Mass Flow Controllers')
        #self.cb_MFCs.stateChanged.connect(self.toggleMFCOptions)
        self.cb_GC = QCheckBox('Enable Gas Chromatograph')
        #self.cb_GC.stateChanged.connect(self.toggleGCOptions)


        self.heater_options_label = QLabel('Please Select A Heater Configuration...')
        self.heater_options_dropdown = QComboBox()
        self.heater_options_dropdown.addItem('Option 1')
        self.heater_options_dropdown.addItem('Option 2')
        self.heater_options_dropdown.addItem('Option 3')

        # Hide options on startup
        self.heater_options_label.hide()
        self.heater_options_dropdown.hide()

        # Add to main widget
        econtroller_layout.addWidget(self.cb_heater)
        econtroller_layout.addWidget(self.heater_options_dropdown)
        econtroller_layout.addWidget(self.heater_options_label)
        econtroller_layout.addWidget(self.cb_MFCs)
        econtroller_layout.addWidget(self.cb_GC)
        self.tabs.addTab(tab_widget,tab_name)


    def toggleHeaterOptions(self,state):
        if state:
            self.heater_options_label.show()
            self.heater_options_dropdown.show()
        else:
            self.heater_options_label.hide()
            self.heater_options_dropdown.hide()




    def submit_settings(self):
        settings = {
            "file_path": self.file_path.text(),
            #"B": self.input2.text(),
        }
        print(f"[SettingsWindow] Submitting settings: {settings}")
        self.settings_submitted.emit(settings)
        self.close()