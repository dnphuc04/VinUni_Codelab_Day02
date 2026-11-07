# 01 — Problem Scan & Quick Cards

## Phase 1 — SCAN

4 Lenses: (1) Lặp lại, (2) Tốn thời gian, (3) AI có thể tốt hơn, (4) Pain từ người khác.

| # | Subsidiary (VinFast/Xanh SM...) | Lens | Mô tả ngắn bài toán |
|---|---|---|---|
| 1 | VinFast | (2) Tốn thời gian | Tra cứu sơ đồ mạch, Datasheet linh kiện và chuẩn đoán mã lỗi hệ thống (DTC) |
| 2 | VinFast | (1) Lặp lại | Viết tài liệu kỹ thuật (Documentation) và comment giải thích code firmware |
| 3 | VinFast | (3) AI có thể tốt hơn | Tự động phân tích log telemetry/cảm biến của xe để phát hiện bất thường sớm |
| 4 | Xanh SM | (4) Pain từ người khác | Kiểm tra & đánh giá độ thoái hóa pin (SoH) dựa trên lịch sử sạc/vận hành |
| 5 | Vinhomes | (2) Tốn thời gian | Phân tích log kết nối các thiết bị IoT/Cảm biến trong đô thị thông minh |

---

## Phase 2 — QUICK-ASSESS

### QUICK PROBLEM CARD #1
- **Bài toán (1 câu):** Tra cứu nhanh sơ đồ mạch và chuẩn đoán mã lỗi (DTC) từ kho Datasheet/Tài liệu kỹ thuật VinFast.
- **Công ty thành viên:** [x] VinFast  [ ] Xanh SM  [ ] Vinhomes  [ ] Vinmec  [ ] Khác: ___
- **Ai đang đau (Actor)?** Kỹ sư R&D Firmware / Kỹ thuật viên bảo trì xưởng dịch vụ
- **Workflow thủ công hiện tại (3-5 bước):**
  1. Đọc mã lỗi từ phần mềm chẩn đoán -> 2. Mở kho tài liệu PDF/Datasheet hàng trăm trang -> 3. Tìm thủ công các trang mô tả chân/mạch liên quan -> 4. Đọc quy trình kiểm tra điện áp/điện trở -> 5. Lập danh sách linh kiện cần thay thế
- **Bước nào tốn thời gian/lỗi nhất?** Bước 2 & 3 (⏱ 30 phút/lượt)
- **AI có thể nhảy vào hỗ trợ ở bước nào?** Tra cứu RAG trên kho Datasheet/Sơ đồ kỹ thuật, trả về trực tiếp nguyên nhân gốc, sơ đồ chân và checklist kiểm tra.
- **Metric thành công (có số):** Giảm thời gian chẩn đoán mã lỗi từ 30 phút xuống 2 phút; chính xác 95%.
- **Quick Architecture:** [ ] No AI  [ ] Rule  [ ] LLM  [x] Agent

---

### QUICK PROBLEM CARD #2
- **Bài toán (1 câu):** Phân tích log cảm biến/telemetry xe điện theo thời gian thực để cảnh báo sự cố phần cứng sớm.
- **Công ty thành viên:** [x] VinFast  [ ] Xanh SM  [ ] Vinhomes  [ ] Vinmec  [ ] Khác: ___
- **Ai đang đau (Actor)?** Kỹ sư Vận hành Hệ thống Telemetry / Bảo trì kỹ thuật
- **Workflow thủ công hiện tại (3-5 bước):**
  1. Đẩy file log dữ liệu thô (tần suất cao) về máy chủ -> 2. Lọc và vẽ đồ thị thủ công -> 3. So sánh các ngưỡng thông số (Nhiệt độ, Dòng điện, Điện áp) -> 4. Phát hiện các điểm bất thường -> 5. Viết báo cáo cảnh báo sự cố
- **Bước nào tốn thời gian/lỗi nhất?** Bước 3 & 4 (⏱ 60 phút/tệp log)
- **AI có thể nhảy vào hỗ trợ ở bước nào?** Tự động phát hiện chuỗi anomaly (bất thường) trong log chuỗi thời gian (time-series) và gắn nhãn mức độ rủi ro.
- **Metric thành công (có số):** Phát hiện sự cố tiềm ẩn sớm trước 48h; giảm 80% thời gian soi log thủ công.
- **Quick Architecture:** [ ] No AI  [ ] Rule  [ ] LLM  [x] Agent

---

### QUICK PROBLEM CARD #3
- **Bài toán (1 câu):** Viết tự động tài liệu hướng dẫn kỹ thuật (Technical Spec) từ mã nguồn Firmware và sơ đồ phần cứng.
- **Công ty thành viên:** [x] VinFast  [ ] Xanh SM  [ ] Vinhomes  [ ] Vinmec  [ ] Khác: ___
- **Ai đang đau (Actor)?** Kỹ sư Phát triển Embedded Firmware
- **Workflow thủ công hiện tại (3-5 bước):**
  1. Đóng gói hoàn tất bản build code -> 2. Review lại từng module/chức năng -> 3. Soạn thảo file mô tả API/Hàm/Luồng dữ liệu -> 4. Format theo mẫu báo cáo kỹ thuật -> 5. Gửi Trưởng nhóm phê duyệt
- **Bước nào tốn thời gian/lỗi nhất?** Bước 3 & 4 (⏱ 120 phút/phiên bản)
- **AI có thể nhảy vào hỗ trợ ở bước nào?** Đọc codebase/struct/comments để tự động sinh file tài liệu Markdown/Doc theo chuẩn định dạng quy định.
- **Metric thành công (có số):** Tiết kiệm 90% thời gian viết tài liệu kỹ thuật; đảm bảo 100% tài liệu đồng bộ với code.
- **Quick Architecture:** [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent
