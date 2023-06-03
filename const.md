# 阿里云数据库
`请注意 阿里云数据库的表名称是data` `请注意 阿里云数据库的表名称是data` `请注意 阿里云数据库的表名称是data`
`需要修改function文件夹下功能实现的sql语句` `需要修改function文件夹下功能实现的sql语句` `需要修改function文件夹下功能实现的sql语句`
pymysql.connect(host='8.130.52.33', port=3306, user='root', password="test1234", db='xiaoyulejia', charset='utf8')
('8.130.52.33',3306,'root',"xiaoyulejia",'data')

# 主数据库
pymysql.connect(host='10.211.55.3', port=3306, user='xiaoyulejiatest', password="test1234", db='xiaoyulejiatest', charset='utf8')
('10.211.55.3',3306,'xiaoyulejiatest',"test1234",'xiaoyulejiatest')


# 测试用数据库
pymysql.connect(host='10.211.55.3', port=3306, user='xiaoyulejia', password="test1234", db='xiaoyulejia', charset='utf8')
('10.211.55.3',3306,'xiaoyulejia',"test1234",'xiaoyulejia')

## 其他
`插入已有表中`
ALTER TABLE test ADD age INT;
ALTER TABLE test ADD area varchar(255);

`删除列`
ALTER TABLE test DROP COLUMN biryear;

list(map(str, age_data.keys()))