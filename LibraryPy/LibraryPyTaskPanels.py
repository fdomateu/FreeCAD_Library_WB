# FreeCAD TaskPableLibraryPy script of LibraryPy module

#***************************************************************************
#*   Copyright (c) 2019 Fernando Mateu    <fdomateu@gmail.com>             *
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

# Definition of the panel which should be displayed when the Library Workbench is activated

class InitTaskPanelWidget(QtGui.QDockWidget):

    def __init__(self):
        super(InitTaskPanelWidget, self).__init__()
        self.initUI()

    def initUI(self):
        # formatting
        self.setWindowTitle('Standard part')
        self.layout = QtGui.QHBoxLayout()
        
        self.layout.addWidget(self.addpart)
    
    def onStandardPart():
        pass

class InitTaskPanel:
    def __init__(self):
        self.form = InitTaskPanelWidget()

#class InitTaskPanel:
#    def __init__(self):
#        self.mw = FreeCADGui.getMainWindow()
#    def show(self, DockWidget):
#        self.mw.addDockWidget(QtCore.Qt.RightDockWidgetArea, DockWidget)

# Definition of the panel which should be displayed when the command create Standard Part is activated

class CollectionTreePanelWidget(QtGui.QWidget):

    def __init__(self):
        super(CollectionTreePanelWidget, self).__init__()
        self.initUI()
    
    def initUI(self):
        # formatting
        self.setWindowTitle('Collection')
        # Definition of the main layout
        self.mainLayout = QtGui.QGridLayout(self)
        # Definition of tree widget
        self.categorytree = QtGui.QTreeWidget()
        self.categorytree.setColumnCount(1)
        self.categorytree.header().hide()
        # Introduction of widgets inside the main layout      
        self.mainLayout.addWidget(self.categorytree)
    
    def itemClicked(self):
        print('Item clicked')

class CollectionTreePanel:
    def __init__(self):
        self.form = CollectionTreePanelWidget()

class ImportStandardPartPanel:
    def __init__(self):
        self.form = [CollectionTreePanelWidget()]
        