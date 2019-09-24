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
Originally, I started off by creating two classes: a Club class and a User class. From here, I used a list to store instances of these classes as a psuedo-database. I switched this to a more formal database using sqlite3. Nothing needs to be installed to use sqlite3, because it automatically comes included with python. Inside my database, I had three seperate tables: a users table, a clubs table, and an events table. (Events is part of my additional feature which I will describe in detail further down in the readme). All of the code (helper functions used in index.py) that actually connects with the database is stored inside util/db_builder.py. <br/> 

In my users table, I had these columns: id, name, username, email, password, favoritedClubs.<br/> 
In my clubs table, I had these columns: id, name, description, tags, favoritedUsers. <br/>
In my events table, I had these columns: id, name, description, user, location, time. 

## Additional Feature
For my additional feature, I chose to allow users to store a calendar of events that they have. This is especially helpful when the user needs to juggle the load between different club interest meetings, applications, and existing club commitments that the user has. Through the help of an additional sqlite table, I store the data of each seperate event inside this table. I also created two additional routes in implementing this feature: `/api/event` and `/api/event/<username>`.  `/api/event` takes in a POST with the mandatory parameters being all the data necessary to create an event and the actual username assigned to that event. `/api/event/<username>` displays all of the events tied to a specific user. In the making of the actual site, we can use some front-end with an api designed similarly to this to display a calendar of events that the user has. 

## Bonus Challenges 
1. I allowed the possibility to update existing clubs using the `api/clubs` route. I did this by adding an additional mandatory parameter into the POST request called 'update', which should either be True or False. From here, if update was true, I checked to see that the club that was trying to be updated already existed. If it did already exist, then the update would go through. If it didn't exist, it'd return "Invalid club name". <br/>
2. I stored all of my information in a sqlite3 database. I've talked about this more above. <br/>
3. I wrote a few basic tests in python just to ensure functionality on my site. I did this with the requests package in python. To run these tests, first run `pipenv install requests` inside the terminal. Then run `python3 request.py`. 

## Design Choices / Implementation Choices 
1. In the `/api/user/:username` route, I only returned the user's username, name, favoritedClubs, and email. A design choice to be made is whether users are okay to have their email displayed. I think if this product were launched to live, I'd allow users to customize whether their email is displayed publically. 
2. In the `/api/favorite`, I made sure to check if a club had already been favorited. If it did, then nothing would happen inside the database. 

## Future features
1. Implement a compact well-designed front-end for the api. <br/>
2. Do more error testing by adding more tests. <br/>
3. Implement sign in/sign out functionality using session. <br/>
4. Hash passwords and add improved basic security <br/>
5. Allow users to unfavorite a club. 
6. Allow users to update and delte events. 


