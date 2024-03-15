import pandas as pd
import pycountry
from country_converter import CountryConverter
    
def get_alpha3(country_name):
    '''
    returns the ISO alpha 3 code for given country name
    '''
    try:
        country = pycountry.countries.get(name=country_name)
        return country.alpha_3
    except AttributeError:
        return None


# Happiness Report Data 2023
file_path = 'data/WHR/DataForTable2.1WHR2023.xls'

happiness = pd.read_excel(file_path)

happiness['Country Code'] = happiness['Country name'].apply(get_alpha3) #assigns country code to each country
happiness = happiness.sort_values('year', ascending=True) #sorts df by year in ascending order


#These countries don't exactly match the country name in pycountry dataset so need to be manually assigned
countries = ['Iran', 'Turkiye', 'Venezuela', 'Vietnam', 'Moldova', 'State of Palestine',
 'Russia', 'South Korea', 'Bolivia', 'Hong Kong S.A.R. of China', 'Laos',
 'Tanzania', 'Taiwan Province of China', 'Kosovo', 'Congo (Brazzaville)',
 'Syria', 'Congo (Kinshasa)', 'Somaliland region', 'Ivory Coast']
codes = ['IRN', 'TUR', 'VEN', 'VNM', 'MDA', 'PSE', 
         'RUS', 'KOR', 'BOL', 'HKG', 'LAO', 
         'TZA', 'TWN', 'XKK', 'COG', 
         'SYR', 'COD', 'SOM', 'CIV']
for country, code in zip(countries, codes):
    #assigns country its corresponding country code
    happiness.loc[happiness['Country name'] == country, 'Country Code'] = code

cc = CountryConverter()

# add continents of each country using country code with country converter library
happiness['Continent'] = happiness['Country Code'].apply(lambda x: cc.convert(names=x, to='continent_7', not_found=None))
happiness.loc[happiness['Country name'] == 'Kosovo', 'Continent'] = 'Europe'

# add regions of each country using country code with country converter library
happiness['Region'] = happiness['Country Code'].apply(lambda x: cc.convert(names=x, to='IMAGE', not_found=None))
happiness.loc[happiness['Country name'] == 'State of Palestine', 'Region'] = 'Middle East'
happiness.loc[happiness['Country name'] == 'Cuba', 'Region'] = 'Central America'
happiness.loc[happiness['Country name'] == 'South Sudan', 'Region'] = 'Eastern Africa'
happiness.loc[happiness['Country name'] == 'Kosovo', 'Region'] = 'Central Europe'

# saves cleaned up dataframe as a csv
happiness.to_csv('data/WHR/cleanData/clean2023HappinessData.csv', index=False)