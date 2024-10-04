import csv
import datetime
import random
import string

# Nhập đầu vào từ người dùng
seri_length = 15 # Mặc định là 15 cho trùng với Viettel
# seri_length = input("Nhập độ dài của Serial number: ") 

# fixed_prefix = input("Nhập đầu số mặc định: ")
number = input('Nhập số lượng thẻ cần sinh: ')
provider = input('Nhập mã provider code vào đây:')
amount = input('Nhập mệnh giá của thẻ:')

#GETDate
# Lấy ngày hiện tại
current_date = datetime.date.today()
date_now=datetime.datetime.now()
# Khoảng thời gian bạn muốn cộng (ở đây là 1 ngày)
delta = datetime.timedelta(days=6 *365)

# Cộng ngày hiện tại với khoảng thời gian
new_date = current_date + delta
# Chuyển đổi định dạng ngày
date =current_date.strftime("%d%m%Y")
formatted_date = new_date.strftime("%d/%m/%Y")
# Mặc định prefix=date
fixed_prefix = date_now.strftime("%Y%d%m%H%M%S")


length= int(seri_length) - len(fixed_prefix)
# In ra đầu vào đã nhập
# print('Chiều dài chuỗi', length)

# # Độ dài của dãy số
# length = 10
# # Chuỗi cố định 4 ký tự đầu
# fixed_prefix = "12345"

# Tạo chuỗi ngẫu nhiên
random_suffix = ''.join(random.choices(string.digits, k=length))

# Ghép chuỗi cố định và chuỗi ngẫu nhiên
result = fixed_prefix + random_suffix
random_suffix2  = ''.join(random.choices(string.digits, k=length))

# Ghép chuỗi cố định và chuỗi ngẫu nhiên
result2 = fixed_prefix + random_suffix2 
# print('Chuỗi 1: ',result, ' - ', 'Chuỗi 2:', result2)




# Hiển thị ngày
print('Expire date: ',formatted_date, ' - ', 'Ngày hiện tại' , date)

# Tạo một mảng rỗng
parent_array = []
children_array =[]
# Vòng lặp để đẩy dữ liệu vào mảng
for i in range(0, int(number)):
    seri1 =int(result) + i
    seri2 = int(result2) + i
    # print('Chiều dài của chuỗi 1, 2: ',len(str(seri1)), len(str(seri2)))
    child = [seri1, seri2, formatted_date]
    children_array.append(child)


# Hiển thị mảng
# print(children_array)


filename = f"C:/Users/Admin/Documents/IMEDIA/Automation_Testing_API/AutoPAYMENT/cypress/fixtures/{provider}_{amount}_{date}_1.csv"
# Mở file CSV và ghi dữ liệu vào
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Ghi tên trường dữ liệu (header)
    # writer.writerow(field_names)
    
    # Ghi dữ liệu từng hàng
    writer.writerows(children_array)

print("File CSV đã được tạo thành công.")
