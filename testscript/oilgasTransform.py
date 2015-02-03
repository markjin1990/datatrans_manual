import sys
sys.path.append('../lib/manipulation')
sys.path.append('../lib/io')

import transOp
import csvOp
import textOp


inputData = "../testfile/oilgas-allyears-states.txt"
relation = csvOp.readCsv(inputData)

print "\nInput data:"
for i in range(0,10):
	print relation[i]
print "length: "+str(len(relation))

relation = transOp.drop(relation,10)
relation = transOp.drop(relation,9)
relation = transOp.drop(relation,8)
relation = transOp.drop(relation,7)
relation = transOp.drop(relation,6)
relation = transOp.drop(relation,5)
relation = transOp.drop(relation,4)

print "\nDrop columns 4-10:"
for i in range(0,10):
	print relation[i]
print "length: "+str(len(relation))

relation = transOp.unfold(relation,2,3,ifContainAttributeRow =True)
relation = transOp.drop(relation,24)

print "\nUnfold column 2,3:"
for i in range(0,10):
	print relation[i]
print "length: "+str(len(relation))