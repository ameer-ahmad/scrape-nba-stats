from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import json
import os

def getPlayers():
    players_table = driver.find_element(By.CLASS_NAME, "Crom_table__p1iZz")
    rows = players_table.find_elements(By.CSS_SELECTOR, "tbody tr")
    
    for row in rows:
        player = row.find_elements(By.TAG_NAME, "td")
        playerInfo = {}
        playerInfo['name'] = player[1].text
        playerInfo['image'] = player[1].find_element(By.TAG_NAME, "a").get_attribute('href').split('/')[-2]
        playerInfo['mpg'] = player[7].text
        playerInfo['ppg'] = player[8].text
        playerInfo['rpg'] = player[20].text
        playerInfo['apg'] = player[21].text
        playerInfo['tpg'] = player[22].text
        playerInfo['spg'] = player[23].text
        playerInfo['bpg'] = player[24].text
        playerStats.append(playerInfo)

playerStats = []

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.nba.com/stats/players/traditional?PerMode=PerGame&dir=A&sort=NBA_FANTASY_PTS")

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "DropDown_select__4pIg9"))
)
select_element = driver.find_elements(By.CLASS_NAME, 'DropDown_select__4pIg9')[-1]
dropdown = Select(select_element)
dropdown.select_by_value("-1")

getPlayers()

driver.quit

json_data = json.dumps(playerStats)
with open('player_stats.json', 'w') as file:
    file.write(json_data)

os.system('git add .')
os.system('git commit -m "Daily update"')
os.system('git push main')