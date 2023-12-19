import csv
import datetime
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
random_suffix2  = ''.join(random.choices(string.digits, k=length))

# Ghép chuỗi cố định và chuỗi ngẫu nhiên
result2 = fixed_prefix + random_suffix2
print(result)
print(result2)


#GETDate
# Lấy ngày hiện tại
current_date = datetime.date.today()
# Khoảng thời gian bạn muốn cộng (ở đây là 1 ngày)
delta = datetime.timedelta(days=6 *365)

# Cộng ngày hiện tại với khoảng thời gian
new_date = current_date + delta

# Hiển thị kết quả
print(new_date)
# Chuyển đổi định dạng ngày
formatted_date = new_date.strftime("%d/%m/%Y")

# Hiển thị ngày
print(formatted_date)


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
