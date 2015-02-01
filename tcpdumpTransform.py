import lib.transOp as transOp
import lib.textOp as textOp

inputData = textOp.readText("./testfile/tcpdump.txt")
lengthCol = textOp.extract(inputData=inputData,valueRegex="\d+",prefixRegex="id ")
print lengthCol
