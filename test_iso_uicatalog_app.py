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
driver.find_element_by_accessibility_id('Switches').click()
default_switch = driver.find_elements_by_class_name('XCUIElementTypeSwitch')
default_switch_value = default_switch.__getattribute__('value')
print(default_switch_value)
if default_switch_value == '1':
    default_switch.click()
print(default_switch_value)
time.sleep(2)
driver.quit()