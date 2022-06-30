from flask import Flask, render_template, request, redirect, send_file
from scrappers.scraper_workpolis import get_workpolis_jobs
from scrappers.scraper_wework import get_wework_jobs
from scrappers.scraper_remoteok import get_remoteok_jobs
from exporter import save_to_file

app= Flask("RemoteJobScrapper")
#fake db
db={}

@app.route("/")
def home():
  return render_template('home.html')

@app.route("/result")
def result():
  # this data is from the search input in search page
  keyword = request.args.get("keyword")
  if keyword:
    keyword = keyword.lower()
    existing_jobs = db.get(keyword)
    if existing_jobs:
      jobs = existing_jobs
    else:
      jobs = get_remoteok_jobs(keyword)+ get_wework_jobs(keyword) + get_workpolis_jobs(keyword)
      db[keyword] = jobs
  else:
    return redirect("/") 
  return render_template( 'result.html',
                          searchingBy=keyword,
                          resultNumber=len(jobs),
                          jobs=jobs )

@app.route("/export")
def export():
  try:
    keyword = request.args.get("keyword")
    if not keyword:
      raise Exception()
    keyword = keyword.lower()
    jobs = db.get(keyword)
    if not jobs: 
      raise Exception()
    save_to_file(jobs, keyword)
    return send_file(f"{keyword}_jobs.csv")
  except:
    return redirect("/") 
    
app.run(debug=True)