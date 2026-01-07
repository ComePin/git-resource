from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    StaleElementReferenceException,
    NoSuchElementException,
    TimeoutException,
)
import time


def withdraw_invitations():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 15)
    driver.maximize_window()

    try:
        # Step 1: Manual Login
        driver.get("https://www.linkedin.com/login")
        print("⏳ Please log in manually within 20 seconds...")
        time.sleep(20)

        # Step 2: Navigate to Sent Invitations
        driver.get("https://www.linkedin.com/mynetwork/invitation-manager/sent/")
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        time.sleep(2)

        # Step 3: Loop for Withdrawals
        while True:
            try:
                wait.until(EC.presence_of_all_elements_located(
                    (By.XPATH, "//span[contains(text(), 'Withdraw')]")))
                withdraw_buttons = driver.find_elements(By.XPATH, "//span[contains(text(), 'Withdraw')]")

                if not withdraw_buttons:
                    print("✅ All invitations withdrawn or none left.")
                    break

                for button in withdraw_buttons:
                    try:
                        driver.execute_script("arguments[0].click();", button)
                        confirm_button = wait.until(EC.presence_of_element_located(
                            (By.XPATH,
                             "//h2[contains(text(), 'Withdraw invitation')]/ancestor::header/../div//button[contains(@aria-label,'Withdraw')]")
                        ))
                        driver.execute_script("arguments[0].click();", confirm_button)
                        time.sleep(2)
                    except (StaleElementReferenceException, NoSuchElementException, TimeoutException) as e:
                        print("⚠️ Skipped one due to:", e)
                        continue

                # Load more invitations
                try:
                    load_more = wait.until(EC.element_to_be_clickable(
                        (By.XPATH, "//span[text()='Load more']")
                    ))
                    driver.execute_script("arguments[0].scrollIntoView();", load_more)
                    load_more.click()
                    time.sleep(3)
                except TimeoutException:
                    print("📦 No more invitations to load.")
                    break

            except TimeoutException:
                print("⏰ Timeout while finding 'Withdraw' buttons.")
                break
    finally:
        driver.quit()
        print("🚪 Done and browser closed.")


# Run it
withdraw_invitations()