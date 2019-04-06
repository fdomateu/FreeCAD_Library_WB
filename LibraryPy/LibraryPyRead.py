# FreeCAD LibraryPyRead script of LibraryPy module

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

class StandardPartInfo():

    "The generic standard part info object from standard part object"

    def __init__(self):
        self.libraryPyObject = "LibraryPy::StandardPartInfo"
    
    def setObjectName(self):
        return self.libraryObject
    
    def setDescription(self, text):
        self.description = text
    
    def getDescription(self):
        if self.description != None:
            return self.description
        else:
            return None
    
    def setNorm(self, text):
        self.norm = text
    
    def getNorm(self):
        if self.norm != None:
            return self.norm
        else:
            return None

    def setOldNorm(self, text):
        self.oldNorm = text
    
    def getOldNorm(self):
        if self.oldNorm != None:
            return self.oldNorm
        else:
            return None
    
    def setIcon(self, iconFile):
        self.icon = iconFile
    
    def getIcon(self):
        if self.icon != None:
            return self.icon
        else:
            return None
    
    def setImage(self, drawingFile):
        self.image = drawingFile
    
    def getImage(self):
        if self.image != None:
            return self.image
        else:
            return None
    
    def setDimensions(self, dic):
        self.dimensions = dic
    
    def getDimensions(self):
        if self.dimensions != None:
            return self.dimensions
        else:
            return None
    
    def setGeometry(self, shape):
        self.geometry = shape
    
    def getGeometry(self):
        if self.geometry != None:
            return self.geometry
        else:
            return None
    
    def setRefineGeometry(self, shape):
        self.refineGeometry = shape
    
    def getRefineGeometry(self):
        if self.refineGeometry != None:
            return self.refineGeometry
        else:
            return None