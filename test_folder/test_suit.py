import time
from selenium import webdriver
import requests
# import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestDocker:
    def test_1(self):
        r = requests.request('get', 'https://www.google.com.ua/', verify=False)
        response = r.status_code
        assert 200 == response

    def test_sel(self):
        driver = webdriver.Chrome()

        url = 'https://www.google.com.ua/'
        driver.get(url)

        text_field = driver.find_element(by=By.CSS_SELECTOR, value="div textarea")
        text_field.click()
        text_field.send_keys('Штучний інтелект')
        text_field.send_keys(Keys.ENTER)
        cur_url = driver.current_url
        assert 'https://www.google.com.ua/search?q' in cur_url
