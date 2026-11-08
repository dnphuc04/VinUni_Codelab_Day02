# 📑 Deep-Dive Report - Bài toán: AI Medication Reminder Assistant – Trợ lý AI nhắc nhở và theo dõi việc sử dụng thuốc

**Lý do lựa chọn bài toán**: Dựa trên painpoint của người bệnh khi thường xuyên quên uống thuốc làm ảnh hưởng đến quá trình điều trị bệnh.
Lưu ý: Mọi số liệu được đưa ra trong bài toán đều là dữ liệu giả định.
## 3.1. Current-State Workflow

┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ Bước 1       │     │ Bước 2       │     │ Bước 3       │
│ Khám bệnh và │     │ Nhận đơn     │     │ Tự thiết lập │
│ được kê đơn  │ ──→ │ thuốc từ     │ ──→ │ lịch uống    │
│              │     │ bác sĩ       │     │ thuốc        │
│ Ai: Bác sĩ   │     │ Ai: Bệnh nhân│     │ Ai: Bệnh nhân│
│ In: Triệu chứng│   │ In: Đơn thuốc│     │ ⏱ Thủ công   │
│ Out: Chỉ định│     │ Out: Thuốc,  │     │ Out: Lịch cá  │
│ điều trị     │     │ liều, cách dùng│   │ nhân (nếu có)│
└──────────────┘     └──────────────┘     └──────────────┘
                                                    │
                                                    ▼
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ Bước 6       │     │ Bước 5       │     │ Bước 4       │
│ Tái khám và  │     │ Xử lý khi có │     │ Theo dõi và  │
│ đánh giá     │ ←── │ thắc mắc hoặc│ ←── │ ghi nhớ việc │
│ điều trị     │     │ vấn đề       │     │ uống thuốc   │
│              │     │              │     │              │
│ Ai: Bác sĩ   │     │ Ai: Bệnh nhân│     │ Ai: Bệnh nhân│
│ In: Lịch sử  │     │ In: Câu hỏi, │     │ ⏱ Liên tục   │
│ điều trị     │     │ triệu chứng  │     │ Out: Tình trạng│
│ Out: Đánh giá│     │ Out: Tư vấn  │     │ dùng thuốc   │
└──────────────┘     └──────────────┘     └──────────────┘

🔴 = Bottlenecks tiềm năng: Bước 3, 4 và 5.

## 3.2. Problem Statement (6-field) — AI Medication Reminder Assistant


## 3.2. Problem Statement (6-field)

