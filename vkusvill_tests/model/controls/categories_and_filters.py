from selene import command
from selene.support.shared import browser


def hide_show_categories():
    browser.element('[class*=hide]').click()
    browser.element('[onclick*=ShowMenu]').click()

def today_delivery():
    browser.element('#FILTER2_51').perform(command.js.click)

def only_vkusvill_products():
    browser.element('#FILTER2_101').perform(command.js.click)

def for_vegetarians():
    browser.element('#FILTER2_151').perform(command.js.click)

def without_white_sugar():
    browser.element('#FILTER2_152').perform(command.js.click)