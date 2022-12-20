from selene.support.shared import browser
import os
import pytest


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.window_width = 1366
    browser.config._window_height = 1000
    browser.config.base_url = 'https://vkusvill.ru'


