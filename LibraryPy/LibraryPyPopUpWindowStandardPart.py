# FreeCAD LibraryPyPopUpWindowStandardPart script of LibraryPy module

#***************************************************************************
#*   Copyright (c) YEAR YOUR NAME         <Your e-mail address>            *
#*                                                                         *
#*   This file is part of the FreeCAD CAx development system.              *
#*                                                                         *
#*   This program is free software; you can redistribute it and/or modify  *
#*   it under the terms of the GNU Lesser General Public License (LGPL)    *
#*   as published by the Free Software Foundation; either version 2 of     *
#*   the License, or (at your option) any later version.                   *
#*   for detail see the LICENCE text file.                                 *
#*                                                                         *
#*   FreeCAD is distributed in the hope that it will be useful,            *
#*   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
#*   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
#*   GNU Lesser General Public License for more details.                   *
#*                                                                         *
#*   You should have received a copy of the GNU Library General Public     *
#*   License along with FreeCAD; if not, write to the Free Software        *
#*   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
#*   USA                                                                   *
#*                                                                         *
#***************************************************************************/

import sys, FreeCAD
from PySide import QtCore, QtGui, QtSvg
from PySide.QtCore import SIGNAL

# Definition of the list box for the election of one property (material, metric, lenth, section, etc.) from the standard part

class ListBoxPropWidget(QtGui.QGroupBox):

    # Definition of the list box of properties

    def __init__(self, prop):
        super(ListBoxPropWidget, self).__init__()
        self.initUI(prop)
    
    def initUI(self, prop):

        # Definition of main layout

        self.setTitle(prop)
        self.mainLayout = QtGui.QVBoxLayout(self)

        # Definition widget

        self.widgetList = QtGui.QListWidget()
        self.widgetList.itemDoubleClicked.connect(self.itemselect)
        self.mainLayout.addWidget(self.widgetList)

    def itemselect(self):

        "Defines the property selected"
        self.propSelected = None

# Definition of the selection tab from the main window

class StandardPartSelectionWidget(QtGui.QWidget):

    # Definition of the Table view tab

    def __init__(self):
        super(StandardPartSelectionWidget, self).__init__()
        self.initUI()
    
    def initUI(self):

        # Definition of main layout

        self.mainLayout = QtGui.QHBoxLayout(self)

        # image column definition

        self.imageColumn = QtGui.QWidget()
        self.imageColumnLayout = QtGui.QVBoxLayout(self.imageColumn)
        self.imageColumn.image = QtSvg.QSvgWidget("")
        self.imageColumn.image.setMaximumWidth(200)
        self.imageColumn.image.setMinimumHeight(120)
        self.imageColumnLayout.addWidget(self.imageColumn.image)
        self.imageColumnLayout.addItem(QtGui.QSpacerItem(30, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum))
        self.mainLayout.addWidget(self.imageColumn)

        # properties column definition

        self.metricList = ListBoxPropWidget("Metric")
        self.mainLayout.addWidget(self.metricList)
        self.lengthList = ListBoxPropWidget("Lenght")
        self.mainLayout.addWidget(self.lengthList)

# Definition of the properties table tab from the main window

class DimensionsTableWidget(QtGui.QWidget):

    # Definition of the Table view tab

    def __init__(self):
        super(DimensionsTableWidget, self).__init__()
        self.initUI()
    
    def initUI(self):

        # Definition of main layout

        self.mainLayout = QtGui.QHBoxLayout(self)

        # Definition of widgets

        self.dimensionsTable = QtGui.QTableWidget(self)
        #horHeaders = dimlist
        #verHeaders = []

        # Definition of the table dimensions

        #table.setRowCount(len(partlist.keys()))
        #table.setColumnCount(len(horHeaders))

        # Definition of each table cell

        #for n, key in enumerate(partlist.keys()):
            #verHeaders.append(key)
            #for m, item in enumerate(partlist[key]):
                #newitem = QtGui.QTableWidgetItem(item)
                #print (m,n,item)
                #table.setItem(m, n, newitem)
        
        #Add Header

        #table.setHorizontalHeaderLabels(horHeaders)
        #table.setVerticalHeaderLabels(verHeaders)
        self.dimensionsTable.resizeColumnsToContents()
        self.dimensionsTable.resizeRowsToContents()

        # Introduction of widgets inside main layout

        self.mainLayout.addWidget(self.dimensionsTable)

# Definition of the info tab from the main window

