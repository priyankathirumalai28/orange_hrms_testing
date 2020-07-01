import time
from behave import *

use_step_matcher("re")


@given("I navigate to Orange Hrms website")
def step_impl(context):
    """
    Login into hrms portal
    """
    context.browser.get('https://opensource-demo.orangehrmlive.com/')
    time.sleep(10)


@when('I input the "username" and "password"')
def step_impl(context):
    context.login.setUsername('Admin')
    context.login.setPassword('admin123')


@step("I click the login button")
def step_impl(context):
    context.login.click_login()


@then("I must navigate to the other page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.browser.title != None