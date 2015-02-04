import sys
sys.path.append('../lib/manipulation')
sys.path.append('../lib/io')

import transOp
import csvOp

inputData = "../testfile/TSCAINV_wPMNACC_June2011.csv"
relation = csvOp.readCsv(inputData)

print "\nInput data:"
for i in range(0,10):
	print relation[i]
print "Length: "+str(len(relation))


# Select tuples who is not empty in column 4
def pred(row):
	if row[4] != '':
		return True
	else:
		return False

relation = transOp.select(relation=relation,pred=pred)
print "\nSelect tuples who is not empty in column 4:"
for i in range(0,10):
	print relation[i]
print "Length: "+str(len(relation))


def pred(s):
	if s == 'P; XU':
		return True
	else:
		return False

# Divide the column 4 into 2 columns based on if column 4 is "P; XU"
relation = transOp.divide(relation=relation,col=4,pred=pred,ifContainAttributeRow=True)
print "\nDivide the column 4 into 2 columns based on if column 4 is \"P; XU\":"
for i in range(0,10):
	print relation[i]
print "Length: "+str(len(relation))




