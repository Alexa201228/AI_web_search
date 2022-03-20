import sys

from PyQt5 import QtWidgets
from main_window import Ui_MainWindow
from neuro_engine import AgentsSearch


class MainWindow(QtWidgets.QMainWindow):

    _link_template = '<a href={0}>{1}</a>'

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.search_results.setOpenExternalLinks(True)
        self.ui.start_search_btn.pressed.connect(self.start_search)

    def start_search(self):
        search_agents = AgentsSearch(agents_count=self.ui.agents_count.value(),
                                     user_request=self.ui.search_request.toPlainText())
        search_agents.search()


app = QtWidgets.QApplication([])
application = MainWindow()
application.show()

sys.exit(app.exec())
