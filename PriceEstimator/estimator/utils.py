import pickle
import pandas as pd
from sklearn.linear_model import LinearRegression
from .models import CityCode

# Load machine learning model
realtorModel = pickle.load(open('Data/realtor-model.pkl', 'rb'))

# Create house from json data
def createHouse(houseData):
  cityCode = list(CityCode.objects.filter(city=houseData['city']).values('id'))[0]['id']
  
  house = pd.DataFrame({'bed':[float(houseData['beds'])],
                         'bath':[float(houseData['baths'])],
                         'acre_lot':[float(houseData['lot'])],
                         'city': [cityCode],
                         'house_size':[float(houseData['sqft'])],
                         'Alabama':'Alabama' == houseData['state'],
                         'Alaska':'Alaska' == houseData['state'],
                         'Arizona':'Arizona' == houseData['state'],
                         'Arkansas':'Arkansas' == houseData['state'],
                         'California':'California' == houseData['state'],
                         'Colorado':'Colorado' == houseData['state'],
                         'Connecticut':'Connecticut' == houseData['state'],
                         'Delaware':'Delaware' == houseData['state'],
                         'District of Columbia':'District of Columbia' == houseData['state'],
                         'Florida':'Florida' == houseData['state'],
                         'Georgia':'Georgia' == houseData['state'],
                         'Hawaii':'Hawaii' == houseData['state'],
                         'Idaho':'Idaho' == houseData['state'],
                         'Illinois':'Illinois' == houseData['state'],
                         'Indiana':'Indiana' == houseData['state'],
                         'Iowa':'Iowa' == houseData['state'],
                         'Kansas':'Kansas' == houseData['state'],
                         'Kentucky':'Kentucky' == houseData['state'],
                         'Louisiana':'Louisiana' == houseData['state'],
                         'Maine':'Maine' == houseData['state'],
                         'Maryland':'Maryland' == houseData['state'],
                         'Massachusetts':'Massachusetts' == houseData['state'],
                         'Michigan':'Michigan' == houseData['state'],
                         'Minnesota':'Minnesota' == houseData['state'],
                         'Mississippi':'Mississippi' == houseData['state'],
                         'Missouri':'Missouri' == houseData['state'],
                         'Montana':'Montana' == houseData['state'],
                         'Nebraska':'Nebraska' == houseData['state'],
                         'Nevada':'Nevada' == houseData['state'],
                         'New Hampshire':'New Hampshire' == houseData['state'],
                         'New Jersey':'New Jersey' == houseData['state'],
                         'New Mexico':'New Mexico' == houseData['state'],
                         'New York':'New York' == houseData['state'],
                         'North Carolina':'North Carolina' == houseData['state'],
                         'North Dakota': 'North Dakota' == houseData['state'],
                         'Ohio':'Ohio' == houseData['state'],
                         'Oklahoma':'Oklahoma' == houseData['state'],
                         'Oregon':'Oregon' == houseData['state'],
                         'Pennsylvania':'Pennsylvania' == houseData['state'],
                         'Puerto Rico':'Puerto Rico' == houseData['state'],
                         'Rhode Island':'Rhode Island' == houseData['state'],
                         'South Carolina':'South Carolina' == houseData['state'],
                         'South Dakota':'South Dakota' == houseData['state'],
                         'Tennessee':'Tennessee' == houseData['state'],
                         'Texas':'Texas' == houseData['state'],
                         'Utah':'Utah' == houseData['state'],
                         'Vermont':'Vermont' == houseData['state'],
                         'Virgin Islands':'Virgin Islands' == houseData['state'],
                         'Virginia':'Virginia' == houseData['state'],
                         'Washington':'Washington' == houseData['state'],
                         'West Virginia':'West Virginia' == houseData['state'],
                         'Wisconsin':'Wisconsin' == houseData['state'],
                         'Wyoming':'Wyoming' == houseData['state']})
  return house

# Make predition on house
def estateEstimation(house):
  prediction = realtorModel.predict(house)

  offset = prediction * 0.29
  
  if offset > 100000:
    offset = prediction * 0.1
  
  lowerBound = prediction - offset
  upperBound = prediction + offset

  lowerBound = "${:,}".format(round(lowerBound[0]))
  prediction = "${:,}".format(round(prediction[0]))
  upperBound = "${:,}".format(round(upperBound[0]))

  estimation = [lowerBound, prediction, upperBound]

  return estimation