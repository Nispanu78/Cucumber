import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


@given(u'I navigate to google.com')
def step_impl(context):
    context.driver = webdriver.Chrome(service=webdriver.ChromeService(ChromeDriverManager().install()))
    context.driver.get("http://google.com")



@when(u'I validate the page title')
def step_impl(context):
    title = context.driver.title
    print("Title is " + title)
    assert "Google" in title

@then(u'I enter the text as "{search_text}"')
def step_impl(context, search_text):
    # Here we handle the "accept all cookies" pop-up window in Google
    context.accept_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Accept all']"))
    )
    context.accept_button.click()
    # Here we locate the search box and insert text
    context.driver.find_element(By.NAME, "q").send_keys(search_text)
    time.sleep(3)

@then(u'I click the search button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//div[@id='jZ2SBf']//div[1]//span[1]").click()
    time.sleep(3)
