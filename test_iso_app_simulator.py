import time
from appium import webdriver

desired_cap = dict(
    platformName='iOS',
    platformVersion='14.5',
    deviceName='iPhone 12 Pro',
    udid='A97D4189-AB2F-490F-B1CC-FBABDC54259C',
    app='/Users/animeshmukherjee/PycharmProjects/pythonProject/Appium_iOS_Testing/app/simulator/IntegrationApp.app',
    noRest=True
)

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
driver.implicitly_wait(10)
driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='Alerts']").click()
driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='Create Sheet Alert']").click()
read_text = driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='Magic Sheet']").text
print(read_text)
time.sleep(2)
driver.quit()