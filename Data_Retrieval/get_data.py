# 
# FILENAME: get_data.py
# CREATED:  2020/05/18
#
# PURPOSE: 
# Sample program to retrieve water level observations for a 
# given station using the the Center for Operational Oceanographic
# Products and Services (CO-OPS) APIs, including the Data API. More 
# information about CO-OPS API for data retrieval can be found at 
# https://tidesandcurrents.noaa.gov/api/.
# 
# CO-OPS' data API call is limited to 31 days of 6-minute data so this function
# will send multiple successive requests for monthly time series data and then
# compile them all into a single output structure.
#
# PLEASE BE AWARE that sending too many API data requests at once can overload
# CO-OPS' data servers. To account for this, the time.sleep() function is implemented 
# to pause for 3 seconds between successive API requests. Users should also ensure
# that this function is implemented between API requests when augmenting this code
# for their own use.
#
# LICENSE
# Software code created by U.S. Government employees is not subject to 
# copyright in the United States (17 U.S.C.?105). The United States/
# Department of Commerce reserve all rights to seek and obtain copyright 
# protection in countries other than the United States for Software authored
# in its entirety by the Department of Commerce. To this end, the Department
# of Commerce hereby grants to Recipient a royalty-free, nonexclusive 
# license to use,copy, and create derivative works of the Software outside 
# of the United States.
#
# REVISION HISTORY:
# 

import datetime

# Import the main CO-OPS API helper class
from CoopsApi import CoopsApi

# Data parameters
#station_id="9414290-INVALID"
station_id="9414290"
start_date=datetime.datetime(2020,4,1)
end_date=datetime.datetime(2020,4,30)


# Create a CoopsApi instance and query the API for data. Check for errors
coopsapi = CoopsApi()
[output, errors] = coopsapi.get_data(station_id,[start_date, end_date])
print("Errors: " + str(errors))


# Return keys of dictionary for specific product and request
print("Returned keys:" + str(output.keys()))


# Let's iterate through the timestamps and water level values
num_values=len(output['Date Time'])
i=0
while i<num_values:
    print(str(output['Date Time'][i]),output['Water Level'][i])
    i=i+1

