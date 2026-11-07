# 📑 Deep-Dive Report - Vinhomes: Phân loại & điều phối yêu cầu bảo trì cư dân

> **Bài toán được chọn:** Card #3 trong [01-problem-scan.md](01-problem-scan.md) - *Vinhomes · Lens: Lặp lại (Repetitive)*.
>
> *Lưu ý: Các con số về khối lượng, thời gian, tỷ lệ lỗi trong báo cáo là **ước tính giả định** dựa trên quan sát vận hành điển hình của ban quản lý tòa nhà; cần được xác minh bằng log ticket thực tế trong giai đoạn shadow mode (xem Phase 5).*

---

## 🗳️ Lý do chọn bài toán

| Card | Quyết định | Lý do |
|---|---|---|
| **#1 Vinmec - Ghi chú khám bệnh** | Loại (để sau) | Giá trị lớn nhưng rủi ro cao: dữ liệu y tế nhạy cảm, cần đồng ý ghi âm của bệnh nhân, STT tiếng Việt với thuật ngữ y khoa chưa được kiểm chứng, hallucination có thể ảnh hưởng an toàn người bệnh. Cần thẩm định pháp lý và hội đồng y khoa trước. |
| **#2 Xanh SM - Gợi ý điểm đón** | Loại | Đây là bài toán dữ liệu không gian (tọa độ), không phải bài toán ngôn ngữ. Giải pháp phù hợp là Rule (geofence, snap-to-road) + ML truyền thống; dùng LLM là over-engineering. |
| **#3 Vinhomes - Yêu cầu bảo trì** | ✅ **Chọn** | Khối lượng lớn, lặp lại hằng ngày; đầu vào là **văn bản tự do** (đúng thế mạnh của LLM); rủi ro khi AI sai có thể kiểm soát bằng HITL + rule khẩn cấp; dễ pilot phạm vi hẹp. |

---

# 🏗️ Phase 3 - DEEP-DIVE

## 3.1. Current-State Workflow Mapping

Quy trình hiện tại tại quầy lễ tân / CSKH của ban quản lý một tòa nhà Vinhomes:

```text
┌───────────────┐      ┌───────────────┐      ┌───────────────┐      ┌───────────────┐      ┌───────────────┐
│ Bước 1        │      │ Bước 2        │      │ Bước 3        │      │ Bước 4        │      │ Bước 5        │
│ Cư dân gửi    │  🔄  │ Đọc, hỏi lại  │      │ Phân loại &   │  🔄  │ Gọi/nhắn      │  🔄  │ Cập nhật      │
│ yêu cầu       │ ───→ │ thông tin     │ ───→ │ tạo ticket,   │ ───→ │ trưởng bộ phận│ ───→ │ trạng thái    │
│ (App/Hotline/ │      │ thiếu (căn hộ,│      │ chọn bộ phận  │      │ giao việc,    │      │ cho cư dân    │
│ Zalo/Lễ tân)  │      │ vị trí, mô tả)│      │               │      │ chờ xác nhận  │      │               │
│               │      │               │      │               │      │               │      │               │
│ Ai: Cư dân    │      │ Ai: Lễ tân    │      │ Ai: Lễ tân    │      │ Ai: Lễ tân →  │      │ Ai: Lễ tân    │
│               │      │               │      │               │      │ Tổ kỹ thuật   │      │               │
│ ⏱ 3 phút      │      │ ⏱ 5 phút 🔴   │      │ ⏱ 5 phút 🔴   │      │ ⏱ 15 phút 🔴  │      │ ⏱ 2 phút      │
│ In: Văn bản   │      │ In: Tin nhắn  │      │ In: Mô tả đã  │      │ In: Ticket    │      │ In: Xác nhận  │
│ tự do, ảnh    │      │ thô           │      │ làm rõ        │      │               │      │ của tổ KT     │
│ Out: Tin nhắn │      │ Out: Mô tả đủ │      │ Out: Ticket   │      │ Out: Việc đã  │      │ Out: Thông báo│
│               │      │               │      │               │      │ được nhận     │      │ cho cư dân    │
└───────────────┘      └───────────────┘      └───────────────┘      └───────────────┘      └───────────────┘
                                                      │
                                                      ▼  (~15% giao nhầm bộ phận)
                                               ┌───────────────┐
                                               │ ↩️ Tổ KT trả   │
                                               │ lại, lễ tân   │
                                               │ phân loại lại │
                                               │ ⏱ +30–60 phút │
                                               └───────────────┘

🔴 Bottleneck   🔄 Handoff
⏱ Tổng thời gian từ khi nhận yêu cầu đến khi giao đúng bộ phận: ~30 phút/lượt
   (chưa tính các ca giao nhầm và yêu cầu gửi ngoài giờ hành chính phải chờ đến sáng hôm sau).
```

