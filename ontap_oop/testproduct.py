from K224161808.ontap_oop.filefactory import FileFactory
from K224161808.ontap_oop.product import Product

p1=Product(1,"Coca",100)

dataset=[]
dataset.append(p1)
dataset.append(Product(2,"Pepsi",20))
dataset.append(Product(3,"Sting",80))
dataset.append(Product(4,"Aqua",70))
dataset.append(Product(5,"Redbull",50))
print("Danh sách sản phẩm:")
for product in dataset:
    print(product)

while True:
    id=(int(input("Nhập mã:")))
    name=input("Nhâp tên: ")
    price=float(input("Nhập giá:"))
    p=Product(id,name,price)
    dataset.append(p)
    ask=input("Nhập tiếp không?(c/k):")
    if ask=="k":
        break
print("Danh sách sản phẩm sau khi nhập:")
for product in dataset:
    print(product)
#Gọi chức năng chụp ảnh đối tượng xuống ổ cứng
#Chụp thành định dạng json:
ff=FileFactory()
ff.writeData("mydataset.json",dataset)


def products_by_price(a, b, dataset):
    filtered_products = [product for product in dataset if a <= product.price <= b]

    print(f"Các sản phẩm có giá từ {a} đến {b}:")
    for product in filtered_products:
        print(product)


# Gọi hàm với ví dụ giá từ 50 đến 100
a=int(input("Mời bạn nhập mức gía khởi điểm mà bạn muốn lọc:"))
b=int(input("Mời bạn nhập giá cao nhất bạn muốn lọc:"))
products_by_price(a,b,dataset)

def remove_specific_product(x,dataset):
    i = 0
    while i < len(dataset):
        if dataset[i].price < x:
            dataset.pop(i)
        else:
            i += 1
x=int(input("Mời bạn nhập giá sản phẩm nhỏ nhất mà dưới đó bạn muốn xóa (x)"))
remove_specific_product(x,dataset)
print("Danh sách sản phẩm sau khi xóa các sản phẩm nhỏ hơn ",x,": ")
for product in dataset:
    print(product)