# Page 1/2
# Connect us on Twitter @myrzadev

country = ['Austria', 'Germany', 'Bosnia', 'USA', ]
city = ['Vienna', 'Berlin', 'Sarajevo', 'New York']
continent = ['Europe', 'Europe', 'Europe', 'North America']

for country, city, continent in zip(country, city, continent):
    print(f"{country} - {city} - {continent}")
    
# Page 2/2

country = ['Austria', 'Germany', 'Bosnia', 'USA', ]
city = ['Vienna', 'Berlin', 'Sarajevo', 'New York']
continent = ['Europe', 'Europe', 'Europe', 'North America']

for value in zip(country, city, continent):
    print(value) 
