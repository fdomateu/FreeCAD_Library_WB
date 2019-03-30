# FreeCAD LibraryPyStandardPart script of LibraryPy module

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
        
class _StandardPart:

	"The Standard Part object from libraryPy workbench"

	def __init__(self, obj):
		self.Type = "StandardPart"
		obj.addExtension('App::OriginGroupExtensionPython', self)
		obj.Proxy = self
		# Definition of properties
		self.setProperties(obj)

	def setProperties(self,obj):
		propList = obj.PropertiesList
        if not "Label" in propList:
            obj.addProperty("App::PropertyString","Label","Base","Label")
        if not "License" in propList:
            obj.addProperty("App::PropertyString","License","Base","License")
        if not "License URL" in propList:
            obj.addProperty("App::PropertyString","License URL","Base","License URL")
        if not "Base Feature" in propList:
            obj.addProperty("App::PropertyLinkChild","BaseFeature","Base","Base Feature")
        if not "Placement" in propList:
            obj.addProperty("App::PropertyPlacement","Placement","Base","Placement")
        if not "Material" in propList:
            obj.addProperty("App::PropertyLink","Material","Base","Material")
		if not "Color" in propList:
			obj.addProperty("App::PropertyColor","Color","Base","Color")
		if not "Group" in propList:
			obj.addProperty("App::PropertyLinkList","Group","Base","Group")

class _ViewProviderStandardPart:

    "A View Provider for the Standard Part object"

	def __init__(self, obj):
		''' Set this object to the proxy object of the actual view provider '''
        obj.addExtension("Gui::ViewProviderGeoFeatureGroupExtensionPython", self)
        obj.Proxy = self

	def attach(self, obj):
		''' Setup the scene sub-graph of the view provider, this method is mandatory '''
		return

	def updateData(self, fp, prop):
		''' If a property of the handled feature has changed we have the chance to handle this here '''
		return

	def getDisplayModes(self,obj):
		''' Return a list of display modes. '''
		modes=[]
		return modes

	def getDefaultDisplayMode(self):
		''' Return the name of the default display mode. It must be defined in getDisplayModes. '''
		return "Shaded"

	def setDisplayMode(self,mode):
		''' Map the display mode defined in attach with those defined in getDisplayModes.
		Since they have the same names nothing needs to be done. This method is optional.
		'''
		return mode

	def onChanged(self, vp, prop):
		''' Print the name of the property that has changed '''
		return prop

	def getIcon(self):
		''' Return the icon in XMP format which will appear in the tree view. This method is optional
		and if not defined a default icon is shown.
		'''
		return 

	def __getstate__(self):
		''' When saving the document this object gets stored using Python's cPickle module.
		Since we have some un-pickable here -- the Coin stuff -- we must define this method
		to return a tuple of all pickable objects or None.
		'''
		return None

	def __setstate__(self,state):
		''' When restoring the pickled object from document we have the chance to set some
		internals here. Since no data were pickled nothing needs to be done here.
		'''
		return None