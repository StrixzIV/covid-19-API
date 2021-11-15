import requests
import datetime as dt

country = 'th'

url = f'https://disease.sh/v3/covid-19/countries/{country}'

try:
    req = requests.get(url)

except requests.exceptions.ConnectionError:
    print('Error: Cannot connect to the internet')
    exit()

data = req.json()

dateData = dt.datetime.fromtimestamp(int(data['updated'] // 1000)).strftime('Last updated: %y-%m-%d at %H:%M:%S')
localTimeZone = dt.datetime.utcnow().astimezone().tzinfo

cases = data['cases']
todayCases = data['todayCases']
recovered = data['recovered']
todayRecovered = data['todayRecovered']
deaths = data['deaths']
todayDeaths = data['todayDeaths']

print(f'{dateData} {localTimeZone} UTC')
print(f'All cases: {cases} (+{todayCases})')
print(f'Recovered: {recovered} (+{todayRecovered})')
print(f'Deaths: {deaths} (+{todayDeaths})')