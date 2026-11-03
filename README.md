# DỰ ÁN: TỪ DỮ LIỆU ĐẾN PHÂN TÍCH VỚI PYTHON
- **Họ và tên:** Hồ Văn Khương
- **MSSV:** 2311553770

## Trả lời câu hỏi thu hoạch
- **Câu 1:** Chuỗi tiếng Anh sử dụng mã ASCII (0–127) nên chỉ tốn 1 byte/ký tự khi mã hóa UTF-8. Chuỗi tiếng Việt có dấu thuộc dải mở rộng của Unicode, UTF-8 dùng mã hóa độ dài biến thiên (variable-length) nên tốn từ 2 đến 3 bytes cho mỗi ký tự có dấu.
- **Câu 2:** CSV chỉ thích hợp cho dữ liệu bảng 2 chiều (hàng/cột) đơn giản. JSON linh hoạt hỗ trợ cấu trúc dữ liệu lồng nhau dạng đối tượng/mảng. Khi dữ liệu phân cấp lồng nhau (nested), ta nên dùng định dạng JSON.
- **Câu 3:** Mở file ảnh bằng Notepad sẽ xuất hiện các ký tự lỗi font, kỳ lạ và vô nghĩa. Do file ảnh là file nhị phân (binary file) lưu trữ điểm ảnh, còn Notepad là trình soạn thảo văn bản thuần (text editor) cố giải mã các byte nhị phân thành ký tự chữ.
- **Câu 4:** Tách data/raw/ để giữ nguyên bản dữ liệu gốc (chế độ chỉ đọc), bảo đảm tính toàn vẹn và khả năng tái lập phân tích. Dữ liệu đã làm sạch lưu tại data/processed/. File .gitignore loại bỏ các file tạm/rác (__pycache__, cache notebook), giữ repository gọn nhẹ.
- **Câu 5:** Điểm GPA trung bình của nhóm sinh viên là 3.56; sinh viên có GPA cao nhất là Vu Hai Yen (3.9), thấp nhất là Le Van C (3.1). Mặt bằng chung điểm số tương đối đồng đều ở mức khá - giỏi.