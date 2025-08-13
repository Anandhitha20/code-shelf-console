#!/usr/bin/env python3
"""
Code Shelf: A Smart Library Organizer
A comprehensive Library Management System using various data structures
"""

import hashlib
from typing import Optional, List, Dict
from datetime import datetime
import os
import sys

class Book:
    """Represents a book in the library"""
    
    def __init__(self, book_id: str, title: str, author: str, year: int):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.is_borrowed = False
        self.borrowed_by = None
        self.borrow_date = None
        
    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"ID: {self.book_id} | Title: {self.title} | Author: {self.author} | Year: {self.year} | Status: {status}"

class Node:
    """Node for linked list implementation"""
    
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """Linked list implementation for book collection"""
    
    def __init__(self):
        self.head = None
        self.size = 0
    
    def add_book(self, book: Book) -> None:
        """Add a book to the linked list"""
        new_node = Node(book)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1
    
    def remove_book(self, book_id: str) -> bool:
        """Remove a book by ID"""
        if not self.head:
            return False
        
        if self.head.data.book_id == book_id:
            self.head = self.head.next
            self.size -= 1
            return True
        
        current = self.head
        while current.next:
            if current.next.data.book_id == book_id:
                current.next = current.next.next
                self.size -= 1
                return True
            current = current.next
        return False
    
    def search_by_title(self, title: str) -> List[Book]:
        """Search books by title"""
        results = []
        current = self.head
        while current:
            if title.lower() in current.data.title.lower():
                results.append(current.data)
            current = current.next
        return results
    
    def search_by_id(self, book_id: str) -> Optional[Book]:
        """Search book by ID"""
        current = self.head
        while current:
            if current.data.book_id == book_id:
                return current.data
            current = current.next
        return None
    
    def get_all_books(self) -> List[Book]:
        """Get all books in the list"""
        books = []
        current = self.head
        while current:
            books.append(current.data)
            current = current.next
        return books
    
    def sort_by_title(self) -> None:
        """Sort books by title"""
        if not self.head or not self.head.next:
            return
        
        # Convert to list, sort, and rebuild
        books = self.get_all_books()
        books.sort(key=lambda x: x.title.lower())
        
        # Rebuild linked list
        self.head = None
        self.size = 0
        for book in books:
            self.add_book(book)
    
    def sort_by_author(self) -> None:
        """Sort books by author"""
        if not self.head or not self.head.next:
            return
        
        # Convert to list, sort, and rebuild
        books = self.get_all_books()
        books.sort(key=lambda x: x.author.lower())
        
        # Rebuild linked list
        self.head = None
        self.size = 0
        for book in books:
            self.add_book(book)

class Stack:
    """Stack implementation for borrowing history"""
    
    def __init__(self):
        self.items = []
    
    def push(self, item):
        """Push item to stack"""
        self.items.append(item)
    
    def pop(self):
        """Pop item from stack"""
        if not self.is_empty():
            return self.items.pop()
        return None
    
    def peek(self):
        """Peek at top item"""
        if not self.is_empty():
            return self.items[-1]
        return None
    
    def is_empty(self):
        """Check if stack is empty"""
        return len(self.items) == 0
    
    def size(self):
        """Get stack size"""
        return len(self.items)
    
    def get_all_items(self):
        """Get all items in stack"""
        return self.items.copy()

class Queue:
    """Queue implementation for waitlist"""
    
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        """Add item to queue"""
        self.items.append(item)
    
    def dequeue(self):
        """Remove item from queue"""
        if not self.is_empty():
            return self.items.pop(0)
        return None
    
    def peek(self):
        """Peek at front item"""
        if not self.is_empty():
            return self.items[0]
        return None
    
    def is_empty(self):
        """Check if queue is empty"""
        return len(self.items) == 0
    
    def size(self):
        """Get queue size"""
        return len(self.items)
    
    def get_all_items(self):
        """Get all items in queue"""
        return self.items.copy()

