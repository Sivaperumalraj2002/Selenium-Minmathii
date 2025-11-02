from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import random
import pandas as pd
from datetime import datetime, timedelta
import time

root_url = r"https://minmathiidcard.bontonsoftwares.com/#/login"
node_url = r"https://minmathiidcard.bontonsoftwares.com/#/main/page/mathi/members/view/"

user_name = "username"
password = "password"

chrome_options = Options()
driver = webdriver.Chrome(options=chrome_options)  # Modern versions of Selenium will automatically manage the driver

driver.get(root_url)

userNameEle = driver.find_element(By.ID,'username')
userNameEle.send_keys(user_name)
passwordNameEle = driver.find_element(By.ID,'password-input')
passwordNameEle.send_keys(password)
passwordNameEle.send_keys(Keys.ENTER)

time.sleep(5)

df = pd.read_excel("dataset.xlsx")

KUPPUR = df[df['grampanchayat'] == "KUPPUR"]
village = KUPPUR.village.to_list()
id = KUPPUR.id.to_list()
dateOfFormation = KUPPUR.date_of_formation.to_list()



def generate_random_date(start_date, end_date):
    """
    Generates a random date between start_date and end_date.
    Returns the date in 'dd-mm-yyyy' format.
    """
    # Convert input strings to datetime objects
    start = datetime.strptime(start_date, "%d-%m-%Y")
    end = datetime.strptime(end_date, "%d-%m-%Y")

    # Calculate total number of days between dates
    delta = end - start

    # Pick a random number of days within the range
    random_days = random.randint(0, delta.days)

    # Generate and format the random date
    random_date = start + timedelta(days=random_days)
    return random_date.strftime("%d-%m-%Y")


def get_random_tamil_god():
    tamil_gods = [
        "Murugan",
        "Shiva",
        "Parvati",
        "Ganesha",
        "Vishnu",
        "Lakshmi",
        "Saraswati",
        "Perumal",
        "Krishna",
        "Rama",
        "Ayyappan",
        "Kali",
        "Durga",
        "Meenakshi",
        "Andal",
        "Karuppasamy",
        "Mariamman",
        "Veerabhadra",
        "Venkateswara",
        "Anjaneya"
    ]
    return random.choice(tamil_gods)


def generate_random_number(start, end):
    """
    Returns a random integer between start and end (inclusive).
    """
    return random.randint(start, end)

def generate_random_number_with_digits(digits):
    """
    Generates a random integer with the specified number of digits.
    Example: digits=4 → range 1000–9999
    """
    if digits <= 0:
        raise ValueError("Number of digits must be positive")

    lower = 10**(digits - 1)
    upper = (10**digits) - 1

    return random.randint(lower, upper)

def get_door_no():
    return f"{generate_random_number(3,4)}/{generate_random_number(50,150)}"

for i in range(len(id)):
    cur_node = f"{node_url}{id[i].strip()}"
    
    driver.get(cur_node)
    time.sleep(0.3)

    # Find all form groups
    form_groups = driver.find_elements(By.CSS_SELECTOR, ".form-group")

    # Loop through each group
    for group in form_groups:
        try:
            # Get label text
            label = group.find_element(By.TAG_NAME, "label").text.strip()

            # Try to find input or textarea
            try:
                field = group.find_element(By.TAG_NAME, "input")
            except:
                field = group.find_element(By.TAG_NAME, "textarea")

            # Get some identifying info (like formcontrolname or placeholder)
            value = field.get_attribute("value").strip()
            match label:
                case "Date of Birth":
                    if not value:
                        field.send_keys(generate_random_date("01-01-1990", "31-12-1999"))
                        field.send_keys(Keys.ENTER)
                case "Date of Joining":
                    if not value:
                        field.send_keys(generate_random_date(dateOfFormation[i], "01-10-2025"))
                        field.send_keys(Keys.ENTER)
                case "Contact Number":
                    if not value or len(value)>10:
                        field.send_keys(int("8"+str(generate_random_number_with_digits(9))))
                case "Aadhaar Number":
                    if not value:
                        field.send_keys(int("4"+str(generate_random_number_with_digits(9))))
                case "Husband Name":
                    if not value:
                        field.send_keys(get_random_tamil_god())
                case "PDS Number":
                    if not value:
                        field.send_keys(int("333"+str(generate_random_number_with_digits(9))))
                case "Occupation":
                    if not value or value == "-":
                        field.clear()
                        field.send_keys("Daily Wager")
                case "Pin Code":
                    if not value:
                        field.send_keys(636704)
                case "Address":
                    if not value:
                        field.send_keys(f"{get_door_no()}, {village[i]}, Kuppur, Dharmapuri.")

        except Exception as e:
            print("Skipped one group:", e)

    form = driver.find_element(By.TAG_NAME, "form")
    form.submit()


    # Create a short dynamic wait (it returns as soon as condition is met)
    wait = WebDriverWait(driver, 10)  # 10 is just the MAX limit, not a delay!

    # Wait for the SweetAlert popup to appear
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "swal2-popup")))

    # As soon as the popup is visible, click the OK button
    ok_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.swal2-confirm.swal2-styled"))
    )
    ok_button.click()
    print(i)




