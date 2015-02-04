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

# Extract information:
relation = transOp.transpose(relation = relation)
relation = transOp.drop(relation=relation,col=17)
relation = transOp.drop(relation=relation,col=16)
relation = transOp.drop(relation=relation,col=15)
relation = transOp.drop(relation=relation,col=14)
relation = transOp.drop(relation=relation,col=9)
relation = transOp.drop(relation=relation,col=8)
relation = transOp.drop(relation=relation,col=3)
relation = transOp.drop(relation=relation,col=2)
relation = transOp.drop(relation=relation,col=0)
relation = transOp.transpose(relation=relation)

print "\nExtract information:"
for row in relation:
	print row

# Add column and move to front:
relation = transOp.add(relation=relation,value=["","Organic price 1","Organic price 1","Organic price 1","Organic price 1","Conventional price 1","Conventional price 1","Conventional price 1","Conventional price 1"])
relation = transOp.moveColumn(relation=relation,origPosn=13,dstPosn=0)
print "\nAdd column and move to front:"
for row in relation:
	print row

# Format column 2-13 as Month:number
relation = transOp.reform(relation = relation,col=2,inputFormat = "(\d+\.\d+)",outputFormat="Jan.:{0}",ifContainAttributeRow=True)
relation = transOp.reform(relation = relation,col=3,inputFormat = "(\d+\.\d+)",outputFormat="Feb.:{0}",ifContainAttributeRow=True)
relation = transOp.reform(relation = relation,col=4,inputFormat = "(\d+\.\d+)",outputFormat="Mar.:{0}",ifContainAttributeRow=True)
relation = transOp.reform(relation = relation,col=5,inputFormat = "(\d+\.\d+)",outputFormat="Apr.:{0}",ifContainAttributeRow=True)
relation = transOp.reform(relation = relation,col=6,inputFormat = "(\d+\.\d+)",outputFormat="May:{0}",ifContainAttributeRow=True)
relation = transOp.reform(relation = relation,col=7,inputFormat = "(\d+\.\d+)",outputFormat="Jun.:{0}",ifContainAttributeRow=True)
relation = transOp.reform(relation = relation,col=8,inputFormat = "(\d+\.\d+)",outputFormat="Jul.:{0}",ifContainAttributeRow=True)
relation = transOp.reform(relation = relation,col=9,inputFormat = "(\d+\.\d+)",outputFormat="Aug.:{0}",ifContainAttributeRow=True)
relation = transOp.reform(relation = relation,col=10,inputFormat = "(\d+\.\d+)",outputFormat="Sep.:{0}",ifContainAttributeRow=True)
relation = transOp.reform(relation = relation,col=11,inputFormat = "(\d+\.\d+)",outputFormat="Oct.:{0}",ifContainAttributeRow=True)
relation = transOp.reform(relation = relation,col=12,inputFormat = "(\d+\.\d+)",outputFormat="Nov.:{0}",ifContainAttributeRow=True)
relation = transOp.reform(relation = relation,col=13,inputFormat = "(\d+\.\d+)",outputFormat="Dec.:{0}",ifContainAttributeRow=True)
print "\nFormat column 2-13 as Month:number"
for row in relation:
	print row

# Fold columns 2-13:
relation = transOp.fold(relation=relation,foldColumns=[2,3,4,5,6,7,8,9,10,11,12,13],ifContainAttributeRow=True)
print "\nFold columns 2-13:"
for row in relation:
	print row

# Split column 2 based on delimiter=:
relation = transOp.split(relation=relation,col=2,delimiter=":",ifContainAttributeRow =True)
print "\nSplit column 2 based on delimiter=: "
for row in relation:
	print row