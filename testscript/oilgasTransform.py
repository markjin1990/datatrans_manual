import sys
sys.path.append('../lib/manipulation')
sys.path.append('../lib/io')

import transOp
import csvOp
import textOp


inputData = "../testfile/oilgas-allyears-states.txt"
relation = csvOp.readCsv(inputData)
relation = transOp.removeEmpty(relation=relation)

print "\nInput data:"
for i in range(0,10):
	print relation[i]
print "length: "+str(len(relation))

# Drop columns 4-10:
relation = transOp.drop(relation=relation,col=10)
relation = transOp.drop(relation=relation,col=9)
relation = transOp.drop(relation=relation,col=8)
relation = transOp.drop(relation=relation,col=7)
relation = transOp.drop(relation=relation,col=6)
relation = transOp.drop(relation=relation,col=5)
relation = transOp.drop(relation=relation,col=4)

print "\nDrop columns 4-10:"
for i in range(0,10):
	print relation[i]
print "length: "+str(len(relation))

# Unfold column 2,3:
relation = transOp.unfold(relation=relation,col1=2,col2=3,ifContainAttributeRow =True)

print "\nUnfold column 2,3:"
for i in range(0,10):
	print relation[i]
print "length: "+str(len(relation))