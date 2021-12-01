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
            query = "SELECT email, name FROM users;"
            self.cursor.execute(query)
            users = self.cursor.fetchall()
            # users = [user[0] for user in users]
            return users
        except mariadb.Error as e:
            print(f"Error: {e}")

    def get_user(self, userid):
        try:
            query = "SELECT name, email FROM users WHERE id=%s;"
            self.cursor.execute(query, (userid,))
            print(users)
            users = self.cursor.fetchall()
            users = [user[0] for user in users]
            return users
        except mariadb.Error as e:
            print(f"Error: {e}")


    def close(self):
        self.conn.close()