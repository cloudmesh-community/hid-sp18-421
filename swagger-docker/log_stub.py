import platform

def get_log_entry():
	if platform.system() == "Windows":
		return "Priya is a beautiful woman"
		#file = '%SystemRoot%\System32\Winevt\Logs\Application.evtx'
	elif platform.system() == "Darwin":
		file = '/var/log/system.log'
	elif platform.system() == "Linux":
		return "Priya is a mad girl ! "
		#file = '/var/log/syslog'
	with open(file,"r") as syslogFile:
		log_entry = syslogFile.readline()
		return log_entry

