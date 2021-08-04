import requests
import os
from colorama import init, Fore
import time
import json


init(convert=True)


def refresh():
	if os.name == 'nt':
		os.system("CLS")
	else:
		os.system("clear")

	print(Fore.LIGHTBLUE_EX+"""
╔═══════════════╗
║=WEBHOOK COMET=║
║Discord WebHook║
║Chat Utility   ║
╚═══════════════╝
#Made By Imalaia3

"""+Fore.WHITE)



url = ''
message_to=''
debug_mode = False
cool_header = { "Content-Type": "application/json"}



#login
while True:
	refresh()
	print("\n")
	print(Fore.LIGHTBLUE_EX+'Welcome User! Please Enter Your WebHook URL.')
	url = input("URL ~> "+Fore.WHITE)
	rq = requests.get(url)
	if rq.status_code == 200:
	    refresh()
	    print(Fore.GREEN+"RESPONSE: OK"+Fore.WHITE)
	    
	else:
	    print(Fore.RED+f"Failed. Response: {rq.status_code}. Token or ID Might Not Be Valid. Check Your Internet Connection And URL"+Fore.WHITE)
	    time.sleep(3)
	    exit(0)
	break





refresh()
print(Fore.YELLOW + "Welcome! To Chat Type Your Message In The Field! \n")
print("Use '*help' To See All Valid Commands and '*exit' To Quit The application. \n\n"+Fore.WHITE)
while True:
	message_to = str(input(Fore.LIGHTBLUE_EX + "WebHook: " + Fore.WHITE))
	if message_to == "*exit":
		exit(0)
	elif message_to == "*help":
		print(Fore.YELLOW+"""

	*exit | Exit
	*help | Help
	*name | Change WebHook Name (TODO)
	*pfp  | Change WebHook PFP  (TODO)
	*debug| See more info about request (TODO) (OFF BY DEFAULT)

\n
""")


	

	else:
		#send message (finally)
		




		payload = {"content": message_to}
		rq = requests.post(url, data=json.dumps(payload), headers={ "Content-Type": "application/json"})
		if rq.status_code == 204:
			print(Fore.GREEN+"RESPONSE: OK. \n" + Fore.WHITE)
			
		else:
			print(Fore.RED+"Failed. Response: "  + rq.status_code + ". WebHook Might Be Deleted Or You Are Sending Messages Too Fast \n " + Fore.WHITE)
