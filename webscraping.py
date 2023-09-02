import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize Chrome driver
driver = webdriver.Chrome()

# Maximize the browser window
driver.maximize_window()

# Navigate to the website
driver.get("https://www.dgca.gov.in/digigov-portal/?page=259/4184/servicename")
time.sleep(5)

# Wait for the first search input element to be present
search_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "form-control.form-control-sm"))
)

# Input your search query
search_input.send_keys("Indigo")

# Wait for the link element to be clickable
link_element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="DataTables_Table_0"]/tbody/tr/td[4]/font/a'))
)

# Click on the link
link_element.click()
time.sleep(3)
# Wait for the second input field to be present
input_field_2 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="DataTables_Table_1_filter"]/label/input'))
)

# Input text into the second input field
input_text = "indigo"
input_field_2.send_keys(input_text)

# Click on the specified element using its XPath
element_to_click = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="DataTables_Table_1"]/tbody/tr/td[4]/font/a'))
)
element_to_click.click()
time.sleep(3)
# Wait for the third input field to be present
input_field_3 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="DataTables_Table_2_filter"]/label/input'))
)

# Input text into the third input field
input_text_3 = "indigo"
input_field_3.send_keys(input_text_3)

# Click on the specified link using its XPath
link_to_click = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="DataTables_Table_2"]/tbody/tr/td[4]/font/a'))

)
link_to_click.click()
time.sleep(3)
# Wait for the fourth input field to be present
input_field_4 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="DataTables_Table_3_filter"]/label/input'))
)

# Input text into the forth input field
input_text_4 = "indigo"
input_field_4.send_keys(input_text_4)

# Click on the specified link using its XPath
link_to_click1 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="DataTables_Table_3"]/tbody/tr/td[4]/font/a'))

)
link_to_click1.click()

time.sleep(3)
# Wait for the fifth input field to be present
input_field_5 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="DataTables_Table_4_filter"]/label/input'))
)

# Input text into the fifth input field
input_text_5 = "indigo"
input_field_5.send_keys(input_text_5)

# Click on the specified link using its XPath
link_to_click2 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="DataTables_Table_4"]/tbody/tr/td[4]/font/a'))

)
link_to_click2.click()
time.sleep(3)
# Wait for the sixth input field to be present
input_field_6 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="DataTables_Table_5_filter"]/label/input'))
)

# Input text into the sixth input field
input_text_6 = "indigo"
input_field_6.send_keys(input_text_6)

# Click on the specified link using its XPath
link_to_click3 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="DataTables_Table_5"]/tbody/tr/td[4]/font/a'))

)
link_to_click3.click()
time.sleep(3)
# Wait for the seventh input field to be present
input_field_7 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="DataTables_Table_6_filter"]/label/input'))
)

# Input text into the seventh input field
input_text_7 = "indigo"
input_field_7.send_keys(input_text_7)

# Click on the specified link using its XPath
link_to_click4 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="DataTables_Table_6"]/tbody/tr/td[4]/font/a'))

)
link_to_click4.click()
time.sleep(3)
# Wait for the eight input field to be present
input_field_8 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="DataTables_Table_7_filter"]/label/input'))
)

# Input text into the eight input field
input_text_8 = "indigo"
input_field_8.send_keys(input_text_8)

# Click on the specified link using its XPath
link_to_click5 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="DataTables_Table_7"]/tbody/tr/td[4]/font/a'))

)
link_to_click5.click()
time.sleep(6)
# Close the browser when done
driver.quit()
