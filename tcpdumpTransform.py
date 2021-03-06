import lib.manipulation.transOp as transOp
import lib.manipulation.textOp as textOp
import lib.io.csvOp as csvOp

inputData = textOp.readText("./testfile/tcpdump.txt")

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
print relation
#csvOp.writeCsv(relation,"output.txt")
