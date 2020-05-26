# OVERVIEW

This function will get data via the CO-OPS data API and return a Python Dictionary containing the downloaded data and metadata. More information about CO-OPS API for data retrieval can be found at https://tidesandcurrents.noaa.gov/api/.

CO-OPS' data API call is limited to 31 days of 6-minute data so this function will send multiple successive requests for monthly time series data and then compile them all into a single output structure.
PLEASE BE AWARE that sending too many API data requests at once can overload CO-OPS' data servers. To account for this, the time.sleep() function is implemented to pause for 3 seconds between successive API requests. Users should also ensure that this function is implemented between API requests when augmenting this code for their own use.

## NOAA Open Source Disclaimer

This repository is a scientific product and is not official communication of the National Oceanic and Atmospheric Administration, or the United States Department of Commerce. All NOAA GitHub project code is provided on an ?as is? basis and the user assumes responsibility for its use. Any claims against the Department of Commerce or Department of Commerce bureaus stemming from the use of this GitHub project will be governed by all applicable Federal law. Any reference to specific commercial products, processes, or services by service mark, trademark, manufacturer, or otherwise, does not constitute or imply their endorsement, recommendation or favoring by the Department of Commerce. The Department of Commerce seal and logo, or the seal and logo of a DOC bureau, shall not be used in any manner to imply endorsement of any commercial product or activity by DOC or the United States Government.

## License

Software code created by U.S. Government employees is not subject to copyright in the United States (17 U.S.C. �105). The United States/Department of Commerce reserve all rights to seek and obtain copyright protection in countries other than the United States for Software authored in its entirety by the Department of Commerce. To this end, the Department of Commerce hereby grants to Recipient a royalty-free, nonexclusive license to use, copy, and create derivative works of the Software outside of the United States.

# CoopsAPI
Class of data retrieval functions for CO-OPS APIs

# get_data
Sample program to retrieve water level observations for a given station using the the Center for Operational Oceanographic Products and Services (CO-OPS) APIs, including the Data API.
