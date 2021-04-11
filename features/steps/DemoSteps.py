from behave import *
from nose.tools import assert_equal, assert_true
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import allure

@given('User opens Swaglabs portal')
def step_impl(context):
    context.logger.debug("Launching the browser")
    context.browser.get("https://www.saucedemo.com/")


@when('User enters the Username')
def step_impl(context):
    context.logger.debug("Entering the Username")
    user_name = context.browser.find_element_by_xpath("//input[@id='user-name']")
    user_name.send_keys("standard_user")
    time.sleep(2)

@when('User enters the Password')
def step_impl(context):
    context.logger.debug("Entering the Password")
    user_name = context.browser.find_element_by_xpath("//input[@id='password']")
    user_name.send_keys("secret_sauce")
    time.sleep(2)

@then('Navigate to Home page')
def step_impl(context):
    context.logger.debug("Page title is - {}".format(context.browser.title))
    context.browser.find_element_by_xpath("//input[@id='login-button']").click()
    assert_equal(context.browser.title, "Swag Labs")
    time.sleep(2)


@then('User has sorted the items by Price Low to High')
def step_impl(context):
    context.logger.debug("Sorting the items by Price")
    item_sorter = context.browser.find_element_by_xpath("//*[@class='product_sort_container']/option[@value='lohi']")
    item_sorter.click()
    time.sleep(2)

@then(u'User adds the Cheapest item to the basket')
def step_impl(context):
    items_list = "//*[@class='inventory_list']"
    context.browser.total_items = context.browser.find_elements_by_xpath("//*[@class='inventory_list']/div")
    cheapest_item = context.browser.find_element_by_xpath("//*[@class='inventory_list']/div[" + '1' + "]/div[2]/div[2]/*[@class='btn btn_primary btn_small btn_inventory']")
    cheapest_item.click()
    time.sleep(2)
    context.logger.debug("User adds the Cheapest item to the basket")
    # context.logger.debug("Total Items text are: {}".format(dir(total_items)))
    # context.logger.debug("Total Items length is: {}".format(total_items.__len__()))

@then(u'User adds the second costliest item to the basket')
def step_impl(context):
    items_list = "//*[@class='inventory_list']"
    # second_costliest_item = context.browser.find_element_by_xpath("//*[@class='inventory_list']"+ "/div[0]/" + "div[2]/div[2]/*[@class='btn btn_primary btn_small btn_inventory']")
    second_costliest_item = context.browser.find_element_by_xpath("//*[@class='inventory_list']/div[" + str(context.browser.total_items.__len__() - 1)  + "]/div[2]/div[2]/*[@class='btn btn_primary btn_small btn_inventory']")
    second_costliest_item.click()
    context.logger.debug("User adds the second costliest item to the basket")
    # context.logger.debug("Items text are: {}".format(items_list[1].text))
    time.sleep(2)

@then(u'User navigates to the basket')
def step_impl(context):
    context.logger.debug("Navigating to the basket")
    basket = context.browser.find_element_by_xpath("//*[@class='shopping_cart_link']")
    basket.click()
    time.sleep(2)

@then(u'User checks out the items')
def step_impl(context):
    context.logger.debug("Checking out the items")
    context.browser.find_element_by_xpath("//*[@id='checkout']").click()
    context.browser.find_element_by_xpath("//*[@id='first-name']").send_keys("Kiran")
    context.browser.find_element_by_xpath("//*[@id='last-name']").send_keys("Nidasale Chaluvaiah")
    context.browser.find_element_by_xpath("//*[@id='postal-code']").send_keys("NG15 1AB")
    time.sleep(2)
    context.browser.find_element_by_xpath("//*[@id='continue']").click()
    time.sleep(2)
    context.browser.find_element_by_xpath("//*[@id='finish']").click()
    time.sleep(2)
    order_confirmation = context.browser.find_element_by_xpath("//*[@class='complete-header']").text
    assert_equal(order_confirmation, "THANK YOU FOR YOUR ORDER")
    time.sleep(2)
