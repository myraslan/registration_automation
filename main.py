from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

username = "username"
password = "password"
course1= "ENG 103"

driver.get("https://registrar.nu.edu.kz/my-registrar")
driver.find_element("id", "edit-name").send_keys(username)
driver.find_element("id", "edit-pass").send_keys(password)
driver.find_element("name", "op").click()
driver.find_element("link text", "COURSE REGISTRATION").click()
driver.find_element("id", "titleText-inputEl").send_keys(course1)
driver.find_element("id", "show_courses_button-btnEl").click()
driver.implicitly_wait(10)
driver.find_element("class name", "x-grid-cell-inner").click()
driver.find_element("link text", "Add to Selected Courses").click()
driver.find_element("link text", "Go to Selected Courses").click()
driver.find_element("class name", "course-cloud").click()
driver.find_element("xpath","//input[@value='Section 2']").click()
driver.find_element("link text", "Pre-Register").click()
