from selenium import webdriver
import time
website = 'https://adamchoi.co.uk/overs/detailed'

path = '/Users/HP/Downloads/edgedriver_win64'
driver = webdriver.Edge(path)
driver.get(website)
time.sleep(5)
# driver.quit()
all_matches_button = driver.find_element('//label[@analytics-event= "All matches"]')
all_matches_button.click()


# //tag_name[@attribute= "Class_Name"]

