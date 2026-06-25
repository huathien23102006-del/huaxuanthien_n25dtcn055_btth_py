from library import Library

library = Library()

while True:
    print("""
========== LIBRARY MANAGEMENT ==========
1. Add Book
2. View Books
3. Search Book
4. Delete Book
5. Add Student
6. View Students
7. Search Student
8. Delete Student
9. Borrow Book
10. Return Book
0. Exit
========================================
""")
    choice=input("Chọn: ")

    if choice=="1":
        library.add_book()
    elif choice=="2":
        library.view_books()
    elif choice=="3":
        library.search_book()
    elif choice=="4":
        library.delete_book()
    elif choice=="5":
        library.add_student()
    elif choice=="6":
        library.view_students()
    elif choice=="7":
        library.search_student()
    elif choice=="8":
        library.delete_student()
    elif choice=="9":
        library.borrow_book()
    elif choice=="10":
        library.return_book()
    elif choice=="0":
        print("Bye")
        break
    else:
        print("Lựa chọn sai")