# 🔍 Phase 1 - SCAN (Cá nhân, 20 min)

**Hình thức:** Báo cáo nhóm — Lab 02

**Nguồn bài được chọn:** Nguyễn Hoa Thanh Tùng — nhánh `nguyenhoathanhtung` ([bài gốc](https://github.com/dnphuc04/VinUni_Codelab_Day02/tree/25ef9df)).

**Đại diện tổng hợp:** Đồng Ngọc Phúc — 2A202603399.

> Code Python vẫn được chấm riêng trên nhánh cá nhân. Kết quả thử nghiệm Xanh SM trong AI log không phải bằng chứng đạt KPI phân loại bảo trì Vinhomes.


### 📝 List bài toán của tôi:
| # | Subsidiary (VinFast/Xanh SM...) | Lens | Mô tả ngắn bài toán |
|---|----------------------------------|------|---------------------|
| 1 | Vinmec | Tốn thời gian (Time-consuming) | Dùng AI Speech-to-Text + LLM chuyển nội dung trao đổi bác sĩ – bệnh nhân thành bản nháp ghi chú khám bệnh, giảm thời gian nhập liệu cho bác sĩ. |
| 2 | Xanh SM | Pain từ người khác (Stakeholder Pain) | Hệ thống gợi ý điểm đón chưa chính xác khiến tài xế đi vòng, khách phải chờ và phát sinh liên hệ hỗ trợ; dùng AI tối ưu gợi ý điểm đón. |
| 3 | VinFast | Tốn thời gian (Time-consuming) | Tự động đọc, trích xuất và đối chiếu hồ sơ bảo hành, phiếu sửa chữa, hóa đơn phụ tùng (OCR + LLM) để rút ngắn thời gian xét duyệt yêu cầu bảo hành. |
| 4 | Vinhomes | Lặp lại (Repetitive) | Tự động tiếp nhận, phân loại và chuyển tiếp yêu cầu bảo trì của cư dân (thang máy, điện nước, điều hòa, vệ sinh) đến đúng bộ phận phụ trách. |
| 5 | Xanh SM | AI có thể tốt hơn (AI-upgrade) | Nâng cấp CSKH bằng AI Copilot + RAG để tra cứu chính sách, giải đáp câu hỏi và đề xuất phản hồi khiếu nại nhanh, chính xác hơn. |

# 🃏 Phase 2 - QUICK-ASSESS (Cá nhân, 30 min)

> Chọn bài #1 (Vinmec), #2 (Xanh SM), #4 (Vinhomes) từ danh sách Phase 1.
> *Các con số thời gian/tỷ lệ là **ước tính giả định** để đặt baseline, cần xác minh bằng log thực tế ở Phase 3.*

### Card #1 - Vinmec: Ghi chú khám bệnh tự động

```
┌─────────────────────────────────────────────────────────────
│ QUICK PROBLEM CARD #1
│
│ Bài toán (1 câu): Bác sĩ ngoại trú mất nhiều thời gian gõ ghi chú
│   khám bệnh vào EMR, làm giảm thời gian tương tác với bệnh nhân.
│ Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [ ] Vinhomes
│                     [x] Vinmec   [ ] Khác
│
│ Ai đang đau (Actor)? Bác sĩ khám ngoại trú (chính); bệnh nhân
│   (bị bác sĩ "nhìn màn hình" thay vì nhìn mình, chờ lâu hơn).
│
│ Workflow thủ công hiện tại:
│   1. Hỏi bệnh, khám lâm sàng
│   ──> 2. Ghi nhanh ra giấy / ghi nhớ trong đầu
│   ──> 3. Gõ lý do khám, triệu chứng, tiền sử, chẩn đoán vào EMR/HIS
│   ──> 4. Chỉ định xét nghiệm, kê đơn
│   ──> 5. Rà soát, ký xác nhận hồ sơ
│
│ Bước nào tốn thời gian/lỗi nhất? Bước 3 - gõ ghi chú
│   (⏱ ~5–7 phút/lượt trên ca khám ~15 phút; dễ thiếu thông tin
│   khi dồn cuối ca).
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 1–3: Speech-to-Text
│   ghi lại hội thoại (có đồng ý của bệnh nhân) ──> LLM tạo bản nháp
│   ghi chú theo cấu trúc SOAP ──> bác sĩ review, sửa, ký.
│   AI KHÔNG chẩn đoán, KHÔNG kê đơn.
│
│ Đo thành công bằng gì (Metric có số)?
│   - Giảm thời gian nhập ghi chú từ ~6 phút ──> dưới 2 phút/lượt
│   - ≥ 85% bản nháp được bác sĩ chấp nhận với ≤ 3 chỗ sửa
│   - 0 trường hợp ghi chú chứa thông tin không có trong hội thoại
│     (hallucination) lọt qua bước ký duyệt
│
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent
│   (STT + LLM tóm tắt có cấu trúc; bác sĩ luôn duyệt - HITL bắt buộc)
└─────────────────────────────────────────────────────────────
```

**Tự phản biện:** Rủi ro lớn nhất là hallucination và bảo mật dữ liệu y tế (ghi âm, lưu trữ); STT tiếng Việt với thuật ngữ y khoa có thể sai. Rule-based (template/macro điền sẵn) giải quyết được một phần cho ca bệnh lặp lại, nhưng không xử lý được hội thoại tự do → LLM có lý do tồn tại.

---

### Card #2 - Xanh SM: Gợi ý điểm đón chính xác

```
┌─────────────────────────────────────────────────────────────
│ QUICK PROBLEM CARD #2
│
│ Bài toán (1 câu): Điểm đón gợi ý theo GPS của khách thường sai
│   (trong ngõ, sai cổng tòa nhà, đường cấm dừng) khiến tài xế đi
│   vòng, khách chờ lâu và phát sinh liên hệ hỗ trợ.
│ Công ty thành viên: [ ] VinFast  [x] Xanh SM  [ ] Vinhomes
│                     [ ] Vinmec   [ ] Khác
│
│ Ai đang đau (Actor)? Tài xế Xanh SM (mất thời gian, km rỗng);
│   khách hàng (chờ lâu); nhân viên CSKH (nhận khiếu nại).
│
│ Workflow thủ công hiện tại:
│   1. Khách đặt chuyến, app lấy tọa độ GPS làm điểm đón
│   ──> 2. Tài xế nhận chuyến, chạy theo tọa độ
│   ──> 3. Đến nơi không thấy khách ──> gọi điện / nhắn tin xác nhận
│   ──> 4. Quay đầu, đi vòng sang cổng/đường khác
│   ──> 5. Khách lên xe, hoặc hủy chuyến / gửi khiếu nại CSKH
│
│ Bước nào tốn thời gian/lỗi nhất? Bước 3–4 - xác nhận & đi vòng
│   (⏱ ~3–5 phút/lượt với chuyến bị sai điểm đón).
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 1: khi khách đặt chuyến,
│   "snap" điểm đón về điểm đón hợp lệ gần nhất (cổng tòa nhà, điểm
│   dừng được phép) dựa trên lịch sử điểm đón thành công + dữ liệu
│   bản đồ; hiển thị cho khách xác nhận trước khi gửi tài xế.
│
│ Đo thành công bằng gì (Metric có số)?
│   - Tỷ lệ chuyến phải gọi điện xác nhận điểm đón: ~25% ──> dưới 10%
│   - Thời gian từ tài xế đến nơi ──> khách lên xe: ~4 phút ──> dưới 1.5 phút
│   - Giảm ≥ 30% ticket CSKH liên quan đến điểm đón
│
│ Quick Architecture: [ ] No AI  [x] Rule  [ ] LLM  [ ] Agent
│   (Rule geofence/snap-to-road + mô hình ML clustering điểm đón lịch
│   sử. Dữ liệu là tọa độ, không phải ngôn ngữ ──> LLM KHÔNG phù hợp)
└─────────────────────────────────────────────────────────────
```

**Tự phản biện:** Đây là bài toán dữ liệu không gian, không phải bài toán ngôn ngữ - dùng LLM là over-engineering. Phần lớn giá trị có thể đạt bằng rule (danh sách cổng/điểm dừng hợp lệ) + ML truyền thống. Cần log GPS chuyến đi và log cuộc gọi tài xế–khách để xác lập baseline 25% trước khi cam kết.

---

### Card #3 - Vinhomes: Phân loại & điều phối yêu cầu bảo trì

```
┌─────────────────────────────────────────────────────────────
│ QUICK PROBLEM CARD #3
│
│ Bài toán (1 câu): Yêu cầu bảo trì của cư dân đến từ nhiều kênh,
│   được nhân viên đọc và phân loại thủ công nên chậm giao việc và
│   hay chuyển nhầm bộ phận.
│ Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [x] Vinhomes
│                     [ ] Vinmec   [ ] Khác
│
│ Ai đang đau (Actor)? Nhân viên lễ tân/CSKH ban quản lý tòa nhà
│   (operator); cư dân (chờ xử lý); tổ kỹ thuật (nhận việc sai).
│
│ Workflow thủ công hiện tại:
│   1. Cư dân gửi yêu cầu qua app / hotline / Zalo / lễ tân
│      (văn bản tự do, có thể kèm ảnh)
│   ──> 2. Nhân viên đọc, xác định loại sự cố, vị trí, mức độ khẩn
│   ──> 3. Tạo ticket, chọn bộ phận (điện, nước, thang máy, điều hòa,
│      vệ sinh)
│   ──> 4. Gọi/nhắn trưởng bộ phận giao việc
│   ──> 5. Cập nhật trạng thái cho cư dân
│
│ Bước nào tốn thời gian/lỗi nhất? Bước 2–3 - đọc & phân loại
│   (⏱ ~5 phút/yêu cầu; ~15% giao nhầm bộ phận; tồn đọng ngoài giờ
│   hành chính).
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2–3: LLM đọc nội dung,
│   trích xuất {loại sự cố, vị trí, mức độ khẩn, bộ phận} ──> tạo
│   ticket nháp; từ khóa khẩn cấp (kẹt thang máy, rò điện, cháy, ngập)
│   ──> rule escalate ngay lên hotline trực, không chờ AI.
│
│ Đo thành công bằng gì (Metric có số)?
│   - Thời gian từ nhận yêu cầu ──> giao đúng bộ phận: ~30 phút ──> dưới 5 phút
│   - ≥ 90% ticket phân loại đúng bộ phận ngay lần đầu
│   - 100% sự cố khẩn cấp được escalate trong vòng 1 phút
│
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent
│   (LLM classify + extract JSON; Rule cho nhánh khẩn cấp;
│   confidence thấp ──> nhân viên duyệt)
└─────────────────────────────────────────────────────────────
```

**Tự phản biện:** Nếu app đã có form dropdown chọn loại sự cố thì rule-based có thể đủ cho kênh app; LLM chỉ thực sự cần cho kênh văn bản tự do (Zalo, hotline đã chép lời, mô tả mơ hồ như "nhà có mùi khét"). Cần đo tỷ lệ yêu cầu đến từ kênh tự do trước khi đầu tư.
