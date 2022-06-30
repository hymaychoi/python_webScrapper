import requests
import math
from bs4 import BeautifulSoup

def get_last_page(url):
  result = requests.get(url)
  soup = BeautifulSoup(result.text, "html.parser")
  pagination = soup.find('span', {'class':'ResultText-numTotal'})
  total_jobs = int(pagination.text)
  jobs_per_page = 20
  last_page = math.ceil(total_jobs / jobs_per_page)
  return last_page

def extract_jobs(last_page, url):
  jobs=[]
  for page in range(last_page):
    print(f"scrapping page {page + 1}")
    result = requests.get(f"{url}&pn={page+1}")
    soup = BeautifulSoup(result.text, 'html.parser')
    results = soup.find_all("article", {"class":"JobCard"})
    for result in results:
      job = save_jobs(result, url)
      jobs.append(job)
  return jobs

def save_jobs(html, url):
  position = html.find("h2", {"class":"JobCard-title"})["title"]
  company = html.find("div", {"class":"JobCard-company"}).text
  link = f'{url}&job={html["data-jobkey"]}'
  return {"position": position, 
          "company": company, 
          "link": link}

def get_workpolis_jobs(keyword):
  url=f"https://www.workopolis.com/jobsearch/find-jobs?ak={keyword}&l=Remote&lg=en&st=true"
  last_page = get_last_page(url)
  jobs=extract_jobs(last_page, url)
  return jobs
