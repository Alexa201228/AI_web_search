import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QListWidgetItem

from main_window import Ui_MainWindow
from neuro_engine import AgentsSearch


class MainWindow(QtWidgets.QMainWindow):

    _link_template = '<a href={0}>{1}</a>'
    _agents: dict = None

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.search_results.setOpenExternalLinks(True)
        self.ui.start_search_btn.pressed.connect(self.start_search)
        self.ui.agents_list.itemClicked.connect(self.show_agent_answers)

    def start_search(self):
        self.ui.agents_list.clear()
        self.ui.search_results.setText('')
        search_agents = AgentsSearch(agents_count=self.ui.agents_count.value(),
                                     user_request=self.ui.search_request.toPlainText())
        self._agents = search_agents.search()
        for agent in self._agents:
            list_item = QListWidgetItem(agent)
            self.ui.agents_list.addItem(list_item)

    def show_agent_answers(self, item: QListWidgetItem):
        self.ui.search_results.setText('')
        data = [f'<a href={result[0][:result[0].rindex("/")]}>{result[1]}</a>' for result in self._agents[item.text()]]
        for line in data:
            self.ui.search_results.append(line)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = MainWindow()
    application.show()
    sys.exit(app.exec())

