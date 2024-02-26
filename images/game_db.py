import mysql.connector as MySQLdb

def login(username, password):
    try:
        db_connection = MySQLdb.connect(user='root', password='123456', host='localhost', database='sample')
        cursor = db_connection.cursor()
        sql = "select * from tbl_user where username = %s and password = %s"
        val=(username, password)
        cursor.execute(sql, val)
        results = cursor.fetchall() 
        if results:
            return True
            
    except Exception as e:
        print("Database error occured1")
        print(e)
    return False

def register(username, password, name, gender): 
    try:
        db_connection = MySQLdb.connect(user='root', password='123456', host='localhost', database='sample')
        cursor = db_connection.cursor()
        sql = "INSERT INTO tbl_user(username, password, full_name, gender) VALUES(%s, %s, %s, %s )"
        val=(username, password, name, gender)
        cursor.execute(sql, val)
        db_connection.commit()
        user_id=cursor.lastrowid
        db_connection.close()
        if user_id:
            return True
    except Exception as e:
        print("Database error occured2")
        print(e)
    return False

def save_score(score, username):
    try:
        # Create connection
        db_connection = MySQLdb.connect(user='root', password='123456', host='localhost', database='sample')
        cursor = db_connection.cursor()
        sql = "SELECT username FROM tbl_user WHERE username = '" + username + "'"
        print(sql)
        cursor.execute(sql)
        results = cursor.fetchall() 
        userid = results[0][0]
        # Insert query
        sql = "INSERT INTO tbl_scores VALUES(null, %s , %s , now())"
        val=(str(username), str(score))
        cursor.execute(sql, val)
        # Executer query
        db_connection.commit()
        score_id=cursor.lastrowid
        # Return true after successful insertion to database
        if score_id:
            return True
    except Exception as e:
        print("Database error occurred3")
        print(e)
    finally:
        db_connection.close()
    return False

def high_scores():
    try:
        # Create connection
        db_connection = MySQLdb.connect(user='root', password='123456', host='localhost', database='sample')
        cursor = db_connection.cursor()

        #  query
        sql = "SELECT  tbl_user.username, tbl_scores.score,tbl_scores.time  FROM tbl_scores join tbl_user on tbl_user.username=tbl_scores.username ORDER BY score DESC LIMIT 10; "
        cursor.execute(sql)
        # Executer query
        results = cursor.fetchall() 
        txt = "                    <b><u>HIGH SCORES<u></b>                   <br>"
        txt += "<b>Name           Score       Date                Time</b><br>"
        for row in results:
            txt+= str(row[0])+"         "+str(row[1])+"         "+str(row[2])[0:]+"            "+str(row[2])[10:]+"<br>"

        return txt
    except Exception as e:
        print("Database error occurred4")
        print(e)
    finally:
        db_connection.close()
    return False
