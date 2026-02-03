import os
import random
import datetime

year = 2026
start_month = 1
end_month = 2
num_commits = 40   # how many random commits you want

start_date = datetime.date(year, start_month, 1)
end_date = datetime.date(year, end_month, 28)

date_range_days = (end_date - start_date).days

for _ in range(num_commits):
    random_days = random.randint(0, date_range_days)
    random_date = start_date + datetime.timedelta(days=random_days)

    with open("medi.h5", "a") as file:
        file.write(str(random_date) + "\n")

    os.system("git add medi.h5")

    commit_date = random_date.strftime("%Y-%m-%dT12:00:00")

    os.system(f'git commit --date="{commit_date}" -m "Random commit {random_date}"')

os.system("git push origin main")