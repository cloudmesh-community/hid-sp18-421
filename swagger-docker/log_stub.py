import platform

def get_log_entry():
	if platform.system() == "Darwin":
		#file = 'var/log/system.log'
	    f = open('var/log/system.log')
	    #log_entry = f.readline()
	    return f.readline()
	elif platform.system() == "linux":
		return "This linux Docker environment has no logentry files"
	elif platform.system() == "Windows":
		return "This linux Docker environment has no logentry files"