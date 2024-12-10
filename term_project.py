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
        "15. Update a student information",
        "16. Update a club information",
        "17. Update a club manager information",
        "18. Update a group-study information",
        "19. Delete a student information",
        "20. Delete a club information",
        "21. Delete a club manger information",
        "22. Delete a group-study information"
    ]

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

if __name__ == "__main__":
    main()