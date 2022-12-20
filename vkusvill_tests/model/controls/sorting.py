from selene import command
from selene.support.shared import browser


def default():
    browser.element('[data-value=DEFAULT]').perform(command.js.click)

def price_asc():
    browser.element('[data-value=PRICE_ASC]').perform(command.js.click)

def price_desc():
    browser.element('[data-value=PRICE_DESC]').perform(command.js.click)
