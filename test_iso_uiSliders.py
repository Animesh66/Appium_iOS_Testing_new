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
driver.find_element_by_accessibility_id('Sliders').click()
slider = driver.find_elements_by_class_name("XCUIElementTypeSlider")
slider[0].send_keys('0.6')
print(slider[0].get_attribute('value'))
slider[1].send_keys('0.8')
print(slider[1].get_attribute('value'))
slider[2].send_keys('0.2')
print(slider[2].get_attribute('value'))
time.sleep(2)
driver.quit()
