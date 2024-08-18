import re
from selenium import webdriver
from flask import Flask,jsonify
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager



app = Flask(__name__)


@app.route("/")
def upcomingContest():
    opt = webdriver.ChromeOptions()
    opt.add_argument("--headless")
    opt.add_argument("--no-sandbox")
    opt.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=opt)
    driver. get ( "https://smartinterviews.in/contests" )
    wait = WebDriverWait(driver, 10) 
    ele = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='contest-card']")))

    contests = driver.find_elements(By.XPATH,"//div[@class='contest-card']")

    cards = []

    for contest in contests:
        link = contest.find_element(By.XPATH,".//a")
        s=["title"]
        s += re.split(': | *\n',contest.text)
        m={}
        for i in range(0,len(s),2):
            m[s[i]]=s[i+1]
        if "Starts in" in m.keys():
            if "days" in m["Starts in"] and int(m["Starts in"].split("days")[0]) >7:
                break
        m["url"]=link.get_attribute("href")
        cards.append(m)
    driver.quit()

    return jsonify(cards) 


if __name__=="__main__":
    app.run(debug=True,port=3000)

