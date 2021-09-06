import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

desired_cap = dict(
    platformName='iOS',
    platformVersion='14.5',
    deviceName='iPhone 12 Pro',
    udid='A97D4189-AB2F-490F-B1CC-FBABDC54259C',
    bundleId='com.Animesh66.IntegrationApp'
)

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
driver.implicitly_wait(10)
element = driver.find_element_by_accessibility_id('Scrolling').click()
driver.find_element_by_accessibility_id('TableView').click()
action = TouchAction(driver)
i = 0
while not driver.find_element_by_accessibility_id('35').is_displayed():
    action.press(x=0, y=707).wait(2000).move_to(x=0, y=223).perform()
    i += 1

time.sleep(2)
driver.quit()
