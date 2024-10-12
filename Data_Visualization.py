import pandas as pd

import matplotlib.pyplot as plt



dataset = pd.read_csv("covid.csv")

states = dataset["Name of State / UT"]

total_confirmed = dataset["Total Confirmed cases"]

total_deaths = dataset["Death"]

total_cured = dataset["Cured/Discharged/Migrated"]


plt.bar(states, total_confirmed, label="Total Confirmed")

plt.bar(states, total_deaths, label="Total Deaths")

plt.bar(states, total_cured, label="Total Cured/Discharged/Migrated")


plt.xlabel("State/UT")

plt.ylabel("Number of Cases")

plt.title("COVID-19 Cases in India by State/UT")

plt.legend()

plt.xticks(rotation=90)  # Rotate x-axis labels for better readability

plt.tight_layout()  # Adjust layout to fit labels

plt.show()

labels = ["Total Cases", "Total Deaths", "Total Recovered"]

sizes = [total_cases.sum(), total_deaths.sum(), total_recovered.sum()]


plt.pie(sizes, labels=labels, autopct="%1.1f%%")

plt.title("COVID-19 Cases Proportion")

plt.show()

