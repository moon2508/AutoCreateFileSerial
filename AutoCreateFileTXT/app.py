#Sinh ra file insert dữ liệu chuyển mạng giữ số
import datetime
import random
import string


count_phones = 1
prefix = "20240110"
random_string = '1705230400008983'
phone_number = "84368099996"
origion_provider = '01'
current_provider = '04'
now_datetime = "2024-01-11 11:00:44"
phone_data = prefix+ random_string+ "," + "MOBILE,PORT"+","+phone_number+ ","+origion_provider+","+origion_provider+","+current_provider+","+current_provider+","+ now_datetime
data = "Count of Telephone Numbers:" + str(count_phones) +'\n' + phone_data


# Open the file in write mode
with open("./CCH_broadcast-20240110090000.txt", "w") as file:
    # Write the data to the file
    file.write(data)

print("File exported successfully.")