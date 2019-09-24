from flask import Flask, request
import json #Imports standard python json library to easily convert
from scraper import * # Web Scraping utility functions for Online Clubs with Penn.
from util import db_builder as db #Importing sqllite database functions from util folder
app = Flask(__name__)


''' //Previous classes used for data storage functionality before sqlite3 was implemented
class Club:
    def __init__(self, tags, description, name, favoritedUsers = []):
        self.name = name
        self.tags = tags
        self.description = description
        self.favoritedUsers = favoritedUsers
    def addUser(self, user):
        self.favoritedUsers.append(user)
        return True
class User:
    def __init__(self, username, name, email, password, favoriteClubs=[]):
        self.username = username
        self.name = name
        self.favoriteClubs = favoriteClubs
        self.email = email
        self.password = password

    def addClub(self, club):
        self.favoriteClubs.append(club)
        return True


user1 = User('jen','Jennifer Doe', 'jen@pennlabs.org', 'password')
users = []
users.append(user1)
clubsData = []
'''
db.create_database() #Creates the data base
def sourceClubData(): #Sources all of the club data into the list data structure
    html = get_clubs_html()
    soup = soupify(html)
    clubs = get_clubs(soup)
    for club in clubs:
        name = get_club_name(club)
        description = get_club_description(club)
        tags = get_club_tags(club)
        db.add_club(name,description,tags)

sourceClubData()
db.add_user('jen','Jennifer Doe', 'jen@pennlabs.org', 'password')
db.add_user('jerry','jerry1ye10','je', 'das')
#db.favorite("Arun Fan Club", 'jerry1ye10')
@app.route('/')
def main():
    return "Welcome to Penn Club Review!"

@app.route('/api')
def api():
    return "Welcome to the Penn Club Review API!."

#Ask in office hours if we can assume all parameters are met in the post request
@app.route('/api/clubs', methods=['POST','GET'])
def clubs():
    if (request.method == "GET"):
        returnList = []
        clubsData = db.get_club_data()
        for club in clubsData:
            dict = {}
            dict["name"] = club[1]
            dict["description"] = club[2]
            dict["tags"] = club[3]
            dict['favoritedUsers'] = club[4]
            returnList.append(dict)
        return json.dumps(returnList)
    elif (request.method == "POST"):
        args = request.form
        print(args['update'])
        clubsData = db.get_club_data()
        if args['update'] == "True":
            print(100)
            for club in clubsData:
                if club[1] == args['name']:
                    print(club[1])
                    db.update_club(args['name'],args['description'], args['tags'])
                    return "Club has updated"
            return "Invalid club name"
        db.add_club(args['name'], args['description'], args['tags'])

        return "Club has been added"



@app.route('/api/user/<username>', methods=['GET'] )
def user(username):
    users = db.get_user_data()
    for user in users:
        if user[2] == username:
            return json.dumps({'username': user[2],'name': user[1],'clubs': user[5],'email': user[3]})

#Ask about return statements in these functions
@app.route('/api/favorite', methods=['POST'])
def favor():
    #print(args)
    db.favorite(request.form['club_name'], request.form['username'])
    return "Club has been favorited"

@app.route('/api/event', methods=['POST'])
def event():
    args = request.form
    db.add_event(request.form['username'],request.form['event_name'], args['event_description'], args['location'], args['time'])
    return "Event created!"

@app.route('/api/event/<username>', methods=['GET'])
def user_event(username):
    events = db.find_events(username)
    returnList = []
    for event in events:
        d = {}
        d['name'] = event[1]
        d['description'] = event[2]
        d['user'] = event[3]
        d['location'] = event[4]
        d['time'] = event[5]
        returnList.append(d)
    return json.dumps(returnList)



if __name__ == '__main__':
    app.run()
