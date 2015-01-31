import xml.etree.ElementTree as ET

tree = None

def readXml(name):
	global tree
	tree = ET.parse(name)

def getChildTag(root):
	if root:
		for child in root:
			if child.text and child.text != "":
				print child.tag + ":" + str(child.text)
			else:
				print child.tag
			getChildTag(child)
	else:
		return

def findall(xpath):
	global tree
	root = tree.getroot()
	return root.findall(xpath)

# Find all tag elements, or the index-th tag element in the entire tree
def findChild(tag,index=-1,parent=None):
	global tree
	root = tree.getroot()
	if parent:
		tag = parent+"/"+tag

	if index > 0:
		return root.findall('.//'+tag)[index]
	else:
		return root.findall('.//'+tag)

# Find number of tag elements
def numOfChild(tag):
	global tree
	root = tree.getroot()
	return len(root.findall('.//'+tag))

readXml("../testfile/nutrition.xml")
for child in findChild(tag = "a",parent = "vitamins"):
	print child.text

