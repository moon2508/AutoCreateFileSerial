import csv

# Định tên các trường dữ liệu
# field_names = ['Name', 'Age', 'Email']
# Tạo số nguyên ngẫu nhiên trong khoảng từ 1 đến 10
import random
import string

# Độ dài của dãy số
length = 10
# Chuỗi cố định 4 ký tự đầu
fixed_prefix = "12345"

# Tạo chuỗi ngẫu nhiên
random_suffix = ''.join(random.choices(string.digits, k=length))

# Ghép chuỗi cố định và chuỗi ngẫu nhiên
result = fixed_prefix + random_suffix

print(result)




# Dữ liệu các hàng

data = [
    ['John Doe', 30, 'john.doe@example.com'],
    ['Jane Smith', 25, 'jane.smith@example.com'],
    ['Bob Johnson', 35, 'bob.johnson@example.com']
]

# Mở file CSV và ghi dữ liệu vào
# with open('./data.csv', mode='w', newline='') as file:
#     writer = csv.writer(file)
    
#     # Ghi tên trường dữ liệu (header)
#     # writer.writerow(field_names)
    
#     # Ghi dữ liệu từng hàng
#     writer.writerows(data)

print("File CSV đã được tạo thành công.")