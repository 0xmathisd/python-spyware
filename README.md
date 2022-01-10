# Python spyware
A suite of python tools dedicated to spying a machine running on GNU / linux.

## Warning <img src="https://www.reed-sensor.com/wp-content/uploads/icon_disclaimer.jpg" width="25" height="25">

This program was not created for the purpose of stealing private information from anyone, this was created for educational and preventative purposes ONLY. I do not endorse this kind of action. Using or integrating my work in anything is not without risk for you, I am not responsible for any misappropriation. No one can be held responsible for your fraudulent actions.

## Available tools

- the keylogger : capture all keyboard inputs
- the spycam : capture picture from the camera with a regular time interval

## Modules required

- Opencv2
- Pyxhook

## How to use
```diff
+ `python3 linux/main.py --help` -> to find up-to-date information !
```

Be root on the victim's computer, then
```
nohup python3 linux/main.py [functions] [options]
```
> nohup (No Hang Up) is a command in Linux systems that runs the process even after logging out from the shell/terminal.

Stolen data can be found by default at `./RESULT/`
 
