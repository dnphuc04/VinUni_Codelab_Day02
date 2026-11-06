# 📊 Báo Cáo Chuyên Sâu: Xử Lý Sự Cố Sạc Pin Thực Địa (Xanh SM Smart Dispatching)

## 🏛️ 1. Tổng Quan Dự Án & Bối Cảnh Vận Hành

* **Đơn vị thực hiện:** Vin Smart Future (phối hợp cùng Khối Vận Hành Xanh SM - GSM).
* **Mục tiêu chính:** Xây dựng giải pháp trợ lý AI hỗ trợ Điều phối viên (Dispatcher) tại Trung tâm Điều vận Xanh SM xử lý các tình huống khẩn cấp khi tài xế báo cạn kiệt pin hoặc gặp sự cố sạc pin dọc đường.
* **Tác động mong muốn:** Giảm 80% thời gian xử lý sự cố thực địa, tối ưu hóa thời gian hoạt động của xe điện, và giảm áp lực ca trực cho đội ngũ điều phối viên trong các khung giờ cao điểm tại Hà Nội và TP.HCM.

---

## 🔴 2. Phân Tích Quy Trình Hiện Tại (Current-State Workflow)

Vào giờ cao điểm, các điều phối viên phải tiếp nhận hàng chục cuộc gọi khẩn cấp cùng lúc. Quy trình xử lý thủ công hiện tại kéo dài trung bình **15 phút/lượt**, bao gồm 5 bước:

```text
┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ Bước 1       │     │ Bước 2       │     │ Bước 3       │     │ Bước 4       │
│ Nhận cuộc    │     │ Tra cứu định │     │ Tra cứu trạm │     │ Soạn văn bản │
│ gọi sự cố    │ ──→ │ vị GPS xe    │ ──→ │ sạc VinFast  │ ──→ │ hướng dẫn    │
│              │     │              │     │ còn trụ trống│     │ gửi tài xế   │
│ Ai: Dispatch │     │ Ai: Dispatch │     │ Ai: Dispatch │     │ Ai: Dispatch │
│ ⏱ 2 phút     │     │ ⏱ 2 phút     │     │ ⏱ 5 phút 🔴  │     │ ⏱ 5 phút 🔴  │
│ In: Điện thoại│     │ In: Biển số  │     │ In: Vị trí GPS│     │ In: Raw data │
│ Out: Log sự cố│     │ Out: Toạ độ  │     │ Out: Địa chỉ │     │ Out: SMS     │
└──────────────┘     └──────────────┘     └──────────────┘     └──────────────┘
                                                                      │
                                                                      ▼
                                                               ┌──────────────┐
                                                               │ Bước 5       │
                                                               │ Gọi xe cứu   │
                                                               │ hộ (nếu cần) │
                                                               │ Ai: Dispatch │
                                                               │ ⏱ 1 phút     │
                                                               └──────────────┘
🔴 = Bottlenecks
⏱ Tổng thời gian xử lý thủ công: 15 phút/lượt.
```

### 🎯 Đánh giá Bottlenecks:
* **Bước 3 (Tra cứu trạm sạc):** Mất 5 phút để điều phối viên tra cứu thủ công trụ sạc còn trống phù hợp với loại cổng sạc (CCS2/GBT) của từng dòng xe điện (VF5, VFe34, VF8, VF9).
* **Bước 4 (Soạn tin nhắn hướng dẫn):** Mất 5 phút để viết văn bản chỉ đường chi tiết. Trong lúc căng thẳng, điều phối viên dễ mắc lỗi chọn trạm sạc quá xa hoặc trạm đã hết trụ trống.

---

## 📋 3. Problem Statement & Success Metrics (Chuẩn 6-Field)

