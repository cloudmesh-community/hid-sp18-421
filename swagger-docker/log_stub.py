import platform

def get_log_entry():
	if platform.system() == "Windows":
		file = '%SystemRoot%\System32\Winevt\Logs\Application.evtx'
	elif platform.system() == "Darwin":
		file = '/var/log/system.log'
	elif platform.system() == "Linux":
		file = '/var/log/syslog'
	with open(file,"r") as syslogFile:
		log_entry = syslogFile.readline()
		return log_entry

