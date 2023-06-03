import pymysql
import datetime
import re
from collections import Counter

# 计算生日


def calculate_age(birth_date):
    today = datetime.date.today()
    age = today.year - birth_date.year - \
        ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age


def age_function(host, port, user, password, database):
    # 连接到MySQL数据库
    db = pymysql.connect(host=host, port=port, user=user,
                         password=password, db=database, charset='utf8')

# 创建游标对象
    cursor = db.cursor()

# 查询生日数据
    cursor.execute("SELECT birth FROM data")

# 获取所有行
    rows = cursor.fetchall()

    ages = []
# 计算年龄并将其插入到数据库中
    for row in rows:
        string = row[0]
        pattern = r"(\d{4})-(\d{1,2})-(\d{1,2})"
        match = re.search(pattern, string)
        age = calculate_age(datetime.date(int(match.group(1)),
                                          int(match.group(2)), int(match.group(3))))
        ages.append(age)

    result = dict(Counter(ages))
    sorted_result = dict(sorted(result.items(), key=lambda x: x[0]))
# 提交更改并关闭连接
    db.close()
    return sorted_result
