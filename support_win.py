# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'support_win.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(246, 698)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frameComission_2 = QtWidgets.QFrame(Form)
        self.frameComission_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frameComission_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameComission_2.setObjectName("frameComission_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frameComission_2)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.clbImport = QtWidgets.QCommandLinkButton(self.frameComission_2)
        self.clbImport.setMaximumSize(QtCore.QSize(33, 16777215))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.clbImport.setFont(font)
        self.clbImport.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("import.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clbImport.setIcon(icon)
        self.clbImport.setDescription("")
        self.clbImport.setObjectName("clbImport")
        self.horizontalLayout_5.addWidget(self.clbImport)
        self.cmbFolders = QtWidgets.QComboBox(self.frameComission_2)
        self.cmbFolders.setObjectName("cmbFolders")
        self.horizontalLayout_5.addWidget(self.cmbFolders)
        self.verticalLayout.addWidget(self.frameComission_2)
        self.frameComission = QtWidgets.QFrame(Form)
        self.frameComission.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frameComission.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameComission.setObjectName("frameComission")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frameComission)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.leCostMin = QtWidgets.QLineEdit(self.frameComission)
        self.leCostMin.setObjectName("leCostMin")
        self.horizontalLayout.addWidget(self.leCostMin)
        self.leCostMax = QtWidgets.QLineEdit(self.frameComission)
        self.leCostMax.setObjectName("leCostMax")
        self.horizontalLayout.addWidget(self.leCostMax)
        self.leComission = QtWidgets.QLineEdit(self.frameComission)
        self.leComission.setMaximumSize(QtCore.QSize(80, 16777215))
        self.leComission.setObjectName("leComission")
        self.horizontalLayout.addWidget(self.leComission)
        self.verticalLayout.addWidget(self.frameComission)
        self.frameMetro = QtWidgets.QFrame(Form)
        self.frameMetro.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frameMetro.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameMetro.setObjectName("frameMetro")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frameMetro)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.leMetroMetersMax = QtWidgets.QLineEdit(self.frameMetro)
        self.leMetroMetersMax.setObjectName("leMetroMetersMax")
        self.horizontalLayout_6.addWidget(self.leMetroMetersMax)
        self.lblCount_2 = QtWidgets.QLabel(self.frameMetro)
        self.lblCount_2.setObjectName("lblCount_2")
        self.horizontalLayout_6.addWidget(self.lblCount_2)
        self.leMetroMinutesMax = QtWidgets.QLineEdit(self.frameMetro)
        self.leMetroMinutesMax.setObjectName("leMetroMinutesMax")
        self.horizontalLayout_6.addWidget(self.leMetroMinutesMax)
        self.lblCount_3 = QtWidgets.QLabel(self.frameMetro)
        self.lblCount_3.setObjectName("lblCount_3")
        self.horizontalLayout_6.addWidget(self.lblCount_3)
        self.verticalLayout.addWidget(self.frameMetro)
        self.lwStatuses = QtWidgets.QListWidget(Form)
        self.lwStatuses.setMaximumSize(QtCore.QSize(16777215, 60))
        self.lwStatuses.setObjectName("lwStatuses")
        self.verticalLayout.addWidget(self.lwStatuses)
        self.lwCards = QtWidgets.QListWidget(Form)
        self.lwCards.setObjectName("lwCards")
        self.verticalLayout.addWidget(self.lwCards)
        self.frameOkCncl = QtWidgets.QFrame(Form)
        self.frameOkCncl.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameOkCncl.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameOkCncl.setObjectName("frameOkCncl")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frameOkCncl)
        self.horizontalLayout_4.setContentsMargins(-1, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.clbLoad = QtWidgets.QCommandLinkButton(self.frameOkCncl)
        self.clbLoad.setMaximumSize(QtCore.QSize(33, 16777215))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.clbLoad.setFont(font)
        self.clbLoad.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("reload.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clbLoad.setIcon(icon1)
        self.clbLoad.setDescription("")
        self.clbLoad.setObjectName("clbLoad")
        self.horizontalLayout_4.addWidget(self.clbLoad)
        spacerItem = QtWidgets.QSpacerItem(111, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.lblCount = QtWidgets.QLabel(self.frameOkCncl)
        self.lblCount.setObjectName("lblCount")
        self.horizontalLayout_4.addWidget(self.lblCount)
        spacerItem1 = QtWidgets.QSpacerItem(111, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.clbUpdate = QtWidgets.QCommandLinkButton(self.frameOkCncl)
        self.clbUpdate.setMaximumSize(QtCore.QSize(33, 16777215))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.clbUpdate.setFont(font)
        self.clbUpdate.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("ok.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clbUpdate.setIcon(icon2)
        self.clbUpdate.setDescription("")
        self.clbUpdate.setObjectName("clbUpdate")
        self.horizontalLayout_4.addWidget(self.clbUpdate)
        self.verticalLayout.addWidget(self.frameOkCncl)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.cmbStatus = QtWidgets.QComboBox(self.frame)
        self.cmbStatus.setObjectName("cmbStatus")
        self.horizontalLayout_2.addWidget(self.cmbStatus)
        self.lblComission = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblComission.sizePolicy().hasHeightForWidth())
        self.lblComission.setSizePolicy(sizePolicy)
        self.lblComission.setText("")
        self.lblComission.setObjectName("lblComission")
        self.horizontalLayout_2.addWidget(self.lblComission)
        self.verticalLayout.addWidget(self.frame)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(Form)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.verticalLayout.addWidget(self.dateTimeEdit)
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lePhone1 = QtWidgets.QLineEdit(self.frame_2)
        self.lePhone1.setObjectName("lePhone1")
        self.horizontalLayout_3.addWidget(self.lePhone1)
        self.clbTrash = QtWidgets.QCommandLinkButton(self.frame_2)
        self.clbTrash.setMaximumSize(QtCore.QSize(33, 16777215))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.clbTrash.setFont(font)
        self.clbTrash.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../crmand/trash.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clbTrash.setIcon(icon3)
        self.clbTrash.setDescription("")
        self.clbTrash.setObjectName("clbTrash")
        self.horizontalLayout_3.addWidget(self.clbTrash)
        self.lePhone2 = QtWidgets.QLineEdit(self.frame_2)
        self.lePhone2.setObjectName("lePhone2")
        self.horizontalLayout_3.addWidget(self.lePhone2)
        self.verticalLayout.addWidget(self.frame_2)
        self.leNote = QtWidgets.QLineEdit(Form)
        self.leNote.setObjectName("leNote")
        self.verticalLayout.addWidget(self.leNote)
        self.lwCalls = QtWidgets.QListWidget(Form)
        self.lwCalls.setObjectName("lwCalls")
        self.verticalLayout.addWidget(self.lwCalls)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.leCostMin.setText(_translate("Form", "0"))
        self.leCostMax.setText(_translate("Form", "100000"))
        self.leComission.setText(_translate("Form", "50"))
        self.leMetroMetersMax.setText(_translate("Form", "10000"))
        self.lblCount_2.setText(_translate("Form", "м"))
        self.leMetroMinutesMax.setText(_translate("Form", "45"))
        self.lblCount_3.setText(_translate("Form", "мин"))
        self.lblCount.setText(_translate("Form", "0"))

