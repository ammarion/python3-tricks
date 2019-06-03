def city_country(city, country):
     string_formatted = f"{city.title()} city is in  {country.title()} "
     return  string_formatted 



name = city_country('khartoum', 'sudan')
name1 = city_country('dongola', 'sudan')
print(name)
print(name1)