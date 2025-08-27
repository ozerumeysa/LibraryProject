import sqlite3

class Librarian:
    def __init__(self):
        self.conn = sqlite3.connect('../my_book.db')
        self.cursor = self.conn.cursor()

        self.cursor.execute('DROP TABLE IF EXISTS librarians')

        self.cursor.execute('''
            CREATE TABLE librarians (
                id INTEGER PRIMARY KEY,
                name TEXT,
                surname TEXT,
                age INTEGER,
                contact TEXT
            )
        ''')

        records = [
            (1, "Alice", "Smith", 35, "123-456-7890"),
            (2, "Bob", "Johnson", 40, "234-567-8901"),
            (3, "Carol", "Williams", 29, "345-678-9012"),
            (4, "David", "Brown", 50, "456-789-0123"),
            (5, "Eve", "Davis", 42, "567-890-1234")
        ]

        sql = '''
            INSERT INTO librarians VALUES (?, ?, ?, ?, ?)
        '''
        self.cursor.executemany(sql, records)
        self.conn.commit()

    def list_librarians(self):

        self.cursor.execute('SELECT * FROM librarians')
        rows = self.cursor.fetchall()

        print("---- List of Librarian ----")
        for record in rows:
            print(record)


if __name__ == "__main__":
    librarian_manager = Librarian()
    librarian_manager.list_librarians()
