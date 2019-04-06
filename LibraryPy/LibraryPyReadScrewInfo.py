# FreeCAD LibraryPyReadScrewInfo script of LibraryPy module

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

class ScrewInfo(StandardPartInfo):

    "The standard part info object from standard screw object"

    def __init__(self):
        StandardPartInfo.__init__(self)
    
    def setMetric(self, prop):
        self.metric = prop
    
    def getMetric(self):
        if self.metric != None:
            return self.metric
        else:
            return None
    
    def setLength(self, prop):
        self.length = prop
    
    def getLength(self):
        if self.length != None:
            return self.length
        else:
            return None
    
    def setPitch(self, prop):
        self.pitch = prop
    
    def getPitch(self):
        if self.pitch != None:
            return self.pitch
        else:
            return None
    
    def setPossibleMetrics(self):
        self.posmetrics = list()
        if self.getDimensions() != None:
            for screw in self.getDimensions().keys():
                self.posmetrics.append(self.getDimensions()[screw][0])

    def getPossibleMetrics(self):
        if self.posmetrics != None:
            return self.posmetrics
        else:
            return None
    
    def setPossibleLengths(self):
        self.poslengths = list()
        if self.getDimensions() != None:
            for screw in self.getDimensions().keys():
                if self.getMetric() != None:
                    if self.getDimensions()[screw][0] == self.getMetric():
                        self.poslengths.append(self.getDimensions()[screw][1])
    
    def getPossibleLengths(self):
        if self.poslength != None:
            return self.poslength
        else:
            return None
    
    def setPossiblePitches(self):
        self.pospitches = list()
        if self.getDimensions() != None:
            for screw in self.getDimensions().keys():
                if self.getMetric() != None:
                    if self.getDimensions()[screw][0] == self.getMetric():
                        if self.getDimensions()[screw][2] not in self.pospitches:
                            self.pospitches.append(self.getDimensions()[screw][2])
   
    def getPossiblePitches(self):
        if self.pospitch != None:
            return self.pospitch
        else:
            return None