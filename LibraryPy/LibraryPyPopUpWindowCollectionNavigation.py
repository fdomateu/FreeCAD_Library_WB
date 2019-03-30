# FreeCAD LibraryPyPopUpWindowCollectionNavigation script of LibraryPy module

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
from PySide import QtCore, QtGui
from PySide.QtCore import SIGNAL

# Definition of the action buttons from the main window

class ActionButtonsWidget(QtGui.QWidget):

    # Definition of the Table view tab

    def __init__(self):
        super(ActionButtonsWidget, self).__init__()
        self.initUI()
    
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
        import LibraryPyPopUpWindowStandardPart
        Window = LibraryPyPopUpWindowStandardPart.StandardPartDialog()
        self.close()
        Window.exec_()
        
    def onCancel(self):
        self.close()

# Dialog to navigate arround the collection directory

class CollectionNaviationDialog(QtGui.QDialog):

    def __init__(self):
        super(CollectionNaviationDialog, self).__init__()
        self.initUI()
    
    def initUI(self):
        # formatting
        self.setGeometry(300, 200, 400, 500)
        self.setWindowTitle("FreeCAD Collection")

        # Definition of main layout

        self.mainLayout = QtGui.QVBoxLayout(self)

        # Introduction of widgets inside main layout
        self.buttons = ActionButtonsWidget()
        self.mainLayout.addWidget(self.buttons)

        # Command to show the window, it is a mast

        self.show()
    
    def mainWidget(self):
            
        # Definition of the main widget
    
    def selectFamily(self):
        "Event to display the family list when a familly has been selected with doble click at the tree/grid window"
    
    def selectStandardPart(self):
        "Close dialog and display StandardPartOptionsDialog when a standard part has been selected with doble click at the tree/folder window or at the case of pushing the accept button with a standard part selected"