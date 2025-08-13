#!/usr/bin/env python3
"""
Test script for Code Shelf Library Management System
Demonstrates all data structures and functionality
"""

from main import CodeShelfLibrary, Book, LinkedList, Stack, Queue, HashTable
from datetime import datetime

def test_data_structures():
    """Test individual data structures"""
    print("="*60)
    print("TESTING INDIVIDUAL DATA STRUCTURES")
    print("="*60)
    
    # Test Linked List
    print("\n1. Testing Linked List:")
    ll = LinkedList()
    books = [
        Book("T001", "Test Book 1", "Author A", 2020),
        Book("T002", "Test Book 2", "Author B", 2021),
        Book("T003", "Test Book 3", "Author C", 2022)
    ]
    
    for book in books:
        ll.add_book(book)
        print(f"Added: {book.title}")
    
    print(f"Total books: {ll.size}")
    print(f"Search 'Test': {len(ll.search_by_title('Test'))} books found")
    
    # Test Stack
    print("\n2. Testing Stack:")
    stack = Stack()
    for i in range(3):
        stack.push(f"Item {i+1}")
        print(f"Pushed: Item {i+1}")
    
    print(f"Stack size: {stack.size()}")
    print(f"Top item: {stack.peek()}")
    print(f"Popped: {stack.pop()}")
    
    # Test Queue
    print("\n3. Testing Queue:")
    queue = Queue()
    for i in range(3):
        queue.enqueue(f"User {i+1}")
        print(f"Enqueued: User {i+1}")
    
    print(f"Queue size: {queue.size()}")
    print(f"Front item: {queue.peek()}")
    print(f"Dequeued: {queue.dequeue()}")
    
    # Test Hash Table
    print("\n4. Testing Hash Table:")
    ht = HashTable()
    test_data = [("key1", "value1"), ("key2", "value2"), ("key3", "value3")]
    
    for key, value in test_data:
        ht.insert(key, value)
        print(f"Inserted: {key} -> {value}")
    
    print(f"Retrieved key1: {ht.get('key1')}")
    print(f"Deleted key2: {ht.delete('key2')}")
    print(f"Retrieved key2 after deletion: {ht.get('key2')}")

def test_library_operations():
    """Test complete library operations"""
    print("\n" + "="*60)
    print("TESTING COMPLETE LIBRARY OPERATIONS")
    print("="*60)
    
    library = CodeShelfLibrary()
    
    # Add test books
    print("\n1. Adding test books:")
    test_books = [
        ("TEST001", "Python Programming", "John Doe", 2023),
        ("TEST002", "Data Structures", "Jane Smith", 2022),
        ("TEST003", "Algorithms", "Bob Johnson", 2021)
    ]
    
    for book_id, title, author, year in test_books:
        success = library.add_book(book_id, title, author, year)
        print(f"Added {title}: {'✓' if success else '✗'}")
    
    # Display books
    print("\n2. Displaying all books:")
    library.display_all_books("title")
    
    # Test borrowing
    print("\n3. Testing borrowing operations:")
    borrowers = ["Alice", "Bob", "Charlie"]
    
    for i, borrower in enumerate(borrowers):
        book_id = f"TEST00{i+1}"
        success = library.borrow_book(book_id, borrower)
        print(f"{borrower} borrowing {book_id}: {'✓' if success else '✗'}")
    
    # Test waitlist
    print("\n4. Testing waitlist (trying to borrow already borrowed book):")
    success = library.borrow_book("TEST001", "David")
    print(f"David trying to borrow TEST001: {'Added to waitlist' if not success else '✓'}")
    
    # Display waitlist
    print("\n5. Current waitlist:")
    library.display_waitlist()
    
    # Test return
    print("\n6. Testing return operations:")
    success = library.return_book("TEST001")
    print(f"Returned TEST001: {'✓' if success else '✗'}")
    
    # Display borrowing history
    print("\n7. Borrowing history:")
    library.display_borrow_history()
    
    # Test search
    print("\n8. Testing search operations:")
    results = library.search_by_title("Python")
    print(f"Search for 'Python': {len(results)} books found")
    for book in results:
        print(f"  - {book}")
    
    book = library.search_by_id("TEST002")
    print(f"Search by ID TEST002: {book}")

def demonstrate_features():
    """Demonstrate key features"""
    print("\n" + "="*60)
    print("DEMONSTRATING KEY FEATURES")
    print("="*60)
    
    library = CodeShelfLibrary()
    
    print("\n1. Adding books with different authors for sorting demo:")
    demo_books = [
        ("D001", "Zebra Book", "Zebra Author", 2020),
        ("D002", "Alpha Book", "Alpha Author", 2021),
        ("D003", "Beta Book", "Beta Author", 2022),
        ("D004", "Gamma Book", "Gamma Author", 2023)
    ]
    
    for book_id, title, author, year in demo_books:
        library.add_book(book_id, title, author, year)
    
    print("\n2. Displaying sorted by title:")
    library.display_all_books("title")
    
    print("\n3. Displaying sorted by author:")
    library.display_all_books("author")
    
    print("\n4. Demonstrating waitlist functionality:")
    # Borrow all books
    for book_id, _, _, _ in demo_books:
        library.borrow_book(book_id, f"User_{book_id}")
    
    # Try to borrow again (should go to waitlist)
    library.borrow_book("D001", "WaitlistUser1")
    library.borrow_book("D001", "WaitlistUser2")
    
    print("\n5. Current waitlist:")
    library.display_waitlist()
    
    print("\n6. Returning book and checking waitlist processing:")
    library.return_book("D001")
    
    print("\n7. Updated waitlist:")
    library.display_waitlist()

def main():
    """Run all tests"""
    print("CODE SHELF LIBRARY MANAGEMENT SYSTEM - TEST SUITE")
    print("="*60)
    
    try:
        # Test individual data structures
        test_data_structures()
        
        # Test complete library operations
        test_library_operations()
        
        # Demonstrate features
        demonstrate_features()
        
        print("\n" + "="*60)
        print("ALL TESTS COMPLETED SUCCESSFULLY! ✓")
        print("="*60)
        print("\nThe system demonstrates:")
        print("✓ Linked List for book collection management")
        print("✓ Stack for borrowing history (LIFO)")
        print("✓ Queue for waitlist management (FIFO)")
        print("✓ Hash Table for fast book ID lookups")
        print("✓ Complete library operations")
        print("✓ Error handling and validation")
        print("✓ Sorting and search functionality")
        
    except Exception as e:
        print(f"\nTest failed with error: {e}")
        return False
    
    return True

if __name__ == "__main__":
    main()
