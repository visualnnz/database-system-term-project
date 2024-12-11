import getpass
import mysql.connector

# MySQL 연결
def connectToDatabase(username, pw):
    return mysql.connector.connect(
        host="192.168.40.3",
        user=username,
        password=pw,
        database="term_project",
        port=4567
    )

# 데이터 삽입
def insertData(connection, relation):
    cursor = connection.cursor()

    if relation == "STUDENT":
        query = "INSERT INTO STUDENT VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        print("-------------------------------------------")
        sin = input("Sin: ")
        phone = input("Phone: ")
        sname = input("SName: ")
        sex = input("sex: ")
        major = input("major: ")
        super_sin = input("Super_Sin: ")
        cin = input("Cin: ")
        signup_date = input("Signup_date: ")
        print("-------------------------------------------")
        cursor.execute(query, (sin, phone, sname, sex, major, super_sin, cin, signup_date))
        connection.commit()
        print(f"Data inserted: {sin}, {phone}, {sname}, {sex}, {major}, {super_sin}, {cin}, {signup_date}")
    elif relation == "CLUB":
        query = "INSERT INTO CLUB VALUES (%s, %s, %s)"
        print("-------------------------------------------")
        cin = input("Cin: ")
        cname = input("CName: ")
        location = input("Location: ")
        print("-------------------------------------------")
        cursor.execute(query, (cin, cname, location))
        connection.commit()
        print(f"Data inserted: {cin}, {cname}, {location}")
    elif relation == "CLUB_MANAGER":
        query = "INSERT INTO CLUB_MANAGER VALUES (%s, %s, %s, %s, %s, %s, %s)"
        print("-------------------------------------------")
        cin = input("Cin: ")
        president_sin = input("President_Sin: ")
        p_start_date = input("P_Start_date: ")
        vicepresident_sin = input("VicePresident_Sin: ")
        vp_start_date = input("VP_Start_date: ")
        treasurer_sin = input("Treasurer_Sin: ")
        t_start_date = input("T_Start_date: ")
        print("-------------------------------------------")
        cursor.execute(query, (cin, president_sin, p_start_date, vicepresident_sin, vp_start_date, treasurer_sin, t_start_date))
        connection.commit()
        print(f"Data inserted: {cin}, {president_sin}, {p_start_date}, {vicepresident_sin}, {vp_start_date}, {treasurer_sin}, {t_start_date}")
    elif relation == "GROUP_STUDY":
        query = "INSERT INTO GROUP_STUDY VALUES (%s, %s, %s, %s, %s, %s)"
        query2 = "INSERT INTO PARTICIPATE_IN VALUES (%s, %s %s)"
        print("-------------------------------------------")
        gin = input("Gin: ")
        gname = input("GName: ")
        leader_sin = input("Leader_Sin: ")
        l_start_date = input("L_Start_date: ")
        subject = input("Subject: ")
        cin = input("Cin: ")
        print("-------------------------------------------")
        cursor.execute(query, (gin, gname, leader_sin, l_start_date, subject, cin))
        cursor.execute(query2, (leader_sin, gin, l_start_date))
        connection.commit()
        print(f"Data inserted: {gin}, {gname}, {leader_sin}, {l_start_date}, {subject}, {cin}")