class HashTable:
    """Hash table implementation for quick book lookups"""
    
    def __init__(self, size=100):
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def _hash(self, key):
        """Generate hash for key"""
        return hash(key) % self.size
    
    def insert(self, key, value):
        """Insert key-value pair"""
        hash_key = self._hash(key)
        for item in self.table[hash_key]:
            if item[0] == key:
                item[1] = value
                return
        self.table[hash_key].append([key, value])
    
    def get(self, key):
        """Get value by key"""
        hash_key = self._hash(key)
        for item in self.table[hash_key]:
            if item[0] == key:
                return item[1]
        return None
    
    def delete(self, key):
        """Delete key-value pair"""
        hash_key = self._hash(key)
        for i, item in enumerate(self.table[hash_key]):
            if item[0] == key:
                del self.table[hash_key][i]
                return True
        return False

class BorrowRecord:
    """Record for book borrowing"""
    
    def __init__(self, book: Book, borrower: str, borrow_date: datetime):
        self.book = book
        self.borrower = borrower
        self.borrow_date = borrow_date
        self.return_date = None
    
    def __str__(self):
        return f"{self.book.title} borrowed by {self.borrower} on {self.borrow_date.strftime('%Y-%m-%d %H:%M')}"

class WaitlistEntry:
    """Entry for book waitlist"""
    
    def __init__(self, book_id: str, user_name: str, request_date: datetime):
        self.book_id = book_id
        self.user_name = user_name
        self.request_date = request_date
    
    def __str__(self):
        return f"{self.user_name} waiting for book ID {self.book_id} since {self.request_date.strftime('%Y-%m-%d %H:%M')}"

