from selenium import webdriver

def before_all(context):
#     context.driver = webdriver.Firefox(executable_path='/Users/jamit/Downloads/driver/geckodriver')
    context.driver = webdriver.Chrome(executable_path='/Users/jamit/Downloads/driver/chromedriver')
    context.driver.maximize_window()
    context.driver.implicitly_wait(30)
def after_all(context):
    context.driver.quit()