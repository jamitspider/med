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
#     print("error text here===========" + context.driver.find_element_by_xpath("//*[@role='alert']/h2").text)
#     assert context.driver.find_element_by_xpath("//*[@role='alert']/h2").text == text

    print("error text here===========" + context.driver.current_url)
    assert context.driver.current_url == Locater.url +"dashboard"
    
@when('user click on user profile pic to select logout')
def step_user_click_on_profile_image(context):
    context.driver.find_element_by_id('navbarDropdown').click()
    
@when('user click on logout button in navbar dropdown')
def step_user_click_on_logout_in_navbar_dropdown(context):
    context.driver.find_element_by_xpath("//*[@href='/accounts/logout/']").click()
    
@when('user click on sign out button to confirm logout from the Medsembly')
def step_user_click_on_signout_button_to_confirm_logout(context):
    context.driver.find_element_by_xpath("//*[@class='btn bg-red white-text' and text()='Sign Out']").click()
    
@then('ensure that user should be redirect to signin page of Medsembly and recive message {text}')
def step_ensure_user_signout(context, text):
#     print("error text here===========" + context.driver.find_element_by_xpath("//*[@role='alert']/h2").text)
#     assert context.driver.find_element_by_xpath("//*[@role='alert']/h2").text == text

    print("error text here===========" + context.driver.current_url)
    assert context.driver.current_url == Locater.url +"accounts/login/"
    
@then('ensure that user should get error message {text}')
def step_ensure_user_login_failed(context, text):
    print("error text here===========" + context.driver.find_element_by_xpath("//*[@class='errorlist nonfield']/li").text)
    assert context.driver.find_element_by_xpath("//*[@class='errorlist nonfield']/li").text == text