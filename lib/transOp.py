# This is a module of transformation operation
# It has operators: Format, Merge, Divide, Split, Add, Drop, Copy, Fold, Unfold, Select
import re


def reform(relation,col,formatFuncInput,formatFuncOutput):
	if col >= len(relation[0]):
		print "ERROR: Index Out of Range"
		return relation

	newRelation = list()
	pattern = re.compile(formatFuncInput)

	for idx,row in enumerate(relation):
		match = re.match(pattern,formatFuncInput)
		if not match:
			print "ERROR: No match found. Please check your regular expression."
		newRow = formatFuncOutput.format(match.group())
		newRelation.append(newRow)

	return newRelation

relation = [["a","aaa>bbb"],["b","mmm>lll"]]
print reform(relation,1,"(\w+)>(\w+)","{1},{2}")

def drop(self,relation,col):
	if col >= len(relation[0]):
		print "ERROR: Index Out of Range"
		return relation

	for idx,row in enumerate(relation):
		row.pop(col)
		newRelation.append(row) 

	return newRelation



def add(self,relation,value):
	newRelation = list()
	if len(value) > 1 and len(value)!=len(relation):
		print "ERROR: The number of added values is less than number of rows"
		return relation

	for idx,row in enumerate(relation):
		if len(value) > 1:
			row.append(value[idx])
		else:
			row.append(value)

		newRelation.append(row) 

	return newRelation

def copy(self,relation,col):
	if col >= len(relation[0]):
		print "ERROR: Index Out of Range"
		return relation

	newRelation = list()
	for idx,row in enumerate(relation):
		row.append(row[col])	
		newRelation.append(row) 

	return newRelation

def merge(self,relation,col1,col2,delimiter):
	if col1 >= len(relation[0]) or col2 >= len(relation[0]):
		print "ERROR: Index Out of Range"
		return relation
	elif col1 == col2:
		print "ERROR: Two columns can not be identical"
		return relation

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
	for foldCol in foldList:
		if foldCol >= len(relation[0]):
			print "ERROR: Index Out of Range"
			return relation
	if len(foldList) > len(set(foldList)):
		print "ERROR: Two columns can not be identical"
		return relation

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