import csv

relation = None

def readCsv(filename,delimiter=",",quotechar="\"",doublequote = True,escapechar=None,lineterminator="\r\n",quoting=csv.QUOTE_MINIMAL,skipinitialspace=False):
	global relation

	relation = list()

	csv.register_dialect('mydialect', delimiter=delimiter,quotechar=quotechar,doublequote=doublequote,escapechar=escapechar,lineterminator=lineterminator,quoting=quoting,skipinitialspace=skipinitialspace)

	f = open(filename, 'r')
	try:
		reader = csv.reader(f,dialect='mydialect')
		for row in reader:
			relation.append(row)
	finally:
		f.close()

	return relation

def writeCsv(relation,filename,delimiter=",",quotechar="\"",doublequote = True,escapechar=None,lineterminator="\r\n",quoting=csv.QUOTE_MINIMAL,skipinitialspace=False):
	f = open(filename, 'w')
	csv.register_dialect('mydialect', delimiter=delimiter,quotechar=quotechar,doublequote=doublequote,escapechar=escapechar,lineterminator=lineterminator,quoting=quoting,skipinitialspace=skipinitialspace)

	try:
		wr = csv.writer(f, dialect='mydialect')
		for row in relation:
			wr.writerow(row)
	finally:
		f.close()

	return