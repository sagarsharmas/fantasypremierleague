#Usage: python FantasyPremierLeague.py league_url
#e.g.: python FantasyPremierLeague.py https://fantasy.premierleague.com/a/leagues/standings/167244/classic
import time,sys
from selenium import webdriver
from selenium.webdriver.common.by import By
chromedriver = "/home/dell/Documents/chromedriver"
driver = webdriver.Chrome(chromedriver)

urls = []
result = dict()

driver.get(sys.argv[-1]) #The argument should be the league URL
time.sleep(2)
tbody = driver.find_element_by_css_selector("tbody")
for row in tbody.find_elements(By.TAG_NAME, "tr"):
	urls.append(row.find_element(By.TAG_NAME, "a").get_attribute("href"))

for url in urls:
	driver.get(url)
	time.sleep(2)
	x=driver.find_element_by_xpath("//*[@id=\"ismr-side\"]/div/section/h2").text
	y=driver.find_element_by_xpath("//*[@id=\"ismr-scoreboard\"]/div/div[2]/div[1]/div/div").text
	y = int(y[:2])
	z=driver.find_element_by_xpath("//*[@id=\"ismr-side\"]/div/section/div/div[2]/div[1]/ul/li[1]/div").text
	result[x]=[y,z]
driver.quit()
print "{:<20} {:<15} {:<10}".format('Player','Gameweek','Total')
for k, v in sorted(result.items(), key=lambda (k, (v1, v2)): v1,reverse=True):
    label, num = v
    print "{:<20} {:<15} {:<10}".format(k, label, num)
