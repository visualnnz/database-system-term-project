import mysql.connector

# MySQL 연결
def connect_to_database():
    return mysql.connector.connect(
        host="192.168.40.3",
        user="nnz",
        password="blackberry00",
        database="madang",
        port=4567
    )

# 데이터 삽입
def insert_data(connection, bookid, bookname, publisher, price):
    cursor = connection.cursor()
    query = "INSERT INTO Book VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (bookid, bookname, publisher, price))
    connection.commit()
    print(f"Data inserted: {bookid}, {bookname}, {publisher}, {price}")

# 데이터 삭제
def delete_data(connection, bookid):
    cursor = connection.cursor()
    query = "DELETE FROM Book WHERE bookid = %s"
    cursor.execute(query, (bookid,))
    connection.commit()
    print(f"Data deleted: ID {bookid}")

# 데이터 검색
def search_data(connection):
    cursor = connection.cursor()
    query = "SELECT * FROM Book"
    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        print(row)

# 메인 함수
def main():
    try:
        connection = connect_to_database()
        print("Connected to the database.")
        
        # 사용자 작업 선택
        while True:
            print("\nChoose an action:")
            print("1. Insert Data")
            print("2. Delete Data")
            print("3. Search Data")
            print("4. Exit")
            
            choice = input("Enter your choice: ")
            if choice == "1":
                bookid = input("bookid: ")
                bookname = input("bookname: ")
                publisher = input("publisher: ")
                price = int(input("price: "))
                insert_data(connection, bookid, bookname, publisher, price)
            elif choice == "2":
                bookid = int(input("Enter bookid to delete: "))
                delete_data(connection, bookid)
            elif choice == "3":
                search_data(connection)
            elif choice == "4":
                break
            else:
                print("Invalid choice. Please try again.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if connection:
            connection.close()
            print("Connection closed.")

if __name__ == "__main__":
    main()