**Phân tích bottleneck:**
- **Bước 2 – 3 (10 phút):** Yêu cầu đến dưới dạng văn bản tự do, mơ hồ ("nhà có mùi khét", "nước yếu từ hôm qua"). Lễ tân phải tự suy luận loại sự cố và mức độ khẩn, thường phải nhắn hỏi lại cư dân.
- **Bước 4 (15 phút):** Handoff qua điện thoại/Zalo, phụ thuộc vào việc trưởng bộ phận có rảnh để nghe máy hay không.
- **Giao nhầm (~15%):** Sự cố giáp ranh (VD: điều hòa chảy nước → bộ phận điều hòa hay bộ phận nước?) bị chuyển qua lại giữa các tổ.

---

## 3.2. Problem Statement (6-field) & Metrics

| Field | Nội dung chi tiết |
|---|---|
| **1. Actor / Operator** | **Operator:** Nhân viên lễ tân / CSKH thuộc Ban quản lý tòa nhà Vinhomes (trực tiếp tiếp nhận và phân loại). **Stakeholder bị ảnh hưởng:** Cư dân (chờ xử lý), các tổ kỹ thuật (điện, nước, thang máy, điều hòa, vệ sinh, an ninh) nhận việc sai hoặc muộn. |
| **2. Current Workflow** | Cư dân gửi yêu cầu qua 4 kênh (App Vinhomes Resident, hotline, nhóm Zalo tòa nhà, quầy lễ tân). Lễ tân đọc nội dung, nhắn hỏi lại nếu thiếu thông tin, tự xác định loại sự cố và mức độ khẩn, tạo ticket trên phần mềm quản lý vận hành, sau đó gọi/nhắn Zalo cho trưởng bộ phận để giao việc và cập nhật lại cho cư dân. 5 bước, hoàn toàn thủ công, trung bình **~30 phút** từ lúc nhận đến lúc giao đúng bộ phận. |
| **3. Bottleneck** | **Bước 2 – 3:** Đọc hiểu văn bản tự do, trích xuất thông tin (căn hộ, vị trí, loại sự cố) và phân loại bộ phận/mức độ khẩn - mất ~10 phút/yêu cầu, sai bộ phận ~15%. **Bước 4:** Handoff thủ công qua điện thoại, chờ trung bình ~15 phút. Đây là bước **cần xử lý ngôn ngữ tự nhiên nhiều nhất**. |
| **4. Business Impact** | Giả định một khu ~10.000 căn hộ nhận **~300 yêu cầu/ngày**. Thời gian xử lý bước 2 – 3 là 300 × 10 phút = **50 giờ công/ngày (~6 FTE)** chỉ để đọc và phân loại. ~45 ticket/ngày bị giao nhầm, mỗi ticket chậm thêm 30 – 60 phút. Sự cố khẩn cấp (kẹt thang máy, rò điện, ngập nước) bị lẫn trong hàng đợi chung, có rủi ro an toàn. Thời gian xử lý chậm là nguyên nhân hàng đầu của đánh giá 1 – 2 sao trên App Resident, ảnh hưởng điểm hài lòng cư dân (CSAT) và uy tín thương hiệu Vinhomes. |
| **5. Success Metric** | **Efficiency:** Thời gian từ nhận yêu cầu → giao đúng bộ phận giảm từ **~30 phút xuống dưới 5 phút** (P90). **Quality:** **≥ 90%** ticket được phân loại đúng bộ phận ngay lần đầu (so với ~85% hiện tại); **≥ 95%** trích xuất đúng mã căn hộ. **Safety:** **100%** sự cố khẩn cấp (thang máy, điện, cháy, ngập, khí gas) được escalate lên hotline trực trong vòng **1 phút**, recall nhóm khẩn cấp **= 100%** (chấp nhận báo động nhầm). **Workload:** Giảm ≥ 60% thời gian lễ tân dành cho phân loại. |
| **6. Operational Boundary** | **AI ĐƯỢC PHÉP:** Đọc nội dung yêu cầu (văn bản, ảnh đính kèm); trích xuất `{căn hộ, vị trí, loại sự cố, mô tả}`; đề xuất bộ phận và mức độ ưu tiên kèm điểm tin cậy; tạo **ticket nháp** (`status = DRAFT`); soạn **nháp** tin nhắn xác nhận đã tiếp nhận cho cư dân. **AI TUYỆT ĐỐI KHÔNG ĐƯỢC:** (1) Cam kết thời gian hoàn thành sửa chữa, chi phí, bồi thường hay miễn phí dịch vụ; (2) Hạ mức ưu tiên hoặc trì hoãn một yêu cầu đã khớp rule khẩn cấp; (3) Tự đóng / hủy ticket; (4) Trả lời các vấn đề phí dịch vụ, tranh chấp, pháp lý - phải chuyển cho nhân viên; (5) Tiết lộ thông tin của cư dân/căn hộ khác; (6) Hướng dẫn cư dân tự sửa thiết bị điện, gas, thang máy. **ĐIỂM CẦN DUYỆT (HITL):** Ticket có confidence < 0.8; mọi ticket khẩn cấp (con người xác nhận *sau* khi rule đã escalate); yêu cầu có phát sinh phí; mọi tin nhắn gửi cư dân trong 4 tuần đầu pilot. |

