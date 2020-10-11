my_string=input("Nhập chuỗi: ")
def layDauDuoi(my_string):
    print(my_string[0:2]+my_string[-2:])
    if len(my_string)<2:
        print("     ")
layDauDuoi(my_string)