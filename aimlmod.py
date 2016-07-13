import io
import os

def modifyaiml(path, topic):
	topfile =""
	botfile =""	
	if(os.path.isfile(path)):
		file = open(path,"r")
		lines = file.readlines()
		for line in lines:
			if line != "</topic>\n" and line != "</aiml>":
				topfile += line
			else:
				botfile += line
		file.close()
		print("file "+path+"read")
	else:
		topfile='<aiml>\n<topic name="'+topic+'">\n'
		botfile='</topic>\n</aiml>'
	pattern = raw_input("What input would you like me to answer? Please no punctuation marks >> ").upper()
	template = raw_input("How should I answer it? >> ")
	file = open(path,"w")
	file.write(topfile)	
	file.write("<category>\n<pattern>"+pattern+"</pattern>\n<template>"+template+"</template>\n</category>\n")
	file.write(botfile)
