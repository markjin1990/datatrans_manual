import sys
sys.path.append('../lib/manipulation')
sys.path.append('../lib/io')

import transOp
import xmlOp
import csvOp

xmlOp.readXml("../testfile/nutrition.xml")

nameCol = xmlOp.findElements("food/name")
mfrCol = xmlOp.findElements("food/mfr")
servingCol = xmlOp.findElements("food/serving")
caloriesCol = xmlOp.findElements("food/calories")



totalFatCol = xmlOp.findElements("food/total-fat")
saturatedFatCol = xmlOp.findElements("food/saturated-fat")
cholesterolCol = xmlOp.findElements("food/cholesterol")
sodiumCol = xmlOp.findElements("food/sodium")
cardCol = xmlOp.findElements("food/carb")
fiberCol = xmlOp.findElements("food/fiber")
proteinCol = xmlOp.findElements("food/protein")
vitaminsACol = xmlOp.findElements("food/vitamins/a")
vitaminsCCol = xmlOp.findElements("food/vitamins/c")
mineralsCaCol = xmlOp.findElements("food/minerals/ca")
mineralsFeCol = xmlOp.findElements("food/minerals/fe")

relation = [nameCol,mfrCol,servingCol,caloriesCol,totalFatCol,saturatedFatCol,cholesterolCol,sodiumCol,cardCol,
fiberCol,proteinCol,proteinCol,vitaminsACol,vitaminsCCol,mineralsCaCol,mineralsCaCol]

relation = transOp.transpose(relation)

valueRelation = list()
for row in relation:
	newRow = list()
	for col in row:
		if col.tag != None:
			newRow.append(col.tag)
		if col.attrib != None:
			newRow = newRow + col.attrib.values()
	valueRelation.append(newRow)
print valueRelation
			