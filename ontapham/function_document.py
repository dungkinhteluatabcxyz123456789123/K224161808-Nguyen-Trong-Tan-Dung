def first_degree(a,b):
    """
    Đây là phương trình bac 1: ax+b=0
    :param a: he so a
    :param b: he so b
    :return: tra ve 3 truong hop ket qua
    """

    if a==0 and b==0:
        print("Phuong trinh vo so nghiem")
    elif a==0 and b!=0:
        print("phuong trinh vo nghiem")
    else:
        x=-b/a
        print("No cua phuong trinh = ",x)
print("Phuong trinh bac 1")
a=float(input("nhap he so a:"))
b=float(input("nhap he so b:"))
first_degree(a,b)
