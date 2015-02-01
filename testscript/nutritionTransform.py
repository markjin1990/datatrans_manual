import sys
sys.path.append('../lib/manipulation')
sys.path.append('../lib/io')

import transOp
import xmlOp
import csvOp

xmlOp.readXml("../testfile/nutrition.xml")

nameCol = xmlOp.findElements("name")
mfrCol = xmlOp.findElements("mfr")
servingCol = xmlOp.findElements("serving")
caloriesCol = xmlOp.findElements("calories")
totalFatCol = xmlOp.findElements("total-fat")
saturatedFatCol = xmlOp.findElements("saturated-fat")
cholesterolCol = xmlOp.findElements("cholesterol")
sodiumCol = xmlOp.findElements("sodium")
cardCol = xmlOp.findElements("carb")
fiberCol = xmlOp.findElements("fiber")
proteinCol = xmlOp.findElements("protein")
vitaminsACol = xmlOp.findElements("vitamins/a")
vitaminsCCol = xmlOp.findElements("vitamins/c")
mineralsCaCol = xmlOp.findElements("minenrals/ca")
mineralsFeCol = xmlOp.findElements("minenrals/fe")

relation = [nameCol,mfrCol,servingCol,caloriesCol,totalFatCol,saturatedFatCol,cholesterolCol,sodiumCol,cardCol,
fiberCol,proteinCol,proteinCol,vitaminsACol,vitaminsCCol,mineralsCaCol,mineralsCaCol]

for row in relation:
	for col in row:
		print col.text+","
	print "\n"