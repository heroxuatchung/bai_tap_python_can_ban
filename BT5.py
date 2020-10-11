my_string = input("nhập chuỗi: ")
def kyTuLonNho(my_string):
    max = min =my_string[0]
    for i in my_string:
        if max<i:
            max = i
        if min>i:
            min = i
    print("Ki tu lon nhat la",max)
    print("ki tu nho nhat la",min)
kyTuLonNho(my_string)