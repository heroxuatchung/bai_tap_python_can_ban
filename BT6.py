my_string = input("Nhập chuỗi: ")
def hoaThuong(s):
    kq=""
    for i in my_string:
        if i.islower():
            kq+=i.upper()
        else:
            kq+=i.lower()
    return kq
print(f"Kết quả: {hoaThuong(my_string)}")