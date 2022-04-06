# Logbook
## Marking online presence with selenium (chromedriver)

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
> you can also automatically run it on startup by placing the file in windows startup folder that you can access by opening up run and typing `shell:startup`. 

create a .bat file to run the codes (and to exit current instance after executing the script)

![image](https://user-images.githubusercontent.com/85608673/161985022-d67be291-b176-40f6-a6ae-3ccfb833a3fa.png)


inside the SAK.py / prese.py:
- adjust the chromedriver path to where it's located
  ![image](https://user-images.githubusercontent.com/85608673/161983938-c6a4a8c6-91cd-4edd-a3f4-c3e88ebc2315.png)

- change the geoLocation latitude & longitude to wherever you are supposed to be. 
  ![image](https://user-images.githubusercontent.com/85608673/161984012-13ee95cc-06b7-4f95-abdd-efc07f0010f1.png)

- find and rename 'NIP' and 'Password' () according to your credential.

  ![image](https://user-images.githubusercontent.com/85608673/161984048-e1d3c539-7d9a-443b-99c0-e6eb24482472.png)

### 4. Run the batch file on 5 AM (or anytime it is accesible) by launching it using auto power-on
`important` separate the 'waking up' event from the other event in which it runs the batch file as it will not trigger the launch event if it's directly assigned at the same time

### 5. Forget about it

![image](https://user-images.githubusercontent.com/85608673/156689053-2c339478-7241-4643-bbc6-ac6346daf6c6.png)
