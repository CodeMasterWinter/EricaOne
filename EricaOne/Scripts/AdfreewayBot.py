import time
from random import choice
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException, ElementClickInterceptedException, StaleElementReferenceException

driver = webdriver.Firefox()
driver.get('https://adfreeway.com/users/sign_in')

# accept cookies

cookies = driver.find_element(By.CLASS_NAME, "js-cookies-eu-ok")
cookies.click()
time.sleep(5)

time.sleep(3)
#login sequence
username = driver.find_element(By.ID, "user_email")
username.send_keys("yabeenduped@gmail.com")

password = driver.find_element(By.ID, "user_password")
password.send_keys("#Yabeen112672")
time.sleep(3)

submit = driver.find_element(By.ID,"access-wifi-btn")
submit.click()
time.sleep(5)
print("Login sequence complete")

print("initiating like sequence")
elements = []
states = ["left-btn-form", "right-btn-form"]
while True:
    posts = driver.find_elements(By.CLASS_NAME, "ugc-wrap")
    for post in posts:
        if post not in elements:
            try:
                driver.execute_script("arguments[0].scrollIntoView();", post)
                time.sleep(0.1)

                liking = True
                while liking:
                    like = post.find_element(By.CLASS_NAME, choice(states))
                    driver.execute_script("arguments[0].scrollIntoView();", like)
                    try:
                        like.click()
                        time.sleep(0.5)
                        elements.append(post)
                        break
                    except ElementNotInteractableException:
                        driver.execute_script("window.scrollBy(0, 100);")
                        continue
                    except ElementClickInterceptedException:
                        driver.refresh()
                        break
                    except StaleElementReferenceException:
                        driver.refresh()
                        break
            except StaleElementReferenceException:
                driver.refresh()
                break