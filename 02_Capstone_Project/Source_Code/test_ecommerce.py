import json
import os

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# ============================================================
# LOAD TEST DATA
# ============================================================

with open("test_data/testdata.json", "r") as file:
    test_data = json.load(file)


# ============================================================
# CREATE REQUIRED FOLDERS
# ============================================================

os.makedirs("screenshots", exist_ok=True)
os.makedirs("reports", exist_ok=True)


# ============================================================
# TEST CASE
# ============================================================

def test_ecommerce_purchase():

    # --------------------------------------------------------
    # 1. LAUNCH BROWSER
    # --------------------------------------------------------

    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 15)

    driver.maximize_window()

    try:

        # ----------------------------------------------------
        # OPEN APPLICATION
        # ----------------------------------------------------

        driver.get(test_data["url"])

        print("\nApplication launched successfully.")

        # ----------------------------------------------------
        # 2. LOGIN TO APPLICATION
        # ----------------------------------------------------

        my_account = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//span[contains(text(),'My Account')]")
            )
        )
        my_account.click()

        login_link = wait.until(
            EC.element_to_be_clickable(
                (By.LINK_TEXT, "Login")
            )
        )
        login_link.click()

        email_field = wait.until(
            EC.visibility_of_element_located(
                (By.ID, "input-email")
            )
        )

        password_field = wait.until(
            EC.visibility_of_element_located(
                (By.ID, "input-password")
            )
        )

        email_field.send_keys(test_data["username"])
        password_field.send_keys(test_data["password"])

        login_button = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//input[@value='Login']")
            )
        )

        login_button.click()

        print("Login completed successfully.")

        # ----------------------------------------------------
        # 3. SEARCH PRODUCT
        # ----------------------------------------------------

        search_box = wait.until(
            EC.visibility_of_element_located(
                (By.NAME, "search")
            )
        )

        search_box.clear()
        search_box.send_keys(test_data["product"])
        search_box.send_keys(Keys.ENTER)

        print(
            f"Product search completed: "
            f"{test_data['product']}"
        )

        # ----------------------------------------------------
        # 4. ADD PRODUCT TO CART
        # ----------------------------------------------------
        product_link = wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    f"//div[contains(@class,'product-layout')]"
                    f"//a[contains(normalize-space(), "
                    f"'{test_data['product']}')]"
                )
            )
        )

        driver.execute_script(
            "arguments[0].click();",
            product_link
        )

        print("Product selected successfully.")

        add_to_cart_button = wait.until(
            EC.element_to_be_clickable(
                (
                    By.ID,
                    "button-cart"
                )
            )
        )

        add_to_cart_button.click()

        print("Product added to cart.")
        # ----------------------------------------------------
        # HANDLE POSSIBLE CART SUCCESS MESSAGE
        # ----------------------------------------------------

        try:

            wait.until(
                EC.visibility_of_element_located(
                    (
                        By.CSS_SELECTOR,
                        ".alert-success"
                    )
                )
            )

            print("Cart success notification displayed.")

        except Exception:

            print(
                "No success popup detected. "
                "Continuing with the test."
            )

        # ----------------------------------------------------
        # 5. UPDATE QUANTITY
        # ----------------------------------------------------

        cart_link = wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//a[contains(@href,'checkout/cart')]"
                )
            )
        )

        cart_link.click()

        quantity_field = wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//input[contains(@name,'quantity')]"
                )
            )
        )

        quantity_field.click()
        quantity_field.send_keys(Keys.CONTROL, "a")
        quantity_field.send_keys(
            str(test_data["quantity"])
        )

        # Click update button
        update_button = wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//button[contains(@name,'update')]"
                    " | //button[contains(@data-original-title,'Update')]"
                )
            )
        )

        update_button.click()

        print(
            f"Quantity updated to "
            f"{test_data['quantity']}."
        )

        # ----------------------------------------------------
        # 6. VERIFY CART DETAILS
        # ----------------------------------------------------

        updated_quantity = wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//input[contains(@name,'quantity')]"
                )
            )
        )

        actual_quantity = updated_quantity.get_attribute(
            "value"
        )

        assert actual_quantity == str(
            test_data["quantity"]
        ), (
            f"Expected quantity "
            f"{test_data['quantity']} "
            f"but found {actual_quantity}"
        )

        print(
            "Cart quantity verification successful."
        )

        # Verify product appears in cart

        cart_product = wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//div[contains(@class,'table-responsive')]"
                    "//tbody//tr//td[2]//a"
                )
            )
        )

        cart_product_text = cart_product.text.strip()

        assert test_data["product"] in cart_product_text, (
            f"Expected product '{test_data['product']}' "
            f"was not found in cart."
        )

        print("Cart product verification successful.")

        # ----------------------------------------------------
        # 7. CAPTURE SCREENSHOT
        # ----------------------------------------------------

        screenshot_path = (
            "screenshots/cart_verification.png"
        )

        driver.save_screenshot(
            screenshot_path
        )

        print(
            f"Screenshot captured: "
            f"{screenshot_path}"
        )

        # ----------------------------------------------------
        # 9. HANDLE POPUP / ALERT IF AVAILABLE
        # ----------------------------------------------------

        try:

            alert = WebDriverWait(
                driver, 3
            ).until(
                EC.alert_is_present()
            )

            alert.accept()

            print(
                "Browser alert detected and accepted."
            )

        except Exception:

            print(
                "No browser alert was present."
            )

        # ----------------------------------------------------
        # FINAL RESULT
        # ----------------------------------------------------

        print(
            "\n========================================"
        )
        print(
            "TEST COMPLETED SUCCESSFULLY"
        )
        print(
            "========================================"
        )

    except Exception:

        # Capture screenshot if test fails

        failure_screenshot = (
            "screenshots/test_failure.png"
        )

        driver.save_screenshot(
            failure_screenshot
        )

        print(
            f"\nTest failed. "
            f"Failure screenshot saved at: "
            f"{failure_screenshot}"
        )

        raise

    finally:

        # ----------------------------------------------------
        # CLOSE BROWSER
        # ----------------------------------------------------

        driver.quit()
        print("Browser closed.")