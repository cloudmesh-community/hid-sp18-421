def get_log_entry():
	try:
		file = 'var/log/system.log'
	except:
		try:
			file = '%SystemRoot%\System32\Winevt\Logs\Application.evtx'
		except:
			file = '/var/log/syslog'
	with open(file,"r") as syslogFile:
		log_entry = syslogFile.readline()
	return log_entry