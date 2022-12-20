from selene import command
from selene.support.shared import browser


def show_goods():
    browser.element('[class*=catalog-load-more]').perform(command.js.click)