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

def get_user_by_name(username):
    connect_to_db()
    query = """SELECT id FROM users WHERE username = ?"""
    DB.execute(query, (username, ))
    row = DB.fetchone()
    print "THIS IS THE ROW", row[0]
    return row[0]

# get_all_posts(username):
def get_all_posts(username):
    connect_to_db()
    query = """SELECT users.username, wall_posts.content, wall_posts.created_at  
    FROM users
    JOIN wall_posts ON (users.id = wall_posts.owner_id)
    WHERE username == (?)"""
    DB.execute(query, (username, ))
    rows = DB.fetchall()
    return rows

def submit_post(owner_id,author_id,wall_post):
    connect_to_db()
    now = datetime.datetime.utcnow()
    print "TIMESTAMP", now
    query = """INSERT INTO wall_posts values (null, ?, ?, ?, ?)"""
    DB.execute(query, (owner_id, author_id, now, wall_post))
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


#authenticate("test", "test123") 

