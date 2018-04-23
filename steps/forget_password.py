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
    
@when('user open mail for password reset mail id')
def step_open_mail_for_reset_password(context):
    context.driver.find_element_by_xpath("//*[text()='[Medsembly] Reset Password']").click()
     
@when('user click on password reset link')
def step_click_on_reset_password_link(context):
    iframe = context.driver.find_element_by_id('msg_body')
    context.driver.switch_to_frame(iframe)
    context.driver.find_element_by_partial_link_text(Locater.url+'accounts/password/reset/').click()
     
@then('ensure that user should redirect to {text} page for reset password')   
def step_ensure_user_redirect_to_change_password_page(context, text):
    window_change = context.driver.window_handles[1]
    context.driver.switch_to_window(window_change)
    print("error text here===========" + context.driver.find_element_by_xpath("//*[@class='card-header text-center white-text bg-red']/h2").text)
    assert context.driver.find_element_by_xpath("//*[@class='card-header text-center white-text bg-red']/h2").text == text
    
@when('user enter {text} as a new password on change password page')
def step_user_enter_new_password(context, text):
    context.driver.find_element_by_id('id_password1').send_keys(text)
    
@when('user enter {text} as a confirm new password on change password page')
def step_user_enter_confirm_new_password(context, text):
    context.driver.find_element_by_id('id_password2').send_keys(text)
     
@when('user click on chage password button to reset password')
def step_user_click_on_change_password_button(context):
    context.driver.find_element_by_xpath("//*[@value='Change Password']").click()
     
@then('ensure that after click on change password button user get {text} message on screen')
def step_ensure_user_on_password_changed_screen(context, text):
    print("error text here===========" + context.driver.find_element_by_xpath("//*[text()='Your password is now changed.']").text)
    assert context.driver.find_element_by_xpath("//*[text()='Your password is now changed.']").text == text
    
@then('ensure that after click on reset my password button user should be get error message {text}')
def step_ensure_user_can_not_change_password_with_erong_email(context, text):
    print("error text here===========" + context.driver.find_element_by_xpath("//*[@class='errorlist']/li").text)
    assert context.driver.find_element_by_xpath("//*[@class='errorlist']/li").text == text

    
    