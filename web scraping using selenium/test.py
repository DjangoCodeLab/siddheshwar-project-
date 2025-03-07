from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
# Setup WebDriver
driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

# Navigate to the web page
driver.get('https://www.adamchoi.co.uk/overs/detailed')

# Define your XPath expression
xpath_expression = '//label[@analytics-event="All matches"]'
date = []
home_team = []
score = []
away_team = []

try:
    # Find the element using XPath
    element = driver.find_element(By.XPATH, xpath_expression)
    
    # Interact with the element (for example, click it)
    element.click()

    
    tags = driver.find_elements(By.TAG_NAME,'tr' )

    
    for tag in tags:
        date_tag = tag.find_element(By.XPATH,'./td[1]').text
        home_team_tag= tag.find_element(By.XPATH,'./td[2]').text
        score_tag = tag.find_element(By.XPATH,'./td[3]').text
        away_team_tag = tag.find_element(By.XPATH,'./td[4]').text

        date.append(date_tag)
        home_team.append(home_team_tag)
        score.append(score_tag)
        away_team.append(away_team_tag)


    # Print success message
    print(f"Element found and clicked using XPath: {xpath_expression}")
except Exception as e:
    print(f"Error: {str(e)}")


df = pd.DataFrame({
    'date': date,
    'home_team':home_team,
    'score':score_tag,
    'away_team':away_team
})

df.to_csv('data.csv', index = False)
# Close the driver
# driver.quit()
