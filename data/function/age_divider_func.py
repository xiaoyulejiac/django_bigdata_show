def age_divider_function(age_data):
    peopl_num = list(map(int, age_data.values()))
    young_people_num = mid_people_num = old_people_num = all_people_num = 0

    for i in list(map(int, age_data.keys())):
        all_people_num += peopl_num[i]
        if i <= 14:
            young_people_num += peopl_num[i]
        elif i <= 64:
            mid_people_num += peopl_num[i]
        else:
            old_people_num += peopl_num[i]
    result = [all_people_num, young_people_num, mid_people_num, old_people_num]
    return result