---

## 3.3. Future-State Flow & AI Fit

### So sánh các phương án (AI-Fit Matrix)

| Tiêu chí | Rule / State-Machine | **LLM Feature** | Agentic Loop |
|---|---|---|---|
| Xử lý văn bản tự do, mơ hồ ("mùi khét", "nước yếu") | ❌ Keyword dễ sót, không hiểu ngữ cảnh | ✅ Hiểu ngữ nghĩa, trích xuất có cấu trúc | ✅ |
| Phát hiện sự cố khẩn cấp | ✅ **Deterministic, recall cao, giải thích được** | ⚠️ Có thể sai, không nên là lớp duy nhất | ⚠️ |
| Chi phí & độ trễ | Rất thấp | Thấp (1 lần gọi/ticket) | Cao (nhiều vòng gọi) |
| Rủi ro hành động sai | Thấp | Thấp (chỉ tạo nháp) | **Cao** (tự gọi API giao việc, nhắn cư dân) |
| Khả năng kiểm thử | Dễ | Trung bình (eval set có nhãn) | Khó |
| Kết luận | Dùng cho **lớp an toàn khẩn cấp** và kênh form có dropdown | ✅ **Dùng cho phân loại & trích xuất** | Không cần - quy trình cố định, không cần lập kế hoạch nhiều bước |

**➡️ Quyết định AI Fit:** `[x] Rule / State-Machine` + `[x] LLM Feature` (hybrid) · `[ ] Agentic Loop`

