# FreeCAD LibraryPyReadShapeInfo script of LibraryPy module

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

from LibraryPyRead import StandardPartInfo

class ShapeInfo(StandardPartInfo):

    "The standard part info object from standard shape object"

    def __init__(self):
        StandardPartInfo.__init__(self)
    
    def setSection(self, prop):
        self.section = prop
    
    def getSection(self):
        if self.section != None:
            return self.section
        else:
            return None
    
    def setPossibleSections(self):
        self.possections = list()
        if self.getDimensions() != None:
            self.possections.append(self.getDimensions().keys())
    
    def getPossibleSections(self):
        if self.possections != None:
            return self.possections
        else:
            return None