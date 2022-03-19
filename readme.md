# Logbook
## Marking online presence with selenium

> downside: i apply this method in a local computer, so it has to be either stand-by or hibernated so as to enable the power-on app to work. This is only a web scraping exercise, A much more convenient way to automate this process is to utilize the web's private API.

### 1. Install auto power-on app

### 2. Install python and selenium lib
- download and install python, get the latest version [here](https://www.python.org/downloads/).
- install selenium library using command prompt
```bash
pip i selenium
```
- download chromedriver [here](https://chromedriver.chromium.org/downloads) and make sure it is the same version as chrome browser installed

### 3. create a batch file to automatically run SAK.py / Prese.py
you can also automatically run it on startup by placing the file in windows startup folder that you can access by opening up run and typing `shell:startup`. inside the SAK.py / prese.py:
- change the geoLocation latitude & longitude to wherever you are supposed to be. 
- find and rename 'NIP' and 'Password' according to your credential.

### 4. Run the batch file on 5 AM (or anytime it is accesible) by launching it using auto power-on
`important` separate the 'waking up' event from the other event in which it runs the batch file as it will not trigger the launch event if it's directly assigned at the same time

### 5. Forget about it

![image](https://user-images.githubusercontent.com/85608673/156689053-2c339478-7241-4643-bbc6-ac6346daf6c6.png)
