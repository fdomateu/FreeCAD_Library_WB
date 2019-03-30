# FreeCAD LibraryPyTaskPanels script of LibraryPy module

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
        
        # self.layout.addWidget(self.addpart)
    
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

# Definition of the collection panel

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

# Definition of the Standrd Part options panel

class StandardPartOptionsPanelWidget(QtGui.QWidget):

    def __init__(self):
        super(StandardPartOptionsPanelWidget, self).__init__()
        self.initUI()
    
    def initUI(self):
        from  LibraryPyPartsWidget import StandardPartOptionsWidget
        # formatting
        self.setWindowTitle('Standard Part')
        # Definition of the main layout
        self.mainLayout = QtGui.QGridLayout(self)
        # Definition of widget
        self.standardpartwidget = StandardPartOptionsWidget()
        # Introduction of widgets inside the main layout      
        self.mainLayout.addWidget(self.standardpartwidget)
    
class StandardPartOptionsPanel:
    def __init__(self):
        self.form = StandardPartOptionsPanelWidget()

# Definition of the importing option panel

class ImportOptionsWidget(QtGui.QWidget):

    # Definition of the buttons that define which type of FreeCAD object will be the standard part (object in the active document or link to object from other document) 

    def __init__(self):
        super(ImportOptionsWidget, self).__init__()
        self.initUI()
    
    def initUI(self):
        # formatting
        self.setWindowTitle('Import options')
        # Definition of the main layout
        self.mainLayout = QtGui.QVBoxLayout(self)
        self.mainLayout.setSpacing(5)
        
        # Introduction of widgets inside the main layout

        # Definition of the radio button to choose creating a link of the Standard Part. The standard part is created at a new FreeCAD document.

        self.CADOption = QtGui.QRadioButton('CAD Mechanics')
        self.CADOption.clicked.connect(self.onCADOption)
        self.CADOption.setText("CAD Mechanics")
        iconCAD = QtGui.QIcon()
        iconCAD.addPixmap(QtGui.QPixmap(FreeCAD.getHomePath() + "Mod/LibraryPy/Resources/icons/Part.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CADOption.setIcon(iconCAD)
        self.CADOption.setIconSize(QtCore.QSize(100, 20))
        self.CADOption.setChecked(True)  # default option

        # Definition of the radio button to choose creatin the Satandard part in the active document

        self.BIMOption = QtGui.QRadioButton('BIM model')
        self.BIMOption.clicked.connect(self.onBIMOption)
        self.BIMOption.setText("BIM model")
        iconBIM = QtGui.QIcon()
        iconBIM.addPixmap(QtGui.QPixmap(FreeCAD.getHomePath() + "Mod/LibraryPy/Resources/icons/BIM.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BIMOption.setIcon(iconBIM)
        self.BIMOption.setIconSize(QtCore.QSize(100, 20))

        # Definition of the layout 

        buttonGroup = QtGui.QButtonGroup()
        self.mainLayout.addWidget(self.CADOption)
        buttonGroup.addButton(self.CADOption)
        self.mainLayout.addWidget(self.BIMOption)
        buttonGroup.addButton(self.BIMOption)
    
    def onCADOption(self):
        self.encapsulateTypeChoosed = "CAD_Mechanics"
    
    def onBIMOption(self):
        self.encapsulateTypeChoosed = "BIM_model"
    

class ImportOptions:
    def __init__(self):
        self.form = ImportOptionsWidget()

# Creation of the general task panel for importing standard parts

class ImportStandardPartPanel:
    def __init__(self):
        self.form = [CollectionTreePanelWidget(), StandardPartOptionsPanelWidget(), ImportOptionsWidget()]   