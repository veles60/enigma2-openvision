from enigma import RT_HALIGN_LEFT, RT_VALIGN_CENTER, eListboxPythonMultiContent, gFont

from skin import fonts, parameters
from Components.MenuList import MenuList
from Tools.Directories import SCOPE_GUISKIN, resolveFilename
from Tools.LoadPixmap import LoadPixmap


def ChoiceEntryComponent(key=None, text=None):
	if text is None:
		text = ["--"]
	res = [text]
	if text[0] == "--":
		x, y, w, h = parameters.get("ChoicelistDash", (0, 0, 800, 25))
		res.append((eListboxPythonMultiContent.TYPE_TEXT, x, y, w, h, 0, RT_HALIGN_LEFT | RT_VALIGN_CENTER, "-" * 200))
	else:
		if key:
			x, y, w, h = parameters.get("ChoicelistName", (45, 0, 800, 25))
			res.append((eListboxPythonMultiContent.TYPE_TEXT, x, y, w, h, 0, RT_HALIGN_LEFT | RT_VALIGN_CENTER, text[0]))
			if key == "dummy":
				png = None
			elif key == "expandable":
				png = LoadPixmap(resolveFilename(SCOPE_GUISKIN, "icons/expandable.png"))
			elif key == "expanded":
				png = LoadPixmap(resolveFilename(SCOPE_GUISKIN, "icons/expanded.png"))
			elif key == "verticalline":
				png = LoadPixmap(resolveFilename(SCOPE_GUISKIN, "icons/verticalline.png"))
			elif key == "bullet":
				png = LoadPixmap(resolveFilename(SCOPE_GUISKIN, "icons/bullet.png"))
			else:
				png = LoadPixmap(resolveFilename(SCOPE_GUISKIN, "buttons/key_%s.png" % key))
			if png:
				x, y, w, h = parameters.get("ChoicelistIcon", (5, 0, 35, 25))
				res.append((eListboxPythonMultiContent.TYPE_PIXMAP_ALPHABLEND, x, y, w, h, png))
		else:
			x, y, w, h = parameters.get("ChoicelistNameSingle", (5, 0, 800, 25))
			res.append((eListboxPythonMultiContent.TYPE_TEXT, x, y, w, h, 0, RT_HALIGN_LEFT | RT_VALIGN_CENTER, text[0]))
	return res


class ChoiceList(MenuList):
	def __init__(self, list, selection=0, enableWrapAround=False):
		MenuList.__init__(self, list, enableWrapAround, eListboxPythonMultiContent)
		font = fonts.get("ChoiceList", ("Regular", 20, 30))
		self.l.setFont(0, gFont(font[0], font[1]))
		self.l.setItemHeight(font[2])
		self.selection = selection

	def postWidgetCreate(self, instance):
		MenuList.postWidgetCreate(self, instance)
		self.moveToIndex(self.selection)
		self.instance.setWrapAround(True)