# 모든 데이터 검색
def searchAllData(connection, relation):
    cursor = connection.cursor()
    query = "SELECT * FROM %s" % (relation)
    cursor.execute(query)
    results = cursor.fetchall()

    if relation == "STUDENT":
        print("--------------------------------------------------------------------------------------------------------")
        print("%s%6s %5s %7s %4s %3s %3s%s%s %7s %7s %5s %2s%1s%s%s%s" % 
            ("|", "학번", "|", "전화번호", "|", "이름", "|", "성별", "|", "학과", "|", "멘토학번", "|", "동아리번호", "|", "동아리가입날짜", "|"))
        print("--------------------------------------------------------------------------------------------------------")
        for row in results:
            print(row)
        print("--------------------------------------------------------------------------------------------------------")
    elif relation == "CLUB":
        print("----------------------------")
        print("%s%s%s%s%s%s%s" % ("|", "동아리번호", "|", "동아리이름", "|", "장소", "|"))
        print("----------------------------")
        for row in results:
            print(row)
        print("----------------------------")
    elif relation == "CLUB_MANAGER":
        print("----------------------------------------------------------------------------------------------------------------------")
        print("%s%s%s%s%s%13s%9s %s %s%13s%7s %s %s %s%s" % 
            ("|", "동아리번호", "|", "회장 학번", "|", "회장 임명날짜", "|", "부회장 학번", "|", "부회장 임명날짜", "|", "총무 학번", "|", "총무 임명날짜", "|"))
        print("----------------------------------------------------------------------------------------------------------------------")
        for row in results:
            print(row)
        print("----------------------------------------------------------------------------------------------------------------------")
    elif relation == "GROUP_STUDY":
        print("----------------------------------------------------------------------------------------------")
        print("%s%s%s %7s%6s %6s%2s %12s%8s %5s%5s%s%s" %
            ("|", "그룹번호", "|", "그룹이름", "|", "관리자 학번", "|", "관리자 임명날짜", "|", "주제", "|", "동아리번호", "|"))
        print("----------------------------------------------------------------------------------------------")
        for row in results:
            print(row)
        print("----------------------------------------------------------------------------------------------")

    return results

# 특정 조건을 가진 데이터 검색
# def searchDataByFilter(connection, relation):
#     cursor = connection.cursor()
#     query = "SELECT * FROM %s" % (relation)
#     cursor.execute(query)
#     results = cursor.fetchall()

