# FreeCAD initGui script of LibraryPyGui module

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

import FreeCAD, FreeCADGui
from PySide import QtCore, QtGui

class ImportStandardPart:
    "Create an standard part in the FreeCAD document"
    def GetResources(self):
        return {'Pixmap'  : 'Import_StandardPart',
                'MenuText': "Import Standard Part",
                'Accel': "",
                'ToolTip': "Insert an Standard Part"}
    
    def IsActive(self):
                if FreeCAD.ActiveDocument == None:
                        return False
                else:
                        return True

    def Activated(self):
        from LibraryPyStandardPart import _StandardPart
        from LibraryPyStandardPart import _ViewProviderStandardPart

        #a=FreeCAD.ActiveDocument.addObject("Part::FeaturePython","Test")
        #_StandardPart(a)
        #_ViewProviderStandardPart(a.ViewObject)
        #_ViewProviderStandardPart(a)
        #FreeCAD.ActiveDocument.recompute()

        Dialog = True
        TaskPanel = False

        if Dialog:
                import LibraryPyPopUpWindowCollectionNavigation
                Window = LibraryPyPopUpWindowCollectionNavigation.CollectionNaviationDialog()
                Window.exec_()
        
        if TaskPanel:
                from LibraryPyTaskPanels import ImportStandardPartPanel, CollectionTreePanelWidget, CollectionTreePanel
                FreeCADGui.Control.showDialog(ImportStandardPartPanel())


class ImportStandardAssembly:
    "Create an standard assembly in the FreeCAD document"
    def GetResources(self):
        return {'Pixmap'  : 'Import_StandardAssembly',
                'MenuText': "Import Standard Assembly",
                'Accel': "",
                'ToolTip': "Insert an standard Assembly"}
    
    def IsActive(self):
                if FreeCAD.ActiveDocument == None:
                        return False
                else:
                        return True

    def Activated(self):
        FreeCAD.Console.PrintMessage("Import Standard Assembly command still not available\n")

FreeCADGui.addCommand('Import_StandardPart', ImportStandardPart())
FreeCADGui.addCommand('Import_StandardAssembly', ImportStandardAssembly())