class CodeShelfLibrary:
    """Main library management system"""
    
    def __init__(self):
        self.books = LinkedList()
        self.borrow_history = Stack()
        self.waitlist = Queue()
        self.book_hash_table = HashTable()
        self.borrowed_books = {}  # book_id -> BorrowRecord
    
    def add_book(self, book_id: str, title: str, author: str, year: int) -> bool:
        """Add a new book to the library"""
        if self.books.search_by_id(book_id):
            return False
        
        book = Book(book_id, title, author, year)
        self.books.add_book(book)
        self.book_hash_table.insert(book_id, book)
        return True
    
    def remove_book(self, book_id: str) -> bool:
        """Remove a book from the library"""
        book = self.books.search_by_id(book_id)
        if not book:
            return False
        
        if book.is_borrowed:
            return False  # Cannot remove borrowed book
        
        self.books.remove_book(book_id)
        self.book_hash_table.delete(book_id)
        return True
    
    def search_by_title(self, title: str) -> List[Book]:
        """Search books by title"""
        return self.books.search_by_title(title)
    
    def search_by_id(self, book_id: str) -> Optional[Book]:
        """Search book by ID using hash table"""
        return self.book_hash_table.get(book_id)
    
    def borrow_book(self, book_id: str, borrower: str) -> bool:
        """Borrow a book"""
        book = self.search_by_id(book_id)
        if not book:
            return False
        
        if book.is_borrowed:
            # Add to waitlist
            waitlist_entry = WaitlistEntry(book_id, borrower, datetime.now())
            self.waitlist.enqueue(waitlist_entry)
            return False
        
        book.is_borrowed = True
        book.borrowed_by = borrower
        book.borrow_date = datetime.now()
        
        # Create borrow record
        record = BorrowRecord(book, borrower, datetime.now())
        self.borrow_history.push(record)
        self.borrowed_books[book_id] = record
        
        return True
    
    def return_book(self, book_id: str) -> bool:
        """Return a borrowed book"""
        book = self.search_by_id(book_id)
        if not book or not book.is_borrowed:
            return False
        
        book.is_borrowed = False
        book.borrowed_by = None
        book.borrow_date = None
        
        # Update borrow record
        if book_id in self.borrowed_books:
            self.borrowed_books[book_id].return_date = datetime.now()
            del self.borrowed_books[book_id]
        
        # Check waitlist
        if not self.waitlist.is_empty():
            # Find next person waiting for this book
            temp_queue = Queue()
            found_waiting = None
            
            while not self.waitlist.is_empty():
                entry = self.waitlist.dequeue()
                if entry.book_id == book_id and not found_waiting:
                    found_waiting = entry
                else:
                    temp_queue.enqueue(entry)
            
            # Restore queue
            while not temp_queue.is_empty():
                self.waitlist.enqueue(temp_queue.dequeue())
            
            if found_waiting:
                print(f"Book {book.title} is now available for {found_waiting.user_name}")
        
        return True
    
    def display_all_books(self, sort_by: str = "title") -> None:
        """Display all books with optional sorting"""
        if sort_by.lower() == "title":
            self.books.sort_by_title()
        elif sort_by.lower() == "author":
            self.books.sort_by_author()
        
        books = self.books.get_all_books()
        if not books:
            print("No books in the library.")
            return
        
        print(f"\n{'='*80}")
        print(f"LIBRARY COLLECTION (Sorted by {sort_by.title()})")
        print(f"{'='*80}")
        print(f"{'ID':<10} {'Title':<25} {'Author':<20} {'Year':<6} {'Status':<12}")
        print(f"{'-'*80}")
        
        for book in books:
            status = "Borrowed" if book.is_borrowed else "Available"
            print(f"{book.book_id:<10} {book.title:<25} {book.author:<20} {book.year:<6} {status:<12}")
        
        print(f"{'='*80}")
        print(f"Total books: {len(books)}")
    
    def display_borrow_history(self) -> None:
        """Display borrowing history"""
        records = self.borrow_history.get_all_items()
        if not records:
            print("No borrowing history.")
            return
        
        print(f"\n{'='*80}")
        print("BORROWING HISTORY (Most Recent First)")
        print(f"{'='*80}")
        
        for i, record in enumerate(reversed(records), 1):
            return_info = f"Returned: {record.return_date.strftime('%Y-%m-%d %H:%M')}" if record.return_date else "Not returned"
            print(f"{i}. {record.book.title} - {record.borrower}")
            print(f"   Borrowed: {record.borrow_date.strftime('%Y-%m-%d %H:%M')} | {return_info}")
            print()
    
    def display_waitlist(self) -> None:
        """Display current waitlist"""
        entries = self.waitlist.get_all_items()
        if not entries:
            print("No books in waitlist.")
            return
        
        print(f"\n{'='*80}")
        print("CURRENT WAITLIST")
        print(f"{'='*80}")
        
        for i, entry in enumerate(entries, 1):
            book = self.search_by_id(entry.book_id)
            book_title = book.title if book else "Unknown Book"
            print(f"{i}. {entry.user_name} waiting for '{book_title}' (ID: {entry.book_id})")
            print(f"   Requested: {entry.request_date.strftime('%Y-%m-%d %H:%M')}")
            print()

