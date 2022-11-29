# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'actForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1064, 730)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.projectPathLinedit = QtWidgets.QLineEdit(self.centralwidget)
        self.projectPathLinedit.setObjectName("projectPathLinedit")
        self.gridLayout.addWidget(self.projectPathLinedit, 1, 1, 1, 1)
        self.createSysAndPreModBtn = QtWidgets.QPushButton(self.centralwidget)
        self.createSysAndPreModBtn.setObjectName("createSysAndPreModBtn")
        self.gridLayout.addWidget(self.createSysAndPreModBtn, 5, 0, 1, 3)
        self.rawmodelButton = QtWidgets.QPushButton(self.centralwidget)
        self.rawmodelButton.setObjectName("rawmodelButton")
        self.gridLayout.addWidget(self.rawmodelButton, 0, 2, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 0, 0, 1, 1)
        self.openSpaceClaimBtn = QtWidgets.QPushButton(self.centralwidget)
        self.openSpaceClaimBtn.setObjectName("openSpaceClaimBtn")
        self.gridLayout.addWidget(self.openSpaceClaimBtn, 3, 0, 1, 3)
        self.projectPathBtn = QtWidgets.QPushButton(self.centralwidget)
        self.projectPathBtn.setObjectName("projectPathBtn")
        self.gridLayout.addWidget(self.projectPathBtn, 1, 2, 1, 1)
        self.endModePreBtn = QtWidgets.QPushButton(self.centralwidget)
        self.endModePreBtn.setObjectName("endModePreBtn")
        self.gridLayout.addWidget(self.endModePreBtn, 6, 0, 1, 3)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.rocketPathLinedit = QtWidgets.QLineEdit(self.centralwidget)
        self.rocketPathLinedit.setObjectName("rocketPathLinedit")
        self.gridLayout.addWidget(self.rocketPathLinedit, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.rawmodellineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.rawmodellineEdit.setObjectName("rawmodellineEdit")
        self.gridLayout.addWidget(self.rawmodellineEdit, 0, 1, 1, 1)
        self.rocketPathBtn = QtWidgets.QPushButton(self.centralwidget)
        self.rocketPathBtn.setObjectName("rocketPathBtn")
        self.gridLayout.addWidget(self.rocketPathBtn, 2, 2, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.minSizelineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.minSizelineEdit.setObjectName("minSizelineEdit")
        self.gridLayout_2.addWidget(self.minSizelineEdit, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        self.maxSizelineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.maxSizelineEdit.setObjectName("maxSizelineEdit")
        self.gridLayout_2.addWidget(self.maxSizelineEdit, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)
        self.curvatureNormalAnglineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.curvatureNormalAnglineEdit.setObjectName("curvatureNormalAnglineEdit")
        self.gridLayout_2.addWidget(self.curvatureNormalAnglineEdit, 2, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 3, 0, 1, 1)
        self.featureAnglelineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.featureAnglelineEdit.setObjectName("featureAnglelineEdit")
        self.gridLayout_2.addWidget(self.featureAnglelineEdit, 3, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 4, 0, 1, 1)
        self.firstAspectRatiolineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.firstAspectRatiolineEdit.setObjectName("firstAspectRatiolineEdit")
        self.gridLayout_2.addWidget(self.firstAspectRatiolineEdit, 4, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 5, 0, 1, 1)
        self.boiSizelineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.boiSizelineEdit.setObjectName("boiSizelineEdit")
        self.gridLayout_2.addWidget(self.boiSizelineEdit, 5, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 6, 0, 1, 1)
        self.boundaryNumlineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.boundaryNumlineEdit.setObjectName("boundaryNumlineEdit")
        self.gridLayout_2.addWidget(self.boundaryNumlineEdit, 6, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 7, 0, 1, 1)
        self.inletVelocitylineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.inletVelocitylineEdit.setObjectName("inletVelocitylineEdit")
        self.gridLayout_2.addWidget(self.inletVelocitylineEdit, 7, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 8, 0, 1, 1)
        self.inletTemplineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.inletTemplineEdit.setObjectName("inletTemplineEdit")
        self.gridLayout_2.addWidget(self.inletTemplineEdit, 8, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 9, 0, 1, 1)
        self.outPressurelineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.outPressurelineEdit.setObjectName("outPressurelineEdit")
        self.gridLayout_2.addWidget(self.outPressurelineEdit, 9, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 10, 0, 1, 1)
        self.iterNumlineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.iterNumlineEdit.setObjectName("iterNumlineEdit")
        self.gridLayout_2.addWidget(self.iterNumlineEdit, 10, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout.addWidget(self.label_15)
        self.multiCasesExcellineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.multiCasesExcellineEdit.setObjectName("multiCasesExcellineEdit")
        self.horizontalLayout.addWidget(self.multiCasesExcellineEdit)
        self.multiCasesExcelBtn = QtWidgets.QPushButton(self.centralwidget)
        self.multiCasesExcelBtn.setObjectName("multiCasesExcelBtn")
        self.horizontalLayout.addWidget(self.multiCasesExcelBtn)
        self.gridLayout_2.addLayout(self.horizontalLayout, 12, 0, 1, 2)
        self.startBtn = QtWidgets.QPushButton(self.centralwidget)
        self.startBtn.setObjectName("startBtn")
        self.gridLayout_2.addWidget(self.startBtn, 11, 0, 1, 2)
        self.multiCaseBtn = QtWidgets.QPushButton(self.centralwidget)
        self.multiCaseBtn.setObjectName("multiCaseBtn")
        self.gridLayout_2.addWidget(self.multiCaseBtn, 13, 0, 1, 2)
        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1064, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.createSysAndPreModBtn.setText(_translate("MainWindow", "创建workbengch流体计算系统(暂不可用)"))
        self.rawmodelButton.setText(_translate("MainWindow", "打开"))
        self.label_14.setText(_translate("MainWindow", "选择原始未处理模型"))
        self.openSpaceClaimBtn.setText(_translate("MainWindow", "打开SpaceClaim进行模型处理"))
        self.projectPathBtn.setText(_translate("MainWindow", "打开"))
        self.endModePreBtn.setText(_translate("MainWindow", "结束模型预处理(暂不可用)"))
        self.label_3.setText(_translate("MainWindow", "选择处理后的模型输出路径"))
        self.label.setText(_translate("MainWindow", "选择工程文件路径"))
        self.rocketPathBtn.setText(_translate("MainWindow", "打开"))
        self.label_2.setText(_translate("MainWindow", "全局网格最小尺寸(mm)"))
        self.minSizelineEdit.setText(_translate("MainWindow", "5"))
        self.label_4.setText(_translate("MainWindow", "全局网格最大尺寸(mm)"))
        self.maxSizelineEdit.setText(_translate("MainWindow", "50"))
        self.label_5.setText(_translate("MainWindow", "曲率角(deg)"))
        self.curvatureNormalAnglineEdit.setText(_translate("MainWindow", "18"))
        self.label_6.setText(_translate("MainWindow", "特征角度(deg)"))
        self.featureAnglelineEdit.setText(_translate("MainWindow", "40"))
        self.label_7.setText(_translate("MainWindow", "first aspect ratio "))
        self.firstAspectRatiolineEdit.setText(_translate("MainWindow", "8"))
        self.label_8.setText(_translate("MainWindow", "加密尺寸(mm)"))
        self.boiSizelineEdit.setText(_translate("MainWindow", "3"))
        self.label_9.setText(_translate("MainWindow", "边界层层数"))
        self.boundaryNumlineEdit.setText(_translate("MainWindow", "5"))
        self.label_10.setText(_translate("MainWindow", "速度入口速度(m/s)"))
        self.inletVelocitylineEdit.setText(_translate("MainWindow", "3"))
        self.label_11.setText(_translate("MainWindow", "速度入口温度(K)"))
        self.inletTemplineEdit.setText(_translate("MainWindow", "290"))
        self.label_12.setText(_translate("MainWindow", "压力出口压力(pa)"))
        self.outPressurelineEdit.setText(_translate("MainWindow", "100"))
        self.label_13.setText(_translate("MainWindow", "迭代次数"))
        self.iterNumlineEdit.setText(_translate("MainWindow", "100"))
        self.label_15.setText(_translate("MainWindow", "多工况输入文件"))
        self.multiCasesExcelBtn.setText(_translate("MainWindow", "打开"))
        self.startBtn.setText(_translate("MainWindow", "开始流体计算"))
        self.multiCaseBtn.setText(_translate("MainWindow", "多工况计算"))
