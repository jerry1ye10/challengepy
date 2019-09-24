# Penn Labs Server Challenge
Remember to **document your work** in this `README.md` file! Feel free to delete these installation instructions in your fork of this repository.

## Installation
1. Fork + clone this repository. 
2. `cd` into the cloned repository.
3. Install `pipenv`
  * `brew install pipenv` if you're on a Mac.
  * `pip install --user --upgrade pipenv` for most other machines.
4. Install packages using `pipenv install`.

## Developing
1. Use `pipenv run index.py` to run the project.
2. Follow the instructions [here](https://www.notion.so/pennlabs/Server-Challenge-Fall-19-480abf1871fc4a8d9600154816726343).
3. Document your work in the `README.md` file.

## Submitting
Submit a link to your git repository to [this form](https://airtable.com/shrqdIzlLgiRFzEWh) by 11:59pm on Monday, September 23rd.

## Installing Additional Packages
To install additional packages run `pipenv install <package_name>` within the cloned repository.

## Database
Originally, I started off by creating two classes: a Club class and a User class. From here, I used a list to store instances of these classes as a psuedo-database. I switched this to a more formal database using sqlite3. Nothing needs to be installed to use sqlite3, because it automatically comes included with python. Inside my database, I had three seperate tables: a users table, a clubs table, and an events table. (Events is part of my additional feature which I will describe in detail further down in the readme). All of the code (helper functions used in index.py) that actually connects with the database is stored inside util/db_builder.py. 

## Additional Feature
For my additional feature, I chose to allow users to store a calendar of events that they have. This is especially helpful when the user needs to juggle the load between different club interest meetings, applications, and existing club commitments that the user has. Through the help of an additional sqlite table, I store the data of each seperate event inside this table. I also created two additional routes in implementing this feature: '/api/event' and '/api/event/<username>'.  '/api/event' takes in a POST with the mandatory parameters being all the data necessary to create an event and the actual username assigned to that event. '/api/event/<username>' displays all of the events tied to a specific user. In the making of the actual site, we can use some front-end with an api designed similarly to this to display a calendar of events that the user has. 

## Bonus Challenges 

