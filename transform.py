
# Library
import sys
import subprocess
import re

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

	attr_list.append(attr_tarip)
	attr_list.append(attr_srcip)
	attr_list.append(attr_length)
	attr_list.append(attr_flag)
	attr_list.append(attr_offset)
	attr_list.append(attr_id)
	attr_list.append(attr_ttl)
	attr_list.append(attr_tos)
	attr_list.append(attr_timestamp)	

	relation.append(attr_list)
	



	
	def txtReader(self,fn):
		f = open(fn, "r")		
		print "read txt"

		text = f.read()
		return text

	def binReader(self,fn):
		f = open(fn, "rb")		
		print "read binary"

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

			# Remove : if it is in the end of the string
			if len(datum) > 0 and datum[len(datum)-1] == ':':
				datumToAdd = datum[:len(datum)-1]

			print datumToAdd
			# Remove space
			if datumToAdd != '\s':
				newDataArray.append(datumToAdd)
			else:
				print "it is space"
			

		mydata = " ".join(newDataArray)

		return mydata


	def is_text(self,fn):
		msg = subprocess.Popen(["file", fn], stdout=subprocess.PIPE).communicate()[0]
		return re.search('text', msg) != None

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
		
		for idxInData,datum in enumerate(dataArray):
			# If this is an attribute we are looking for in the relation
			print str(idxInData) +":"+datum
			'''
			if datum in self.attr_list:
				idxInRelation = self.attr_list.index(datum)
				# There is no value under attribute datum for this instance

				print str(len(self.relation)) + " " +  str(len(self.relation[instancePointer]))
				if len(self.relation) >= instancePointer:
					if not self.relation[instancePointer][idxInRelation]:
						self.relation[instancePointer][idxInRelation] = dataArray[idxInData+1]
					else:
						instancePointer += 1
						l = [None] * 10
						self.relation.append(l)
						self.relation[instancePointer][idxInRelation] = dataArray[idxInData+1]
				
				else:
					l = [None] * len(self.)
					self.relation.append(l)
					self.relation[instancePointer][idxInRelation] = dataArray[idxInData+1]
				'''
				

		print self.relation







	# Transformation
	def transformation(self):
		print "transformation"

	def production(self):
		print "production"



def main(argv):
	m = Transform()
	m.desearialize("./testfile/tcpdump.txt")
	m.extraction()

if __name__ == "__main__":
    main(sys.argv[1:])


