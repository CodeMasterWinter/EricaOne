import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.get('https://acgl.gg/user/login')

#login sequence
print('Attempting sign in...')
username = driver.find_element(By.ID, "edit-name")
username.send_keys("theSuperlonely")

password = driver.find_element(By.ID, "edit-pass")
password.send_keys("Proxima28")

time.sleep(2)
submit = driver.find_element(By.ID, "edit-submit")
submit.click()

time.sleep(3)

#navigating to rebuild page
nav = driver.find_element(By.CSS_SELECTOR, '[title="Redragon Digital Keyboard Rebuild"]')
nav.click()
#rebuild sequence
sequence_counter = 0

while True:
        if sequence_counter > 0:
            retry = driver.find_element(By.ID, "try_again")
            retry.click()
            time.sleep(1)

        outer = driver.find_element(By.CLASS_NAME, 'keyboard_outer')
        driver.execute_script("arguments[0].scrollIntoView();", outer)
        time.sleep(0.5)
        keys = driver.find_elements(By.CLASS_NAME, 'ui-draggable')
        for key in keys:
            slot_id = key.get_property('id').replace('key_', 'slot_')
            slot = driver.find_element(By.ID, slot_id)
            actions = ActionChains(driver)
            actions.drag_and_drop(key, slot).perform()
            time.sleep(1)
        submit = driver.find_element(By.CLASS_NAME, 'submit')
        submit.click()
        time.sleep(3)
        sequence_counter += 1
        print(sequence_counter)