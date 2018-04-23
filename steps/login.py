from behave import given, when, then
from common import Locater
 
@given('the user on medsembly signin page')
def step_user_on_signin(context):
    context.driver.get(Locater.url + "accounts/login/")
     
@when('user enter {email} as email in signin page')
def step_user_enter_email(context, email):
    context.driver.find_element_by_id('id_login').send_keys(email)
     
@when('user enter {password} as password in signin page')
def step_user_enter_password(context, password):
    context.driver.find_element_by_id('id_password').send_keys(password)
     
@when('user click on signin button')
def step_user_click_on_signin_button(context):
    context.driver.find_element_by_xpath("//*[@class='primaryAction btn bg-red white-text' and text()='Sign In']").click()
     
@then('ensure that user should be on dashboard page with welcome message {text}')
def step_ensure_user_on_dashboard(context, text):
    print("error text here===========" + context.driver.find_element_by_xpath("//*[@class='alert alert-danger']").text)
    assert context.driver.find_element_by_xpath("//*[@class='alert alert-danger']").text == text