class StandardPartInfoWidget(QtGui.QGroupBox):

    # Definition of the Table view tab

    def __init__(self):
        super(StandardPartInfoWidget, self).__init__()
        self.initUI()
    
    def initUI(self):

        # Definition of main layout

        self.mainLayout = QtGui.QHBoxLayout(self)
        self.iconColumn = QtGui.QWidget()
        self.iconColumnLayout = QtGui.QVBoxLayout(self.iconColumn)
        self.infoColumn = QtGui.QWidget()
        self.infoColumnLayout = QtGui.QVBoxLayout(self.infoColumn)

        # icon column definition

        self.iconColumn.icon = QtSvg.QSvgWidget("")
        self.iconColumn.icon.setMaximumWidth(200)
        self.iconColumn.icon.setMinimumHeight(120)
        self.iconColumnLayout.addWidget(self.iconColumn.icon)
        self.iconColumnLayout.addItem(QtGui.QSpacerItem(30, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum))

        # info column definition

        display = True
        self.infoColumn.pos = 0
        
        # Norm display

        if display:
            self.infoColumn.valuenorm = QtGui.QLineEdit()
            self.infoColumn.valuenorm.setText('Norm from part')
            self.infoColumn.valuenorm.setEnabled(False)
            self.infoColumnLayout.addWidget(QtGui.QLabel('Norm'), self.infoColumn.pos, 1)
            self.infoColumnLayout.addWidget(self.infoColumn.valuenorm, self.infoColumn.pos + 1, 1)
            self.infoColumn.pos += 2
        
        # Description display

        if display:
            self.infoColumn.valuedescription = QtGui.QLineEdit()
            self.infoColumn.valuedescription.setText('Description from part')
            self.infoColumn.valuedescription.setEnabled(False)
            self.infoColumnLayout.addWidget(QtGui.QLabel('Description'), self.infoColumn.pos, 1)
            self.infoColumnLayout.addWidget(self.infoColumn.valuedescription, self.infoColumn.pos + 1, 1)
            self.infoColumn.pos += 2
        
        # Old Norm display

        if display:
            self.infoColumn.valueoldnorm = QtGui.QLineEdit()
            self.infoColumn.valueoldnorm.setText('Old Norm from part')
            self.infoColumn.valueoldnorm.setEnabled(False)
            self.infoColumnLayout.addWidget(QtGui.QLabel('Old Norm'), self.infoColumn.pos, 1)
            self.infoColumnLayout.addWidget(self.infoColumn.valueoldnorm, self.infoColumn.pos + 1, 1)
            self.infoColumn.pos += 2
        
        # Manufacturer display

        if display:
            self.infoColumn.valuemanufacturer = QtGui.QLineEdit()
            self.infoColumn.valuemanufacturer.setText('Manufacturer from part')
            self.infoColumn.valuemanufacturer.setEnabled(False)
            self.infoColumnLayout.addWidget(QtGui.QLabel('Manufacturer'), self.infoColumn.pos, 1)
            self.infoColumnLayout.addWidget(self.infoColumn.valuemanufacturer, self.infoColumn.pos + 1, 1)
            self.infoColumn.pos += 2
        
        self.infoColumnLayout.addItem(QtGui.QSpacerItem(30, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum))


        # Introduction of widgets inside main layout        

        self.mainLayout.addWidget(self.iconColumn)
        self.mainLayout.addWidget(self.infoColumn)

# Definition of the action buttons from the main window

class ActionButtonsWidget(QtGui.QWidget):

    # Definition of the Table view tab

    def __init__(self, w):
        super(ActionButtonsWidget, self).__init__()
        self.initUI()
        self.parent = w
    
    def initUI(self):

        # Definition of main layout

        self.mainLayout = QtGui.QHBoxLayout(self)

        # Definition of the buttons Accept, Apply, Cancel and Help

        self.pushButtonBox = QtGui.QGroupBox()
        self.pushbuttonsLayout = QtGui.QHBoxLayout()

        # Definition of the accept button

        self.acceptbutton = QtGui.QPushButton('accept')
        self.acceptbutton.clicked.connect(self.onAccept)
        self.acceptbutton.setCheckable(False)
        self.acceptbutton.setChecked(False)

        # Definition of the cancel button

        self.cancelbutton = QtGui.QPushButton('Cancel')
        self.cancelbutton.clicked.connect(self.onCancel)
        self.cancelbutton.setCheckable(False)
        self.cancelbutton.setChecked(False)

        # Definition of the help button

        self.helpbutton = QtGui.QPushButton()
        self.helpbutton.setCheckable(False)
        self.helpbutton.setChecked(False)
        self.helpbutton.setText("")
        self.iconHelp = QtGui.QIcon()
        self.iconHelp.addPixmap(QtGui.QPixmap(FreeCAD.getHomePath() + "Mod/Library/Resources/icons/help.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.helpbutton.setIcon(self.iconHelp)
        self.helpbutton.setIconSize(QtCore.QSize(24, 24))
        self.helpbutton.setToolTip("Help")

        # Definition of the layout

        self.pushbuttonsLayout.addWidget(self.helpbutton)
        self.spacerItem = QtGui.QSpacerItem(30, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.pushbuttonsLayout.addItem(self.spacerItem)
        self.pushbuttonsLayout.addWidget(self.acceptbutton)
        self.pushbuttonsLayout.addWidget(self.cancelbutton)
        self.pushButtonBox.setLayout(self.pushbuttonsLayout)
        self.mainLayout.addWidget(self.pushButtonBox)
    
    def onAccept(self):
        
        "If an standard part has been selected, the fle from the standard part has to be read and the LibraryPyPartWidget has to be displayed"

        self.parent.close()
        
    def onCancel(self):
        self.parent.close()

# Dialog to select the options from the selected standard part available 

class StandardPartDialog(QtGui.QDialog):

    def __init__(self):
        super(StandardPartDialog, self).__init__()
        self.initUI()
    
    def initUI(self):
        # formatting
        self.setGeometry(300, 200, 400, 500)
        self.setWindowTitle("Norm from selected part")

        # Definition of main layout

        self.mainLayout = QtGui.QVBoxLayout(self)

        # Introduction of widgets inside main layout

        self.selectTab = StandardPartSelectionWidget()
        self.tableTab = DimensionsTableWidget()
        self.infoTab = StandardPartInfoWidget()
        self.tabs = QtGui.QTabWidget()
        self.tabs.addTab(self.selectTab,"Select")	
        self.tabs.addTab(self.tableTab,"Table")
        self.tabs.addTab(self.infoTab,"Family Info")
        self.mainLayout.addWidget(self.tabs)
        self.buttons = ActionButtonsWidget(self)
        self.mainLayout.addWidget(self.buttons)

        # Command to show the window, it is a mast

        self.show()