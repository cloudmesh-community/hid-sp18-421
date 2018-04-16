import platform
import logging

def get_log_entry():
	if platform.system() == "Darwin":
	    f = open('var/log/system.log')
	    return f.readline()
	elif platform.system() == "linux":
		f = open(log.handlers[0].stream)
		return f.readline()
		#return "This linux Docker environment has no logentry files"
	elif platform.system() == "Windows":
		return "This linux Docker environment has no logentry files"