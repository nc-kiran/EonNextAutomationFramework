from selenium import webdriver
from util import loggerutils
import os

def before_all(context):
    driver_file_path = os.getcwd()  + "/Driver/chromedriver"
    # print(driver_file_path)
    context.browser = webdriver.Chrome(executable_path=driver_file_path)
    loggerutils.setup_logging()
    loggerutils.setup_formatted_logging(context)
    context.browser.set_page_load_timeout(10)
    context.browser.implicitly_wait(10)
    context.browser.maximize_window()

def after_all(context):
    context.browser.quit()
