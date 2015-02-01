import re


# return an array of retrieved values, 
def extract(inputData,valueRegex, prefixRegex="",postfixRegex=""):
	pattern = prefixRegex + "("+valueRegex+")"+postfixRegex
	
	match = re.findall(pattern,inputData)
	if not match:
		return

	return match

print extract(inputData="(tos 0x20, ttl  48, id 34859, id 124124, ids 235, length: 84)",valueRegex="\d+",prefixRegex="id ")

