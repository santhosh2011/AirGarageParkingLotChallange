##INTRODUCTION
This project demonstrates a simple command line application that takes a json data  and outputs a list of parking spots that match the query.

###Requirements 
1. Python can be downloaded from (https://www.python.org/downloads/). Once installed check the version by running the command `python --version` and make sure it is greater than V3.8

###Running the project
The project is triggered by running a command in the format `python parkbot.py <file_path> <command> <token>` from the project folder. The arguments description is as follows.
1. `file_path` -  This is the location of the file that contains the data. Please refer to the sample data in **_data.json_**
2. `command` - The argument only allows *locate, find_price_hourly_lte, find_price_hourly_gt* commands
   - `locate`: This command will return a list of spot names by location (state only). Example: locate AZ will return spots in Arizona 
   - `find_price_hourly_lte`. This command will return a list of spot names where the hourly price is less than or equal to the query price. (Note: the price is in cents). Example: find_price_hourly_lte 200 should return spots that are less than or equal to $2 per hour. 
   - `find_price_hourly_gt`. This command will return a list of spot names where the price is greater than the query price. (Note: the price is in cents). Example: find_price_hourly_gt 200 will return spots that are greater than $2.00 per hour.
3. `token` - The token is the value that is used to filter the results  

Example :
1. Command - `python parkbot.py data.json find_price_hourly_gt 200` - result - `Sweetgreen, Sandwiches n More, Azusa Ramen`
2. Command - `python parkbot.py data.json locate AZ` - result - `Tempe Beach Park, Safeway, Azusa Ramen`
3. Command - `python parkbot.py data.json find_price_hourly_lte 200` - result - `Church of 8 Wheels, Tempe Beach Park, AirGarage HQ, Safeway, Walgreens, Goldilocks Pizza, The Salon, Archer Salon`
