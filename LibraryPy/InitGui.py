# FreeCAD initGui script of LibraryPy module

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

class LibraryPyWorkbench ( Workbench ):
    "LibraryPy workbench object"
    Icon = FreeCAD.getHomePath() + "Mod/LibraryPy/Resources/icons/Library.svg"
    MenuText = "LibraryPy"
    ToolTip = "LibraryPy workbench"

    def Initialize(self):
        # load the module
        import LibraryPyGui

        # self.appendToolbar(str(QtCore.QT_TRANSLATE_NOOP("LibraryPy","Import part")), cmdlst1)
        self.appendToolbar("LibraryPy", ["Import_StandardPart", "Import_StandardAssembly"])
        self.appendCommandbar("LibraryPy", ["Import_StandardPart", "Import_StandardAssembly"])
        self.appendMenu("LibraryPy", ["Import_StandardPart", "Import_StandardAssembly"])

        FreeCADGui.addIconPath(":/icons")
        # FreeCADGui.addLanguagePath(":/translations")
        # FreeCADGui.addPreferencePage(":/ui/preferences-library.ui')","LibraryPy")

    def Activated(self):
        
        from LibraryPyTaskPanelInit import InitTaskPanelWidget
        from PySide import QtGui, QtCore
        #FreeCADGui.Control.showDialog(InitTaskPanel())
        mw = FreeCADGui.getMainWindow()
        d = QtGui.QDockWidget()
        d.setWidget(InitTaskPanelWidget())
        mw.addDockWidget(QtCore.Qt.RightDockWidgetArea, d)
        #FreeCADGui.getMainWindow().addDockWidget(QtCore.Qt.RightDockWidgetArea, InitTaskPanelWidget)
        Msg("LibraryPyWorkbench::Activated()\n")
        Log("LibraryPy workbench activated\n")

    def Deactivated(self):
        #InitTaskPanelWidget.destroyed()
        Msg("LibraryPyWorkbench::Deactivated()\n")
        Log("LibraryPy workbench deactivated\n")

    def ContextMenu(self, recipient):
        self.appendContextMenu("LibraryPy", [])

    def GetClassName(self):
        return "Gui::PythonWorkbench"

FreeCADGui.addWorkbench(LibraryPyWorkbench)