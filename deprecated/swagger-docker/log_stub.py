import platform
import logging

def get_log_entry():
	if platform.system() == "Darwin":
	    f = open('var/log/system.log')
	    return f.readline()
	elif platform.system() == "linux":
		return "This linux Docker environment has no logentry files"
	else:
		return "This linux Docker environment has no logentry files"