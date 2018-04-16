import platform
import logging

def get_log_entry():
	if platform.system() == "Darwin":
	    f = open('var/log/system.log')
	    return f.readline()
	elif platform.system() == "linux":
		f = open(log.handlers[].stream)
		return "Log entry:", f.readline()
		#If log entry is emoty that means there are not any
	elif platform.system() == "Windows":
		return "This linux Docker environment has no logentry files"