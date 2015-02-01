import csv

relation = None

def readCsv(filename,delimiter=",",quotechar="\"",doublequote = True,escapechar=None,lineterminator="\r\n",quoting=csv.QUOTE_MINIMAL,skipinitialspace=False):
	global relation

	relation = list()

	csv.register_dialect('mydialect', delimiter=delimiter,quotechar=quotechar,doublequote=doublequote,escapechar=escapechar,lineterminator=lineterminator,quoting=quoting,skipinitialspace=skipinitialspace)

	f = open(filename, 'rt')
	try:
		reader = csv.reader(f,dialect='mydialect')
		for row in reader:
			relation.append(row)
	finally:
		f.close()

	return relation

print len(readCsv("../testfile/TSCAINV_wCASRN_June2011.csv"))