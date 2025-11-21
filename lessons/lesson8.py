import sqlite3



def create_table():
    connect = sqlite3.connect('students.db')
    cursor = connect.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR (20) NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS grades(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        grade INTEGER NOT NULL,
        subject VARCHAR (30) NOT NULL,
        student_id INTEGER NOT NULL,
        FOREIGN KEY(student_id) REFERENCES students(id)
    )
    ''')

    connect.commit()
    connect.close()

# create_table()


def insert_test_db():
    # cursor.execute(
        # 'INSERT INTO students (name) VALUES (?)',
        # ("Oleg",)
        # [
        #     ("Jon",),
        #     ("Ardager",),
        #     ("Oleg",)
        # ]
    # )
    connect = sqlite3.connect('students.db')
    cursor = connect.cursor()
    cursor.execute(
        'INSERT INTO grades (grade, subject, student_id) VALUES (?,?,?)',
            (70, "Алгебру", 1)
    #         # (90, "Физика", 3),
    #         # (30, "История", 2),
    #         # (40, "Химия", 1),
    #         # (50, "Биология", 2),
    #         # (20, "Алгебру", 1),
    #         (10, "Алгебру", 4)
    )
    connect.commit()
    connect.close()
    print("Данные успешно добавлены")

# insert_test_db()



def get_students_grade():
    cursor.execute('''
    SELECT students.name, grades.subject, grades.grade
    FROM students FULL OUTER JOIN grades ON students.id = grades.student_id
                   ''')
    users = cursor.fetchall()
    print(users)
# get_students_grade()




def get_student_hi_grade():

    # MAX() MIN() AVG() COUNT() SUM()
    cursor.execute(
        'SELECT students.name, MAX(grades.grade) FROM students INNER JOIN grades ON students.id = grades.student_id'
    )
    users = cursor.fetchall()

    print(users)

# get_student_hi_grade()


def get_best_student():

    cursor.execute(
        '''
        SELECT name FROM students WHERE id IN (
            SELECT student_id FROM grades
            WHERE grade >= 70
        );
        '''
    )
    users = cursor.fetchall()
    print(users)

# get_best_student()

def create_my_view():
    cursor.execute('''
        CREATE VIEW IF NOT EXISTS my_view_2 AS
        SELECT students.name, grades.subject, grades.grade
        FROM students RIGHT JOIN grades ON students.id = grades.student_id
    ''')
    connect.commit()

# create_my_view()

def get_students():

    cursor.execute('SELECT * FROM my_view')
    users = cursor.fetchall()
    print(users)

# get_students()