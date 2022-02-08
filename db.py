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
            query = "SELECT title, DATE_FORMAT(edate,'%M %d, %Y') AS formatted_date, description, hostid FROM events WHERE eventid=%s;"
            self.cursor.execute(query, (event_id,))
            event = self.cursor.fetchone()
            host = self.get_user(event[3])
            participants = self.get_partipants(event_id)
            return {"eventid": event_id, "name": event[0], "date": event[1], "description": event[2], "host": host, "participants": participants}
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

    def add_user(self, user):
        try:
            query = "INSERT INTO users (email,password,name) VALUES (%s,%s,%s);"
            self.cursor.execute(
                query, (user["email"], user["password"], user["name"]))
            self.conn.commit()
        except mariadb.Error as e:
            print(f"Error: {e}")

    def add_event(self, event):
        try:
            query = "INSERT INTO events (title,edate,description,hostid) VALUES (%s,%s,%s,%d);"
            self.cursor.execute(
                query, (event["name"], event["date"], event["description"], event["hostId"]))
            event_id = self.cursor.lastrowid
            for participant_id in event["participantIds"]:
                self.add_participant(participant_id, event_id)
            self.conn.commit()
        except mariadb.Error as e:
            print(f"Error: {e}")

    def add_participant(self, user_id, event_id):
        try:
            query = "INSERT INTO participants (eventid,userid) VALUES (%d,%d);"
            self.cursor.execute(query, (event_id, user_id))
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

    def close(self):
        self.conn.close()