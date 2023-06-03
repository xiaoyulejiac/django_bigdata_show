from data.function.edu_func import edu_function
from data.function.age_func import age_function
from data.function.edu_data import edudata_function
from data.function.age_divider_func import age_divider_function
from data.function.marriage_func import marriage_function


def age_data_provider():
    age_data = age_function('8.130.52.33',3306,'root',"test1234",'xiaoyulejia')
    # {0: 6408, 1: 10540, 2: 10614, 3: 10903, 4: 10785, 5: 10624, 6: 10562, 7: 10654, 8: 10518, 9: 10645, 10: 10673, 11: 10725, 12: 10599, 13: 10619, 14: 10809, 15: 7570, 16: 5176, 17: 5116, 18: 5344, 19: 5279, 20: 5267, 21: 5337, 22: 5324, 23: 5321, 24: 5349, 25: 5229, 26: 5138, 27: 5231, 28: 5349, 29: 5358, 30: 5321, 31: 5388, 32: 5306, 33: 5250, 34: 5439, 35: 5140, 36: 5300, 37: 5271, 38: 5195, 39: 5188, 40: 5300, 41: 5300, 42: 5346, 43: 5360, 44: 5337, 45: 5257, 46: 5438, 47: 5250, 48: 5447, 49: 5180, 50: 5240, 51: 5301, 52: 5169, 53: 5318, 54: 5191, 55: 5272, 56: 5128, 57: 5322, 58: 5351, 59: 5265, 60: 2192, 61: 66, 62: 57, 63: 66, 64: 76, 65: 62, 66: 59, 67: 80, 68: 63, 69: 73, 70: 60, 71: 54, 72: 66, 73: 64, 74: 68, 75: 61, 76: 77, 77: 60, 78: 52, 79: 60, 80: 56, 81: 58, 82: 75, 83: 68, 84: 58, 85: 54, 86: 64, 87: 61, 88: 66, 89: 69, 90: 52, 91: 69, 92: 64, 93: 58, 94: 60, 95: 74, 96: 22}
    return age_data

def age_sorted_data_provider():
    age_sorted_data = age_divider_function(age_data_provider())
    # [400080, 155648, 242444, 1988]
    return age_sorted_data

def edu_data_provider():
    edu_data = edu_function('8.130.52.33',3306,'root',"test1234",'xiaoyulejia')
    # {'专科': 31272, '其他': 93378, '本科': 9515, '硕士学历及以上': 2474, '高中学历及以下': 263441}
    return edu_data

def edu_list_data_provider():
    edu_list_data = edudata_function(edu_data_provider())
    # [['专科', 31272, '7.82%'], ['其他', 93378, '23.34%'], ['本科', 9515, '2.38%'], ['硕士学历及以上', 2474, '0.62%'], ['高中学历及以下', 263441, '65.85%']]
    return edu_list_data

def changchun_edu_list_data_provider():
    changchun_edu_list_data = list(list(map(int, edu_data_provider().values())))
    # [[31272, 93378, 9515, 2474, 263441]]
    return changchun_edu_list_data

def marriage_data_provider():
    marriage_data = marriage_function('8.130.52.33',3306,'root',"test1234",'xiaoyulejia')
    print(marriage_data)
    marriage_data.append(marriage_data[0]+marriage_data[1])
    # [156956, 243124, 233333] 已婚 未婚 总和
    return marriage_data


