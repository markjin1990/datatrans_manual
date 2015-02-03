import sys
sys.path.append('../lib/manipulation')
sys.path.append('../lib/io')

import transOp
import csvOp
import textOp


inputData = "../testfile/milkprices.txt"
relation = csvOp.readCsv(inputData)

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


relation = transOp.reform(relation,2,"(\d+\.\d+)","Jan.:{0}",True)
relation = transOp.reform(relation,3,"(\d+\.\d+)","Feb.:{0}",True)
relation = transOp.reform(relation,4,"(\d+\.\d+)","Mar.:{0}",True)
relation = transOp.reform(relation,5,"(\d+\.\d+)","Apr.:{0}",True)
relation = transOp.reform(relation,6,"(\d+\.\d+)","May:{0}",True)
relation = transOp.reform(relation,7,"(\d+\.\d+)","Jun.:{0}",True)
relation = transOp.reform(relation,8,"(\d+\.\d+)","Jul.:{0}",True)
relation = transOp.reform(relation,9,"(\d+\.\d+)","Aug.:{0}",True)
relation = transOp.reform(relation,10,"(\d+\.\d+)","Sep.:{0}",True)
relation = transOp.reform(relation,11,"(\d+\.\d+)","Oct.:{0}",True)
relation = transOp.reform(relation,12,"(\d+\.\d+)","Nov.:{0}",True)
relation = transOp.reform(relation,13,"(\d+\.\d+)","Dec.:{0}",True)
print "\nFormat column 2-13 as Month:number"
for row in relation:
	print row


relation = transOp.fold(relation,[2,3,4,5,6,7,8,9,10,11,12,13],ifContainAttributeRow=True)
print "\nFold columns 2-13:"
for row in relation:
	print row

relation = transOp.split(relation,2,delimiter=":",ifContainAttributeRow =True)
print "\nSplit column 2 based on delimiter=: "
for row in relation:
	print row