def clear_screen():
    """Clear the console screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    """Display the main menu"""
    print("\n" + "="*60)
    print("           CODE SHELF - SMART LIBRARY ORGANIZER")
    print("="*60)
    print("1. Add a new book")
    print("2. Remove a book")
    print("3. Search books by title")
    print("4. Search book by ID")
    print("5. Display all books")
    print("6. Borrow a book")
    print("7. Return a book")
    print("8. View borrowing history")
    print("9. View waitlist")
    print("10. Exit")
    print("="*60)

def main():
    """Main function to run the library system"""
    library = CodeShelfLibrary()
    
    # Add some sample books
    sample_books = [
        ("B001", "The Great Gatsby", "F. Scott Fitzgerald", 1925),
        ("B002", "To Kill a Mockingbird", "Harper Lee", 1960),
        ("B003", "1984", "George Orwell", 1949),
        ("B004", "Pride and Prejudice", "Jane Austen", 1813),
        ("B005", "The Hobbit", "J.R.R. Tolkien", 1937),
        ("B006", "The Catcher in the Rye", "J.D. Salinger", 1951),
        ("B007", "Lord of the Flies", "William Golding", 1954),
        ("B008", "Animal Farm", "George Orwell", 1945),
        ("B009", "Brave New World", "Aldous Huxley", 1932),
        ("B010", "The Alchemist", "Paulo Coelho", 1988)
    ]
    
    for book_id, title, author, year in sample_books:
        library.add_book(book_id, title, author, year)
    
    print("Welcome to Code Shelf - Smart Library Organizer!")
    print("Sample books have been added to get you started.")
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-10): ").strip()
        
        if choice == "1":
            clear_screen()
            print("\n=== ADD NEW BOOK ===")
            book_id = input("Enter book ID: ").strip()
            title = input("Enter book title: ").strip()
            author = input("Enter author name: ").strip()
            try:
                year = int(input("Enter publication year: ").strip())
                if library.add_book(book_id, title, author, year):
                    print(f"\n✓ Book '{title}' added successfully!")
                else:
                    print(f"\n✗ Book with ID '{book_id}' already exists!")
            except ValueError:
                print("\n✗ Invalid year format!")
        
        elif choice == "2":
            clear_screen()
            print("\n=== REMOVE BOOK ===")
            book_id = input("Enter book ID to remove: ").strip()
            if library.remove_book(book_id):
                print(f"\n✓ Book with ID '{book_id}' removed successfully!")
            else:
                print(f"\n✗ Book with ID '{book_id}' not found or is currently borrowed!")
        
        elif choice == "3":
            clear_screen()
            print("\n=== SEARCH BY TITLE ===")
            title = input("Enter title to search: ").strip()
            results = library.search_by_title(title)
            if results:
                print(f"\nFound {len(results)} book(s):")
                for i, book in enumerate(results, 1):
                    print(f"{i}. {book}")
            else:
                print("\nNo books found with that title.")
        
        elif choice == "4":
            clear_screen()
            print("\n=== SEARCH BY ID ===")
            book_id = input("Enter book ID: ").strip()
            book = library.search_by_id(book_id)
            if book:
                print(f"\nFound book: {book}")
            else:
                print(f"\nNo book found with ID '{book_id}'")
        
        elif choice == "5":
            clear_screen()
            print("\n=== DISPLAY ALL BOOKS ===")
            sort_choice = input("Sort by (title/author) [default: title]: ").strip().lower()
            if sort_choice not in ["title", "author"]:
                sort_choice = "title"
            library.display_all_books(sort_choice)
        
        elif choice == "6":
            clear_screen()
            print("\n=== BORROW BOOK ===")
            book_id = input("Enter book ID: ").strip()
            borrower = input("Enter borrower name: ").strip()
            if library.borrow_book(book_id, borrower):
                book = library.search_by_id(book_id)
                print(f"\n✓ Book '{book.title}' borrowed successfully by {borrower}!")
            else:
                book = library.search_by_id(book_id)
                if book and book.is_borrowed:
                    print(f"\n✗ Book '{book.title}' is already borrowed. Added to waitlist.")
                else:
                    print(f"\n✗ Book with ID '{book_id}' not found!")
        
        elif choice == "7":
            clear_screen()
            print("\n=== RETURN BOOK ===")
            book_id = input("Enter book ID to return: ").strip()
            if library.return_book(book_id):
                book = library.search_by_id(book_id)
                print(f"\n✓ Book '{book.title}' returned successfully!")
            else:
                print(f"\n✗ Book with ID '{book_id}' not found or not borrowed!")
        
        elif choice == "8":
            clear_screen()
            print("\n=== BORROWING HISTORY ===")
            library.display_borrow_history()
        
        elif choice == "9":
            clear_screen()
            print("\n=== WAITLIST ===")
            library.display_waitlist()
        
        elif choice == "10":
            clear_screen()
            print("\nThank you for using Code Shelf - Smart Library Organizer!")
            print("Goodbye!")
            break
        
        else:
            print("\n✗ Invalid choice! Please enter a number between 1-10.")
        
        input("\nPress Enter to continue...")
        clear_screen()

if __name__ == "__main__":
    main()
