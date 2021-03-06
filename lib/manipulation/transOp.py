# This is a module of transformation operation
# It has operators: Format, Merge, Divide, Split, Add, Drop, Copy, Fold, Unfold, Select
import re

# E.g., inputFormat = (\w+):(\w+), outputFormat = {0}-{1}
def reform(relation,col,inputFormat,outputFormat,ifContainAttributeRow = False):
	if col >= len(relation[0]):
		print "ERROR: Index out of range"
		return relation

	newRelation = list()

	for idx,row in enumerate(relation):
		if idx == 0 and ifContainAttributeRow:
			newRelation.append(list(row))
			continue

		match = re.match(inputFormat,row[col],re.M|re.I)
		if not match:
			print "WARNING: No match found. Please check your regular expression."
			return relation

		newRow = list(row)
		row[col] = outputFormat.format(*match.groups())
		newRelation.append(row)

	return newRelation

#relation = [["abbbb","aaa>bbb"],["b","mmm>lll"]]
#print reform(relation,1,"(\w+)>(\w+)","{0}>={1}")

def divide(relation,col,pred,ifContainAttributeRow = False,newColumnName1='',newColumnName2=''):
	if col >= len(relation[0]):
		print "ERROR: Index out of range"
		return relation

	newRelation = list()

	for idx,row in enumerate(relation):

		newRow = list(row)

		if ifContainAttributeRow and idx == 0:
			temp = newRow[col]
			newRow.pop(col)
			newRow.append(newColumnName1)
			newRow.append(newColumnName2)
			newRelation.append(newRow)
			continue
		
		if pred(row[col]):
			temp = newRow[col]
			newRow.pop(col)
			newRow.append(temp)
			newRow.append("")
		else:
			temp = newRow[col]
			newRow.pop(col)
			newRow.append("")
			newRow.append(temp)

		newRelation.append(newRow)

	return newRelation

#def pred(s):
#	if len(s) > 2:
#		return True
#	else:
#		return False


#relation = [["abbbb","aaa>bbb"],["b","mmm>lll"]]
#print divide(relation,0,pred)



def drop(relation,col):
	if col >= len(relation[0]):
		print "ERROR: Index out of range"
		return relation

	newRelation = list()

	for idx,row in enumerate(relation):
		row.pop(col)
		newRelation.append(row) 

	return newRelation



# Add a column of values
def add(relation,value):
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



def copy(relation,col):
	if col >= len(relation[0]):
		print "ERROR: Index out of range"
		return relation

	newRelation = list()
	for idx,row in enumerate(relation):
		row.append(row[col])	
		newRelation.append(row) 

	return newRelation



def merge(relation,col1,col2,delimiter):
	if col1 >= len(relation[0]) or col2 >= len(relation[0]):
		print "ERROR: Index out of range"
		return relation
	elif col1 == col2:
		print "ERROR: Two columns can not be identical"
		return relation

	newRelation = list()
	for idx,row in enumerate(relation):
		newRow = list(row)
		if col1 > col2:
			newRow.pop(col1)
			newRow.pop(col2)
		else:
			newRow.pop(col2)
			newRow.pop(col1)		
		newRow.append(row[col1] + delimiter + row[col2])
		newRelation.append(newRow) 

	return newRelation

def split(relation,col,delimiter,ifContainAttributeRow = False):
	if col >= len(relation[0]):
		print "ERROR: Index out of range"
		return relation

	newRelation = list()
	for idx,row in enumerate(relation):
		newRow = list(row)
		splitList = newRow[col].split(delimiter)
		if len(splitList) < 2:
			print "WARNING: nothing is splited by delimiter "+delimiter
		newRow.pop(col)
		for item in splitList:
			newRow.append(item)
		newRelation.append(newRow) 

	if ifContainAttributeRow and len(newRelation[0]) < len(newRelation[1]):
		for i in range(0,len(newRelation[1])-len(newRelation[0])):
			newRelation[0].append("")


	return newRelation

#relation = [["abbbb","aaa>bbb"],["b","mmm>lll"]]
#print split(relation,1,">")


# Fold the columns in foldColumns
def fold(relation,foldColumns,ifContainAttributeRow = False,name=""):
	for foldCol in foldColumns:
		if foldCol >= len(relation[0]):
			print "ERROR: Index Out of Range"
			return relation
	if len(foldColumns) > len(set(foldColumns)):
		print "ERROR: Two columns can not be identical"
		return relation

	rowNum = len(foldColumns)
	newRelation = list()
	reverseFoldList = list(foldColumns)
	reverseFoldList.sort(reverse=True)
	foldColumns.sort()

	for idx,row in enumerate(relation):
		if idx == 0 and ifContainAttributeRow:
			newRow = list(row)
			for col in reverseFoldList:
				newRow.pop(col)
			newRow.append(name)
			newRelation.append(newRow)
		else:
			rowTemp = list(row)
			for col in reverseFoldList:
				rowTemp.pop(col)

			for i in range(0,rowNum):
				newRow = list(rowTemp)
				newRow.append(row[foldColumns[i]])
				newRelation.append(newRow)
		

	return newRelation


