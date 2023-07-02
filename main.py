# Go to this web page: app.cloudqa.io/home/AutomationPracticeForm.
# Write a program or algorithm using Python and Selenium to automatically test any three fields on that page.
# The main goal of your program is to make sure it still works even if the position or any other properties of the HTML elements for those three fields change.
# Good luck with your task!

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

def waiting(driver, locator):
    return WebDriverWait(driver, 10).until(EC.element_to_be_clickable(locator))

def fetch_and_change_value(driver, field_locator, field_value):
    field = waiting(driver, field_locator)
    try:
        field.clear()
    except:
        pass
    field.send_keys(field_value)

def form_test(forms, driver):
    if len(forms) == 0:
        field_locator = (By.CSS_SELECTOR, "input[type='number']")
        fetch_and_change_value(driver, field_locator, "8546795221")

        field_locator = (By.TAG_NAME, "textarea")
        fetch_and_change_value(driver, field_locator, "About Yourself - I am [Your name] and I am [your occupation]")

        driver.find_element(By.CSS_SELECTOR, "input[type='radio'][value='Female']").click()
        return
    
    for form in forms:  
        fields = form.find_elements(By.TAG_NAME, "form")
        form_test(fields, driver)
    

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

print("Navigating to browser")
driver.get("http://app.cloudqa.io/home/AutomationPracticeForm")
driver.maximize_window()

try:
    forms = driver.find_elements(By.TAG_NAME, "form")
    form_test(forms, driver)

    input("Press any key to continue...")
finally:
    driver.quit()
    print("Quit the browser")