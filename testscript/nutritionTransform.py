import sys
sys.path.append('../lib/manipulation')
sys.path.append('../lib/io')

import transOp
import xmlOp

xmlOp.readXml("../testfile/nutrition.xml")

nameCol = xmlOp.findElements("food/name")
mfrCol = xmlOp.findElements("food/mfr")
servingCol = xmlOp.findElements("food/serving")
caloriesCol = xmlOp.findElements("food/calories")



totalFatCol = xmlOp.findElements("food/total-fat")
saturatedFatCol = xmlOp.findElements("food/saturated-fat")
cholesterolCol = xmlOp.findElements("food/cholesterol")
sodiumCol = xmlOp.findElements("food/sodium")
carbCol = xmlOp.findElements("food/carb")
fiberCol = xmlOp.findElements("food/fiber")
proteinCol = xmlOp.findElements("food/protein")
vitaminsACol = xmlOp.findElements("food/vitamins/a")
vitaminsCCol = xmlOp.findElements("food/vitamins/c")
mineralsCaCol = xmlOp.findElements("food/minerals/ca")
mineralsFeCol = xmlOp.findElements("food/minerals/fe")

relation = [nameCol,mfrCol,servingCol,caloriesCol,totalFatCol,saturatedFatCol,cholesterolCol,sodiumCol,carbCol,
fiberCol,proteinCol,proteinCol,vitaminsACol,vitaminsCCol,mineralsCaCol,mineralsCaCol]

relation = transOp.transpose(relation)



# Extract all values and create a relation
valueRelation = list()
for row in relation:
	newRow = list()
	for col in row:
		if col.text != None:
			newRow.append(col.text)

		if col.attrib != None:
			newRow = newRow + col.attrib.values()

		
		
	valueRelation.append(newRow)

#valueRelation.insert(0,["name","mfr","serving","unit","calories","total-fat","saturated-fat","cholesterol","sodium","carbCol",
#	"fiber","protein","vitamins/A","vitamins/C","minerals/Ca","mineralsFe"])

print "\nExtracted relation:"
for row in valueRelation:
	print row


# merge column 2 and 3
valueRelation = transOp.merge(valueRelation,2,3," ")

print "\nMerge column 2 and 3:"
for row in valueRelation:
	print row
			
# reform column 16 as 16(g) 
valueRelation = transOp.reform(valueRelation,16,"([\d|\.]+)\s+(\w+)","{0}({1})")

print "\nReform column 16 as \"number(unit)\":"
for row in valueRelation:
	print row

# Select low calories food(food that has less than 200 calories)
def pred(row):
	if float(row[2]) < 200:
		return True
	else:
		return False

valueRelation = transOp.select(valueRelation,pred)

print "\nSelect low calories food(food that has less than 200 calories):"
for row in valueRelation:
	print row

print "\nFinal Output:"
for row in valueRelation:
	print row