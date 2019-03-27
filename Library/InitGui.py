#/***************************************************************************
#*   Copyright (c) YEAR YOUR NAME         <Your e-mail address>            *
#*                                                                         *
#*   This file is part of the FreeCAD CAx development system.              *
#*                                                                         *
#*   This library is free software; you can redistribute it and/or         *
#*   modify it under the terms of the GNU Library General Public           *
#*   License as published by the Free Software Foundation; either          *
#*   version 2 of the License, or (at your option) any later version.      *
#*                                                                         *
#*   This library  is distributed in the hope that it will be useful,      *
#*   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
#*   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
#*   GNU Library General Public License for more details.                  *
#*                                                                         *
#*   You should have received a copy of the GNU Library General Public     *
#*   License along with this library; see the file COPYING.LIB. If not,    *
#*   write to the Free Software Foundation, Inc., 59 Temple Place,         *
#*   Suite 330, Boston, MA  02111-1307, USA                                *
#*                                                                         *
# ***************************************************************************/

class LibraryWorkbench ( Workbench ):
    "Library workbench object"
    def __init__(self):
        self.__class__.Icon = FreeCAD.getResourceDir() + "Mod/Library/Resources/icons/LibraryWorkbench.svg"
        self.__class__.MenuText = "Library"
        self.__class__.ToolTip = "Library workbench"

    def Initialize(self):
        # load the module
        import LibraryGui
        import Library

    def GetClassName(self):
        return "LibraryGui::Workbench"

Gui.addWorkbench(LibraryWorkbench())
