import xml.etree.ElementTree as ET

tree = None

def readXml(name):
	global tree
	tree = ET.parse(name)

def findall(xpath):
	global tree
	root = tree.getroot()
	return root.findall(xpath)

# Find all tag elements, or the index-th tag element in the entire tree
def findElements(tag,index=-1,parent=None):
	global tree
	root = tree.getroot()
	if parent:
		tag = parent+"/"+tag

	if index > 0:
		return root.findall('.//'+tag)[index]
	else:
		return root.findall('.//'+tag)

# Find number of tag elements
def numOfElements(tag):
	global tree
	root = tree.getroot()
	return len(findElements(tag))



readXml("../testfile/nutrition.xml")
getChildTag(tree.getroot())
for child in findChild(tag = "a",parent = "vitamins"):
	print child.text

