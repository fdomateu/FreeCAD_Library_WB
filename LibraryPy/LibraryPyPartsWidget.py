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

# Definition of the standard part options widget depending on the information available

import sys, FreeCAD
from PySide import QtCore, QtGui

class StandardPartOptionsWidget(QtGui.QWidget):

    def __init__(self):
        super(StandardPartOptionsWidget, self).__init__()
        self.initUI()
    
    def initUI(self):
        # Definition of the main layout
        self.mainLayout = QtGui.QGridLayout(self)
        self.mainLayout.setSpacing(0)
        # Introduction of widgets inside the main layout
        self.normwidget = QtGui.QWidget()
        self.normLayout = QtGui.QGridLayout(self.normwidget)
        self.tabswidget = QtGui.QTabWidget()
        self.selectwidget = QtGui.QWidget()
        self.selectLayout = QtGui.QGridLayout(self.selectwidget)
        self.infowidget = QtGui.QWidget()
        self.infoLayout = QtGui.QGridLayout(self.infowidget)

        labelnorm = QtGui.QLabel('Norm')
        self.valuenorm = QtGui.QComboBox()
        #self.valuenorm.currentIndexChanged.connect(self.updateUI(self.valuenorm.currentText()))
        #selectwidgetpos = 0
        self.normLayout.addWidget(labelnorm, 0, 0)
        self.normLayout.addWidget(self.valuenorm, 0, 1)
        self.tabswidget.addTab(self.selectwidget, 'Select')
        self.tabswidget.addTab(self.infowidget, 'Info')
        self.mainLayout.addWidget(self.normwidget)
        self.mainLayout.addWidget(self.tabswidget)
        StandardPartOptionsWidget.updateUI(self)
    
    def updateUI(self):

        display = False
        selectwidgetpos = 0
        # image display

        if display:
            self.image = QtSvg.QSvgWidget("")
            self.image.setMaximumWidth(200)
            self.image.setMinimumHeight(120)
            self.selectLayout.addWidget(self.image, selectwidgetpos, 0)
            selectwidgetpos += 1

        # Diameter selection combobox (Washes, Bolts, Pins, etc.)

        if not display:
            labeldiameter = QtGui.QLabel('Diameter')
            self.valuediameter = QtGui.QComboBox()
            self.selectLayout.addWidget(labeldiameter, selectwidgetpos, 0)
            self.selectLayout.addWidget(self.valuediameter, selectwidgetpos, 1)
            selectwidgetpos += 1

        # Metric selection combobox (Screws, Nuts, etc.)

        if not display:
            labelmetric = QtGui.QLabel('Metric')
            self.valuemetric = QtGui.QComboBox()
            self.selectLayout.addWidget(labelmetric, selectwidgetpos, 0)
            self.selectLayout.addWidget(self.valuemetric, selectwidgetpos, 1)
            selectwidgetpos += 1

        # Lenght selection combobox (Screws, Bolts, etc.)

        if not display:
            labellenght = QtGui.QLabel('Lenght')
            self.valuelenght = QtGui.QComboBox()
            self.selectLayout.addWidget(labellenght, selectwidgetpos, 0)
            self.selectLayout.addWidget(self.valuelenght, selectwidgetpos, 1)
            selectwidgetpos += 1

        # Lenght selection box (profiles, shapes, etc.)

        if display:
            labellenght = QtGui.QLabel('Lenght')
            self.valuelenght = QtGui.QTextBox()
            self.selectLayout.addWidget(labellenght, selectwidgetpos, 0)
            self.selectLayout.addWidget(self.valuelenght, selectwidgetpos, 1)
            selectwidgetpos += 1

        # Model/Type selection box (profiles, shapes, etc.)

        if not display:
            labeltype = QtGui.QLabel('Model/Type')
            self.valuetype = QtGui.QComboBox()
            self.selectLayout.addWidget(labeltype, selectwidgetpos, 0)
            self.selectLayout.addWidget(self.valuetype, selectwidgetpos, 1)
            selectwidgetpos += 1

        # Material combobox

        if not display:
            labelmaterial = QtGui.QLabel('Material')
            self.valuematerial = QtGui.QComboBox()
            self.selectLayout.addWidget(labelmaterial, selectwidgetpos, 0)
            self.selectLayout.addWidget(self.valuematerial, selectwidgetpos, 1)
            selectwidgetpos += 1