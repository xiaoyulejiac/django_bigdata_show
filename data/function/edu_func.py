import pymysql
import re


def edu_function(host, port, user, password, database):
    mydb = pymysql.connect(host=host, port=port, user=user,
                           password=password, db=database, charset='utf8')

    mycursor = mydb.cursor()

    mycursor.execute("SELECT edu, COUNT(*) FROM data GROUP BY edu")

    myresult = mycursor.fetchall()

    result = ""
    for x in myresult:
        result += str(x)

    result = result.replace(")(", ",").replace(
        "(", "").replace(")", "").replace("'", "")
    s = re.sub(" ", "", result)
    lst = s.split(",")
    mp = {lst[i]: int(lst[i+1]) for i in range(0, len(lst), 2)}
    return mp
