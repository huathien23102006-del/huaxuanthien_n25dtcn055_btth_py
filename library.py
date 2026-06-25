from book import Book
from student import Student

class Library:
    def __init__(self):
        self.books = []
        self.students = []

    # BOOK
    def add_book(self):
        try:
            id = input("Mã sách: ")
            title = input("Tên sách: ")
            author = input("Tác giả: ")
            quantity = int(input("Số lượng: "))

            if quantity < 0:
                raise ValueError
            book = Book(
                id,
                title,
                author,
                quantity
            )
            self.books.append(book)
            print("Thêm sách thành công")
        except ValueError:
            print("Số lượng phải là số nguyên >= 0")

    def view_books(self):
        if len(self.books)==0:
            print("Chưa có sách")
        for book in self.books:
            book.show_info()

    def search_book(self):
        id = input("Nhập mã sách: ")

        for book in self.books:
            if book.id == id:
                print("Đã tìm thấy sách")
                book.show_info()
                return
        print("Book not found")

    def delete_book(self):
        id = input("Nhập mã sách cần xóa: ")

        for book in self.books:
            if book.id == id:
                self.books.remove(book)
                print("Xóa thành công")
                return
        print("Book not found")

    # STUDENT

    def add_student(self):
        id = input("Mã sinh viên: ")
        name = input("Họ tên: ")
        class_name = input("Lớp: ")

        student = Student(
            id,
            name,
            class_name
        )

        self.students.append(student)
        print("Thêm sinh viên thành công")

    def view_students(self):
        for s in self.students:
            s.show_info()

    def search_student(self):
        id=input("Nhập mã sinh viên: ")

        for s in self.students:
            if s.id == id:
                s.show_info()
                return
        print("Student not found")

    def delete_student(self):
        id=input("Nhập mã sinh viên: ")
        for s in self.students:
            if s.id == id:
                self.students.remove(s)
                print("Xóa thành công")
                return
        print("Student not found")
    # BORROW RETURN

    def borrow_book(self):
        book_id=input("Mã sách: ")

        for book in self.books:
            if book.id == book_id:
                if book.borrow():
                    print("Mượn sách thành công")
                else:
                    print("Sách hết")
                return

        print("Book not found")

    def return_book(self):
        book_id=input("Mã sách: ")

        for book in self.books:
            if book.id == book_id:
                book.return_book()
                print("Trả sách thành công")
                return
        print("Book not found")