def three_common_letter(string):
    count_dic = {}
    for item in string:
        if item.isalpha() == True:
            if item.lower() not in count_dic.keys():
                count_dic[item.lower()] = 1
            else:
                count_dic[item] += 1
    print(count_dic)
    try:
        if len(count_dic) < 3:
            raise Exception

        count_list = [count for count in count_dic.values()]
        index1 = count_list.index(max(count_list))
        letter1 = list(count_dic)[index1]

        count_list2 = [n for n in count_list if n != max(count_list)]
        index2 = count_list2.index(max(count_list2))
        letter2 = list(count_dic)[index2]

        count_list3 = [n for n in count_list2 if n != max(count_list2)]
        index3 = count_list3.index(max(count_list3))
        letter3 = list(count_dic)[index3]
        return([letter1,letter2,letter3])
    except:
        return("There are no enough letter in the string to count for")
