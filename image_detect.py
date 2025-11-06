from appium import webdriver
desired_caps = {
   "automationName": "UiAutomator2",
   "platformName": "Android",
   "deviceName": "Android",
   "udid": "127.0.0.1:58526",
   "noReset": True,
   "appPackage": "com.example"
}
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.find_element_by_xpath('(//android.widget.RelativeLayout)[2]').click()
driver.quit()