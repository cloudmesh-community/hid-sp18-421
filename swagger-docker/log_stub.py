def get_log_entry():
	file = 'var/log/boot.log'
	with open(file,"r") as syslogFile:
		log_entry = syslogFile.readline()
	return log_entry