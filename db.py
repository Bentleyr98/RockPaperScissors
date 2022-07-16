#import sqlite libraries to access database
import sqlite3
from sqlite3 import Error


class Database:
    def __init__(self):
        pass


    def create_table(self, scoreboard):
        """ 
        Create a table in the database 
        """
        conn = None
        try:
            #connect to database
            conn = sqlite3.connect(scoreboard)
            cur = conn.cursor()

            # Create table
            cur.execute("""CREATE TABLE IF NOT EXISTS SCORES(id PRIMARY KEY, last_name TEXT, first_name TEXT, score REAL);""")

            # Save (commit) the changes
            conn.commit()

        except Error as e:
            print(e)
        finally:
            if conn:
                #close connection
                conn.close()


    def add_score(self, fname, lname, scoreboard):
        """Insert score to the table in the database"""
        conn = None
        try:
            #connect to database
            conn = sqlite3.connect(scoreboard)
            cur = conn.cursor()

            # Insert a row of data
            sql = f'''SELECT score FROM SCORES WHERE first_name = '{fname}' and last_name = '{lname}' '''
            cur.execute(sql)

            #get results from select statement
            old_score = cur.fetchone()
            
            #if user doesn't have a previous score, add them to the database
            if old_score == None:
                # Insert a row of data
                sql = f'''INSERT INTO SCORES VALUES (null, '{lname}', '{fname}', 1)'''
                cur.execute(sql)

                # Save (commit) the changes
                conn.commit()
            

            #if user is in our database, update score
            else:
                #database returns a tuple. Use indexing to grab our score we want
                score = int(old_score[0])
                new_score = score + 1

                # Insert a row of data
                sql = f'''UPDATE SCORES SET score = {new_score} WHERE first_name = '{fname}' and last_name = '{lname}' '''
                cur.execute(sql)

                # Save (commit) the changes
                conn.commit()

        except Error as e:
            print(e)
        finally:
            if conn:
                #close connection
                conn.close()

    def get_scoreboard(self, scoreboard):
        conn = None
        try:
            #connect to database
            conn = sqlite3.connect(scoreboard)
            cur = conn.cursor()
            cur.execute("SELECT * FROM SCORES")

            scores = []

            #fetch result set from query
            rows = cur.fetchall()

            #sort through result set
            for row in rows:
                #create temporary dictionary to hold values for a single player
                temp = dict()
                temp['name'] = row[2] + " " + row[1]
                temp['score'] = row[3]

                #add dictionary to list
                scores.append(temp)

            #sort list by score
            newlist = sorted(scores, key=lambda d: int(d['score'])) 

            #get top five from list
            topFiveList = []
            for i in range(5):
                score = newlist.pop()
                topFiveList.append(score)


            #format top five scores into a dictionary for easy use
            topFive = dict()
            j = 0
            for i in topFiveList:
                j += 1
                for key, value in i.items():
                    if key == 'name':
                        newKeyName = 'name' + str(j)
                        topFive[newKeyName] = value
                    else:
                        newKeyScore = 'score' + str(j)
                        topFive[newKeyScore] = value

            #get average and number of players. Add to dictionary to return
            cur.execute("SELECT avg(score) FROM SCORES")
            avg = cur.fetchone()
            topFive['AVG'] = avg[0]

            cur.execute("SELECT COUNT(*) FROM SCORES")
            cnt = cur.fetchone()
            topFive['CNT'] = cnt[0]

        except Error as e:
            print(e)
        finally:
            if conn:
                #close connection
                conn.close()
        return topFive



    def delete_user(self, scoreboard, fname, lname):
        conn = None
        try:
            #connect to database
            conn = sqlite3.connect(scoreboard)
            cur = conn.cursor()

            #Delete user from database
            sql = f'''DELETE FROM SCORES WHERE last_name LIKE '{lname}' AND first_name LIKE '{fname}' '''
            cur.execute(sql)

            # Save (commit) the changes
            conn.commit()

        except Error as e:
            print(e)
        finally:
            if conn:
                #close connection
                conn.close()

