import sqlite3

ADMIN_USER="hackbright"
ADMIN_PASSWORD=5980025637247534551

DB = None
CONN = None

def connect_to_db():
    global DB, CONN
    CONN = sqlite3.connect("thewall.db")
    DB = CONN.cursor()

def getContent_user_by_name(username):
    query = """SELECT users.id, wall_posts.content  
    FROM users
    JOIN wall_posts ON (users.id = wall_posts.owner_id)
    WHERE username == (?)"""
    DB.execute(query, (username, ))
    row = DB.fetchall()
    print row


def authenticate(username, password):
    connect_to_db()
    query = """ SELECT id, password FROM users where username = (?)"""
    DB.execute(query, (username, ))
    row = DB.fetchone()
    if int(row[1]) == password:
        return row[0]
    else:
        return None
  # row = get_user_by_name("test")
    #get_user_by_name

#    if username == ADMIN_USER and hash(password) == ADMIN_PASSWORD:
#        return ADMIN_USER
#    else:
#        return None


#authenticate("test", "test123") 

