# OVERVIEW

This function will get data via the CO-OPS data API and return a Python Dictionary containing the downloaded data and metadata. More information about CO-OPS API for data retrieval can be found at https://tidesandcurrents.noaa.gov/api/.

CO-OPS' data API call is limited to 31 days of 6-minute data so this function will send multiple successive requests for monthly time series data and then compile them all into a single output structure.
PLEASE BE AWARE that sending too many API data requests at once can overload CO-OPS' data servers. To account for this, the time.sleep() function is implemented to pause for 3 seconds between successive API requests. Users should also ensure that this function is implemented between API requests when augmenting this code for their own use.

# CoopsAPI
