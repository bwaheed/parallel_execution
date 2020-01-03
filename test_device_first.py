import os
import pytest
from appium import webdriver
from TestWebViewAndroid import TestWebViewAndroid 

APPIUM_LOCAL_HOST_URL = 'http://localhost:4723/wd/hub'
PLATFORM_VERSION = '4.4.4'


class TestFirstDevice(TestWebViewAndroid):

    
    @pytest.fixture(scope="function")
    def driver(self, request):
        desired_caps = {
            'appPackage': 'com.example.android.contactmanager',
            'appActivity': '.ContactManager',
            'platformName': 'Android',
            'platformVersion': PLATFORM_VERSION,
            'deviceName': 'Android Emulator',
            # 'app': PATH('/home/bilal/Documents/ContactManager.apk')
        }
        driver = webdriver.Remote(APPIUM_LOCAL_HOST_URL, desired_caps)

        def fin():
            driver.quit()

        request.addfinalizer(fin)
        return driver  # provide the fixture value
    
    def test_add_contacts(self, driver):
        self.base_test(driver)        



