# -*- coding: utf-8 -*-

from selenium.webdriver.firefox.webdriver import WebDriver
from selenium import webdriver
browser = webdriver.Firefox(executable_path = '/Users/alex/anaconda3/bin/geckodriver')
#from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

import unittest


class test_new_contact(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(30)

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/edit.php")

    def login(self, wd):
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_id("LoginForm").submit()

    def open_new_contact_form(self, wd):
        wd.find_element_by_name("firstname").clear()

    def fill_new_contact_form(self, wd):
        wd.find_element_by_name("firstname").send_keys("John")
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys("James")
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("Grady")
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys("john2020")
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys("Google LLC")
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys("Mountain View, California, USA")
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys("123456789")
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys("123456789")
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys("123456789")
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys("email@domain.com")
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys("email2@domain.com")
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys("email3@domain.com")
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys("google.com")
        Select(wd.find_element_by_name("bday")).select_by_visible_text("1")
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text("January")
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("1982")

    def submit_creation(self, wd):
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def back_to_home_page(self, wd):
        wd.find_element_by_link_text("home page").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def test_untitled_test_case(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd)
        self.open_new_contact_form(wd)
        self.fill_new_contact_form(wd)
        self.submit_creation(wd)
        self.back_to_home_page(wd)
        self.logout(wd)

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
