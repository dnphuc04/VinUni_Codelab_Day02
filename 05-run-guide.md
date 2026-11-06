# Hướng dẫn chạy bài nộp

## Thiết lập

Chạy tại thư mục gốc repository bằng PowerShell:

```powershell
.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Nếu chưa có `.venv`, tạo bằng Python đã cài: `python -m venv .venv`.

Tạo tệp `.env` tại thư mục gốc, nội dung `GEMINI_API_KEY=YOUR_KEY`.
Tệp này đã được `.gitignore` loại trừ; không commit key.

## Chạy prototype thật

```powershell
.venv\Scripts\python.exe starter-code\prompt_prototype.py --report evidence\gemini-results.json
```

Mặc định dùng Gemini 3.1 Flash Lite và 3 ca tấn công bắt buộc. Gemini 2.5 Flash trong đề bài trả lỗi 404 cho tài khoản này. Có thể đổi bằng biến môi trường GEMINI_MODEL. Thêm `--full` để chạy cả 9 ca. Chạy tuần tự để giảm lỗi hạn mức 429.
Chỉ báo `Passed` khi có output API thật và vượt kiểm tra. API lỗi hoặc output không đạt sẽ trả mã thoát 1; fallback không tính là thành công của mô hình.
Có thể phát sinh chi phí API theo tài khoản. Dữ liệu gửi đi là fixture giả lập trong code.

## Kiểm tra

```powershell
.venv\Scripts\python.exe -m pytest -q tests
.venv\Scripts\python.exe autograder\autograder.py
```

Autograder gọi API lần nữa và có timeout tổng 30 giây. Chất lượng mạng hoặc hạn mức API có thể ảnh hưởng kết quả; không đổi timeout hoặc làm giả output để vượt kiểm tra.
22 test cục bộ dùng mock cho lỗi API, không thay thế thử nghiệm Gemini.

## Phạm vi thiết kế

Đầu vào `verified_context` phải do người vận hành xác minh; `driver_message` là dữ liệu không đáng tin cậy. Prototype mô phỏng phần soạn nháp sau xác minh; chưa thực hiện đầy đủ hai giai đoạn LLM trong future flow. Không kết nối công cụ gửi tin/điều xe. Kiểm tra nội dung ngôn ngữ cuối cùng thuộc người duyệt.

## Nộp bài

- Nhánh cá nhân: 3 file báo cáo, sơ đồ PNG, code, tests và bằng chứng chạy thật nếu đã tạo.
- Nhóm tổng hợp báo cáo và sơ đồ vào main; không merge bài code cá nhân vào main.
- Chỉ trưởng nhóm điền form theo README.
- NOT YET là quyết định scoping hiện tại; không đồng nghĩa được bỏ phần chạy prototype bắt buộc.

SDK tham chiếu: https://googleapis.github.io/python-genai/
