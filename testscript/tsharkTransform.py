import sys
sys.path.append('../lib/manipulation')
sys.path.append('../lib/io')

import transOp
import textOp
import csvOp

inputData = textOp.readText("../testfile/tshark.txt")
print "\nInputData:"
print inputData

indexCol = textOp.extract(inputData=inputData,valueRegex="\d{3}",postfixRegex="\s{2}\d+\.\d{6}")
timeCol = textOp.extract(inputData=inputData,valueRegex="\d+\.\d{6}")
srcipCol = textOp.extract(inputData=inputData,valueRegex="\d+\.\d+\.\d+\.\d+",postfixRegex="\s->")
dstipCol = textOp.extract(inputData=inputData,valueRegex="\d+\.\d+\.\d+\.\d+",prefixRegex="->\s")
versionCol = textOp.extract(inputData=inputData,valueRegex="[^\s]+",prefixRegex="HTTP\s",postfixRegex="\s\d+")
statusCol = textOp.extract(inputData=inputData,valueRegex="\d+\s\w+",postfixRegex="\s{2}\([\w|\s]+\)")
contentTypeCol = textOp.extract(inputData=inputData,valueRegex="[\w|\/]+",prefixRegex='==\s\\"',postfixRegex='\\"')
contentLengthCol = textOp.extract(inputData=inputData,valueRegex="\d+",prefixRegex="http\.content_length\s==\s")


relation = [indexCol,timeCol,srcipCol,dstipCol,versionCol,statusCol,contentTypeCol,contentLengthCol]
relation = transOp.transpose(relation)


print "\nExtracted Relation"
for row in relation:
	print row

relation = transOp.split(relation,4,'/')
print "\nSplit column 4 by /"
for row in relation:
	print row
#csvOp.writeCsv(relation,"output.txt")
