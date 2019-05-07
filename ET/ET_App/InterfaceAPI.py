import psycopg2

class User:

    def __init__(self, UserId, FirstName, LastName, Age, Gender, State, Email,Password):
        self.UserId = UserId
        self.FirstName = FirstName
        self.LastName = LastName
        self.Age = Age
        self.Gender = Gender
        self.State = State
        self.Email = Email
        self.Password=Password

    def AddUser(self):
        print("Add User Started")
        tempUser1 = User(self.UserId, self.FirstName, self.LastName, self.Age, self.Gender, self.State, self.Email,self.Password)

        # how to take multiple user data ?

        try:
            connection = psycopg2.connect(user="postgres",
                                          password="postgres",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="ET")

            cursor = connection.cursor()

            # call stored procedure
            insert = """INSERT INTO public."ET_App_user"("userId", "firstName", "lastName", age, gender, state, email, password_enc)  VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"""
            
            value = (tempUser1.UserId, tempUser1.FirstName, tempUser1.LastName, tempUser1.Age, tempUser1.Gender, tempUser1.State, tempUser1.Email, tempUser1.Password)

            cursor.execute(insert, value)

            connection.commit()
            '''
                    cursor.callproc('sp_adduser', (tempUser1.UserId, tempUser1.FirstName, tempUser1.LastName, tempUser1.Age,
                                                      tempUser1.Gender, tempUser1.State, tempUser1.Email, "abcd1234"))
            '''
            print("Adding Users...")
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error while connecting to PostgreSQL", error)
        finally:
            # closing database connection.
            if (connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")

        return True


    def GetUsers(user):
        try:
            conn = psycopg2.connect(user="postgres",
                                       password="postgres",
                                       host="127.0.0.1",
                                       port="5432",
                                       database="ET")
            cur = conn.cursor()
            getuserquery = """select * from Et_app_user"""
            cur.execute(getuserquery)
            print("Selecting rows from the user table")
            user_records = cur.fetchall()
            print("Print each row and it's columns values")
            for row in user_records:
                print("UserId = ", row[0], )
                print("firstName = ", row[1])
                print("lastName = ", row[2], "\n")
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error while fetching data from PostgreSQL", error)
        finally:
            # closing database connection.
            if (conn):
                cur.close()
                conn.close()
                print("PostgreSQL connection is closed")


# class Question:
#     def __init__(self, QuestionId, QuestionName, Choice1, Choice2, Choice3, Choice4):
#         self.QuestionId = QuestionId
#         self.QuestionName = QuestionName
#         self.Choice1 = Choice1
#         self.Choice2 = Choice2
#         self.Choice3 = Choice3
#         self.Choice4 = Choice4


    # def GetQuestions(question):
    #     try:
    #         conn = psycopg2.connect(user="postgres",
    #                                    password="postgres",
    #                                    host="127.0.0.1",
    #                                    port="5432",
    #                                    database="ET")
    #         cur = conn.cursor()
    #         getquestionquery = """select * from Et_App_questions"""
    #         cur.execute(getquestionquery)
    #         print("Selecting rows from the questions table")
    #         question_records = cur.fetchall()
    #         print("Print each row and it's columns values")
    #         for row in question_records:
    #             print("QuestionId = ", row[0], )
    #             print("Question = ", row[1],"\n")
    #     except (Exception, psycopg2.DatabaseError) as error:
    #         print("Error while fetching data from PostgreSQL", error)
    #     finally:
    #         # closing database connection.
    #         if (conn):
    #             cur.close()
    #             conn.close()
    #             print("PostgreSQL connection is closed")


'''

class UserDetails:
    def __init__(self, UserId, QuestionID, OptionId):
        tempUser = User()
        self.UserId = tempUser.UserId
        tempQuestion = Question()
        self.QuestionId = tempQuestion.QuestionID
        self.OptionId = tempQuestion.OptionId

    def GetUserDetails(user):
        return user.UserId

'''
