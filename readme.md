# Logbook
## Marking online presence with selenium

> downside: i apply this method in a local computer, so it has to be either stand-by or hibernated so as to enable the power-on app to work

### 1. Install auto power-on app

### 2. Install python and selenium lib
- download and install python, get the latest version [here](https://www.python.org/downloads/).
- install selenium library using command prompt

```bash
pip i selenium
```

### 3. create a batch file to automatically run SAK.py / Prese.py
you can also automatically run it on startup by placing the file in windows startup folder that you can access by opening up run and typing `shell:startup`

### 4. Run the batch file on 5 AM (or anytime it is accesible) by launching it using auto power-on
`important` separate the 'waking up' event from the event in which it runs the batch file as it will not trigger the launch event if it's directly assigned at the same time

### 5. Actually stop concerning and worrying about forgetting to mark online presence and having to seek your picture from the CCTV while printing out some unecessary documents.

