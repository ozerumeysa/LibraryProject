import sqlite3

class Book:
    def __init__(self):
        self.conn = sqlite3.connect('../my_book.db')
        self.cursor = self.conn.cursor()

        sql = '''
            CREATE TABLE IF NOT EXISTS books(
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                page INTEGER NOT NULL
            )
        '''

        records = [
            (1, "The Hobbit", "J.R.R. Tolkien", 310),
            (2, "1984", "George Orwell", 328),
            (3, "To Kill a Mockingbird", "Harper Lee", 281),
            (4, "Pride and Prejudice", "Jane Austen", 279),
            (5, "The Catcher in the Rye", "J.D. Salinger", 214)
        ]

        sql = '''
                    INSERT INTO books VALUES (?, ?, ?, ?)
                '''
        #self.cursor.executemany(sql, records)
        self.conn.commit()


    def create_book(self):
        title = input("Enter title: ")
        author = input("Enter author: ")
        page = input("Enter number of pages: ")
        self.cursor.execute("INSERT INTO books (title, author, page) VALUES (?, ?, ?)", (title, author, page))
        self.conn.commit()
        print("Book created successfully\n")


    def delete_book(self):
        book_id = int(input("Enter book ID to delete: "))
        self.cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
        self.conn.commit()
        print("Book deleted successfully\n")

    def list_book(self):
        self.cursor.execute("SELECT * FROM books")
        books = self.cursor.fetchall()


        for book in books:
            print(book)

        #self.conn.close()
        return books

    def get_longest_book(self):
        self.cursor.execute("SELECT * FROM books ORDER BY page DESC LIMIT 1")
        longest = self.cursor.fetchone()
        if longest:
            print("Longest book:", longest)
        return longest


    def menu(self):
        while True:
            print("=== Book Manager ===")
            print("1. Create Book")
            print("2. Delete Book")
            print("3. List All Books")
            print("4. Longest Book")
            print("5. Exit")

            choice = int(input("Choose an option (1-5): "))

            if choice == 1 :
                self.create_book()
            elif choice == 2 :
                self.delete_book()
            elif choice == 3 :
                self.list_book()
            elif choice == 4 :
                self.get_longest_book()
            elif choice == 5 :
                break
            else:
                print("Invalid choice, please select a number between 1 and 4.")




if __name__ == "__main__":
    book_manager = Book()
    book_manager.menu()