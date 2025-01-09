import pandas as pd


def get_orders_by_total_range(df, minValue, maxValue, sortType=True):
    """
    Tìm danh sách hóa đơn có tổng giá trị trong khoảng [minValue, maxValue]

    Parameters:
    df (DataFrame): DataFrame chứa dữ liệu đơn hàng
    minValue (float): Giá trị tối thiểu
    maxValue (float): Giá trị tối đa
    sortType (bool): True - sắp xếp tăng dần, False - sắp xếp giảm dần

    Returns:
    DataFrame: Gồm 2 cột - OrderID và TotalAmount, đã được sắp xếp theo sortType
    """

    # Tính tổng giá trị cho mỗi đơn hàng
    order_totals = df.groupby('OrderID').apply(
        lambda x: (x['UnitPrice'] * x['Quantity'] * (1 - x['Discount'])).sum()
    ).reset_index()

    # Đặt tên cho các cột
    order_totals.columns = ['OrderID', 'TotalAmount']

    # Lọc các đơn hàng trong khoảng giá trị
    filtered_orders = order_totals[
        (order_totals['TotalAmount'] >= minValue) &
        (order_totals['TotalAmount'] <= maxValue)
        ]

    # Sắp xếp kết quả
    sorted_orders = filtered_orders.sort_values('TotalAmount', ascending=sortType)

    return sorted_orders


# Ví dụ sử dụng:
df = pd.read_csv('../Data set/SalesTransactions.csv')

minValue = float(input("Nhập giá trị min: "))
maxValue = float(input("Nhập giá trị max: "))
sortType = input("Nhập kiểu sắp xếp (True/False): ").lower() == 'true'

result = get_orders_by_total_range(df, minValue, maxValue, sortType)
print("\nDanh sách hóa đơn thỏa điều kiện:")
print(result)