import os

print(f"Thư mục đang đứng: {os.getcwd()}")

file_path = os.path.join("..", "data", "raw", "students.csv")
abs_path = os.path.abspath(file_path)

print(f"Đường dẫn tuyệt đối: {abs_path}")
print(f"Kiểm tra file tồn tại: {os.getcwd() and os.path.exists(abs_path)}")