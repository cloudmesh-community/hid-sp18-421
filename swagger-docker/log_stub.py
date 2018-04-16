import platform

def get_log_entry():
	if platform.system() == "Darwin":
		file = 'var/log/system.log'
	    with open(file,"r") as syslogFile:
	    	log_entry = syslogFile.readline()
	    return log_entry
	else:
		return "This linux Docker environment has no logentry files"