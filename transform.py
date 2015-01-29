
# Library
import sys
import subprocess
import re
import csv
import json

# Constants



class Transform:
	
	data = "";
	relation = list();
	attr_list = list();

	attr_timestamp = "time"
	attr_tos = "tos"
	attr_ttl = "ttl"
	attr_id = "id"
	attr_offset = "offset"
	attr_flag = "flag"
	attr_length = "length"
	attr_srcip = "srcip"
	attr_tarip = "tarip"


	attr_list.append(attr_length)
	attr_list.append(attr_flag)
	attr_list.append(attr_offset)
	attr_list.append(attr_id)
	attr_list.append(attr_ttl)
	attr_list.append(attr_tos)
	attr_list.append(attr_timestamp)
	attr_list.append(attr_srcip)
	attr_list.append(attr_tarip)



	relation.append(attr_list)

	



	
	def txtReader(self,fn):
		f = open(fn, "r")		
		text = f.read()
		return text

	def binReader(self,fn):
		f = open(fn, "rb")		

		text = f.read()
		return text

	# We want \s be the only delimiter
	def dataClearn(self,mydata):
		mydata = mydata.replace(',','')
		mydata = mydata.replace('\n','')
		mydata = mydata.replace('(','')
		mydata = mydata.replace(')','')
		mydata = mydata.replace('\t','')

		dataArray = mydata.split(" ")
		newDataArray = list()
		for idx,datum in enumerate(dataArray):
			datumToAdd = datum

			# Remove : if ":" is in the end of the string
			if len(datum) > 0 and datum[len(datum)-1] == ':':
				datumToAdd = datum[:len(datum)-1]

			# Remove space or empty string
			if datumToAdd != '\s' and datumToAdd != '':
				newDataArray.append(datumToAdd)

		mydata = " ".join(newDataArray)

		return mydata


	def is_text(self,fn):
		msg = subprocess.Popen(["file", fn], stdout=subprocess.PIPE).communicate()[0]
		return re.search('text', msg) != None

	# Merge column 1 and column 2 with a delimiter in the middle
	def merge(self,relation,col1,col2,delimiter):
		newRelation = list()
		for idx,row in enumerate(relation):
			row.append(row[col1] + delimiter + row[col2])
			if col1 > col2:
				row.pop(col1)
				row.pop(col2)
			else:
				row.pop(col2)
				row.pop(col1)
			newRelation.append(row) 

		return newRelation

	# Fold the columns in foldList
	def fold(self,relation,foldList,name="New column with name undefined"):
		rowNum = len(foldList)
		newRelation = list()
		reverseFoldList = list(foldList)
		reverseFoldList.sort(reverse=True)
		foldList.sort()

		for idx,row in enumerate(relation):
			if idx != 0:
				rowTemp = list(row)
				for col in reverseFoldList:
					rowTemp.pop(col)

				for i in range(0,rowNum):
					newRow = list(rowTemp)
					newRow.append(row[foldList[i]])
					newRelation.append(newRow)
			else:
				newRow = list(row)
				for col in reverseFoldList:
					newRow.pop(col)
				newRow.append(name)
				newRelation.append(newRow)

		return newRelation




	# Desearialization
	def desearialize(self,inputFile):
		if self.is_text(inputFile):
			self.data = self.txtReader(inputFile)
		
		else:
			self.data = self.binReader(inputFile)



	# Extraction
	def extraction(self):
		# Data Cleaning
		self.data = self.dataClearn(self.data)
		dataArray = self.data.split(" ")
		
		# We assume the value comes right after attribute name in the actual data file
		# A pointer showing which tuple we are creating
		instancePointer = 1
		timePattern = re.compile("[\d]+\:[\d]+\:[\d]+\.[\d]")
		ipPattern = re.compile("[\d]+\.[\d]+\.[\d]+\.[\d]")
		
		for idxInData,datum in enumerate(dataArray):
			# If this is an attribute we are looking for in the relation
			#print str(idxInData) +":\'"+datum+"\'"
			
			if datum in self.attr_list:
				idxInRelation = self.attr_list.index(datum)
				# There is no value under attribute datum for this instance
			
				#print str(len(self.relation)) + " " +  str(len(self.relation[instancePointer]))
				if len(self.relation) >= instancePointer+1:
					if not self.relation[instancePointer][idxInRelation]:
						self.relation[instancePointer][idxInRelation] = dataArray[idxInData+1]
					else:
						instancePointer += 1
						l = [None] * len(self.attr_list)
						self.relation.append(l)
						self.relation[instancePointer][idxInRelation] = dataArray[idxInData+1]
				
				else:
					l = [None] * len(self.attr_list)
					self.relation.append(l)
					self.relation[instancePointer][idxInRelation] = dataArray[idxInData+1]
			# extract time
			elif timePattern.match(datum) != None:
				idxInRelation = self.attr_list.index(self.attr_timestamp)
				if len(self.relation) >= instancePointer+1:
					if not self.relation[instancePointer][idxInRelation]:
						self.relation[instancePointer][idxInRelation] = datum
					else:
						instancePointer += 1
						l = [None] * len(self.attr_list)
						self.relation.append(l)
						self.relation[instancePointer][idxInRelation] = datum
				
				else:
					l = [None] * len(self.attr_list)
					self.relation.append(l)
					self.relation[instancePointer][idxInRelation] = datum

			# extract ip
			elif ipPattern.match(datum) != None:
				attr_name = "";
				if dataArray[idxInData+1] == '>':
					attr_name = self.attr_srcip
				else:
					attr_name = self.attr_tarip

				idxInRelation = self.attr_list.index(attr_name)
				if len(self.relation) >= instancePointer+1:
					if not self.relation[instancePointer][idxInRelation]:
						self.relation[instancePointer][idxInRelation] = datum
					else:
						instancePointer += 1
						l = [None] * len(self.attr_list)
						self.relation.append(l)
						self.relation[instancePointer][idxInRelation] = datum
				
				else:
					l = [None] * len(self.attr_list)
					self.relation.append(l)
					self.relation[instancePointer][idxInRelation] = datum


	# Transformation
	def transformation(self):
		self.relation = self.merge(self.relation,7,8,' > ')
		self.relation = self.fold(self.relation,[2,3,4])


	def production(self):
		print "production"



	# Output as CSV format
	def toCsv(self,relation):
		output = ""
		for row in relation:
			for idx,column in enumerate(row):
				if idx == len(row)-1:
					output += str(column)+"\n"
				else:
					output += str(column)+","
		return output


def main(argv):
	m = Transform()
	m.desearialize("./testfile/tcpdump.txt")
	m.extraction()
	m.transformation()
	print m.toCsv(m.relation)

if __name__ == "__main__":
    main(sys.argv[1:])


