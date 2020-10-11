my_string=input("Nhập chuỗi: ")
m=int(input("Nhập m: "))
def xoaKyTu(my_string,m):
    while(m<0):
        m=int(input("Nhập m là số không âm: "))
    my_string = my_string[:m] + my_string[(m+1):]
    print(my_string)
xoaKyTu(my_string,m)



