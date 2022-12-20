from vkusvill_tests import model


def hide_show_categories():
    model.controls.categories_and_filters.hide_show_categories()

def today_delivery():
    model.controls.categories_and_filters.today_delivery()

def only_vkusvill_products():
    model.controls.categories_and_filters.only_vkusvill_products()

def for_vegetarians():
    model.controls.categories_and_filters.for_vegetarians()

def without_white_sugar():
    model.controls.categories_and_filters.without_white_sugar()

def default():
    model.controls.sorting.default()

def price_asc():
    model.controls.sorting.price_asc()

def price_desc():
    model.controls.sorting.price_desc()

def show_goods():
    model.controls.show_more_goods.show_goods()

def check_paginator():
    model.controls.paginator.paginator('/goods/novinki/')

def login():
    model.controls.login.login_phone()



