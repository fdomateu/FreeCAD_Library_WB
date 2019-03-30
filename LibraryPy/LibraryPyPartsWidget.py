# FreeCAD LibraryPyPartsWidget script of LibraryPy module

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

# Definition of the standard part options widget depending on the information available

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
        self.valuenorm = QtGui.QComboBox()
        #self.valuenorm.currentIndexChanged.connect(self.updateUI(self.valuenorm.currentText()))
        self.normLayout.addWidget(QtGui.QLabel('Norm'), 0, 0)
        self.normLayout.addWidget(self.valuenorm, 0, 1)
        self.tabswidget.addTab(self.selectwidget, 'Select')
        self.tabswidget.addTab(self.infowidget, 'Info')
        self.mainLayout.addWidget(self.normwidget)
        self.mainLayout.addWidget(self.tabswidget)
        StandardPartOptionsWidget.updateUI(self)
    
    def updateUI(self):

        display = False
        self.selectwidget.pos = 0
        self.infowidget.pos = 0
        
        # Norm display

        if not display:
            self.infowidget.valuenorm = QtGui.QLineEdit()
            self.infowidget.valuenorm.setText('Norm from part')
            self.infowidget.valuenorm.setEnabled(False)
            self.infoLayout.addWidget(QtGui.QLabel('Norm'), self.infowidget.pos, 1)
            self.infoLayout.addWidget(self.infowidget.valuenorm, self.infowidget.pos + 1, 1)
            self.infowidget.pos += 2
        
        # Description display

        if not display:
            self.infowidget.valuedescription = QtGui.QLineEdit()
            self.infowidget.valuedescription.setText('Description from part')
            self.infowidget.valuedescription.setEnabled(False)
            self.infoLayout.addWidget(QtGui.QLabel('Description'), self.infowidget.pos, 1)
            self.infoLayout.addWidget(self.infowidget.valuedescription, self.infowidget.pos + 1, 1)
            self.infowidget.pos += 2
        
        # Old Norm display

        if not display:
            self.infowidget.valueoldnorm = QtGui.QLineEdit()
            self.infowidget.valueoldnorm.setText('Old Norm from part')
            self.infowidget.valueoldnorm.setEnabled(False)
            self.infoLayout.addWidget(QtGui.QLabel('Old Norm'), self.infowidget.pos, 1)
            self.infoLayout.addWidget(self.infowidget.valueoldnorm, self.infowidget.pos + 1, 1)
            self.infowidget.pos += 2
        
        # Manufacturer display

        if not display:
            self.infowidget.valuemanufacturer = QtGui.QLineEdit()
            self.infowidget.valuemanufacturer.setText('Manufacturer from part')
            self.infowidget.valuemanufacturer.setEnabled(False)
            self.infoLayout.addWidget(QtGui.QLabel('Manufacturer'), self.infowidget.pos, 1)
            self.infoLayout.addWidget(self.infowidget.valuemanufacturer, self.infowidget.pos + 1, 1)
            self.infowidget.pos += 2

        # Diameter selection combobox (Washes, Bolts, Pins, etc.)

        if not display:
            self.valuediameter = QtGui.QComboBox()
            self.selectLayout.addWidget(QtGui.QLabel('Diameter'), self.selectwidget.pos, 0)
            self.selectLayout.addWidget(self.valuediameter, self.selectwidget.pos, 1)
            self.selectwidget.pos += 1

        # Metric selection combobox (Screws, Nuts, etc.)

        if not display:
            self.valuemetric = QtGui.QComboBox()
            self.selectLayout.addWidget(QtGui.QLabel('Metric'), self.selectwidget.pos, 0)
            self.selectLayout.addWidget(self.valuemetric, self.selectwidget.pos, 1)
            self.selectwidget.pos += 1

        # Lenght selection combobox (Screws, Bolts, etc.)

        if not display:
            self.valuelenght = QtGui.QComboBox()
            self.selectLayout.addWidget(QtGui.QLabel('Lenght'), self.selectwidget.pos, 0)
            self.selectLayout.addWidget(self.valuelenght, self.selectwidget.pos, 1)
            self.selectwidget.pos += 1

        # Lenght selection box (profiles, shapes, etc.)

        if display:
            self.valuelenght = QtGui.QLineEdit()
            self.valuelenght.setEnabled(True)
            self.selectLayout.addWidget(QtGui.QLabel('Lenght'), self.selectwidget.pos, 0)
            self.selectLayout.addWidget(self.valuelenght, self.selectwidget.pos, 1)
            self.selectwidget.pos += 1

        # Model/Type selection box (profiles, shapes, etc.)

        if not display:
            self.valuetype = QtGui.QComboBox()
            self.selectLayout.addWidget(QtGui.QLabel('Model/Type'), self.selectwidget.pos, 0)
            self.selectLayout.addWidget(self.valuetype, self.selectwidget.pos, 1)
            self.selectwidget.pos += 1

        # Material combobox

        if not display:
            self.valuematerial = QtGui.QComboBox()
            self.selectLayout.addWidget(QtGui.QLabel('Material'), self.selectwidget.pos, 0)
            self.selectLayout.addWidget(self.valuematerial, self.selectwidget.pos, 1)
            self.selectwidget.pos += 1

        # icon display

        if display:
            self.icon = QtSvg.QSvgWidget("")
            self.icon.setMaximumWidth(200)
            self.icon.setMinimumHeight(120)
            self.infoLayout.addWidget(self.icon, 0, 0, self.infowidget.pos, 0)

        # image display

        if display:
            self.image = QtSvg.QSvgWidget("")
            self.image.setMaximumWidth(200)
            self.image.setMinimumHeight(120)
            self.selectLayout.addWidget(self.image, self.selectwidget.pos, 0)