# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created: Wed Apr 16 16:45:44 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(809, 605)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gw_overview = QtGui.QGraphicsView(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gw_overview.sizePolicy().hasHeightForWidth())
        self.gw_overview.setSizePolicy(sizePolicy)
        self.gw_overview.setObjectName("gw_overview")
        self.horizontalLayout_2.addWidget(self.gw_overview)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.scrollView = QtGui.QGraphicsView(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollView.sizePolicy().hasHeightForWidth())
        self.scrollView.setSizePolicy(sizePolicy)
        self.scrollView.setObjectName("scrollView")
        self.horizontalLayout_3.addWidget(self.scrollView)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pb_prev = QtGui.QPushButton(self.centralwidget)
        self.pb_prev.setObjectName("pb_prev")
        self.horizontalLayout.addWidget(self.pb_prev)
        self.pb_next = QtGui.QPushButton(self.centralwidget)
        self.pb_next.setObjectName("pb_next")
        self.horizontalLayout.addWidget(self.pb_next)
        self.pb_save = QtGui.QPushButton(self.centralwidget)
        self.pb_save.setObjectName("pb_save")
        self.horizontalLayout.addWidget(self.pb_save)
        self.pb_load = QtGui.QPushButton(self.centralwidget)
        self.pb_load.setObjectName("pb_load")
        self.horizontalLayout.addWidget(self.pb_load)
        self.pb_toggle = QtGui.QPushButton(self.centralwidget)
        self.pb_toggle.setObjectName("pb_toggle")
        self.horizontalLayout.addWidget(self.pb_toggle)
        self.pb_delete = QtGui.QPushButton(self.centralwidget)
        self.pb_delete.setObjectName("pb_delete")
        self.horizontalLayout.addWidget(self.pb_delete)
        self.pb_debug = QtGui.QPushButton(self.centralwidget)
        self.pb_debug.setObjectName("pb_debug")
        self.horizontalLayout.addWidget(self.pb_debug)
        self.cb_labelType = QtGui.QComboBox(self.centralwidget)
        self.cb_labelType.setObjectName("cb_labelType")
        self.horizontalLayout.addWidget(self.cb_labelType)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 809, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_prev.setText(QtGui.QApplication.translate("MainWindow", "show previous audio file", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_next.setText(QtGui.QApplication.translate("MainWindow", "show next audio file", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_save.setText(QtGui.QApplication.translate("MainWindow", "save", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_load.setText(QtGui.QApplication.translate("MainWindow", "load", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_toggle.setText(QtGui.QApplication.translate("MainWindow", "toggle", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_delete.setText(QtGui.QApplication.translate("MainWindow", "delete", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_debug.setText(QtGui.QApplication.translate("MainWindow", "debug", None, QtGui.QApplication.UnicodeUTF8))

