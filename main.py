import requests
import os
import platform

if 'Linux' in platform.os:
    os.system("clear")
else:
    os.system("clear")
requestedIP = input("Victim's IP: ")
if 'Linux' in platform.os:
    os.system("clear")
else:
    os.system("clear")
response = requests.get(f"https://ipapi.co/{requestedIP}/json")
ip = response.json()
print("IP: " + ip['ip'])
print("Version: " + ip['version'])
print("City: " + ip['city'])
print("Region: " + ip['region'])
print("Region Code: " + ip['region_code'])
print("Country Code: " + ip['country_code'])
print("Country Code ISO3: " + ip['country_code_iso3'])
print("Country Name: " + ip['country_name'])
print("Country Capital: " + ip['country_capital'])
print("Country TLD: " + ip['country_tld'])
print("Continent Code: " + ip['continent_code'])
print("Is in EU: " + str(ip['in_eu']))
print("Postal Code: " + ip['postal'])
print("Latitude: " + str(ip['latitude']))
print("Longitude: " + str(ip['longitude']))
print("Timezone: " + ip['timezone'])
print("UTC Offset: " + ip['utc_offset'])
print("Country Calling Code: " + ip['country_calling_code'])
print("Currency: " + ip['currency'])
print("Currency Name: " + ip['currency_name'])
print("Langauges used in country: " + ip['languages'])
print("Country area: " + str(ip['country_area']))
print("Country population: " + str(ip['country_population']))
print("ASN: " + ip['asn'])
print("Organisation: " + ip['org'])
print()
saveFile = input("Save to file? (yes/no)")
if(saveFile == "yes"):
    with open('info.txt', 'w') as file:
        file.write("IP: " + ip['ip'])
        file.write('\n')
        file.write("Version: " + ip['version'])
        file.write('\n')
        file.write("City: " + ip['city'])
        file.write('\n')
        file.write("Region: " + ip['region'])
        file.write('\n')
        file.write("Region Code: " + ip['region_code'])
        file.write('\n')
        file.write("Country Code: " + ip['country_code'])
        file.write('\n')
        file.write("Country Code ISO3: " + ip['country_code_iso3'])
        file.write('\n')
        file.write("Country Name: " + ip['country_name'])
        file.write('\n')
        file.write("Country Capital: " + ip['country_capital'])
        file.write('\n')
        file.write("Country TLD: " + ip['country_tld'])
        file.write('\n')
        file.write("Continent Code: " + ip['continent_code'])
        file.write('\n')
        file.write("Is in EU: " + str(ip['in_eu']))
        file.write('\n')
        file.write("Postal Code: " + ip['postal'])
        file.write('\n')
        file.write("Latitude: " + str(ip['latitude']))
        file.write('\n')
        file.write("Longitude: " + str(ip['longitude']))
        file.write('\n')
        file.write("Timezone: " + ip['timezone'])
        file.write('\n')
        file.write("UTC Offset: " + ip['utc_offset'])
        file.write('\n')
        file.write("Country Calling Code: " + ip['country_calling_code'])
        file.write('\n')
        file.write("Currency: " + ip['currency'])
        file.write('\n')
        file.write("Currency Name: " + ip['currency_name'])
        file.write('\n')
        file.write("Langauges used in country: " + ip['languages'])
        file.write('\n')
        file.write("Country area: " + str(ip['country_area']))
        file.write('\n')
        file.write("Country population: " + str(ip['country_population']))
        file.write('\n')
        file.write("ASN: " + ip['asn'])
        file.write('\n')
        file.write("Organisation: " + ip['org'])
print("Made with <3 by VoidableMethod")
