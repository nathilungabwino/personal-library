from book import Book
from note import Note

def create_book():
    title = input("Enter book title: ")
    return Book(title)

def add_note_to_book(book):
    title = input("Enter note title: ")
    text = input("Enter note text: ")
    note = Note(title, text)
    book.add_note(note)

def list_notes_in_book(book):
    for note in book.get_notes():
        print(f"Title: {note.title}, Text: {note.text}")

def main():
    books = {}

    while True:
        print("\n1. Create new book")
        print("2. Add note to a book")
        print("3. List notes in a book")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            book = create_book()
            books[book.title] = book
            print(f"Book '{book.title}' created.")
        elif choice == '2':
            book_title = input("Enter the title of the book: ")
            if book_title in books:
                add_note_to_book(books[book_title])
            else:
                print("Book not found!")
        elif choice == '3':
            book_title = input("Enter the title of the book: ")
            if book_title in books:
                list_notes_in_book(books[book_title])
            else:
                print("Book not found!")
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
