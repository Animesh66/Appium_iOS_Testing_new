import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

desired_cap = dict(
    platformName='iOS',
    platformVersion='14.5',
    deviceName='iPhone 12 Pro',
    udid='A97D4189-AB2F-490F-B1CC-FBABDC54259C',
    browserName='safari'
)

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
driver.get("https://www.google.com")
driver.find_element_by_xpath("//*[@name='q']").send_keys("What is appium?")
time.sleep(2)
driver.quit()
