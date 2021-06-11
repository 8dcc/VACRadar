try:
	import requests, random, string, time, sys
	from bs4 import BeautifulSoup
except Exception:
	exit(" [!] Error importing necesary modules: requests, random, string, time, bs4, sys")

############ EDIT ME ############
useTorProxy = False             #  << Put here True or False
#################################

def banner():
	print(" ___________________________________________________________")
	print("   _    _   __       __     ____                            ")
	print("   |   /    / |    /    )   /    )             /            ")
	print("   |  /    /__|   /        /___ /    __    __ /    __   ___ ")
	print("   | /    /   |  /        /    |   /   ) /   /   /   ) /   )")
	print(" __|/____/____|_(____/___/_____|__(___(_(___/___(___(_/_____")
	print()


if useTorProxy == False:
	proxies = ""
elif useTorProxy == True:
	proxies = {
		'http': 'socks5://127.0.0.1:9150',
		'https': 'socks5://127.0.0.1:9150'
	}
else:
	print()
	print(" [!] Error. Invalid proxy. Exiting...")
	print()
	exit(1)

def main():
	banner()
	start_program = input(" [i] Welcome to VACRadar! Press any key to start... ")
	print("     Starting at "+ time.strftime("%d %b %Y - %H:%M:%S", time.gmtime()))
	with open("VACRadar_debug.log", "a") as VacLog:  # Append to the log file
		VacLog.write("[%s] User started.\n" % time.strftime("%d %b %Y - %H:%M:%S", time.gmtime()))
	print()
	sys.stdout.write(" [-] Request for ")
	last = 1
	while True:
		ProfileID = "".join(random.choice(string.digits) for i in range(10))
		ProfileID = "7656119%s" % ProfileID
		ProfileURL = "https://steamcommunity.com/profiles/" + ProfileID
		try:
			r = requests.get(ProfileURL, proxies=proxies, allow_redirects=True)
			souped = BeautifulSoup(r.text, 'html.parser')
			if "Error" in str(souped.title):
				sys.stdout.write(ProfileID + " is bad.")
				sys.stdout.write('\b'*25)
				sys.stdout.flush()
				last1 = 0
			if "Error" not in str(souped.title) and " ban " in str(souped.text):
				if last == 0:
					print()
				sys.stdout.write('\b'*50)
				sys.stdout.flush()
				print(" [+] Request for " + str(ProfileID) + " is good and it has a VAC ban.")
				with open("VACFound.log", "a") as VACFound:  # Append to the log file
					VACFound.write("[%s] VACProfile found: %s" % (time.strftime("%d %b %Y - %H:%M:%S", time.gmtime()), ProfileID))
					VACFound.write("\n")
				if last == 1:
					sys.stdout.write(" [-] Request for ")
				last = 1
		except Exception as e:
			print(" [!] An error ocurred: %s" % e)
			print(" Stopped at "+ time.strftime("%d %b %Y - %H:%M:%S", time.gmtime()))
			with open("VACRadar_debug.log", "a") as VacLog:  # Append to the log file
				VacLog.write("[%s] Exception: %s \n" % (time.strftime("%d %b %Y - %H:%M:%S", time.gmtime()), e))
			print()
			exit(1)

try:
	main()
except Exception as e:
	exit(f" [!] Error: {e}")
except KeyboardInterrupt:
	print()
	print(" Detected Ctrl+C. Shutting down...")
	print(" Stopped at "+ time.strftime("%d %b %Y - %H:%M:%S", time.gmtime()))
	with open("VACRadar_debug.log", "a") as VacLog:  # Append to the log file
		VacLog.write("[%s] User stopped.\n" % time.strftime("%d %b %Y - %H:%M:%S", time.gmtime()))
	print()
	exit(1)

exit("Reached program end.")
