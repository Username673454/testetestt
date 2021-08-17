from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time

firefox_binary = FirefoxBinary(r"C:\Program Files\Mozilla Firefox\firefox.exe")
profile = webdriver.FirefoxProfile(r"C:\Users\Chill\AppData\Local\Mozilla\Firefox\Profiles\t15uhmrx.instacreate")
profile.set_preference('network.proxy_type', 1)
profile.set_preference('network.proxy.ssl', "69.197.181.202")
profile.set_preference('network.proxy.ssl_port', 3128)
profile.update_preferences()

driver = webdriver.Firefox(firefox_profile=profile, firefox_binary=firefox_binary, executable_path=r"C:\webdrivers\geckodriver.exe")
driver.get('http://whatismyipaddress.com')
time.sleep(3)

