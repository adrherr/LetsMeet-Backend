import mariadb, json, sys

class maria:
    def __init__(self):
        # Connect to MariaDB
        config = json.load(open('private.json'))
        try:
            self.conn = mariadb.connect(
                user = config['user'],
                password = config['password'],
                host = 'localhost',
                port = int(config['port']),
                database = 'meet'
            )
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB: {e}")
            sys.exit(1)

        # Get Cursor
        self.cursor = self.conn.cursor()
    
    def get_allusers(self):
        try:
            query = "SELECT name, email FROM users;"
            self.cursor.execute(query)
            users = self.cursor.fetchall()
            return users
        except mariadb.Error as e:
            print(f"Error: {e}")

    def get_user(self, userid):
        try:
            query = "SELECT name, email FROM users WHERE userid=%s;"
            self.cursor.execute(query, (userid,))
            user = self.cursor.fetchone()
            return {"name":user[0],"email":user[1]}
        except mariadb.Error as e:
            print(f"Error: {e}")

    def get_allevents(self):
        try:
            query = "SELECT title, DATE_FORMAT(edate,'%M %d, %Y') AS formatted_date, description, hostid FROM events;"
            self.cursor.execute(query)
            events = self.cursor.fetchall()
            return events
        except mariadb.Error as e:
            print(f"Error: {e}")
    
    def get_event(self, eventid):
        try:
            query = "SELECT title, DATE_FORMAT(edate,'%M %d, %Y') AS formatted_date, description, hostid FROM events WHERE eventid=%s;"
            self.cursor.execute(query, (eventid,))
            event = self.cursor.fetchone()
            host = self.get_user(event[3])["name"]
            # Get participants
            query = "SELECT userid FROM participants WHERE eventid=%s;"
            self.cursor.execute(query, (eventid,))
            participants = self.cursor.fetchall()
            participants = [self.get_user(userid[0]) for userid in participants]
            return {"name":event[0],"date":event[1],"description":event[2],"host":host,"participants":participants}
        except mariadb.Error as e:
            print(f"Error: {e}")

    def close(self):
        self.conn.close()