| **Field** | **Nội dung chi tiết** |
|---|---|
| **1. Actor / Operator** | Bệnh nhân ngoại trú và bệnh nhân sau xuất viện tại hệ thống bệnh viện Vinmec. Các bên liên quan gồm bác sĩ điều trị, dược sĩ lâm sàng và điều dưỡng phụ trách hướng dẫn sử dụng thuốc. |
| **2. Current Workflow** | Bác sĩ thăm khám và kê đơn thuốc trên hệ thống bệnh án điện tử (EMR) -> bệnh nhân nhận đơn thuốc và hướng dẫn sử dụng -> bệnh nhân tự ghi nhớ hoặc thiết lập nhắc nhở trên điện thoại -> đến thời điểm uống thuốc, bệnh nhân kiểm tra đơn và tự uống thuốc -> tự ghi nhớ hoặc ghi chép lại tình trạng đã uống/bỏ lỡ liều -> liên hệ bệnh viện nếu có thắc mắc về việc sử dụng thuốc. Quy trình phụ thuộc phần lớn vào khả năng ghi nhớ và tính chủ động của bệnh nhân. Công cụ: EMR, đơn thuốc giấy/điện tử, điện thoại, ứng dụng báo thức hoặc ghi chú cá nhân. |
| **3. Bottleneck** | **Bước 3–5:** Bệnh nhân phải tự chuyển thông tin từ đơn thuốc thành lịch uống thuốc và duy trì việc tuân thủ trong suốt quá trình điều trị. Đặc biệt, các đơn thuốc có nhiều loại thuốc, thời điểm uống khác nhau hoặc yêu cầu trước/sau ăn khiến việc thiết lập và ghi nhớ trở nên phức tạp. Bệnh nhân có thể quên liều, uống sai thời điểm, không ghi nhận tình trạng đã uống thuốc hoặc không biết cách xử lý khi bỏ lỡ liều. Các ứng dụng nhắc nhở thông thường chủ yếu gửi thông báo theo lịch cố định, chưa hỗ trợ giải thích hướng dẫn sử dụng thuốc dựa trên đơn kê và tài liệu y khoa đã được xác thực. |
| **4. Business Impact** | Việc bệnh nhân không tuân thủ phác đồ điều trị có thể làm giảm hiệu quả điều trị, tăng nguy cơ xảy ra sai sót trong sử dụng thuốc và phát sinh nhu cầu liên hệ tư vấn với nhân viên y tế. Điều này làm tăng khối lượng công việc hành chính và tư vấn lặp lại cho điều dưỡng, dược sĩ và bộ phận chăm sóc khách hàng. Đồng thời, trải nghiệm chăm sóc sau khám và sau xuất viện chưa được duy trì liên tục. **Ước tính (giả định):** Nếu một điều dưỡng dành 5 phút/ngày để hỗ trợ nhắc nhở và giải đáp các câu hỏi lặp lại cho mỗi bệnh nhân, với 20 bệnh nhân/ngày, tổng thời gian có thể lên tới 100 phút/ngày/điều dưỡng. |
| **5. Success Metric** | 1. **Efficiency:** Giảm ít nhất 80% thời gian bệnh nhân cần để thiết lập lịch nhắc uống thuốc từ đơn thuốc đã kê.<br>2. **Adherence:** Tăng tỷ lệ bệnh nhân xác nhận đã uống thuốc đúng lịch so với giai đoạn trước khi triển khai (đo bằng tỷ lệ xác nhận liều uống đúng giờ).<br>3. **Accuracy & Safety:** Độ chính xác trích xuất thông tin thuốc (tên thuốc, liều lượng, tần suất, thời điểm uống) đạt ít nhất 99% trên bộ đơn thuốc kiểm thử được chuyên gia y tế xác nhận.<br>4. **Traceability:** 100% thông tin tư vấn liên quan đến thuốc phải truy xuất được nguồn từ đơn kê hoặc tài liệu y khoa đã được Vinmec phê duyệt.<br>5. **Engagement:** Theo dõi tỷ lệ thông báo được gửi thành công, tỷ lệ bệnh nhân phản hồi và tỷ lệ hoàn thành liều uống theo lịch. |
| **6. Operational Boundary** | **AI được phép:** Đọc (read-only) đơn thuốc điện tử đã được xác thực; trích xuất tên thuốc, liều lượng, tần suất, thời điểm và hướng dẫn sử dụng; tự động tạo lịch nhắc uống thuốc theo đúng đơn kê; gửi thông báo tại thời điểm đã thiết lập; cho phép bệnh nhân xác nhận đã uống, chưa uống hoặc bỏ lỡ liều; cung cấp thông tin hướng dẫn sử dụng thuốc dựa trên tài liệu y khoa được Vinmec phê duyệt; tổng hợp báo cáo tuân thủ thuốc để nhân viên y tế theo dõi.<br><br>**CẤM:** Tự ý thay đổi tên thuốc, liều lượng, tần suất hoặc thời gian sử dụng so với đơn kê; tự đề xuất tăng/giảm liều hoặc thay thế thuốc; tự đưa ra quyết định uống bù khi bệnh nhân quên liều; tự chẩn đoán hoặc đưa ra kết luận về tác dụng phụ; tự ý sửa đổi đơn thuốc hoặc hồ sơ bệnh án; tự khẳng định thông tin khi không có nguồn đáng tin cậy.<br><br>**Cần duyệt:** Mọi thay đổi lịch uống thuốc có liên quan đến thay đổi chỉ định điều trị phải được bác sĩ/dược sĩ xác nhận. Trường hợp phát hiện thông tin đơn thuốc không rõ ràng, có khả năng trùng lặp hoặc mâu thuẫn, hệ thống phải chuyển cho nhân viên y tế xác minh trước khi kích hoạt lịch nhắc. Khi bệnh nhân báo cáo dấu hiệu bất thường hoặc phản ứng có hại của thuốc, AI cần hướng dẫn liên hệ nhân viên y tế hoặc cấp cứu phù hợp, không tự xử lý thay chuyên gia. |

## 3.3. Future-State Flow & AI Fit


┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ Bước 1       │     │ Bước 2       │     │ Bước 3       │     │ Bước 4       │
│ Bác sĩ kê    │     │ 🔵 Auto-pull │     │ 🔵 AI extract│     │ 🟢 Confirm   │
│ đơn thuốc    │ ──→ │ đơn thuốc từ │ ──→ │ thông tin &  │ ──→ │ nhân viên y tế│
│ trên EMR     │     │ hệ thống EMR │     │ tạo lịch nhắc│     │ xác nhận lịch│
└──────────────┘     └──────────────┘     └──────────────┘     └──────────────┘
                                                                  │
                                                                  ▼
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ Bước 7       │     │ Bước 6       │     │ Bước 5       │
│ 🟢 Theo dõi  │     │ 🔵 LLM giải  │     │ 🔵 Auto-send │
│ tuân thủ &   │ ←── │ đáp câu hỏi  │ ←── │ thông báo    │
│ báo cáo      │     │ về thuốc     │     │ nhắc uống thuốc│
└──────────────┘     └──────────────┘     └──────────────┘
       │
       ▼
  ↩️ Fallback:
  Nếu không đọc được đơn thuốc, thiếu thông tin liều lượng
  hoặc phát hiện dữ liệu mâu thuẫn:
  Hệ thống không tự tạo lịch nhắc, chuyển cho bác sĩ/
  dược sĩ xác minh và thiết lập thủ công.

  Nếu bệnh nhân quên liều hoặc báo cáo phản ứng bất thường:
  AI không tự đề xuất uống bù hay thay đổi liều,
  hướng dẫn liên hệ nhân viên y tế để được tư vấn.

# 🏁 Phase 5 — EVALUATE


## AI Readiness Checklist

1. [ ] **Dữ liệu mẫu/logs sạch:** Cần chuẩn bị đơn thuốc điện tử đã ẩn danh và bộ dữ liệu chuẩn (Ground Truth) được bác sĩ/dược sĩ xác nhận để kiểm thử độ chính xác của AI.
2. [x] **Kiểm soát rủi ro:** Có thể kiểm soát thông qua Rule-based Validation, Human-in-the-loop (HITL) và cơ chế Fallback. AI không được tự ý thay đổi liều lượng hoặc quyết định điều trị.
3. [ ] **Stakeholders sẵn sàng:** Cần có sự đồng thuận của bác sĩ, dược sĩ, điều dưỡng và bộ phận CNTT về quy trình vận hành mới.

## Quyết định cuối cùng của Ban Giám Đốc Vinmec

**Đề xuất: GO có điều kiện**

- [x] **GO (Bắt đầu xây dựng Prototype):** Phát triển MVP với phạm vi giới hạn.

### Justification (Lý giải quyết định)

Đề xuất **GO có điều kiện** vì bài toán có tính khả thi về kỹ thuật và giá trị thực tiễn trong việc cải thiện tuân thủ điều trị, giảm gánh nặng cho bệnh nhân và bác sĩ, điều dưỡng.

- **Technical Feasibility:** Đơn thuốc điện tử cung cấp dữ liệu đầu vào tương đối có cấu trúc. Có thể kết hợp OCR/LLM để trích xuất thông tin, Rule-based Engine để kiểm tra dữ liệu và thiết lập lịch nhắc, LLM + RAG để giải đáp câu hỏi về thuốc.
- **Risk Control:** AI chỉ hỗ trợ nhắc thuốc và cung cấp thông tin, không tự thay đổi liều lượng hay đưa ra quyết định điều trị. Các trường hợp bất thường phải chuyển cho nhân viên y tế.
- **Cost Efficiency:** Sử dụng Hybrid AI (LLM + Rule-based Automation) giúp hạn chế số lần gọi LLM, giảm chi phí API và dễ dàng mở rộng.
- **Prototype Scope:** Thử nghiệm trên nhóm bệnh nhân có đơn thuốc điện tử rõ ràng, tập trung vào trích xuất đơn thuốc, tạo lịch nhắc, gửi thông báo và theo dõi phản hồi.

**Kết luận:** Cho phép xây dựng Prototype trong môi trường kiểm thử. Chỉ triển khai thực tế sau khi xác nhận chất lượng dữ liệu, sự đồng thuận của stakeholders và hoàn tất đánh giá an toàn y khoa, bảo mật.
