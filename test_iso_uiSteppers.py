import time
from appium import webdriver

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
driver.find_element_by_accessibility_id('Steppers').click()
element = driver.find_element_by_xpath("(//XCUIElementTypeStaticText[@name='0'])[1]")
increment = driver.find_element_by_xpath("(//XCUIElementTypeButton[@name='Increment'])[1]")
decrement = driver.find_element_by_xpath("(//XCUIElementTypeButton[@name='Decrement'])[1]")
value = element.get_attribute('value')
i = int(value)  # converting the string value to integer
for i in range(5):
    increment.click()
time.sleep(2)
driver.quit()
