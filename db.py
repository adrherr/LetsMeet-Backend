from random import randint
import mariadb
import json
import sys

class maria:
    def __init__(self):
        # Connect to MariaDB
        config = json.load(open('private.json'))
        try:
            self.conn = mariadb.connect(
                user=config['user'],
                password=config['password'],
                host='localhost',
                port=int(config['port']),
                database='meet'
            )
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB: {e}")
            sys.exit(1)

        # Get Cursor
        self.cursor = self.conn.cursor()

    def get_all_users(self):
        try:
            query = "SELECT userid, name, email FROM users;"
            self.cursor.execute(query)
            users = self.cursor.fetchall()
            jsonUsers = []
            for userid, name, email in users:
                jsonUsers.append(
                    {"userid": userid, "name": name, "email": email})
            return jsonUsers
        except mariadb.Error as e:
            print(f"Error: {e}")

    def get_user(self, user_id):
        try:
            query = "SELECT name, email FROM users WHERE userid=%s;"
            self.cursor.execute(query, (user_id,))
            user = self.cursor.fetchone()
            return {"userid": user_id, "name": user[0], "email": user[1]}
        except mariadb.Error as e:
            print(f"Error: {e}")

    def get_user_name(self, user_id):
        try:
            query = "SELECT name FROM users WHERE userid=%s;"
            self.cursor.execute(query, (user_id,))
            return self.cursor.fetchone()[0]
        except mariadb.Error as e:
            print(f"Error: {e}")

    def get_partipants(self, event_id):
        try:
            query = "SELECT userid FROM participants WHERE eventid=%s;"
            self.cursor.execute(query, (event_id,))
            participants = self.cursor.fetchall()
            participants = [self.get_user(userid[0]) for userid in participants]
            return participants
        except mariadb.Error as e:
            print(f"Error: {e}")

    def get_all_events(self):
        try:
            query = "SELECT eventid, title, DATE_FORMAT(edate,'%M %d, %Y') AS formatted_date, description, hostid FROM events;"
            self.cursor.execute(query)
            events = self.cursor.fetchall()
            jsonEvents = []
            for eventid, title, edate, description, hostid in events:
                host = self.get_user(hostid)
                participants = self.get_partipants(eventid)
                jsonEvents.append({"eventid": eventid, "name": title, "date": edate,
                                  "description": description, "host": host, "participants": participants})
            return jsonEvents
        except mariadb.Error as e:
            print(f"Error: {e}")

    def get_event(self, event_id):
        try:
            query = "SELECT title, DATE_FORMAT(edate,'%M %d, %Y') AS formatted_date, description, location, hostid FROM events WHERE eventid=%s;"
            self.cursor.execute(query, (event_id,))
            event = self.cursor.fetchone()
            host = self.get_user(event[4])
            participants = self.get_partipants(event_id)
            return {"eventid": event_id, "name": event[0], "date": event[1], "description": event[2], 
                    "location": event[3], "host": host, "participants": participants}
        except mariadb.Error as e:
            print(f"Error: {e}")

    def get_user_events(self, user_id):
        try:
            query = "SELECT eventid FROM participants WHERE userid=%s;"
            self.cursor.execute(query, (user_id,))
            events = self.cursor.fetchall()
            return [self.get_event(eventid[0]) for eventid in events]
        except mariadb.Error as e:
            print(f"Error: {e}")

    def get_recent_message(self, convo_id):
        try:
            query = "SELECT text FROM messages WHERE pid IN (SELECT MAX(pid) FROM messages where convoid=%s);"
            self.cursor.execute(query, (convo_id,))
            message = self.cursor.fetchone()
            if message == None:
                return None
            else:
                return message[0]
        except mariadb.Error as e:
            print(f"Error: {e}")

    def get_conversations(self, user_id):
        try:
            query = "SELECT convoid FROM conversations WHERE userid=%s;"
            self.cursor.execute(query, (user_id,))
            convos = [convoid[0] for convoid in self.cursor.fetchall()]
            jsonConvos = []
            for convo in convos:
                message = self.get_recent_message(convo)
                if message == None: continue
                query = "SELECT userid FROM conversations WHERE convoid=%s AND userid<>%s;"
                self.cursor.execute(query, (convo, user_id))
                userid = self.cursor.fetchone()[0]
                name = self.get_user_name(userid)
                jsonConvos.append({"convoid": convo, "user": name, "userid": userid, "message": message})
            return jsonConvos
        except mariadb.Error as e:
            print(f"Error: {e}")

    def get_convo(self, user_id, other_user_id):
        try:
            query = "SELECT A.convoid FROM conversations A, conversations B WHERE A.userid=%d AND B.userid=%d AND A.convoid=B.convoid;"
            self.cursor.execute(query, (user_id, other_user_id))
            convoid = self.cursor.fetchone()
            if convoid == None:
                convo_id = randint(1,1000000000)
                query = "INSERT INTO conversations VALUES (%d,%d), (%d,%d);"
                self.cursor.execute(query, (convo_id, user_id, convo_id, other_user_id))
                self.conn.commit()
                return convoid
            else:
                return convoid[0]
        except mariadb.Error as e:
            print(f"Error: {e}")

    def get_messages(self, convo_id):
        try:
            query = "SELECT pid, text, createdat, userid FROM messages WHERE convoid=%s;"
            self.cursor.execute(query, (convo_id,))
            messages = reversed(self.cursor.fetchall())
            jsonMessages = []
            for pid, text, createdat, userid in messages:
                name = self.get_user_name(userid)
                jsonMessages.append({"_id": pid, "text":text, "createdAt": createdat, 
                                    "user": {"_id": userid, "name": name, "avatar": 'https://placeimg.com/140/140/any'}})
            return jsonMessages
        except mariadb.Error as e:
            print(f"Error: {e}")
    
    def get_profile(self, user_id):
        try:
            query = "SELECT name,bio FROM users WHERE userid=%d;"
            self.cursor.execute(query, (user_id,))
            userData = self.cursor.fetchone()
            query = "SELECT tag FROM tags WHERE userid=%d;"
            self.cursor.execute(query, (user_id,))
            tags = [tag[0] for tag in self.cursor.fetchall()]
            return {"name": userData[0], "bio": userData[1], "tags": tags}
        except mariadb.Error as e:
            print(f"Error: {e}")

    def add_user(self, user):
        try:
            query = "SELECT email FROM users WHERE email=%s;"
            self.cursor.execute(query, (user["email"],))
            email = self.cursor.fetchone()
            if email != None:
                return -1
            query = "INSERT INTO users (email,password,name) VALUES (%s,%s,%s);"
            self.cursor.execute(
                query, (user["email"], user["password"], user["name"]))
            self.conn.commit()
            query = "SELECT userid FROM users WHERE email=%s;"
            self.cursor.execute(query, (user["email"],))
            userid = self.cursor.fetchone()
            return userid[0]
        except mariadb.Error as e:
            print(f"Error: {e}")

    def add_event(self, event):
        try:
            query = "INSERT INTO events (title,edate,description,location,hostid) VALUES (%s,%s,%s,%s,%d);"
            values = (event["name"], event["date"], event["description"], event["location"], event["hostId"])
            self.cursor.execute(query, values)
            event_id = self.cursor.lastrowid
            for participant_id in event["participantIds"]:
                self.add_participant(event_id, participant_id)
            self.conn.commit()
        except mariadb.Error as e:
            print(f"Error: {e}")

    def add_participant(self, event_id, user_id):
        try:
            query = "INSERT INTO participants (eventid,userid) VALUES (%d,%d);"
            self.cursor.execute(query, (event_id, user_id))
            self.conn.commit()
        except mariadb.Error as e:
            print(f"Error: {e}")

    def add_message(self, convo_id, text, created_at, user_id):
        try:
            query = "INSERT INTO messages (convoid,text,createdat,userid) VALUES (%s,%s,%s,%s);"
            self.cursor.execute(query, (convo_id, text, created_at, user_id))
            self.conn.commit()
        except mariadb.Error as e:
            print(f"Error: {e}")

    def save_profile(self, user_id, name, bio, tags):
        try:
            query = "UPDATE users SET name=%s, bio=%s WHERE userid=%d;"
            self.cursor.execute(query, (name, bio, user_id))
            query = "DELETE FROM tags WHERE userid=%d;"
            self.cursor.execute(query, (user_id,))
            for tag in tags:
                query = "INSERT IGNORE INTO tags VALUES(%d,%s);"
                self.cursor.execute(query, (user_id, tag))
                self.conn.commit()
        except mariadb.Error as e:
            print(f"Error: {e}")

    def login(self, creds):
        try:
            query = "SELECT userid FROM users WHERE email=%s AND password=%s HAVING COUNT(userid)=1;"
            self.cursor.execute(query, (creds["email"], creds["password"]))
            userid = self.cursor.fetchone()
            if userid == None:
                return -1
            return userid[0]
        except mariadb.Error as e:
            print(f"Error: {e}")
    
    def remove_event(self, event_id):
        try:
            query = "DELETE FROM participants WHERE eventid=%d;"
            self.cursor.execute(query, (event_id,))
            self.conn.commit()
            query = "DELETE FROM events WHERE eventid=%d;"
            self.cursor.execute(query, (event_id,))
            self.conn.commit()
        except mariadb.Error as e:
            print(f"Error: {e}")

    def leave_event(self, event_id, user_id):
        try:
            query = "DELETE FROM participants WHERE eventid=%d AND userid=%d;"
            self.cursor.execute(query, (event_id, user_id))
            self.conn.commit()
        except mariadb.Error as e:
            print(f"Error: {e}")

    def close(self):
        self.conn.close()