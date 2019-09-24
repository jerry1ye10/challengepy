import sqlite3
DB_FILE= "foo.db"

def create_user_table(cur):
    ''' This function creates Users table in database with column names id, favoriteClubs, emails, username, and password.'''
    command = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, username TEXT NOT NULL UNIQUE, email TEXT NOT NULL UNIQUE, password TEXT NOT NULL, favoriteClubs TEXT)" #build SQL stmt, save as string
    cur.execute(command) #run SQL statement

def create_Clubs_table(cur):
    ''' This function creates Clubs table in database with column names id, name, and description, tags, and favoritedUsers .'''
    command = "CREATE TABLE IF NOT EXISTS clubs (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, description TEXT NOT NULL, tags TEXT, favoritedusers TEXT)" #build SQL stmt, save as string
    cur.execute(command) #run SQL statement

def create_Events_table(cur):
    ''' This function creates Events table in database with column names id, name, description, userids, location, and time.'''
    command = "CREATE TABLE IF NOT EXISTS events (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, description TEXT NOT NULL, user TEXT, location TEXT, time TEXT)" #build SQL stmt, save as string
    cur.execute(command) #run SQL statement

def create_database():
    ''' This function connect to the database and calls all the functions that create the tables in the database.'''
    DB_FILE= "foo.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor() #facilitate db ops
    create_user_table(c)
    create_Clubs_table(c)
    create_Events_table(c)
    db.close() #close database

def add_user(name,username, email, password):
    '''Takes in the username and password and adds
    it into the database table "users".'''
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "INSERT INTO users (name, username, email, password)VALUES(?,?,?,?);"
    c.execute(command,(name,username, email,password))
    db.commit()
    db.close()

#This function creates Clubs table in database with column names id, name, and description, tags, and favoritedUsers
def add_club(name, description, tags):
    '''Takes in the username and password and adds
    it into the database table "users".'''
    tagString = ""
    for tag in tags:
        tagString += tag
        tagString += ','
    if len(tagString) != 0:
        tagString = tagString[:-1] #removes the last comma in the string
    if isinstance(tags, str): #Considers case when tags parameter passed in is simply a string
        tagString = tags
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "INSERT INTO clubs (name,description, tags)VALUES(?,?,?);"
    c.execute(command,(name,description,tagString))
    db.commit()
    db.close()

def get_user_data():
    '''Returns the list of all user data.'''
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "SELECT * FROM users;"
    c.execute(command)
    output = c.fetchall()
    db.close()
    user_list = []
    for user in output:
        u = []
        for data in user:
            u.append(data)
        user_list.append(u)
    return user_list

def get_club_data():
    '''Returns the list of all club data.'''
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "SELECT * FROM clubs;"
    c.execute(command)
    output = c.fetchall()
    db.close()
    club_list = []
    for club in output:
        c = []
        for data in club:
            c.append(data)
        club_list.append(c)
    return club_list

def favorite(club_name, username):
    '''modifies the database to note that a user has favorited a club'''
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    clubs = get_club_data()
    users = get_user_data()
    club_favorited_users = ''
    user_favorited_clubs = ''
    for club in clubs:
        if club[1] == club_name:
            club_favorited_users = club[4]
            if club_favorited_users is None:
                club_favorited_users = username
                command = "UPDATE clubs SET favoritedusers = ? WHERE name = ?"
                print(command)
                print(1)
                print(club_favorited_users)
                c.execute(command, (club_favorited_users, club_name))
                break
            u = club_favorited_users.split(',')
            if username in u:
                return "Club has already been favorited"
            if len(club_favorited_users) > 0:
                club_favorited_users = club_favorited_users + ',' + username
                club_favorited_users += username
            else:
                club_favorited_users += username
            command = "UPDATE clubs SET favoritedusers = ? WHERE name = ?"
            print(command)
            print(club_favorited_users)
            c.execute(command, (club_favorited_users, club_name))
            break

    for user in users:
        if user[2] == username:
            print(1000)
            if user[5] is None:
                user_favorited_clubs = club_name
            elif len(user[5]) > 0:
                user_favorited_clubs = user[5] + ',' + club_name
            else:
                user_favorited_clubs = club_name
            command2 = "UPDATE users SET favoriteClubs = ? WHERE username = ?"
            print(command2)
            print(user_favorited_clubs)
            c.execute(command2, (user_favorited_clubs,username))
            break
    db.commit()
    db.close()
    return "Club has been favorited!"

def update_club(club_name, description, tags):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    tagString = ""
    for tag in tags:
        tagString += tag
        tagString += ','
    if len(tagString) != 0:
        tagString = tagString[:-1] #removes the last comma in the string
    if isinstance(tags, str): #Considers case when tags parameter passed in is simply a string
        tagString = tags
    command = "UPDATE clubs SET description = ? WHERE name = ?"
    command2 = "UPDATE clubs SET tags = ? WHERE name = ?"
    c.execute(command, (description, club_name))
    c.execute(command2, (tags, club_name))
    db.commit()
    db.close()

def add_event(username, event_name, event_description, location, time):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "INSERT INTO events (name,description, user, location, time )VALUES(?,?,?,?,?);"
    c.execute(command, (event_name, event_description, username, location, time))
    db.commit()
    db.close()

def find_events(username):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "SELECT * FROM events WHERE user = ?;"
    c.execute(command, (username,))
    output = c.fetchall()
    db.commit()
    db.close()
    event_list = []
    for event in output:
        e = []
        for data in event:
            e.append(data)
        event_list.append(e)
    print(event_list)
    return event_list


#testing
#create_database()
#add_user('jerry','jerry1ye10','je', 'das')
#favorite("pennlabs", 'jerry1ye10')
#get_user_data()
