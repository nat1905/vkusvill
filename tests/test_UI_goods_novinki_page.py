import allure
from allure_commons.types import Severity
import pytest
from selene.support.shared import browser

from vkusvill_tests.model.pages import goods_novinki


@pytest.fixture(scope="function", autouse=True)
def open_browser():
    browser.open('/goods/novinki/')

def test_hide_show_categories():
    allure.dynamic.tag("web")
    allure.dynamic.severity(Severity.NORMAL)
    allure.dynamic.label("owner", "Natalia")
    allure.dynamic.feature("goods/novinki")
    allure.dynamic.story("hide and show categories of goods")

    with allure.step("Check show and hide categories"):
        goods_novinki.hide_show_categories()
    allure.attach

def test_check_filters():
    allure.dynamic.tag("web")
    allure.dynamic.severity(Severity.NORMAL)
    allure.dynamic.label("owner", "Natalia")
    allure.dynamic.feature("goods/novinki")
    allure.dynamic.story("Check filters")

    with allure.step("Check filter Today delivery"):
        goods_novinki.today_delivery()
    with allure.step("Check filter Only vkusvill products"):
        goods_novinki.only_vkusvill_products()
    with allure.step("Check filter For vegeterians"):
        goods_novinki.for_vegetarians()
    with allure.step("Check filter Without white sugar"):
        goods_novinki.without_white_sugar()

def test_check_sorting():
    allure.dynamic.tag("web")
    allure.dynamic.severity(Severity.NORMAL)
    allure.dynamic.label("owner", "Natalia")
    allure.dynamic.feature("goods/novinki")
    allure.dynamic.story("Check sorting")

    with allure.step("Check sorting By default"):
        goods_novinki.default()
    with allure.step("Check sorting By price asc"):
        goods_novinki.price_asc()
    with allure.step("Check sorting By price desc"):
        goods_novinki.price_desc()

def test_show_more_goods_at_page():
    allure.dynamic.tag("web")
    allure.dynamic.severity(Severity.NORMAL)
    allure.dynamic.label("owner", "Natalia")
    allure.dynamic.feature("goods/novinki")
    allure.dynamic.story("Check button Show more goods")

    with allure.step("Check button Show more goods"):
        goods_novinki.show_goods()

def test_check_paginator():
    allure.dynamic.tag("web")
    allure.dynamic.severity(Severity.NORMAL)
    allure.dynamic.label("owner", "Natalia")
    allure.dynamic.feature("goods/novinki")
    allure.dynamic.story("Check paginator")

    with allure.step("Check paginator"):
        goods_novinki.check_paginator()



