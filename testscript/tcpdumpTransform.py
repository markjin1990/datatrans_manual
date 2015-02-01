import sys
sys.path.append('../lib/manipulation')
sys.path.append('../lib/io')

import transOp
import textOp
import csvOp

inputData = textOp.readText("../testfile/tcpdump.txt")
print "\nInputData:"
print inputData

timeCol = textOp.extract(inputData=inputData,valueRegex="\d+\:\d+\:\d+\.\d+")
tosCol = textOp.extract(inputData=inputData,valueRegex="0x\d+",prefixRegex="tos ")
ttlCol = textOp.extract(inputData=inputData,valueRegex="\d+",prefixRegex="ttl  ")
idCol = textOp.extract(inputData=inputData,valueRegex="\d+",prefixRegex="id ")
offsetCol = textOp.extract(inputData=inputData,valueRegex="\d+",prefixRegex="offset ")
flagsCol = textOp.extract(inputData=inputData,valueRegex="[^\s\,]+",prefixRegex="flags ")
lengthCol = textOp.extract(inputData=inputData,valueRegex="\d+",prefixRegex="id ")

srcipCol = textOp.extract(inputData=inputData,valueRegex="\d+\.\d+\.\d+\.\d+",postfixRegex=" >")
dstipCol = textOp.extract(inputData=inputData,valueRegex="\d+\.\d+\.\d+\.\d+",prefixRegex="> ")


relation = [timeCol,tosCol,ttlCol,idCol,offsetCol,flagsCol,lengthCol,srcipCol,dstipCol]
relation = transOp.transpose(relation)


relation = transOp.merge(relation,7,8,">")
print "\nMerge column 7 and 8 with delimiter >"
print relation

relation = transOp.add(relation,[1,2])
print "\nAdd a column of index (row index)"
print relation

relation = transOp.moveColumn(relation,8,0)
print "\nMove the column of index to front"
print relation

print "\nOutput Relation:"
print relation
#csvOp.writeCsv(relation,"output.txt")