| Field | Nội dung chi tiết |
|---|---|
| **1. Actor / Operator** | Điều phối viên (Dispatcher) thuộc Trung tâm Điều vận Xanh SM. |
| **2. Current Workflow** | Khi tài xế báo hết pin, điều phối viên tra cứu vị trí định vị trên bản đồ nội bộ, mở Dashboard trạm sạc VinFast để tìm trụ sạc trống gần nhất, viết tin nhắn chỉ dẫn/định vị gửi qua App tài xế, và gọi cứu hộ nếu pin dưới 5%. 5 bước thủ công, mất 15 phút/lượt. |
| **3. Bottleneck** | Bước 3 & 4 (mất 10 phút): Tra cứu thủ công trụ sạc trống phù hợp với dòng xe và soạn thảo tin nhắn hướng dẫn đường đi chi tiết bằng Tiếng Việt thân thiện. |
| **4. Business Impact** | Mỗi ngày có ~80 sự cố pin thực địa tại Hà Nội. Gây lãng phí 20 giờ làm việc/ngày của team điều vận. Tăng thời gian chờ đợi của tài xế, dẫn đến rò rỉ doanh thu ~15% do xe không thể đón khách và tài xế bị stress. |
| **5. Success Metric** | 1. Giảm tổng thời gian xử lý sự cố từ **15 phút xuống dưới 3 phút** (Efficiency).<br>2. Tỉ lệ hướng dẫn đúng địa điểm và đúng loại trụ sạc phù hợp đạt **98%** (Quality). |
| **6. Operational Boundary** | AI được phép truy xuất API định vị xe, API trạm sạc VinFast trống, tự động soạn thảo tin nhắn hướng dẫn dạng nháp (`[DRAFT_ONLY]`). **CẤM:** AI không được tự động gửi tin đi mà không có điều phối viên phê duyệt (Bắt buộc HITL); không được đề xuất trạm sạc xa quá 5km khi pin xe dưới 5%. |

---

## 🔵 4. Future-State Flow & AI Fit

* **Mức độ AI Fit:** Chọn **LLM Feature** (không dùng Agent tự trị hoàn toàn để phòng tránh rủi ro điều phối sai làm xe chết máy giữa đường).
* **Quy trình tương lai:**

```text
┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ Bước 1       │     │ Bước 2       │     │ Bước 3       │     │ Bước 4       │
│ Nhận cuộc    │     │ 🔵 Auto-pull │     │ 🔵 AI draft  │     │ 🟢 Dispatch  │
│ gọi sự cố    │ ──→ │ vị trí &     │ ──→ │ SMS chỉ dẫn  │ ──→ │ click duyệt  │
│              │     │ trạm sạc trống│    │ & chỉ đường  │     │ & gửi tài xế │
└──────────────┘     └──────────────┘     └──────────────┘     └──────────────┘
                                                                      │
                                                                      ▼
                                                               ↩️ Fallback:
                                                               Nếu AI draft lỗi,
                                                               Dispatcher tự viết
                                                               tay lại như cũ.
```

---

## 🛡️ 5. Technical Boundary Stress-Testing

Bản mẫu `prompt_prototype.py` đã kiểm thử thành công hai ranh giới an toàn then chốt:
1. **Bắt buộc thẻ `[DRAFT_ONLY]`:** Ngăn chặn việc tự động gửi văn bản chưa qua kiểm duyệt con người.
2. **Xử lý Pin Cực Nguy Hại (< 5%):** Khi lượng pin dưới 5%, AI bị cấm đề xuất trạm sạc xa (> 5km) và bắt buộc trả về định dạng JSON kích hoạt xe sạc pin di động:
   `{"action": "dispatch_mobile_charger", "reason": "<explain_why>"}`

---

## 🏁 6. Đánh Giá Readiness & Quyết Định Cuối Cùng

### AI Readiness Checklist:
1. [x] Chúng tôi có sẵn dữ liệu mẫu/logs sạch để test?
2. [x] Rủi ro khi AI sai có nằm trong tầm kiểm soát (qua HITL hoặc Fallback)?
3. [x] Stakeholders sẵn sàng thay đổi quy trình làm việc cũ?

### Quyết định của Ban Giám Đốc Vin Smart Future:
**[x] GO (Bắt đầu xây dựng Prototype)**

**Lý giải quyết định (Justification):**  
Bài toán có mục tiêu rõ ràng, khả thi khi xây dựng dưới dạng LLM Feature. Rủi ro được kiểm soát triệt để nhờ quy trình Human-in-the-loop kết hợp ranh giới an toàn nghiêm ngặt trong Prompt.