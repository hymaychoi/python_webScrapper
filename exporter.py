import csv


def save_to_file(jobs, keyword):
    file = open(f"{keyword}_jobs.csv", mode='w')
    writer = csv.writer(file)
    writer.writerow(["Position", "Company", "Link"])
    for job in jobs:
        writer.writerow(list(job.values()))
    return
