import sqlite3
import datetime

ADMIN_USER="hackbright"
ADMIN_PASSWORD=5980025637247534551

DB = None
CONN = None

def connect_to_db():
    global DB, CONN
    CONN = sqlite3.connect("thewall.db")
    DB = CONN.cursor()

def get_username_by_userid(user_id):
    connect_to_db()
    query = """SELECT username FROM users WHERE id = ?"""
    DB.execute(query, (user_id, ))
    row = DB.fetchone()
    return row[0]

def get_userid_by_name(username):
    connect_to_db()
    query = """SELECT id FROM users WHERE username = ?"""
    DB.execute(query, (username, ))
    row = DB.fetchone()
    return row[0]


def get_username_by_author_id(author_id):
    connect_to_db()
    query = """SELECT users.username FROM 
    users JOIN wall_posts ON (users.id = wall_posts.author_id)
    WHERE author_id = ? """
    DB.execute(query, (author_id, ))
    row = DB.fetchone()
    return row[0]



# get_all_posts(username):
def get_all_posts(username):
    connect_to_db()
    query = """SELECT users.username, wall_posts.content, wall_posts.created_at,wall_posts.author_id  
    FROM users
    JOIN wall_posts ON (users.id = wall_posts.owner_id)
    WHERE username == (?)"""
    DB.execute(query, (username, ))
    rows = DB.fetchall()
    for i in range(len(rows)):
        rows[i] = rows[i] + (get_username_by_author_id(rows[i][3]), )

    return rows

def submit_post(owner_id,author_id,wall_post):
    connect_to_db()
    now = datetime.datetime.utcnow()
    print "TIMESTAMP", now
    query = """INSERT INTO wall_posts values (null, ?, ?, ?, ?)"""
    DB.execute(query, (owner_id, author_id, now, wall_post))
    CONN.commit()
   
def create_account(username,password):
    connect_to_db()
    query = """INSERT INTO users values (null, ?, ?)"""
    DB.execute(query, (username, hash(password)))
    CONN.commit()

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



