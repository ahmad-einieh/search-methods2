
import citiesGraph
import os

import pyvis
from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets
import Astar
import Greedy


# import Distance

class Ui_root(object):
    def setupUi(self, root):
        root.setObjectName("root")
        root.resize(1390, 975)
        root.setStyleSheet("/*  ---------------------------- ALL OTHERS WIDGETS ---------------------------- */\n"
                           "*{\n"
                           "selection-background-color: rgb(67, 128, 179);\n"
                           "selection-color: rgb(255, 255, 255);\n"
                           "}\n"
                           "\n"
                           "/*  ---------------------------- MAIN WINDOW, WIDGET ---------------------------- */\n"
                           "QMainWindow,QWidget\n"
                           "{\n"
                           "color:rgb(0,0,0);\n"
                           "background:rgb(255,255,255);\n"
                           "}\n"
                           "\n"
                           "/*  ---------------------------- MENU BAR ---------------------------- */\n"
                           "QMenuBar\n"
                           "{\n"
                           "color:rgb(120,120,120);\n"
                           "background:rgb(230,230,230);\n"
                           "}\n"
                           "QMenuBar::item:selected\n"
                           "{\n"
                           "color:rgb(100,100,100);\n"
                           "background:rgb(200,200,200);\n"
                           "}\n"
                           "/*  ---------------------------- CONTEXT MENU ---------------------------- */\n"
                           "QMenu\n"
                           "{\n"
                           "color:rgb(90,90,90);\n"
                           "background:rgb(230,230,230);\n"
                           "padding: 3;\n"
                           "}\n"
                           "QMenu::item:selected\n"
                           "{\n"
                           "color:rgb(90,90,90);\n"
                           "background:rgb(200,200,200);\n"
                           "}\n"
                           "QMenu::separator {\n"
                           "background:rgb(200,200,200);\n"
                           "height:1px;\n"
                           "}\n"
                           "\n"
                           "\n"
                           "/*  ---------------------------- Q TAB BAR ---------------------------- */\n"
                           "QTabBar::tab {\n"
                           "color:rgb(150,150,150);\n"
                           "background:rgb(240,240,240);\n"
                           "height:30;\n"
                           "width:80;\n"
                           "border: rgb(240,240,240);\n"
                           "border-width: 0 0 2px 0;\n"
                           "padding-left:10;\n"
                           "}\n"
                           "\n"
                           "QTabBar::tab:selected {\n"
                           "background:white;\n"
                           "color:rgb(100,100,100);\n"
                           "border: solid rgb(0,150,255);\n"
                           "border-width: 0 0 5px 0;\n"
                           "}\n"
                           "QTableWidget QTableCornerButton::section {\n"
                           "background-color: rgb(255, 255, 255);\n"
                           "}\n"
                           "/*-----------------------------------------------------------------\n"
                           "------------------------------ LINE_EDIT --------------------------\n"
                           "------------------------------ TEXT BROWSER -----------------------\n"
                           "------------------------------ TEXT_EDIT---------------------------\n"
                           "------------------------------ PLAIN_TEXT -------------------------\n"
                           "------------------------------------------------------------------- */\n"
                           "QLineEdit,QTextBrowser,QTextEdit,QPlainTextEdit\n"
                           "{\n"
                           "color:rgb(20,20,20);\n"
                           "background-color:white;\n"
                           "border: solid lightgrey;\n"
                           "border-width: 0 0 2px 0;\n"
                           "border-bottom-left-radius: 5;\n"
                           "border-bottom-right-radius: 5;\n"
                           "}\n"
                           "\n"
                           "QLineEdit:disabled\n"
                           "{\n"
                           "color:rgb(160, 150, 150);\n"
                           "background-color:rgb(255, 240, 240);\n"
                           "border: solid rgb(253, 14, 14);\n"
                           "border-width: 0 0 2px 0;\n"
                           "border-bottom-left-radius: 5;\n"
                           "border-bottom-right-radius: 5;\n"
                           "}\n"
                           "\n"
                           "/*  ---------------------------- COMBO BOX ----------------------------*/\n"
                           "QComboBox\n"
                           "{\n"
                           "color:rgb(0,115,170);\n"
                           "background-color:rgb(255, 255, 255);\n"
                           "min-width: 5px;\n"
                           "padding: 1px 0px 1px 3px;\n"
                           "border: 1px solid rgb(0,115,170);\n"
                           "}\n"
                           "\n"
                           "QComboBox:hover\n"
                           "{\n"
                           "color:rgb(0,115,170);\n"
                           "background-color: white;\n"
                           "}\n"
                           "\n"
                           "QComboBox:selected\n"
                           "{\n"
                           "color:rgb(0,115,170);\n"
                           "selection-background-color: rgb(255, 255, 255);\n"
                           "}\n"
                           "\n"
                           "QComboBox::drop-down\n"
                           "{\n"
                           "width: 30px;\n"
                           "background-color:rgb(0,115,170);\n"
                           "}\n"
                           "\n"
                           "QComboBox::down-arrow\n"
                           "{\n"
                           "image: url(assets/UI/Icons/interface_icons/arrow_down.png);\n"
                           "width: 14px;\n"
                           "height: 14px;\n"
                           "}\n"
                           "\n"
                           "\n"
                           "/* -------------------------------- CHECK BOX ----------------------------------------- */\n"
                           "QCheckBox\n"
                           "{\n"
                           "background: rgb(255, 255, 255);\n"
                           "color:rgb(25, 29, 32);\n"
                           "padding: 6;\n"
                           "}\n"
                           "/* ----------------------------  TOOL BOX  ----------------------------  */\n"
                           "QToolBox::tab\n"
                           "{\n"
                           "color:darkgrey;\n"
                           "background:lightgrey;\n"
                           "}\n"
                           "QToolBox::tab::selected\n"
                           "{\n"
                           "color:grey;\n"
                           "background:rgb(250, 250,250);\n"
                           "}\n"
                           "QToolBox::tab::hover\n"
                           "{\n"
                           "color:white;\n"
                           "background:rgb(0,115,170);\n"
                           "}\n"
                           "/*  ---------------------------- PROGRESS BAR ---------------------------- */\n"
                           "QProgressBar {\n"
                           "color:grey;\n"
                           "text-align: center;\n"
                           "font-size:13px;\n"
                           "}\n"
                           "QProgressBar::chunk {\n"
                           "background:rgb(0, 193, 50);\n"
                           "}\n"
                           "/*  ---------------------------- PUSHBUTTON ---------------------------- */\n"
                           "QPushButton\n"
                           "{\n"
                           "border: 1px solid lightgrey;\n"
                           "color:white;\n"
                           "background:rgb(0,115,170);\n"
                           "min-height:30;\n"
                           "min-width: 50;\n"
                           "}\n"
                           "QPushButton:hover\n"
                           "{\n"
                           "border: 1px solid lightgrey;\n"
                           "color:white;\n"
                           "background:rgb(0, 120, 210);\n"
                           "}\n"
                           "\n"
                           "QPushButton:pressed\n"
                           "{\n"
                           "border: 1px solid lightgrey;\n"
                           "color:white;\n"
                           "background:rgb(0, 53, 100);\n"
                           "}\n"
                           "/*  ----------------------------  LCD NUMBER ---------------------------- */\n"
                           "QLCDNumber\n"
                           "{\n"
                           "color:rgb(0,115,170);\n"
                           "border:2 solid rgb(100,100,100);\n"
                           "}\n"
                           "/*  ---------------------------- TABLE_LIST_TABLE ---------------------------- */\n"
                           "QTableView,\n"
                           "QTableWidget\n"
                           "{\n"
                           "alternate-background-color: rgb(240, 250, 255);\n"
                           "}\n"
                           "QTreeView\n"
                           "{\n"
                           "background: rgb(250,250,250);\n"
                           "color: rgb(180,180,180);\n"
                           "}\n"
                           "QTableView::item:selected, \n"
                           "QListView::item:selected,\n"
                           "QTableView::item:hover, \n"
                           "QListView::item:hover, \n"
                           "QTreeView::item:hover\n"
                           "{\n"
                           "background:rgb(0,115,170);\n"
                           "color:rgb(250,250,250);\n"
                           "}\n"
                           "QTableView::item, \n"
                           "QListView::item, \n"
                           "QTreeView::item\n"
                           "{\n"
                           "color:rgb(100,100,100);\n"
                           "}\n"
                           "QTreeView::item:selected,QListView::item:selected,QTableView::item:selected\n"
                           "{\n"
                           "color:rgb(37, 62, 71);\n"
                           "background:rgb(209, 241, 252);\n"
                           "}\n"
                           "/* QTreeView::item:has-children\n"
                           "{\n"
                           "background-color: rgb(0, 78, 134);\n"
                           "color: white;\n"
                           "border-bottom: 2px solid qlineargradient(spread:pad, x1:1, y1:0.5, x2:0, y2:0.5, stop:0 rgba(255, 255, 255, 0), stop:0.5 rgba(0, 150, 255, 255), stop:1 rgba(255, 255, 255, 0));\n"
                           "}\n"
                           "*/\n"
                           "/*  ---------------------------- HEADER VIEW ---------------------------- */\n"
                           "QHeaderView::section\n"
                           "{\n"
                           "color:rgb(133, 133, 133);\n"
                           "background:white;\n"
                           "border:transparent;\n"
                           "text-align:center;\n"
                           "padding:1;\n"
                           "}\n"
                           "/* ------------------------------- CALENDAR -------------------------------------------------- */\n"
                           "QCalendarView\n"
                           "{\n"
                           "color: rgb(20,20,20);\n"
                           "background-color: rgb(240,240,240);\n"
                           "alternate-background-color: rgb(0,115,170);\n"
                           "selection-background-color: white;\n"
                           "selection-color: black;\n"
                           "}\n"
                           "QAbstractItemView\n"
                           "{\n"
                           "color:rgb(200,200,200);\n"
                           "}\n"
                           "\n"
                           "\n"
                           "/* ---------------------------------------- SLIDER HORIZONTAL ----------------------------------------------- */\n"
                           "\n"
                           "\n"
                           "QSlider::groove:horizontal,QSlider::add-page:horizontal\n"
                           "{\n"
                           "background: rgb(255, 255, 255);\n"
                           "height: 27px;\n"
                           "}\n"
                           "QSlider::sub-page:horizontal {\n"
                           "height: 10px;\n"
                           "background: rgb(0,115,170);\n"
                           "}\n"
                           "QSlider::handle:horizontal {\n"
                           "margin-right: -10px;\n"
                           "margin-left: -10px;\n"
                           "background: rgb(0,115,170);\n"
                           "}\n"
                           "QSlider::handle:horizontal:hover {\n"
                           "background:rgb(0,115,170);\n"
                           "}\n"
                           "\n"
                           "/* --------------------------------  VERTICAL SLIDER --------------------------------------------------------------  */\n"
                           "\n"
                           "QSlider::handle\n"
                           "{\n"
                           "border-radius: 3px;\n"
                           "}\n"
                           "\n"
                           "QSlider::groove:vertical,QSlider::add-page:vertical,QSlider::sub-page:vertical\n"
                           "{\n"
                           "width: 20px;\n"
                           "background: rgb(255, 255, 255);\n"
                           "}\n"
                           "\n"
                           "QSlider::handle:vertical {\n"
                           "margin-top: -10px;\n"
                           "margin-bottom: -10px;\n"
                           "background: rgb(0,115,170);\n"
                           "}\n"
                           "QSlider::handle:vertical:hover {\n"
                           "background: rgb(0,115,170);\n"
                           "}\n"
                           "\n"
                           "/* --------------------------------- SCROLLBAR HORIZONTAL --------------------------------------  */\n"
                           "\n"
                           "QScrollBar::groove:horizontal{\n"
                           "background: white;\n"
                           "height: 17px;\n"
                           "}\n"
                           "QScrollBar::sub-page:horizontal,QScrollBar::add-page:horizontal  {\n"
                           "height: 10px;\n"
                           "background: rgb(255, 255, 255);\n"
                           "}\n"
                           "QScrollBar::handle:horizontal {\n"
                           "margin-right: -5px;\n"
                           "background: rgb(0,115,170);\n"
                           "}\n"
                           "QScrollBar::handle:horizontal:hover {\n"
                           "background: rgb(0,115,170);\n"
                           "}\n"
                           "\n"
                           "/* --------------------------------------- SCROLLBAR VERTICAL ----------------------------------------------  */\n"
                           "\n"
                           "/* SCROLLBAR */\n"
                           "QScrollBar:vertical {\n"
                           "background: white;\n"
                           "width: 15px;\n"
                           "margin: 22px 0 22px 0;\n"
                           "}\n"
                           "/* HANDLE*/\n"
                           "QScrollBar::handle:vertical {\n"
                           "background: rgb(0,115,170);\n"
                           "min-height: 20px;\n"
                           "}\n"
                           "\n"
                           "/* UP ARROW */\n"
                           "QScrollBar::up-arrow:vertical {\n"
                           "image: url(assets/UI/Icons/interface_icons/arrow_up.png);\n"
                           "width: 10px;\n"
                           "height: 10px;\n"
                           "}\n"
                           "/* DOWN ARROW */\n"
                           "QScrollBar::down-arrow:vertical {\n"
                           "image: url(assets/UI/Icons/interface_icons/arrow_down.png);\n"
                           "width: 10px;\n"
                           "height: 10px;\n"
                           "}\n"
                           "/* UP BUTTON */\n"
                           "QScrollBar::sub-line:vertical {\n"
                           "background: rgb(0,115,170);\n"
                           "height: 20px;\n"
                           "subcontrol-position: top;\n"
                           "subcontrol-origin: margin;\n"
                           "}\n"
                           "/* DOWN BUTTON */\n"
                           "QScrollBar::add-line:vertical {\n"
                           "background: rgb(0,115,170);\n"
                           "height: 20px;\n"
                           "subcontrol-position: bottom;\n"
                           "subcontrol-origin: margin;\n"
                           "}\n"
                           "/* SUBPAGES - ADDPAGE */\n"
                           "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
                           "background: none;\n"
                           "}\n"
                           "/* ---------------------------------- Q TOOL BAR -------------------------------------------------------- */\n"
                           "/* TOOLBAR REGION */\n"
                           "QToolBar {\n"
                           "background: rgb(35,40,45);\n"
                           "spacing: 20;\n"
                           "\n"
                           "}\n"
                           "/* SEPARATOR */\n"
                           "QToolBar:separator\n"
                           "{\n"
                           "background: rgb(80, 80, 80);\n"
                           "height: 2;\n"
                           "}\n"
                           "/* QToolBar QToolButton { \n"
                           "    width: 100px;\n"
                           "} */\n"
                           "/* -----------------------------------------------Q TOOL BUTTON------------------------------------------- */\n"
                           "/* BUTTON */\n"
                           "QToolButton\n"
                           "{\n"
                           "color: rgb(255, 255, 255);\n"
                           "background:rgb(35,40,45);\n"
                           "}\n"
                           "\n"
                           "QToolButton:hover,QToolButton:pressed\n"
                           "{\n"
                           "background-color: rgb(64, 73, 82);\n"
                           "}\n"
                           "\n"
                           "QMessageBox QLabel\n"
                           "{\n"
                           "color: red;\n"
                           "}")
        self.centralwidget = QtWidgets.QWidget(root)
        self.centralwidget.setObjectName("centralwidget")
        self.city1 = QtWidgets.QComboBox(self.centralwidget)
        self.city1.setGeometry(QtCore.QRect(125, 20, 280, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.city1.setFont(font)
        self.city1.setObjectName("city1")
        self.city2 = QtWidgets.QComboBox(self.centralwidget)
        self.city2.setGeometry(QtCore.QRect(125, 70, 280, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.city2.setFont(font)
        self.city2.setObjectName("city2")
        self.greedy = QtWidgets.QPushButton(self.centralwidget)
        self.greedy.setGeometry(QtCore.QRect(910, 10, 221, 91))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.greedy.setFont(font)
        self.greedy.setObjectName("greedy")
        self.aSTAR = QtWidgets.QPushButton(self.centralwidget)
        self.aSTAR.setGeometry(QtCore.QRect(1150, 10, 221, 91))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.aSTAR.setFont(font)
        self.aSTAR.setObjectName("aSTAR")
        self.path = QtWidgets.QTextBrowser(self.centralwidget)
        self.path.setGeometry(QtCore.QRect(460, 130, 821, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.path.setFont(font)
        self.path.setObjectName("path")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 101, 41))
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 101, 41))
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(210, 130, 151, 61))
        self.label_3.setObjectName("label_3")
        self.distance = QtWidgets.QTextBrowser(self.centralwidget)
        self.distance.setGeometry(QtCore.QRect(230, 220, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.distance.setFont(font)
        self.distance.setObjectName("distance")
        self.cost = QtWidgets.QTextBrowser(self.centralwidget)
        self.cost.setGeometry(QtCore.QRect(550, 220, 191, 61))
        font = QtGui.QFont()
        # font.setPointSize(20)
        font.setPointSize(22)
        self.cost.setFont(font)
        self.cost.setObjectName("cost")
        self.max = QtWidgets.QTextBrowser(self.centralwidget)
        self.max.setGeometry(QtCore.QRect(1140, 220, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.max.setFont(font)
        self.max.setObjectName("max")
        self.widget = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(-1, 310, 1391, 651))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.widget.setFont(font)
        self.widget.setObjectName("widget")
        self.total = QtWidgets.QTextBrowser(self.centralwidget)
        self.total.setGeometry(QtCore.QRect(850, 220, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.total.setFont(font)
        self.total.setObjectName("total")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(110, 230, 111, 41))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(470, 220, 71, 51))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(760, 220, 81, 51))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(1060, 220, 81, 51))
        self.label_7.setObjectName("label_7")
        self.KMforL = QtWidgets.QTextEdit(self.centralwidget)
        self.KMforL.setGeometry(QtCore.QRect(560, 40, 281, 51))
        self.KMforL.setObjectName("KMforL")
        self.KMforL.setFont(font)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(410, 40, 131, 51))
        self.label_8.setObjectName("label_8")
        root.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(root)
        self.statusbar.setObjectName("statusbar")
        root.setStatusBar(self.statusbar)

        with open("allCities.txt", 'r') as f:
            for k in f:
                self.city1.addItem(k)
                self.city2.addItem(k)

        self.retranslateUi(root)
        QtCore.QMetaObject.connectSlotsByName(root)

    def retranslateUi(self, root):
        root.setWindowFlags(root.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)

        _translate = QtCore.QCoreApplication.translate
        root.setWindowTitle(_translate("root", "search 2"))
        self.greedy.setText(_translate("root", "greedy"))
        self.aSTAR.setText(_translate("root", "A*"))
        self.label.setText(_translate("root",
                                      "<html><head/><body><p><span style=\" font-size:20pt;\">city 1</span></p></body></html>"))
        self.label_2.setText(_translate("root",
                                        "<html><head/><body><p><span style=\" font-size:20pt;\">city 2</span></p></body></html>"))
        self.label_3.setText(
            _translate("root", "<html><head/><body><p><span style=\" font-size:22pt;\">path</span></p></body></html>"))
        self.label_4.setText(_translate("root",
                                        "<html><head/><body><p><span style=\" font-size:18pt;\">distance</span></p></body></html>"))
        self.label_5.setText(
            _translate("root", "<html><head/><body><p><span style=\" font-size:22pt;\">cost</span></p></body></html>"))
        self.label_6.setText(
            _translate("root", "<html><head/><body><p><span style=\" font-size:22pt;\">total</span></p></body></html>"))
        self.label_7.setText(
            _translate("root", "<html><head/><body><p><span style=\" font-size:22pt;\">max</span></p></body></html>"))
        self.label_8.setText(_translate("root",
                                        "<html><head/><body><p><span style=\" font-size:22pt;\">KM/liter</span></p></body></html>"))
        self.greedy.clicked.connect(lambda: self.greedyMethod())
        self.aSTAR.clicked.connect(lambda: self.aStarMethod())

    def greedyMethod(self):
        nameOfGraph = "greedy.html"
        pyvis_graph = pyvis.network.Network(notebook=True, height="100%", width="100%")
        a, b, c, d = Greedy.Greedy(citiesGraph.dict_graph, self.city1.currentText(), self.city2.currentText())
        ttt = (b / int(self.KMforL.toPlainText())) * 2.18
        for i in citiesGraph.dict_graph:
            color = 'blue'
            for k in a:
                if i == k:
                    color = 'green'
            pyvis_graph.add_node(i, label=i, title=i, color=color)

        for i in citiesGraph.dict_graph:
            for j in citiesGraph.dict_graph[i]:
                pyvis_graph.add_edge(i, j, label=citiesGraph.dict_graph[i].get(j),
                                     title=citiesGraph.dict_graph[i].get(j))
        self.path.setText(str(a))
        self.distance.setText(str(b))
        self.cost.setText(str(round(ttt, 7)))
        self.total.setText(str(c))
        self.max.setText(str(d))
        pyvis_graph.force_atlas_2based()
        pyvis_graph.show(nameOfGraph)
        directory = os.getcwd()
        directory = directory.replace('\\', '/')
        url = "file:///{dir}/{name}".format(dir=directory, name=nameOfGraph)
        self.widget.setUrl(QtCore.QUrl(url))

    def aStarMethod(self):
        nameOfGraph = "astar.html"
        pyvis_graph = pyvis.network.Network(notebook=True, height="100%", width="100%")

        a, b, c, d = Astar.astar(citiesGraph.dict_graph, self.city1.currentText(), self.city2.currentText())
        ttt = (b / int(self.KMforL.toPlainText())) * 2.18
        for i in citiesGraph.dict_graph:
            color = 'blue'
            for k in a:
                if i == k:
                    color = 'green'
            pyvis_graph.add_node(i, label=i, title=i, color=color)

        for i in citiesGraph.dict_graph:
            for j in citiesGraph.dict_graph[i]:
                pyvis_graph.add_edge(i, j, label=citiesGraph.dict_graph[i].get(j),
                                     title=citiesGraph.dict_graph[i].get(j))
        self.path.setText(str(a))
        self.distance.setText(str(b))
        self.cost.setText(str(round(ttt, 7)))
        self.total.setText(str(c))
        self.max.setText(str(d))
        pyvis_graph.force_atlas_2based()
        pyvis_graph.show(nameOfGraph)
        directory = os.getcwd()
        directory = directory.replace('\\', '/')
        url = "file:///{dir}/{name}".format(dir=directory, name=nameOfGraph)
        self.widget.setUrl(QtCore.QUrl(url))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    root = QtWidgets.QMainWindow()
    ui = Ui_root()
    ui.setupUi(root)
    root.show()
    sys.exit(app.exec_())
