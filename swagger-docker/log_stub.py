import platform

def get_log_entry():
	if platform.system() == "Windows":
	try:
		file = '/var/log/system.log'
		with open(file,"r") as syslogFile:
			log_entry = syslogFile.readline()
		return log_entry
	except:
		try:
			file =  '%SystemRoot%\System32\Winevt\Logs\Application.evtx'
			with open(file,"r") as syslogFile:
				log_entry = syslogFile.readline()
			return log_entry
		except:
			file = '/var/log/syslog'
			with open(file,"r") as syslogFile:
				log_entry = syslogFile.readline()
			return log_entry

