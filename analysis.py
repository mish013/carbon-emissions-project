

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('emissions.csv')

uk = df[df["country_name"] == "United Kingdom"].sort_values("year")
usa = df[df["country_name"] == "United States"].sort_values("year")
rus = df[df["country_name"] == "Russian Federation"].sort_values("year")
ch =  df[df["country_name"]== "China"].sort_values("year")
ind = df[df["country_name"]== "India"].sort_values("year")

plt.figure(figsize=(10,5))

plt.plot(usa["year"], usa["value"], label="USA")
plt.plot(uk["year"], uk["value"], label="UK")
plt.plot(rus["year"], rus["value"], label="Russia")
plt.plot(ch["year"], ch["value"], label="China")
plt.plot(ind["year"], ind["value"], label="India")

plt.title("CO2 Emissions")
plt.xlabel("Year")
plt.ylabel("Emissions Value")
plt.grid(True, alpha=0.3)
plt.legend()

plt.savefig("emissions_comparisons.png")
plt.show()