# Unfold: takes unique col1 values as new columns and col2 as the values of new columns, 
# Every maximal set of rows in T that have identical values in all columns except the i'th 
# and j'th, and distinct values in the i'th column, produces exactly one row

def unfold(relation,col1,col2,ifContainAttributeRow = False):
	col1Set = list()
	for idx,row in enumerate(relation):
		if idx == 0 and ifContainAttributeRow:
			continue
		col1Set.append(row[col1])

	# Remove duplicates
	col1SetTemp = list(set(col1Set))
	tempList = list()
	tempSet = set()
	for item in col1Set:
		if item not in tempSet:
			tempSet.add(item)
			tempList.append(item)
		if len(tempSet) >= len(col1SetTemp):
			col1Set = list(tempList)
			break

	n = len(relation[0])
	m = len(col1Set)

	newRelation = list()

	# make col1 unique values as the attribute name
	if ifContainAttributeRow:
		temp = list(relation[0])
		if col2 > col1:
			temp.pop(col2)
			temp.pop(col1)
		else: 
			temp.pop(col1)
			temp.pop(col2)
		
		attrRow = temp + col1Set
		newRelation.append(attrRow)
		
	else:
		attrRow = ['']*(n-2)
		attrRow = attrRow + col1Set
		newRelation.append(attrRow)
	
	otherColumnsIndexDict = dict()
	for idx,row in enumerate(relation):
		if idx == 0 and ifContainAttributeRow:
			continue
		temp1 = row[col1]
		temp2 = row[col2]
		if col2 > col1:
			row.pop(col2)
			row.pop(col1)
		else: 
			row.pop(col1)
			row.pop(col2)
		key = "_".join(row)

		if key in otherColumnsIndexDict.keys():
			rowIndex = otherColumnsIndexDict[key]
			columnIndex = col1Set.index(temp1) + n-2
			newRelation[rowIndex][columnIndex] = temp2

		else:
			newRow = list(row) + [None]*m			
			columnIndex = col1Set.index(temp1) + n-2
			newRow[columnIndex] = temp2
			rowIndex = len(newRelation)
			newRelation.append(newRow)
			otherColumnsIndexDict[key] = rowIndex

	return newRelation

#a = [["Alice","Math",80],["Alice","English",90],["Bob","Math",85],["Bob","Physics",80]]
#relation = unfold(a,1,2)
#print relation


# Select tuples that match the predicate
def select(relation,pred,ifContainAttributeRow=False):
	newRelation = list()
	for idx,row in enumerate(relation):
		if idx == 0 and ifContainAttributeRow:
			continue
		if pred(row):
			newRelation.append(row)

	return newRelation

#def pred(s):
#	if len(s[0]) > 2:
#		return True
#	else:
#		return False


#relation = [["abbbb","aaa>bbb"],["b","mmm>lll"]]
#print select(relation,pred)


# Tranpose the table, meaning turning all rows to columns and columns to rows
def transpose(relation):
	row = len(relation)
	col = len(relation[0])
	newRelation = [None]*col
	for i in range(0,col):
		newRelation[i] = [None]*row

	for i in range(0,row):
		for j in range(0,col):
			newRelation[j][i] = relation[i][j]

	return newRelation

#a = [[1,2,3],[4,5,6]]
#print transpose(a)

# Move column from origPosn to dstPosn
def moveColumn(relation,origPosn,dstPosn):
	newRelation = list(relation)
	for row in newRelation:
		temp = row[origPosn]
		row.pop(origPosn)
		row.insert(dstPosn,temp)
		
	return newRelation

#a = [[1,2,3],[4,5,6]]
#print moveColumn(a,2,0)

# Move row from origPosn to dstPosn
def moveRow(relation,origPosn,dstPosn):
	newRelation = list(relation)
	temp = newRelation[origPosn]
	newRelation.pop(origPosn)
	newRelation.insert(dstPosn,temp)
		
	return newRelation



# a = [[1,2,3],[4,5,6]]
# print moveRow(a,1,0)

# Remove row if specified column is none, if nothing specified then remove the empty row
def removeEmpty(relation,col=None):
	newRelation = list()
	if col:
		for row in relation:
			if row[col]!="":
				newRelation.append(row)
	else:
		for row in relation:
			for item in row:
				if item != "":
					newRelation.append(row)
					break
	return newRelation



