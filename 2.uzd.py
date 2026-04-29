import requests

# 1. Izveido pieprasījumu uz API
url = "https://restcountries.com/v3.1/all"
response = requests.get(url)

# 2. Pārbaudi, vai atbilde ir korekta
if response.status_code == 200:
    countries = response.json()
    print("Dati veiksmīgi saņemti!\n")
else:
    print("Kļūda pieprasījumā:", response.status_code)
    exit()

# 3. Izvadi visu valstu nosaukumus
print("Valstu nosaukumi:")
for country in countries:
    print(country["name"]["common"])

# 4. Kopējais valstu skaits
total_countries = len(countries)
print("\nKopējais valstu skaits:", total_countries)

# 5. Vidējais iedzīvotāju skaits
total_population = sum(country.get("population", 0) for country in countries)
average_population = total_population / total_countries
print("Vidējais iedzīvotāju skaits:", round(average_population))

# 6. Valsts ar lielāko iedzīvotāju skaitu
most_populated = max(countries, key=lambda c: c.get("population", 0))
print("Valsts ar lielāko iedzīvotāju skaitu:",
      most_populated["name"]["common"],
      "-", most_populated["population"])

# 7. Kopējā platība
total_area = sum(country.get("area", 0) for country in countries)
print("Visu valstu kopējā platība:", round(total_area), "km²")

# 8. Informācija par Latviju
for country in countries:
    if country["name"]["common"] == "Latvia":
        print("\nLatvija:")
        print("Apakšreģions:", country.get("subregion", "Nav datu"))
        print("Robežvalstis:", country.get("borders", []))