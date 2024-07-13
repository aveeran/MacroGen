import sqlite3

class DatabaseConnection:
    _instance = None 
    conn = None

    def __new__(cls):
        if cls._instance is None: 
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance.conn = sqlite3.connect('macros.db')

            # creating table, if necessary
            cursor = cls._instance.conn.cursor()
            create_table_query = '''
            CREATE TABLE IF NOT EXISTS macros (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            date TEXT NOT NULL,
            date_modified TEXT NOT NULL,
            macro TEXT NOT NULL
            )
            '''
            cursor.execute(create_table_query)
            cls._instance.conn.commit()
            cursor.close()

        return cls._instance 
     
    
    @classmethod
    def get_connection(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance.conn
    
    @classmethod
    def close_connection(cls):
        if cls._instance and cls._instance.conn:
            cls._instance.conn.close()
            cls._instance = None
            

    def execute_query(self, query, params=None):
        cursor = self.conn.cursor()
        
        try: 
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            self.conn.commit()
            return cursor 
        except sqlite3.Error as e:
            print(f"Error executing query: {e}")
            return None

    