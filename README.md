# Code Shelf: A Smart Library Organizer

A comprehensive Library Management System that demonstrates practical applications of fundamental data structures in a real-world context.

## 🎯 Project Overview

Code Shelf is a console-based Library Management System that efficiently maintains records of books in a library. The system simulates basic functionalities of a real-world library using various data structures to manage book collections and track operations.

## 🏗️ Data Structures Implemented

### 1. **Linked List** - Book Collection Management
- **Purpose**: Maintains the dynamic list of books in the library
- **Operations**: Add, remove, search, and sort books
- **Features**: 
  - Add new books to the collection
  - Remove books by unique ID
  - Search books by title (partial matching)
  - Sort books by title or author name

### 2. **Stack** - Borrowing History
- **Purpose**: Maintains borrowing history in Last-In-First-Out (LIFO) manner
- **Operations**: Push (add borrow record), Pop (remove record), Peek
- **Features**:
  - Track all book borrowing activities
  - Efficient return management
  - Complete borrowing history with timestamps

### 3. **Queue** - Waitlist Management
- **Purpose**: Manages waiting list for borrowed books in First-In-First-Out (FIFO) order
- **Operations**: Enqueue (add to waitlist), Dequeue (remove from waitlist)
- **Features**:
  - Automatic waitlist management when books are borrowed
  - Fair queuing system for book requests
  - Notification when books become available

### 4. **Hash Table** - Quick Book Lookups
- **Purpose**: Optimizes search operations based on book IDs
- **Operations**: Insert, Get, Delete
- **Features**:
  - O(1) average time complexity for book ID searches
  - Efficient book retrieval and management
  - Collision handling with chaining

## 🚀 Features

### Core Library Operations
- ✅ **Add Books**: Add new books with title, author, year, and unique ID
- ✅ **Remove Books**: Delete books by ID (only if not borrowed)
- ✅ **Search Books**: Search by title (partial matching) or ID
- ✅ **Display Collection**: View all books with sorting options

### Borrowing System
- ✅ **Borrow Books**: Check out books with borrower tracking
- ✅ **Return Books**: Return borrowed books with automatic waitlist processing
- ✅ **Borrowing History**: Complete history of all borrowing activities
- ✅ **Waitlist Management**: Automatic queue management for unavailable books

### Advanced Features
- ✅ **Sorting**: Display books sorted by title or author
- ✅ **Status Tracking**: Real-time book availability status
- ✅ **Timestamp Tracking**: All operations include date/time stamps
- ✅ **Error Handling**: Comprehensive input validation and error messages

## 📋 Requirements

- Python 3.6 or higher
- No external dependencies required (uses only standard library)

## 🛠️ Installation & Usage

### 1. Clone or Download
```bash
# If using git
git clone <repository-url>
cd code-shelf-console

# Or simply download the files
```

### 2. Run the Application
```bash
python main.py
```

### 3. Navigate the Menu
The system provides an intuitive console menu with 10 options:

1. **Add a new book** - Add books to the library
2. **Remove a book** - Remove books by ID
3. **Search books by title** - Find books by title
4. **Search book by ID** - Quick lookup by book ID
5. **Display all books** - View collection with sorting
6. **Borrow a book** - Check out books
7. **Return a book** - Return borrowed books
8. **View borrowing history** - See all borrowing records
9. **View waitlist** - Check current waitlist
10. **Exit** - Close the application

## 📚 Sample Data

The system comes pre-loaded with 10 classic books to demonstrate functionality:

- The Great Gatsby (F. Scott Fitzgerald, 1925)
- To Kill a Mockingbird (Harper Lee, 1960)
- 1984 (George Orwell, 1949)
- Pride and Prejudice (Jane Austen, 1813)
- The Hobbit (J.R.R. Tolkien, 1937)
- The Catcher in the Rye (J.D. Salinger, 1951)
- Lord of the Flies (William Golding, 1954)
- Animal Farm (George Orwell, 1945)
- Brave New World (Aldous Huxley, 1932)
- The Alchemist (Paulo Coelho, 1988)

## 🔧 Technical Implementation

### Class Structure
- **`Book`**: Represents individual books with metadata
- **`Node`**: Linked list node implementation
- **`LinkedList`**: Book collection management
- **`Stack`**: Borrowing history management
- **`Queue`**: Waitlist management
- **`HashTable`**: Fast book ID lookups
- **`BorrowRecord`**: Borrowing transaction records
- **`WaitlistEntry`**: Waitlist queue entries
- **`CodeShelfLibrary`**: Main system orchestrator

### Key Algorithms
- **Linked List Operations**: O(n) for search, O(1) for add/remove
- **Hash Table Lookups**: O(1) average case
- **Stack Operations**: O(1) for push/pop
- **Queue Operations**: O(1) for enqueue/dequeue
- **Sorting**: O(n log n) using Python's built-in sort

## 🎓 Educational Value

This project demonstrates:
- **Data Structure Integration**: How different data structures work together
- **Real-world Applications**: Practical use of theoretical concepts
- **System Design**: Modular, maintainable code architecture
- **User Interface Design**: Intuitive console-based interaction
- **Error Handling**: Robust input validation and error management

## 🔍 Example Usage Scenarios

### Scenario 1: Adding and Borrowing Books
1. Add a new book with ID "B011"
2. Search for the book by ID to verify
3. Borrow the book for a user
4. Check borrowing history
5. Return the book

### Scenario 2: Waitlist Management
1. Borrow a book that's already borrowed
2. Check the waitlist
3. Return the book
4. Verify automatic waitlist processing

### Scenario 3: Search and Display
1. Search books by partial title
2. Display all books sorted by author
3. Search by book ID using hash table optimization

## 🐛 Troubleshooting

### Common Issues
- **Invalid Input**: The system validates all inputs and provides clear error messages
- **Book Not Found**: Check if the book ID exists in the library
- **Cannot Remove**: Books cannot be removed while borrowed

### Performance Notes
- Hash table provides O(1) average lookup time for book IDs
- Linked list operations are O(n) but suitable for typical library sizes
- Stack and queue operations are O(1) for all operations

## 📈 Future Enhancements

Potential improvements for the system:
- **File Persistence**: Save/load library data from files
- **User Management**: Multiple user accounts and permissions
- **Advanced Search**: Search by author, year, or multiple criteria
- **Statistics**: Generate reports and analytics
- **GUI Interface**: Graphical user interface using tkinter or web interface
- **Database Integration**: Use SQLite or other database systems

## 📄 License

This project is created for educational purposes to demonstrate data structure implementations in Python.

## 👨‍💻 Author

Created as a comprehensive Library Management System demonstrating practical applications of data structures.

---

**Happy Coding! 📚✨**
