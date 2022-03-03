# ! https://www.selenium.dev/
# ! PROBLEM : Timeout 504, proxy had noscheme, and other problem> make sure youre running selenium from CMD instead of powershell
# ! PROBLEM : proxy had noscheme, and unable to connect to remote server> if not using proxies, get rid of http_proxy in env variable, and unset proxy through cmd

# FIREFOX
# from selenium import webdriver
# driver = webdriver.Firefox(executable_path='C:\geckodriver.exe')
# driver.get('https://www.google.com/')




# CHROME
# from selenium.webdriver.chrome.options import Options

# opts.set_headless()
# assert opts.headless # Operating in headless mode

# from selenium import webdriver
# userN= driver.find_element_by_id("user-search']")
# driver.execute_script("arguments[0].click();", userN)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as waitfr
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import Select

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
# options.add_argument("--headless")
# options.add_argument('--disable-gpu')
# options.add_argument('window-size=2560,1440')



browser = webdriver.Chrome('C:\chromedriver.exe', chrome_options=options)
browser.maximize_window()
browser.get('https://logbook.pajak.go.id/')


browser.execute_cdp_cmd(
    "Browser.grantPermissions",
    {
        "origin": "https://logbook.pajak.go.id/",
        "permissions": ["geolocation"]
    },
)
# -2.539099, 112.950874
browser.execute_cdp_cmd(
    "Emulation.setGeolocationOverride",
    {
        "latitude": -2.539099,
        "longitude": 112.950874,
        "accuracy": 100,
    },
)



def login(nip, psw):
    WebDriverWait(browser, 20).until(waitfr.presence_of_element_located((By.ID, "nip"))).send_keys(nip)
    WebDriverWait(browser, 20).until(waitfr.presence_of_element_located((By.ID, "password"))).send_keys(psw)
    WebDriverWait(browser, 20).until(waitfr.presence_of_element_located((By.ID, "m_login_signin_submit"))).click()
    

def markPresence():
    try:
        try:
            WebDriverWait(browser, 20).until(waitfr.element_to_be_clickable((By.ID, "btnPresensi")))
        finally:
            
            WebDriverWait(browser, 20).until(waitfr.element_to_be_clickable((By.ID, "btnPresensi"))).click()
    finally:
        browser.save_screenshot('display.png')
        
        
def logOut():
    # m-link
    dp = browser.find_element_by_class_name('m--marginless.m--img-centered'); browser.execute_script("arguments[0].click();", dp)
    # fa flaticon-logout
    lgout = browser.find_element_by_class_name('fa.flaticon-logout'); browser.execute_script("arguments[0].click();", lgout)
    
    
def isiSAK(
        # alamat,
        #    kota,
        #    tinggaltype,
        #    kontakNama,
        #    kontakHP,
        #    golDarah,
           ):
    browser.get('https://logbook.pajak.go.id/SelfAssessmentKesehatan/form')
    # pop-up swal2-confirm swal2-styled 
    WebDriverWait(browser, 20).until(waitfr.presence_of_element_located((By.CLASS_NAME, "swal2-confirm.swal2-styled"))).click()
    #class-alamat 
    # WebDriverWait(browser, 20).until(waitfr.presence_of_element_located((By.ID, "alamat"))).send_keys(alamat)
    #-class-Kota - name='kd_kota'
    # WebDriverWait(browser, 20).until(waitfr.presence_of_element_located((By.NAME, "kd_kota"))).send_keys(kota)
    # tinggal type radio
    # radioOpt = browser.find_elements_by_css_selector('#kel_tinggal'); print(radioOpt)
    # #class-Kontaknama  
    # WebDriverWait(browser, 20).until(waitfr.presence_of_element_located((By.ID, "sub_kontak_nm"))).send_keys(kontakNama)
    # #class-kontakHP  
    # WebDriverWait(browser, 20).until(waitfr.presence_of_element_located((By.ID, "sub_kontak"))).send_keys(kontakHP)
    
    # #class-goldarah 
    # Select(browser.find_element_by_id('id_of_element')).select_by_visible_text(golDarah)
    
    # selanjutnya
    browser.execute_script("document.querySelectorAll('.actions.clearfix ul a')[1].click()")
    # tidak
    browser.execute_script("document.querySelectorAll('.m-radio.m-radio--solid.m-radio--danger').forEach(a => a.click())")
    # selanjutnya
    browser.execute_script("document.querySelectorAll('.actions.clearfix ul a')[1].click()")
    # rumah pribadi (4) -- isolasi lainnya (8)
    browser.execute_script("document.querySelectorAll('.m-radio.m-radio--solid.m-radio--success')[6].click()")
    # selanjutnya
    browser.execute_script("document.querySelectorAll('.actions.clearfix ul a')[1].click()")
    # tidak mengalami gejala
    browser.execute_script("document.querySelectorAll('.m-checkbox.m-checkbox--bold.m-checkbox--success')[21].click()")
    # selanjutnya
    browser.execute_script("document.querySelectorAll('.actions.clearfix ul a')[1].click()")
    # apabila sdh ke dokter -> tidak
    browser.execute_script("document.querySelectorAll('.m-radio.m-radio--solid.m-radio--success')[15].click()")
    # selanjutnya
    browser.execute_script("document.querySelectorAll('.actions.clearfix ul a')[1].click()")
    # apabila riwayat ke kota positip bla
    browser.execute_script("document.querySelectorAll('.m-radio.m-radio--solid.m-radio--danger')[2].click()")
    # selanjutnya
    browser.execute_script("document.querySelectorAll('.actions.clearfix ul a')[1].click()")
    # memberi perawatan ke orang positip
    browser.execute_script("document.querySelectorAll('.m-radio.m-radio--solid.m-radio--danger')[3].click()")
    # selanjutnya
    browser.execute_script("document.querySelectorAll('.actions.clearfix ul a')[1].click()")
    # kontak ke 
    browser.execute_script("document.querySelectorAll('.m-radio.m-radio--solid.m-radio--danger')[4].click()")
    # selanjutnya
    browser.execute_script("document.querySelectorAll('.actions.clearfix ul a')[1].click()")
    # kontak ke 
    browser.execute_script("document.querySelectorAll('.m-radio.m-radio--solid.m-radio--danger')[6].click()")
    # selanjutnya
    browser.execute_script("document.querySelectorAll('.actions.clearfix ul a')[1].click()")
    # 14 hari terakhir pernah swab?? ngentot
    browser.execute_script("document.querySelectorAll('.m-radio.m-radio--solid.m-radio--danger')[9].click()")
    # selanjutnya
    browser.execute_script("document.querySelectorAll('.actions.clearfix ul a')[1].click()")
    # last stupid questions
    browser.execute_script("document.querySelectorAll('.m-radio.m-radio--solid.m-radio--danger').forEach(a => a.click())")
    # saya setuju anjing
    browser.execute_script("document.querySelectorAll('.m-checkbox.m-checkbox--bold.m-checkbox--success')[22].click()")
    # selesai
    browser.execute_script("document.querySelectorAll('.actions.clearfix ul a')[2].click()")
    
login('NIP', 'Password')
isiSAK()
logOut()
browser.quit()

