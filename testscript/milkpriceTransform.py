import sys
sys.path.append('../lib/manipulation')
sys.path.append('../lib/io')

import transOp
import csvOp
import textOp


inputData = "../testfile/milkprices.txt"
relation = csvOp.readCsv(inputData,delimiter=",",lineterminator="\r")

print "\nInput data:"
for row in relation:
	print row

relation = transOp.transpose(relation)
relation = transOp.drop(relation,17)
relation = transOp.drop(relation,16)
relation = transOp.drop(relation,15)
relation = transOp.drop(relation,14)
relation = transOp.drop(relation,9)
relation = transOp.drop(relation,8)
relation = transOp.drop(relation,3)
relation = transOp.drop(relation,2)
relation = transOp.drop(relation,0)
relation = transOp.transpose(relation)

print "\nExtract information:"
for row in relation:
	print row

relation = transOp.add(relation,["","Organic price 1","Organic price 1","Organic price 1","Organic price 1","Conventional price 1","Conventional price 1","Conventional price 1","Conventional price 1"])
relation = transOp.moveColumn(relation,13,0)
print "\nAdd column and move to front:"
for row in relation:
	print row

relation = transOp.fold(relation,[2,3,4,5,6,7,8,9,10,11,12,13],ifContainAttributeRow=True)
print "\nFold columns 2-13:"
for row in relation:
	print row