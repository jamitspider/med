from behave import given, when, then
from common import Locater

@given('the user on medsembly reset password reset page')
def step_user_on_reset_password(context):
    context.driver.get(Locater.url + "accounts/password/reset/")
    
@when('user enter {email} as email in password reset page')
def step_user_enter_email(context, email):
    context.driver.find_element_by_id('id_email').send_keys(email)
    
@when('user click on reset my password button')
def step_user_click_on_reset_my_password_button(context):
    context.driver.find_element_by_xpath("//*[@class='btn bg-red white-text' and @value='Reset My Password']").click()
    
@then('ensure that after click on reset my password button user should be get message {text}')
def step_ensure_user_on_dashboard(context, text):
    print("error text here===========" + context.driver.find_element_by_xpath("//*[text()='We have sent you an e-mail. Please contact us if you do not receive it within a few minutes.']").text)
    assert context.driver.find_element_by_xpath("//*[text()='We have sent you an e-mail. Please contact us if you do not receive it within a few minutes.']").text == text