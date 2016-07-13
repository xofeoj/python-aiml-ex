import aiml
import aimlmod as am
from ASR import record
import pyaudio

# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("load aiml b")

# set this in order to decide whether to use microphone or keyboard as input
useMicrophone = True
# set constants for recording
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
RECORD_SECONDS = 4
BUFFERLENGTH = 25

# Press CTRL-C to break this loop
exitflag = False
while exitflag == False:
	if useMicrophone:
		ip = record.dynamicRecord(CHUNK,FORMAT,CHANNELS,RATE,RECORD_SECONDS,BUFFERLENGTH)
		print("User >> "+ip)
	else:
		ip = raw_input("Enter your message >> ")
	if(ip == "exit"):
		exitflag = True
	elif(ip.lower() == "bad answer" or ip.lower() == "that was a bad answer" or ip.lower() == "that was a bad answer."):
		print("executing AIML modification script")
		# this setup only works if each topic has its own filename
		topic = kernel.getPredicate("topic")
		if topic == "":
			filename = "basic_chat.aiml"
		else:
			filename = "topics/" + topic + ".aiml"
		am.modifyaiml(filename, topic)
		kernel.learn(filename)
	op = kernel.respond(ip)
	print op.getMessage()
	emot = op.getEmotion()
	if(emot != ""):
		print(emot)


''' To compile a robot brain please add:
import os
#to the header and 

kernel.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")
kernel.saveBrain("bot_brain.brn")

### To load the brain as the robot brain rather than needing to reload aiml each time:
kernel.bootstrap(brainFile = "bot_brain.brn")
'''
#call "load aiml b" during raw input to reload live