- **Rule** chạy **trước** LLM: bắt từ khóa khẩn cấp (kẹt thang, rò điện, chập, cháy, khói, ngập, gas…) → escalate ngay, không phụ thuộc LLM.
- **LLM** chỉ làm một việc hẹp: đọc → trả về JSON có cấu trúc → tạo ticket nháp.
- Không dùng Agent vì quy trình có cấu trúc cố định, và việc để AI tự giao việc/nhắn cư dân làm tăng rủi ro mà không tăng nhiều giá trị.

### Future-State Flow

```text
┌───────────────┐      ┌───────────────────┐
│ Bước 1        │      │ Bước 2            │
│ Cư dân gửi    │ ───→ │ ⚙️ RULE: quét từ   │── Khớp khẩn cấp ──→ ┌─────────────────────────┐
│ yêu cầu       │      │ khóa khẩn cấp     │                     │ 🚨 Escalate ngay lên     │
│ (mọi kênh)    │      │ (< 1 giây)        │                     │ hotline trực + tổ KT    │
└───────────────┘      └───────────────────┘                     │ (không chờ LLM)         │
                               │ Không khẩn cấp                    └─────────────────────────┘
                               ▼                                              │
                       ┌───────────────────┐                                  ▼
                       │ Bước 3            │                     🟢 Trực ban xác nhận
                       │ 🔵 LLM: trích xuất │                        sau khi đã điều người
                       │ {căn hộ, vị trí,  │
                       │ loại, bộ phận,    │
                       │ ưu tiên, conf.}   │
                       │ ──→ JSON          │
                       └───────────────────┘
                               │
                 ┌─────────────┴──────────────┐
                 ▼                            ▼
       confidence ≥ 0.8 &               confidence < 0.8 /
       JSON hợp lệ                      JSON lỗi / thiếu căn hộ /
                 │                      có phát sinh phí
                 ▼                            │
       ┌───────────────────┐                  ▼
       │ Bước 4            │        ┌───────────────────┐
       │ 🔵 Tạo ticket nháp │        │ ↩️ FALLBACK:       │
       │ + nháp tin xác    │        │ Đưa vào hàng đợi  │
       │ nhận cho cư dân   │        │ "Cần xem xét",    │
       └───────────────────┘        │ lễ tân phân loại  │
                 │                  │ thủ công như cũ   │
                 ▼                  └───────────────────┘
       ┌───────────────────┐                  │
       │ Bước 5            │ ←────────────────┘
       │ 🟢 Lễ tân review   │
       │ 1-click duyệt /   │
       │ sửa bộ phận       │
       └───────────────────┘
                 │
                 ▼
       ┌───────────────────┐      ┌───────────────────┐
       │ Bước 6            │      │ Bước 7            │
       │ Hệ thống tự đẩy   │ ───→ │ Gửi tin xác nhận  │
       │ ticket vào queue  │      │ cho cư dân        │
       │ của bộ phận       │      │ (đã duyệt)        │
       └───────────────────┘      └───────────────────┘

🔵 AI Step   🟢 Human Step (HITL)   ↩️ Fallback   ⚙️ Rule (deterministic)

⏱ Thời gian dự kiến: ~10 giây (AI) + ~1 phút (lễ tân duyệt) + đẩy queue tự động ≈ dưới 5 phút/lượt.
```

### Cơ chế Fallback

| Tình huống lỗi | Cách xử lý |
|---|---|
| LLM API timeout / lỗi | Ticket vào hàng đợi "Cần xem xét", lễ tân xử lý thủ công như quy trình cũ. Không mất yêu cầu nào. |
| JSON trả về không đúng schema | Retry 1 lần; vẫn lỗi → hàng đợi thủ công. |
| Confidence < 0.8 hoặc thiếu mã căn hộ | Không tạo ticket tự động; hiển thị gợi ý của AI làm tham khảo cho lễ tân. |
| Lễ tân sửa bộ phận AI đề xuất | Ghi log để bổ sung vào eval set và điều chỉnh prompt hàng tuần. |
| Rule khẩn cấp báo nhầm | Chấp nhận (ưu tiên recall); trực ban hủy cảnh báo, ghi log để tinh chỉnh từ khóa. |

