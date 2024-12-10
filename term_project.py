import getpass
import mysql.connector

# MySQL 연결
def connect_to_database(username, pw):
    return mysql.connector.connect(
        host="192.168.40.3",
        user=username,
        password=pw,
        database="term_project",
        port=4567
    )

# 메인 함수
def main():
    menu = [
        "[Menu]",
        "1. Log in",
        "2. Log out",
        "3. View all students",
        "4. View all clubs",
        "5. View all club managers",
        "6. View all group studys",
        "7. Find the students with filters",
        "8. Find the clubs with filters",
        "9. Find the club managers with filters",
        "10. Find the group-studys with filters",
        "11. Add a student",
        "12. Add a club",
        "13. Add a club manager",
        "14. Add a group-study",
        "15. Update a student",
        "16. Update a club",
        "17. Update a club manager",
        "18. Update a group-study",
        "19. Delete a student",
        "20. Delete a club",
        "21. Delete a club manger",
        "22. Delete a group-study"
    ]

    connected = False
    try:
        while True:
            i = 1
            print("\n===================================%s===================================" % (menu[0]))
            while i <= len(menu) - 1:
                if (len(menu) >= i + 2):
                    print("%-40s %-40s" % (menu[i], menu[i + 1]))
                else:
                    print("%-40s" % (menu[i]))
                i = i + 2
            print("============================================================================")
            choice = input("Enter your choice: ")

            if choice == "1":
                if (connected == False):
                    user = input("User: ")
                    pw = getpass.getpass("Password: ")
                    connection = connect_to_database(user, pw)
                    print("Connected to the database.")
                    connected = True
                else:
                    print("You already have been connected to database.")
            elif choice == "2":
                break
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if connection:
            connection.close()
            print("Connection closed.\n")
            connected = False

if __name__ == "__main__":
    main()