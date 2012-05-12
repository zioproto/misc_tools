import os 
import sys
import time
import smtplib
import datetime

IPtocheck = ""
smtpserver = ""

def logToFile(string):
	f=open('wdoglogfile.txt','a')
	f.write(str(datetime.datetime.now())+string+"\n")
	f.close()


while True:
	if (os.system("ping6 -c 1 2a02:688:1::5 > /dev/null") !=0):
		if (os.system("ping6 -c 1 2a02:688:1::5 > /dev/null") !=0):
			if (os.system("ping6 -c 1 2a02:688:1::5 /dev/null") !=0):
			        server = smtplib.SMTP('10.0.1.1')
	        		server.set_debuglevel(0)
				msg = "From:bgp2@ninux.org\r\nTo:zioproto@gmail.com\r\nSubject:BGP Tecnopolo Problem"
	        		logToFile("problem")
				server.sendmail("bgp2@ninux.org", "zioproto@gmail.com", msg)
	        		server.quit()
				time.sleep(30)
	else:
		time.sleep(2)

