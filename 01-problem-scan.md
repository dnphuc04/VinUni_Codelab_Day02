# Phase 1 & Phase 2 Deliverable: Problem Scan & Quick Cards

**Subsidiary context:** Vin Smart Future (Vingroup)  
**Author / Engineer:** AI Product Engineering Team

---

# 🔍 Phase 1 — SCAN: Opportunity Identification

Using the 4 Lenses framework to scan operational workflows across Vingroup subsidiaries:

| # | Subsidiary | Lens | Short Problem Description |
|---|------------|------|---------------------------|
| 1 | **Xanh SM (GSM)** | Lặp lại (Repetitive) | So khớp và phân bổ lại cuốc xe khi khách hàng yêu cầu thay đổi điểm đến/lộ trình giữa chừng qua tổng đài. |
| 2 | **Xanh SM (GSM)** | Tốn thời gian (Time-consuming) | Điều phối viên xử lý thủ công các phản hồi khẩn cấp từ tài xế về sự cố hết pin thực địa (mất 15 min/lượt). |
| 3 | **VinFast** | Lặp lại (Repetitive) | So khớp dữ liệu hóa đơn sạc điện hằng tuần từ các trụ sạc đối tác ngoài với hệ thống thanh toán tự động. |
| 4 | **Vinhomes** | AI-upgrade | Phân loại và định hướng tự động các khiếu nại của cư dân trên App Vinhomes Resident (CSKH cũ xử lý chậm, rập khuôn). |
| 5 | **Vinmec** | Pain từ người khác (Stakeholder Pain) | Bác sĩ mất quá nhiều thời gian viết tóm tắt hồ sơ xuất viện thủ công từ bệnh án điện tử (gây quá tải, phàn nàn nhiều). |

---

# 🃏 Phase 2 — QUICK-ASSESS: 3 Quick Problem Cards

## QUICK PROBLEM CARD #1 (Selected for Deep-Dive)

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                       │
│                                                             │
│ Bài toán: Tài xế Xanh SM báo cáo sự cố hết pin giữa đường   │
│ cần điều phối cứu hộ hoặc tìm trạm sạc trống gần nhất.       │
│ Công ty thành viên: [ ] VinFast  [x] Xanh SM  [ ] Vinhomes  │
│                     [ ] Vinmec   [ ] Khác (Ghi rõ)________  │
│                                                             │
│ Ai đang đau (Actor)? Tài xế (chờ đợi), Điều phối viên (quá tải)│
│                                                             │
│ Workflow thủ công hiện tại (5 bước):                        │
│   1. Tài xế gọi báo sự cố ──> 2. Tra cứu GPS xe ──>         │
│   3. Tìm trụ sạc trống ──> 4. Soạn tin nhắn hướng dẫn ──>   │
│   5. Gọi xe cứu hộ (nếu cần)                                │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 3 & 4 (⏱ 10 phút/lượt)│
│ AI có thể nhảy vào hỗ trợ ở bước nào? Tự động tra cứu trụ sạc│
│ và soạn tin nhắn hướng dẫn dạng nháp (Draft SMS).           │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                        │
│   Giảm thời gian xử lý sự cố từ 15 min ──> dưới 3 min        │
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent │
└─────────────────────────────────────────────────────────────┘
```

## QUICK PROBLEM CARD #2

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                       │
│                                                             │
│ Bài toán: Phân loại và điều phối tự động các yêu cầu, khiếu  │
│ nại của cư dân gửi qua App Vinhomes Resident.               │
│ Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [x] Vinhomes  │
│                     [ ] Vinmec   [ ] Khác (Ghi rõ)________  │
│                                                             │
│ Ai đang đau (Actor)? Ban quản lý tòa nhà, Cư dân            │
│                                                             │
│ Workflow thủ công hiện tại (4 bước):                        │
│   1. Cư dân gửi ticket ──> 2. Nhân viên đọc thủ công nội dung│
│   ──> 3. Xác định bộ phận xử lý ──> 4. Chuyển tiếp ticket   │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2 & 3 (⏱ 30 phút/ticket)│
│ AI có thể nhảy vào hỗ trợ ở bước nào? Đọc hiểu và phân loại  │
│ tự động độ khẩn cấp, gắn nhãn điều hướng đúng bộ phận.       │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                        │
│   Giảm thời gian phân loại ticket từ 30 min ──> dưới 1 min  │
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent │
└─────────────────────────────────────────────────────────────┘
```

## QUICK PROBLEM CARD #3

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                       │
│                                                             │
│ Bài toán: Trích xuất và soạn thảo bản tóm tắt hồ sơ xuất    │
│ viện tự động từ hệ thống bệnh án điện tử cho bác sĩ Vinmec. │
│ Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [ ] Vinhomes  │
│                     [x] Vinmec   [ ] Khác (Ghi rõ)________  │
│                                                             │
│ Ai đang đau (Actor)? Bác sĩ điều trị, Bệnh nhân             │
│                                                             │
│ Workflow thủ công hiện tại (4 bước):                        │
│   1. Mở bệnh án điện tử ──> 2. Tổng hợp kết quả xét nghiệm  │
│   ──> 3. Viết tay/soạn tóm tắt xuất viện ──> 4. Bác sĩ ký   │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2 & 3 (⏱ 25 phút/bệnh nhân)│
│ AI có thể nhảy vào hỗ trợ ở bước nào? Tổng hợp dữ liệu lâm  │
│ sàng và draft sẵn văn bản tóm tắt cho bác sĩ duyệt.         │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                        │
│   Giảm thời gian soạn hồ sơ từ 25 min ──> dưới 5 min        │
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent │
└─────────────────────────────────────────────────────────────┘
```

---

## 🗳️ Selected Card Decision
The team selects **Quick Problem Card #1 (Xanh SM Intelligent Dispatcher)** for Deep-Dive study due to its immediate operational bottleneck in real-time execution and measurable efficiency metrics.