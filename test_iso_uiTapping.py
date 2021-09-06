import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

desired_cap = dict(
    platformName='iOS',
    platformVersion='14.5',
    deviceName='iPhone 12 Pro',
    udid='A97D4189-AB2F-490F-B1CC-FBABDC54259C',
    bundleId='com.Animesh.apple-samplecode.UICatalog',
    noRest=True
)

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
driver.implicitly_wait(10)
element = driver.find_element_by_accessibility_id('Switches')
action = TouchAction(driver)
action.tap(element).perform()
time.sleep(2)
driver.quit()