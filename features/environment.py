import allure
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# This hook is executed before all scenarios
def before_scenario(context, driver):
    context.driver = webdriver.Chrome(service=webdriver.ChromeService(ChromeDriverManager().install()))

# This hook is executed after all scenarios
def after_scenario(context, driver):
    context.driver.quit()

def after_step(context, step):
    print()
    if step.status == 'failed':
        allure.attach(context.driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)