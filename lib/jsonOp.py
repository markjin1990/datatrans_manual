import json


def txtReader(self,fn):
	f = open(fn, "r")		
	text = f.read()
	f.close()
	return text

def binReader(self,fn):
	f = open(fn, "rb")		

	text = f.read()
	f.close()
	return text