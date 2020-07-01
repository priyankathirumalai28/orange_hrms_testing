import time
from behave import *

use_step_matcher("re")


@given("I navigate to Home Page Of Orange Hrms website")
def step_impl(context):
    """
    Login into hrms portal
    """
    context.browser.get('https://opensource-demo.orangehrmlive.com/')
    time.sleep(10)
    context.home.click_welcome()


@when('I click on the "Leave"')
def step_impl(context):
    context.home.click_leave()


@step('I click on the "Assign Leave"')
def step_impl(context):
    context.home.click_assign_leave()

@then("I must navigate to the Assign Leave page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.browser.title != None