---

# 🏁 Phase 5 - EVALUATE

### AI Readiness Checklist

| # | Tiêu chí | Đánh giá | Bằng chứng / Ghi chú |
|---|---|---|---|
| 1 | Chúng tôi có sẵn dữ liệu mẫu/logs sạch để test? | ⚠️ **Một phần** | Phần mềm quản lý vận hành đã lưu lịch sử ticket kèm bộ phận xử lý cuối cùng → có thể dùng làm nhãn. Tuy nhiên tin nhắn Zalo và hotline chưa được lưu tập trung; nhãn có ~15% nhiễu do giao nhầm. Cần gán nhãn lại ~500 mẫu làm eval set. |
| 2 | Rủi ro khi AI sai có nằm trong tầm kiểm soát (qua HITL hoặc Fallback)? | ✅ **Có** | AI chỉ tạo nháp, lễ tân duyệt 100% trong pilot; sự cố khẩn cấp do Rule xử lý độc lập với LLM; lỗi LLM → quay về quy trình thủ công, không mất yêu cầu. |
| 3 | Stakeholders sẵn sàng thay đổi quy trình làm việc cũ? | ⚠️ **Cần xác nhận** | Lễ tân được giảm tải nên có động lực; các tổ kỹ thuật cần chuyển từ nhận việc qua Zalo sang nhận qua queue của hệ thống - cần trưởng ban quản lý tòa nhà cam kết. |

### Quyết định cuối cùng của Ban Giám Đốc Vin Smart Future

[x] **GO (Bắt đầu xây dựng Prototype):** Bắt đầu phát triển với scope hẹp.
[ ] **NOT YET (Cần tích lũy thêm dữ liệu/xác lập baseline):** Trì hoãn để chuẩn bị thêm.
[ ] **NO-GO (Không khả thi / Rule-based tốt hơn):** Hủy bỏ dự án AI này.

**Justification:**

> **GO với scope hẹp, có điều kiện.**
>
> **Vì sao GO:**
> 1. **Đúng bài toán cho LLM:** Bottleneck nằm ở việc đọc hiểu văn bản tự do, mơ hồ - rule-based thuần không xử lý được ("nhà có mùi khét" có thể là điện hoặc gas), trong khi đây là thế mạnh của LLM.
> 2. **Rủi ro kiểm soát được:** Kiến trúc hybrid tách biệt lớp an toàn (Rule khẩn cấp, deterministic) khỏi lớp phân loại (LLM). AI chỉ tạo nháp, con người duyệt, fallback về đúng quy trình cũ khi có lỗi.
> 3. **Chi phí thấp, lợi ích đo được:** Mỗi ticket chỉ cần 1 lần gọi LLM (Gemini 2.5 Flash), ước tính 300 ticket/ngày × ~1.000 token ≈ chi phí API không đáng kể so với ~6 FTE đang dành cho phân loại. Metric rõ ràng (thời gian giao việc, tỷ lệ đúng bộ phận) và đã có baseline từ hệ thống ticket.
>
> **Scope pilot (giai đoạn 1 - 6 tuần):**
> - Chỉ **1 tòa nhà**, chỉ **kênh App Resident + Zalo** (văn bản tự do).
> - **Tuần 1 – 2: Shadow mode** - AI chạy song song, lễ tân vẫn làm thủ công; so sánh kết quả để xác lập baseline thực và đo accuracy.
> - **Tuần 3 – 6:** Bật HITL 1-click, đo các Success Metric.
>
> **Điều kiện dừng (kill criteria):** Sau shadow mode, nếu accuracy phân loại < 85% hoặc có **bất kỳ** sự cố khẩn cấp nào bị sót → dừng mở rộng, quay lại cải thiện Rule/prompt.
>
> **Ngoài scope:** Kênh hotline (cần Speech-to-Text, để giai đoạn 2), mọi câu hỏi về phí dịch vụ/tranh chấp, tự động giao việc không qua duyệt.
