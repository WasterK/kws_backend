import psycopg2


class DatabaseAccess:
    def __init__(self, database_url: str) -> None:
        try:
            self.conn = psycopg2.connect(database_url)
            self.cur = self.conn.cursor()
            print("Connected to database")
        except psycopg2.Error as e:
            print(f"Database connection error : {e}")

    def create_table(self, table_name: str) -> None:
        try:
            create_table_query = f"""
                CREATE TABLE IF NOT EXISTS {table_name} (
                    id SERIAL PRIMARY KEY,
                    username VARCHAR(50) UNIQUE NOT NULL,
                    password VARCHAR(50) NOT NULL
                );
            """
            self.cur.execute(create_table_query)
            self.conn.commit()
            print(f"Table '{table_name}' created successfully.")
        except psycopg2.Error as e:
            print(f"Error creating table '{table_name}': {e}")

    def insert_user_details(self, username: str, password: str):
        try:
            query = "INSERT INTO users(username, password) VALUES(%s, %s)"
            data = (username, password)
            self.cur.execute(query, data)
            self.conn.commit()
            print(f"user {username} is addedd")
        except psycopg2.Error as e:
            print(f"Error inserting user '{username}': {e}")


    def user_validation(self, username: str, password: str) -> bool:
        try:
            query = "SELECT * FROM users WHERE username = %s AND password = %s"
            self.cur.execute(query, (username, password))
            user = self.cur.fetchone()
            if user:
                print("User validated successfully.")
                return True
            else:
                print("Invalid username or password.")
                return False
        except psycopg2.Error as e:
            print("Error validating user:", e)
            return False

    def get_all_users(self):
            try:
                query = "SELECT * FROM users"
                self.cur.execute(query)
                users = self.cur.fetchall()
                return users
            except psycopg2.Error as e:
                print(f"Error getting all users: {e}")
                return None
            
# databaseURL = "postgres://admin:kRz8psM99PcqnOGLHQaY4GU0UXPs2ldC@dpg-cmco2d6d3nmc73ddamdg-a.singapore-postgres.render.com/kalpwebservice"    
# db = DatabaseAccess(databaseURL)
# db.create_table("users")
# db.insert_user_details("Kiran", "Kiran@123")

