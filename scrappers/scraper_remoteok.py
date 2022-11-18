from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

BASE_URL = "https://remoteok.com/"
s = Service('C:\Program Files (x86)\chromedriver.exe')
driver = webdriver.Chrome(service=s)


def get_remoteok_jobs(keyword):
    driver.get(f"{BASE_URL}/remote-dev+{keyword}-jobs")
    jobs = []
    jobs_elems = driver.find_elements(
        By.XPATH, "//table[@id='jobsboard']/tbody/tr[@data-url]")

    for job in jobs_elems:
        company = job.get_attribute("data-company")
        position = job.find_element(
            By.CLASS_NAME, "company_and_position").find_element(By.TAG_NAME, 'a').text
        link = BASE_URL+job.get_attribute("data-url")
        jobs.append({"company": company,
                     "position": position,
                     "link": link})
        print("scraping wework jobs")
    return jobs
