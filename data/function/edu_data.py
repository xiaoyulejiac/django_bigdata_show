def edudata_function(my_dict):
    # my_dict数据示例
    # {'专科': 31272, '其他': 93378, '本科': 9515, '硕士学历及以上': 2474, '高中学历及以下': 263441}
    my_list = [[k, v] for k, v in my_dict.items()]
    edu_num = 0
    for list in my_list:
        edu_num += list[1]
    for list in my_list:
        fraction = list[1] / edu_num
        percentage = "{:.2%}".format(fraction)
        list.append(percentage)
    return my_list
# 返回示例
# [['专科', 31272, '7.82%'], ['其他', 93378, '23.34%'], ['本科', 9515, '2.38%'], ['硕士学历及以上', 2474, '0.62%'], ['高中学历及以下', 263441, '65.85%']]


