from K224161808.ontap_oop.filefactory import FileFactory
from K224161808.ontap_oop.product import Product

ff=FileFactory
dataset=ff.readData("mydataset.json",Product)
print("Danh sach san pham")
for product in dataset:
    print(product)