import pytest
from selenium import webdriver

import tests
from tests import application
from tests.application import Application
from group import Group


@pytest.fixture()
def app(request):
    driver = webdriver.Firefox(executable_path='/Users/alex/anaconda3/bin/geckodriver')
    fixture = Application(driver=driver)
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login(username="admin", password="secret")
    app.init_group_creation()
    app.fill_group_form(Group(name="qwerty", header="qwerty", footer="qwerty"))
    app.submit_group_creation()
    app.logout()


def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.init_group_creation()
    app.fill_group_form(Group(name="", header="", footer=""))
    app.submit_group_creation()
    app.logout()