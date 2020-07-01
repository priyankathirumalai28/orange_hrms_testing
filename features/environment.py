from selenium import webdriver

from features.browser import Browser
from features.pages.login import LoginPage
from features.pages.home import HomePage

def before_all(context):
    browser_obj = Browser()
    context.browser = browser_obj.get_obj()
    context.login = LoginPage(context.browser)
    context.home = HomePage(context.browser)
    print("Executing before all")

# def before_feature(context, feature):
#      print("Before feature\n")

#Scenario level objects are popped off context when scenario exits
def before_scenario(context,scenario):
    pass

def after_scenario(context,scenario):
    pass

# def after_feature(context,feature):
#      print("\nAfter feature")
#
def after_all(context):
     context.browser.quit()

