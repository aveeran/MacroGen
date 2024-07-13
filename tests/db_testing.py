import unittest
import sys 
import os
# Append the parent directory of the current script to the sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from db_connection import DatabaseConnection  # Importing DatabaseConnection from db_connection.py

# class TestDatabaseConnection(unittest.TestCase):
#     def test_singleton_instance(self):
#         conn1 = DatabaseConnection.get_connection()
#         conn2 = DatabaseConnection.get_connection()
        
#         self.assertIs(conn1, conn2, "Instances should be the same")
#         DatabaseConnection.close_connection()

#     def test_close_connection(self):
#         DatabaseConnection.get_connection()
#         DatabaseConnection.close_connection()
#         conn = DatabaseConnection.get_connection()
        
#         self.assertIsNotNone(conn, "Connection should be reopened after close")

# if __name__ == '__main__':
#     unittest.main()
class TestDatabaseConnection(unittest.TestCase):

    def setUp(self):
        # Ensure a fresh start
        DatabaseConnection.close_connection()
        if os.path.exists('macros.db'):
            os.remove('macros.db')
        self.db = DatabaseConnection()
        self.db.execute_query("CREATE TABLE IF NOT EXISTS test_table (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")

    def tearDown(self):
        DatabaseConnection.close_connection()
        if os.path.exists('macros.db'):
            os.remove('macros.db')

    def test_create_table(self):
        query = "CREATE TABLE IF NOT EXISTS another_table (id INTEGER PRIMARY KEY, value TEXT)"
        cursor = self.db.execute_query(query)
        self.assertIsNotNone(cursor)
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='another_table'")
        result = cursor.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result[0], 'another_table')

    def test_insert_data(self):
        query = "INSERT INTO test_table (name, age) VALUES (?, ?)"
        params = ("Alice", 30)
        cursor = self.db.execute_query(query, params)
        self.assertIsNotNone(cursor)

        cursor.execute("SELECT * FROM test_table WHERE name=? AND age=?", params)
        result = cursor.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result[1], "Alice")
        self.assertEqual(result[2], 30)

    def test_select_data(self):
        self.db.execute_query("INSERT INTO test_table (name, age) VALUES ('Alice', 30)")
        query = "SELECT * FROM test_table"
        cursor = self.db.execute_query(query)
        self.assertIsNotNone(cursor)
        result = cursor.fetchall()
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][1], 'Alice')
        self.assertEqual(result[0][2], 30)

    def test_update_data(self):
        self.db.execute_query("INSERT INTO test_table (name, age) VALUES ('Alice', 30)")
        query = "UPDATE test_table SET age = ? WHERE name = ?"
        params = (31, 'Alice')
        cursor = self.db.execute_query(query, params)
        self.assertIsNotNone(cursor)

        cursor.execute("SELECT age FROM test_table WHERE name = ?", ('Alice',))
        result = cursor.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result[0], 31)

    def test_delete_data(self):
        self.db.execute_query("INSERT INTO test_table (name, age) VALUES ('Alice', 30)")
        query = "DELETE FROM test_table WHERE name = ?"
        params = ('Alice',)
        cursor = self.db.execute_query(query, params)
        self.assertIsNotNone(cursor)

        cursor.execute("SELECT * FROM test_table WHERE name = ?", ('Alice',))
        result = cursor.fetchone()
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()