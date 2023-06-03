import pymysql
import re


def  marriage_function(host, port, user, password, database):
    mydb = pymysql.connect(host=host, port=port, user=user,
                           password=password, db=database, charset='utf8')

    mycursor = mydb.cursor()

    mycursor.execute("SELECT marry, COUNT(*) FROM data GROUP BY marry")

    myresult = mycursor.fetchall()

    result = ""
    for x in myresult:
        result += str(x)
    result = result.replace(")(", ",").replace(
        "(", "").replace(")", "").replace("'", "")
    s = re.sub(" ", "", result)
    lst = s.split(",")
    # {'已婚': 156956, '未婚': 243124}
    my_dict = {lst[i]: int(lst[i+1]) for i in range(0, len(lst), 2)}
    # [156956, 243124] 已婚 未婚
    my_list = list(my_dict.values())
    return my_list