# 데이터 수정
def updateData(connection, relation):
    results = searchAllData(connection, relation)
    cursor = connection.cursor()

    if relation == "STUDENT":
        sin_tobe_updated = input("정보를 수정할 학생의 학번: ")

        for row in results:
            if row[0] == sin_tobe_updated:
                break

        new_value = [
            input("학번: "),
            input("전화번호: "),
            input("이름: "),
            input("성별: "),
            input("학과: "),
            input("멘토학번: "),
            input("동아리번호: "),
            input("동아리 가입날짜: ")
            ]

        # 새로 입력한 값들이 ""일 경우 기존 데이터를 유지
        i = 0
        for value in new_value:
            if value == "":
                new_value[i] = row[i]
            i = i + 1

        query = ("UPDATE %s SET Sin='%s', Phone='%s', SName='%s', Sex='%s', Major='%s', Super_Sin='%s', Cin='%s', Signup_date='%s' WHERE Sin='%s'" 
        % (relation, new_value[0], new_value[1], new_value[2], new_value[3], new_value[4], new_value[5], new_value[6], new_value[7], sin_tobe_updated))
        cursor.execute(query)
        connection.commit()
    elif relation == "CLUB":
        cin_tobe_updated = input("정보를 수정할 동아리의 동아리 번호: ")

        for row in results:
            if row[0] == cin_tobe_updated:
                break

        new_value = [
            input("동아리 번호: "),
            input("동아리 이름: "),
            input("장소: ")
        ]

        # 새로 입력한 값들이 ""일 경우 기존 데이터를 유지
        i = 0
        for value in new_value:
            if value == "":
                new_value[i] = row[i]
            i = i + 1

        query = ("UPDATE %s SET Cin='%s', CName='%s', Location='%s' WHERE Cin='%s'" 
                % (relation, new_value[0], new_value[1], new_value[2], cin_tobe_updated))
        cursor.execute(query)
        connection.commit()
    elif relation == "CLUB_MANAGER":
        cin_tobe_updated = input("정보를 수정할 동아리 관리자 목록의 동아리 번호: ")

        for row in results:
            if row[0] == cin_tobe_updated:
                break

        new_value = [
            input("동아리번호: "),
            input("동아리 회장 학번: "),
            input("동아리 회장 임명 날짜: "),
            input("동아리 부회장 학번: "),
            input("동아리 부회장 임명 날짜: "),
            input("동아리 총무 학번: "),
            input("동아리 총무 임명 날짜: ")
        ]

        # 새로 입력한 값들이 ""일 경우 기존 데이터를 유지
        i = 0
        for value in new_value:
            if value == "":
                new_value[i] = row[i]
            i = i + 1

        query = ("UPDATE %s SET Cin='%s', President_Sin='%s', P_Start_date='%s', VicePresident_Sin='%s', VP_Start_date='%s', Treasurer_Sin='%s', T_Start_date='%s' WHERE Cin='%s'"
                % (relation, new_value[0], new_value[1], new_value[2], new_value[3], new_value[4], new_value[5], new_value[6], cin_tobe_updated))
        cursor.execute(query)
        connection.commit()
    elif relation == "GROUP_STUDY":
        gin_tobe_updated = input("정보를 수정할 그룹스터디의 그룹 번호: ")

        for row in results:
            if row[0] == gin_tobe_updated:
                break

        new_value = [
            input("그룹 번호: "),
            input("그룹 이름: "),
            input("관리자 학번: "),
            input("관리자 임명 날짜: "),
            input("주제: "),
            input("동아리번호: ")
        ]
        
        # 새로 입력한 값들이 ""일 경우 기존 데이터를 유지
        i = 0
        for value in new_value:
            if value == "":
                new_value[i] = row[i]
            i = i + 1

        query = ("UPDATE %s SET Gin='%s', GName='%s', Leader_Sin='%s', L_Start_date='%s', Subject='%s', Cin='%s' WHERE Gin='%s'"
                % (relation, new_value[0], new_value[1], new_value[2], new_value[3], new_value[4], new_value[5], gin_tobe_updated))
        cursor.execute(query)
        connection.commit()

    print(f"Data updated to:", end=' ')
    for updated_value in new_value:
        print(updated_value, end=' ')

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
    while True:
        try:
            i = 1
            print("\n===================================%s===================================" % (menu[0]))
            while i <= len(menu) - 1:
                if len(menu) >= i + 2:
                    print("%-40s %-40s" % (menu[i], menu[i + 1]))
                else:
                    print("%-40s" % (menu[i]))
                i = i + 2
            print("============================================================================")
            choice = input("Enter your choice: ")

            if choice == "1":
                if connected == False:
                    user = input("User: ")
                    pw = getpass.getpass("Password: ")
                    connection = connectToDatabase(user, pw)
                    print("Connected to the database.")
                    connected = True
                else:
                    print("You already have been connected to database.")
            elif choice == "2":
                connection.close()
                print("Connection closed.\n")
                connected = False
                break
            elif choice == "3":
                if connected == False:
                    print("You need to log in the database.")
                    continue
                else:
                    searchAllData(connection, "STUDENT")
            elif choice == "4":
                if connected == False:
                    print("You need to log in the database.")
                    continue
                else:
                    searchAllData(connection, "CLUB")
            elif choice == "5":
                if connected == False:
                    print("You need to log in the database.")
                    continue
                else:
                    searchAllData(connection, "CLUB_MANAGER")
            elif choice == "6":
                if connected == False:
                    print("You need to log in the database.")
                    continue
                else:
                    searchAllData(connection, "GROUP_STUDY")
            # elif choice == "7":
            #     if connected == False:
            #         print("You need to log in the database.")
            #         continue
            #     else:
            #         searchDataByFilter(connection, "STUDENT")
            elif choice == "11":
                if connected == False:
                    print("You need to log in the database.")
                    continue
                else:
                    insertData(connection, "STUDENT")
            elif choice == "12":
                if connected == False:
                    print("You need to log in the database.")
                    continue
                else:
                    insertData(connection, "CLUB")
            elif choice == "13":
                if connected == False:
                    print("You need to log in the database.")
                    continue
                else:
                    insertData(connection, "CLUB_MANAGER")
            elif choice == "14":
                if connected == False:
                    print("You need to log in the database.")
                    continue
                else:
                    insertData(connection, "GROUP_STUDY")
            elif choice == "15":
                if connected == False:
                    print("You need to log in the database.")
                    continue
                else:
                    updateData(connection, "STUDENT")
            elif choice == "16":
                if connected == False:
                    print("You need to log in the database.")
                    continue
                else:
                    updateData(connection, "CLUB")
            elif choice == "17":
                if connected == False:
                    print("You need to log in the database.")
                    continue
                else:
                    updateData(connection, "CLUB_MANAGER")
            elif choice == "18":
                if connected == False:
                    print("You need to log in the database.")
                    continue
                else:
                    updateData(connection, "GROUP_STUDY")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

if __name__ == "__main__":
    main()