from selene import command
from selene.support.shared import browser


def paginator(page):
    for i in range(2, 10):
        browser.element(f'a[href="{page}?PAGEN_1={i}"]').perform(command.js.click)