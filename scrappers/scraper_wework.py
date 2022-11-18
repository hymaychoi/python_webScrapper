from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

BASE_URL = "https://weworkremotely.com/remote-jobs/search?term="
s = Service('C:\Program Files (x86)\chromedriver.exe')
driver = webdriver.Chrome(service=s)


def get_wework_jobs(keyword):
    driver.get(f"{BASE_URL}{keyword}")
    jobs = []
    feature_jobs = driver.find_elements(
        By.XPATH, '//section[@class="jobs"]/article/ul/li[@class="feature"]/a')
    no_feature_jobs = driver.find_elements(
        By.XPATH, '//section[@class="jobs"]/article/ul/li[@class=""]/a')
    jobs_elems = feature_jobs + no_feature_jobs

    for job in jobs_elems:
        if len(job.text) == 0:
            continue
        else:
            company = job.find_element(By.CLASS_NAME, "company").text
            position = job.find_element(By.CLASS_NAME, "title").text
            link = job.get_attribute("href")
            jobs.append({"company": company,
                         "position": position,
                         "link": link})
            print("scraping wework jobs")
    return jobs
