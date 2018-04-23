from behave import given, when, then
from common import Locater
 
@given('the user on medsembly signup page')
def step_user_on_signup_page(context):
    context.driver.get(Locater.url + 'accounts/signup/')
     
@when('user enter {email} as email in signup form')
def step_user_enter_email(context, email):
    context.driver.find_element_by_id('id_email').send_keys(email)
     
@when('user enter {password} as password in signup form')
def step_user_enter_password(context, password):
    context.driver.find_element_by_id('id_password1').send_keys(password)
     
@when('user enter {confirm_password} as confirm password in signup form')
def step_user_enter_confirm_password(context, confirm_password):
    context.driver.find_element_by_id('id_password2').send_keys(confirm_password)
     
@when('user click on signup button for signup')
def step_user_click_on_signup_button(context):
    context.driver.find_element_by_xpath("//*[@class='btn bg-red white-text' and text()='Sign Up']").click()
     
@then('ensure that user should get notification for {text}')
def step_ensure_user_verification_notification(context, text):
    print("error text here===========" + context.driver.find_element_by_xpath("//*[@class='card-body text-center']/h1").text)
    assert context.driver.find_element_by_xpath("//*[@class='card-body text-center']/h1").text == text
     
@given('user go to mailinator.com to verify mail')
def step_user_goto_mailinator(context):
    context.driver.get('http://www.mailinator.com/v2/inbox.jsp?zone=public&query=jamit')
     
@when('user open mail for confirm mail id')
def step_open_mail_for_confirm_mail(context):
    context.driver.find_element_by_xpath("//*[text()='[Medsembly] E-mail Confirmation']").click()
     
@when('user click on confirm link')
def step_click_on_verification_link(context):
    iframe = context.driver.find_element_by_id('msg_body')
    context.driver.switch_to_frame(iframe)
    context.driver.find_element_by_partial_link_text(Locater.url+'accounts/confirm-email/').click()
     
@then('ensure that user should redirect to {text} page to verify email')   
def step_ensure_user_redirect_to_confirm_page(context, text):
    window_change = context.driver.window_handles[1]
    context.driver.switch_to_window(window_change)
    print("error text here===========" + context.driver.find_element_by_xpath("//*[text()='Confirm E-mail Address']").text)
    assert context.driver.find_element_by_xpath("//*[text()='Confirm E-mail Address']").text == text
     
@when('user click on confirm button to verify mail')
def step_user_click_on_confirm_button(context):
    context.driver.find_element_by_xpath("//*[@class='btn bg-red white-text' and text()='Confirm']").click()
     
@then('ensure that after verification user goes to {text} page')
def step_ensure_user_on_login(context, text):
    print("error text here===========" + context.driver.find_element_by_xpath("//*[@class='card-header text-center white-text bg-red']/h2").text)
    assert context.driver.find_element_by_xpath("//*[@class='card-header text-center white-text bg-red']/h2").text == text
     
@then('ensure that user should get error notification {text}')
def step_ensure_user_already_register(context, text):
    print("error text here===========" + context.driver.find_element_by_xpath("//*[@class='errorlist']/li").text)
    assert context.driver.find_element_by_xpath("//*[@class='errorlist']/li").text == text




     
     