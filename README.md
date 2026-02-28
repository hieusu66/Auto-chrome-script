Auto Chrome Script GUI
📋 Tổng quan
Auto Chrome Script GUI là công cụ tự động hóa Chrome bằng Python, cho phép tạo và chạy các script tự động với giao diện đồ họa thân thiện. Ứng dụng hỗ trợ đa luồng, quản lý profile, tìm kiếm bằng hình ảnh, và nhiều tính năng mạnh mẽ khác.

✨ Tính năng chính
🤖 Tự động hóa Chrome
Tạo script với nhiều hành động đa dạng

Chạy đa luồng với nhiều profile cùng lúc

Hỗ trợ chế độ headless (ẩn Chrome)

Tự động đóng Chrome sau khi hoàn thành

🖱️ Các hành động hỗ trợ
Mở URL

Click bằng XPath

Gửi ký tự vào ô input

Click Full XPath (JavaScript)

Tìm kiếm và click bằng hình ảnh

Chụp màn hình tạo template

Swipe màn hình

Thực thi mã Python tùy chỉnh

Click Random XPath từ nhiều nhóm khác nhau

🎯 Random XPath Groups
Nhóm 1: Click 1 XPath ngẫu nhiên

Nhóm 2: Click 2 XPath ngẫu nhiên

Nhóm 3: Click 3 XPath ngẫu nhiên

Nhóm 5: Click 5 XPath ngẫu nhiên

Nhóm 10: Click 10 XPath ngẫu nhiên

Nhóm Custom: Click số lượng tùy chỉnh

📊 Dashboard thông minh
Hiển thị số luồng đang chạy

Thống kê số bước script

Đếm số profiles và tài khoản

Trạng thái hệ thống

🪟 Sắp xếp cửa sổ
Tự động sắp xếp cửa sổ Chrome thành lưới

Cấu hình số cột, số hàng, khoảng cách

Tự động sắp xếp khi chạy script

👥 Quản lý tài khoản
Tải tài khoản từ file text

Tự động load file account.txt

Hỗ trợ nhiều định dạng tài khoản

🌐 Đa ngôn ngữ
Tiếng Việt

English

🎨 Giao diện
Hỗ trợ theme sáng/tối

Giao diện hiện đại với ttkbootstrap

Nút floating action button tiện lợi

📦 Yêu cầu hệ thống
Python Packages
text
selenium
ttkbootstrap
opencv-python
pyautogui
pillow
numpy
sympy
pyperclip
undetected-chromedriver (tùy chọn)
Khác
Chrome browser

ChromeDriver (tự động cài hoặc tải thủ công)

🚀 Hướng dẫn cài đặt
1. Clone repository
bash
git clone https://github.com/hieusu66/Auto-chrome-script.git
cd auto-chrome-script
2. Cài đặt packages
bash
pip install selenium ttkbootstrap opencv-python pyautogui pillow numpy sympy pyperclip undetected-chromedriver
3. Cấu trúc thư mục
text
auto-chrome-script/
├── main.py
├── chromedriver.exe (tự động tải)
├── chromeinstall.py (cài đặt ChromeDriver)
├── updateclient.py (cập nhật ứng dụng)
├── account.txt (danh sách tài khoản)
├── settings.txt (cấu hình)
├── xpath_groups.json (lưu nhóm XPath)
├── profiles/ (thư mục chứa Chrome profiles)
├── image_templates/ (thư mục chứa template hình ảnh)
├── script/ (thư mục chứa script)
└── log.txt (file log)
📖 Hướng dẫn sử dụng
Tạo script mới
Chuyển sang tab "⚙️ Thêm bước & Cài đặt"

Chọn hành động từ dropdown

Nhập giá trị tương ứng

Nhấn "➕ Thêm bước"

Ví dụ script đăng nhập Google
text
Bước 1: Mở URL | https://accounts.google.com
Bước 2: Gửi ký tự (XPath|Text) | //*[@id="identifierId"]|email@gmail.com
Bước 3: Click XPath | //*[@id="identifierNext"]/div/button
Bước 4: Ngủ | 2
Bước 5: Gửi ký tự (XPath|Text) | //input[@name="Passwd"]|password
Bước 6: Click XPath | //*[@id="passwordNext"]/div/button
Bước 7: Ngủ | 5
Quản lý Random XPath
Nhấn nút "XPath Random" trong tab Settings

Chọn nhóm cần thêm XPath (1, 2, 3, 5, 10, Custom)

Nhấn "➕ Thêm XPath" và nhập XPath

Sử dụng trong script với các hành động click random tương ứng

Chạy script
Cấu hình số luồng, kích thước Chrome

Bật/tắt các tùy chọn (headless, tự động tạo profile...)

Nhấn "▶️ CHẠY SCRIPT" hoặc nút floating đỏ

Sắp xếp cửa sổ
Chuyển sang tab "🪟 Sắp xếp cửa sổ"

Nhập số cột, số hàng, khoảng cách

Bật "Tự động sắp xếp khi chạy script" nếu muốn

Nhấn "Sắp xếp ngay" để sắp xếp thủ công

🛠️ Cấu hình nâng cao
File account.txt
text
email|password|fullname
user1@gmail.com|pass123|Nguyễn Văn A
user2@gmail.com|pass456|Trần Thị B
File settings.txt
text
threads=3
width=1200
height=800
auto_create_profiles=True
delete_profiles_after_run=False
language=vi
auto_load_accounts=True
theme=darkly
arrange_auto=True
arrange_columns=3
arrange_rows=2
arrange_gap=10
Mã Python tùy chỉnh
python
# Ví dụ: Tính toán và click
x = 5
y = 10
result = x * y
print(f"Kết quả: {result}")
driver.execute_script(f"document.body.style.zoom='{result}%'")
🔧 Xử lý sự cố
ChromeDriver không hoạt động
Nhấn nút "⚙️ Cài Chromedriver" để tự động cài đặt

Hoặc tải thủ công ChromeDriver và đặt cùng thư mục

Không tìm thấy file account.txt
Tạo file account.txt trong thư mục gốc

Hoặc tắt "Tự động tải account.txt" trong cài đặt

Lỗi khi tìm kiếm hình ảnh
Đảm bảo template nằm trong thư mục image_templates

Thử giảm độ chính xác (confidence) xuống 0.7-0.8

📝 Ghi chú
Ứng dụng tự động lưu cài đặt khi thay đổi

Log được ghi vào file log.txt để debug

Profiles được lưu trong thư mục profiles/

Script được lưu dạng JSON trong thư mục script/

🤝 Đóng góp
Mọi đóng góp đều được hoan nghênh! Vui lòng:

Fork repository

Tạo branch mới (git checkout -b feature/AmazingFeature)

Commit changes (git commit -m 'Add some AmazingFeature')

Push to branch (git push origin feature/AmazingFeature)

Mở Pull Request

📄 License
Dự án mã nguồn mở free

📞 Liên hệ
Tác giả: HIEUSU66 & AI
