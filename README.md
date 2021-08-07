##INTRODUCTION
This project demonstrates a simple command line application that takes a json data  and outputs a list of parking spots that match the query.

###Requirements 
1. Python can be downloaded from (https://www.python.org/downloads/). Once installed check the version by running the command `python --version` and make sure it is greater than V3.8

###Running the project
The project is triggered by running a command in the format `python parkbot.py <file_path> <command> <token>` from the project folder. The arguments description is as follows.
1. `file_path` -  This is the location of the file that contains the data. Please refer to the sample data in **_data.json_**
2. `command` - The argument only allows *locate, find_price_hourly_lte, find_price_hourly_gt* commands
3. `token` - The token is the value that is used to filter the results  

Example :
1. Command - `python parkbot.py data.json find_price_hourly_gt 200` - result - `Sweetgreen, Sandwiches n More, Azusa Ramen`
2. Command - `python parkbot.py data.json locate AZ` - result - `Tempe Beach Park, Safeway, Azusa Ramen`
3. Command - `python parkbot.py data.json find_price_hourly_lte 200` - result - `Church of 8 Wheels, Tempe Beach Park, AirGarage HQ, Safeway, Walgreens, Goldilocks Pizza, The Salon, Archer Salon`
