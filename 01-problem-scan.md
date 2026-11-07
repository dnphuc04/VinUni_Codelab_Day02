# LAB 02 — 01-PROBLEM-SCAN
## Phase 1: SCAN (cá nhân) & Phase 2: QUICK-ASSESS (cá nhân)

**Dự án chính lựa chọn:** **VinFast AI Workshop Copilot — Trợ lý AI chuẩn hóa phiếu tiếp nhận, phân loại triệu chứng và tìm tài liệu hỗ trợ sửa chữa tại xưởng dịch vụ VinFast**  
**Vai trò:** AI Product Engineer (bài tập giả lập trong bối cảnh Vin Smart Future)  
**Ngày:** 06/11/2026  
**Họ tên / Nhóm:** ............................................................  
**Liên kết báo cáo tiếp theo:** `02-deep-dive-report.md` — chỉ phân tích sâu **Quick Problem Card #1 (VinFast)**.

> **Tính trung thực của bài làm:** Thông tin về **phạm vi kinh doanh, đặt lịch và các bước dịch vụ chính thức của VinFast** dựa trên nguồn công khai [1]–[3]. Các *điểm nghẽn*, thời gian xử lý, năng suất, chất lượng AI và chi phí bên dưới là **giả thuyết / số liệu minh họa phục vụ Lab**, **KHÔNG phải số liệu nội bộ hoặc kết quả thử nghiệm đã xảy ra**. Phải khảo sát xưởng và thu thập log hợp lệ trước khi triển khai thực tế. Không cần VIN, biển số, thông tin khách hàng thật để làm prototype.

---

# PHASE 1 — SCAN: TÌM CƠ HỘI AI

## 1.1. Bốn lăng kính (Lenses)

| Lens | Câu hỏi dùng để tìm bottleneck |
|---|---|
| **Repetitive — lặp lại** | Nhân viên phải nhập, đọc, đối chiếu hoặc chuyển cùng loại thông tin nhiều lần/ngày? |
| **Time-consuming — tốn thời gian** | Bước nào phải tra nhiều hệ thống, tài liệu dài hoặc chờ người khác phản hồi? |
| **AI-upgrade — AI làm tốt hơn** | Có nhiều văn bản tự do, ảnh, sự kiện khác nhau hoặc mẫu phức tạp mà rule đơn giản khó phủ hết? |
| **Stakeholder Pain — nỗi đau người liên quan** | Bước nào khiến khách hàng chờ, nhân viên quá tải, phát sinh trả lại phiếu hoặc tăng rủi ro? |

## 1.2. Bảng SCAN — 7 bài toán có thể nghiên cứu trong hệ sinh thái Vingroup

| # | Đơn vị | Lens áp dụng | Bài toán / bottleneck **cần khảo sát** | Actor chính | AI khả thi ở phạm vi nhỏ |
|---|---|---|---|---|---|
| **1 ★** | **VinFast — xưởng dịch vụ** | Repetitive; Time-consuming; Stakeholder Pain; AI-upgrade | Mô tả lỗi xe thiếu cấu trúc; cố vấn và kỹ thuật viên cần phân loại triệu chứng, đối chiếu phiếu, lịch sử và tài liệu kỹ thuật; phiếu có thể bị bổ sung hoặc chuyển lại. | Cố vấn dịch vụ, kỹ thuật viên, khách hàng | **LLM + RAG + rule:** chuẩn hóa triệu chứng, phát hiện dấu hiệu an toàn, tìm tài liệu đúng phiên bản, tạo phiếu để con người duyệt. **Đề tài chính.** |
| **2** | **Vinhomes — vận hành đô thị** | Repetitive; Stakeholder Pain; Time-consuming | Phản ánh cư dân về nước, thang máy, tiếng ồn, vệ sinh, an ninh cần chuyển đúng bộ phận và ưu tiên đúng SLA. | Cư dân, CSKH, tổ kỹ thuật | LLM gắn nhãn ticket, trích vị trí; rule áp SLA và cảnh báo nguy hiểm. |
| **3** | **Vinpearl / VinWonders** | Time-consuming; AI-upgrade | Dự báo lượng khách/phòng theo ngày lễ, thời tiết và lịch đặt để phân ca nhân sự, vật tư. | Quản lý vận hành, lễ tân, nhân viên | Mô hình dự báo chuỗi thời gian; rule lập lịch. |
| **4** | **GSM / Xanh SM — liên kết với V-Green** | AI-upgrade; Stakeholder Pain | Lựa chọn thời điểm/điểm sạc khi mức pin, công suất trạm và hàng chờ thay đổi; cần tránh chạy rỗng hoặc chờ lâu. | Điều phối viên, tài xế, trực trạm | Tối ưu hóa + rule + ML; LLM chỉ xử lý văn bản sự cố. **Chưa chọn** do thiếu dữ liệu trạm/sạc đáng tin cậy cho Lab. |
| **5** | **Vinmec** | Time-consuming; Repetitive | Chuẩn hóa giấy tờ hành chính, kiểm tra tài liệu còn thiếu trong hành trình khám/tái khám. | Nhân viên hành chính, điều dưỡng, bệnh nhân | LLM tóm tắt hồ sơ được phép truy cập; rule kiểm tra đủ giấy tờ. Không tự chẩn đoán. |
| **6** | **Vinhomes / VinSpeed — dự án quy mô lớn** | Time-consuming; AI-upgrade | Báo cáo tiến độ các hạng mục/nhà thầu dưới nhiều định dạng, khó đối chiếu rủi ro chậm mốc và phát sinh chi phí. | Kỹ sư dự án, PM, tài chính | LLM chuẩn hóa báo cáo; ML dự báo chậm tiến độ. |
| **7** | **VinSmart Future / VinSOC** | Repetitive; AI-upgrade; Stakeholder Pain | Nhiều cảnh báo an ninh trùng lặp, cần phân loại mức ưu tiên và tổng hợp bằng chứng để chuyên gia xác minh. | Chuyên viên SOC, chủ hệ thống | Rule/ML gom cụm + LLM tóm tắt cảnh báo có kiểm chứng. |

### 1.3. Tại sao VinFast là ứng viên mạnh nhất cho Lab này?

- **Có căn cứ nghiệp vụ công khai:** VinFast có trang đặt lịch dịch vụ cho phép khách hàng điền thông tin xe, chọn nhóm dịch vụ, bổ sung mô tả/ảnh; quy trình công bố có **đặt hẹn → tiếp nhận/tư vấn → bảo dưỡng/sửa chữa → bàn giao → chăm sóc sau dịch vụ** [1], [2]. Do đó bài toán **chuẩn hóa mô tả và hỗ trợ xử lý phiếu** bám vào công việc thực, không giả định VinFast chưa có phần mềm.
- **Quy mô cho thấy lý do đáng nghiên cứu:** Thông cáo 11/05/2026 nêu mạng lưới gần **400 xưởng tại Việt Nam** và gần **800 cơ sở toàn cầu cuối 2025**, mục tiêu **hơn 1.100 xưởng toàn cầu năm 2026**; **mục tiêu không đồng nghĩa số xưởng đã hoàn thành** [3]. Quy mô tạo nhu cầu chuẩn hóa quy trình, nhưng không chứng minh điểm nghẽn cụ thể.
- **Dễ mô phỏng phần LLM:** Có thể tự viết mô tả triệu chứng tiếng Việt, nhãn nhóm hệ thống, dấu hiệu nguy hiểm và kho tài liệu **giả lập**; so với dự báo hàng chờ trạm sạc, không cần dữ liệu thời gian thực hoặc tối ưu hệ thống vật lý.
- **Giới hạn an toàn rõ:** AI **không chẩn đoán chính thức**, không kết luận lỗi pin cao áp, không quyết định thay phụ tùng, không sửa/hướng dẫn sửa hệ thống cao áp, không phê duyệt bảo hành/báo giá.

---

# PHASE 2 — QUICK-ASSESS: CHỌN 3 BÀI TOÁN TIỀM NĂNG

## 2.1. Lựa chọn top 3

| Thứ tự | Đề tài | Khả năng đo được trong Lab | Quyết định |
|---|---|---|---|
| **#1** | **VinFast AI Workshop Copilot — phân loại phiếu sự cố & tra tài liệu** | Đầu vào văn bản; nhãn hệ thống; cờ an toàn; trích xuất JSON; tài liệu giả lập; thời gian xử lý | **CHỌN để phân tích sâu / làm prototype** |
| **#2** | **Vinhomes — ưu tiên phản ánh cư dân** | F1 phân loại, recall sự cố, thời gian phân luồng | Dự phòng phù hợp LLM |
| **#3** | **Vinpearl — dự báo nhu cầu nhân sự/khách** | MAPE/WAPE, độ lệch bố trí nhân sự | Giá trị vận hành nhưng trọng tâm là ML, không lý tưởng cho bài prompt Gemini |

## QUICK PROBLEM CARD #1 — VINFAST AI WORKSHOP COPILOT (ĐỀ TÀI CHÍNH)

**Bài toán (1 câu):** Khi xe đến xưởng với mô tả lỗi không chuẩn hóa, cố vấn dịch vụ và kỹ thuật viên phải mất công làm rõ triệu chứng, kiểm tra dấu hiệu an toàn và tra tài liệu liên quan; đề xuất AI **chuẩn hóa phiếu và gợi ý tài liệu để con người kiểm duyệt**.

**Công ty thành viên:** ☑ VinFast  ☐ Xanh SM  ☐ Vinhomes  ☐ Vinmec  ☐ Khác.

**Ai đang đau (Actor)?** Cố vấn dịch vụ (nhận yêu cầu), kỹ thuật viên (đọc phiếu và tra quy trình), trưởng xưởng/chuyên gia an toàn (xử lý ngoại lệ), khách hàng (chờ phản hồi).

**Workflow hiện tại — mô hình giả định cho đúng phạm vi prototype:**

1. **Tiếp nhận** yêu cầu, mẫu xe, mã lỗi nếu khách hàng/thiết bị có cung cấp; nhân viên hỏi lại thông tin thiếu.
2. **Đọc và chuẩn hóa** mô tả triệu chứng, nhận diện dấu hiệu nguy hiểm; chọn nhóm hệ thống ban đầu.
3. **Tra cứu** lịch sử bảo dưỡng/tài liệu/hướng dẫn phù hợp với dòng xe, phiên bản (nếu có quyền truy cập).
4. **🔄 Handoff:** cố vấn chuyển phiếu và tài liệu cho kỹ thuật viên; kỹ thuật viên hỏi thêm hoặc trả lại phiếu nếu chưa đủ.
5. **Chuyên môn xác minh** ưu tiên, xây dựng kế hoạch kiểm tra; các bước báo giá, sửa chữa, QA và bàn giao thực hiện theo quy trình hiện có.

**Bottleneck:** Bước **2–3** do mô tả tự do và tài liệu phân tán; có thể phải hỏi lại và tìm nhiều lần. **Giả định Lab:** B2 **12 phút**, B3 **18 phút** = **30 phút/phiếu** cho hai tác vụ chính; **không phải baseline thực của VinFast**. Thời gian toàn bộ quy trình xưởng không đồng nhất với con số này.

**AI nhảy vào ở đâu?** Sau bước 1 và trước bước 4. LLM trích xuất `symptoms`, `vehicle_model`, `dtc_codes` (chỉ những mã thật có trong đầu vào), `system_category`, `safety_flags`, `missing_information`, `candidate_document_ids`, `requires_human_review`; **RAG chỉ trả tài liệu có nguồn**; **rule** quyết định khi nào phải gắn cờ an toàn. Kỹ thuật viên phê duyệt mọi gợi ý.

**Ví dụ đầu vào (giả lập):** “VF 5 báo đèn phanh, bàn đạp mềm và phanh kém, chưa đọc mã lỗi.”  
**Ví dụ đầu ra mong đợi:** `system_category="braking"`, `safety_flags=["brake_system_symptom"]`, `dtc_codes=[]`, `requires_human_review=true`, `safe_next_action="escalate_to_service_staff"`, tài liệu chỉ hiện khi truy xuất được bản phù hợp. **Không** kết luận phải thay bộ phận nào.

**Success Metrics (mục tiêu, chưa đo):**
- **≥90% macro-F1** phân loại nhóm hệ thống trên **200 phiếu giả lập có nhãn**.
- **30/30** trường hợp nguy hiểm trong bộ test mẫu được gắn cờ để người kiểm tra (mẫu nhỏ, không chứng minh recall ngoài thực tế).
- **≥95%** JSON hợp lệ ngay lần đầu và **100% output không hợp lệ bị chặn**.
- **Giảm ≥25%** thời gian hoàn thiện phần **phân loại + tra cứu** so với baseline thực nghiệm thủ công trên cùng bộ dữ liệu; không lấy mức 30 phút giả định làm kết quả thật.
- **0 trường hợp** AI tự ra quyết định thay linh kiện/phê duyệt bảo hành trên bộ kiểm thử tấn công.

**Quick Architecture:** ☐ No AI  ☑ **LLM Feature + Rule + RAG**  ☐ Full autonomous Agent.  
**Operational boundary:** AI tạo **bản nháp** và gợi ý tài liệu, không tự xác nhận lỗi, lập báo giá, chỉ định sửa chữa, ghi đè hồ sơ hay xử lý cảnh báo cao áp/phanh không có con người.

**Giá trị tiềm năng:** Giảm thời gian hành chính/tra cứu trước khi sửa; tăng tính đầy đủ của phiếu. **Không hứa giảm tổng thời gian sửa xe khi chưa chứng minh.**

## QUICK PROBLEM CARD #2 — VINHOMES: PHÂN LOẠI & ƯU TIÊN PHẢN ÁNH CƯ DÂN

**Bài toán (1 câu):** Chuẩn hóa phản ánh cư dân đa dạng về từ ngữ và chuyển đúng nhóm xử lý theo mức độ ưu tiên do hệ thống nghiệp vụ quyết định.

**Công ty thành viên:** ☐ VinFast  ☐ Xanh SM  ☑ Vinhomes  ☐ Vinmec  ☐ Khác.  
**Actor:** Nhân viên CSKH/ban quản lý, đội kỹ thuật, cư dân.

**Workflow hiện tại — giả định khảo sát:** (1) Cư dân gửi nội dung qua app/tổng đài → (2) CSKH đọc và hỏi bổ sung → (3) phân loại nhóm sự cố → (4) chuyển tổ và gắn SLA → (5) tổ tiếp nhận, phản hồi và cập nhật ticket.

**Bottleneck:** Bước 2–4, mô tả thiếu địa điểm/không nhất quán; **ví dụ giả định 3 phút/ticket**, không phải thời gian nội bộ Vinhomes.

**AI hỗ trợ:** LLM xuất `category`, `urgency`, `location`, `missing_info`; rule áp SLA và escalations. Phiếu khẩn cấp/thiếu thông tin có người duyệt.

**Metric mục tiêu thử nghiệm:** macro-F1 ≥90%, 100% báo cáo “cháy/khói/điện nguy hiểm” trong bộ test nhỏ được cảnh báo, thời gian phân loại giảm ≥30% so với mẫu thử thủ công.

**Quick Architecture:** ☑ **LLM Feature + Rule** (không dùng agent tự xử lý yêu cầu).  
**Vì sao không chọn:** Vẫn là phương án rất tốt nhưng muốn Lab bám hơn vào quy trình kỹ thuật xưởng và chẩn đoán hỗ trợ của VinFast.

## QUICK PROBLEM CARD #3 — VINPEARL: DỰ BÁO LƯỢT KHÁCH & PHÂN CA

**Bài toán (1 câu):** Dự báo lượng khách theo ngày/khung giờ để gợi ý bố trí nhân lực và vật tư hợp lý, giảm giờ dư thừa và thiếu người.

**Công ty thành viên:** ☐ VinFast  ☐ Xanh SM  ☐ Vinhomes  ☐ Vinmec  ☑ Khác: Vinpearl/VinWonders.  
**Actor:** Quản lý khách sạn/khu vui chơi, lễ tân, bộ phận buồng phòng, F&B và nhân sự.

**Workflow hiện tại — giả định khảo sát:** (1) Thu thập lịch đặt phòng/vé → (2) tổng hợp lịch ngày lễ và sự kiện → (3) nhân viên lập dự báo → (4) quản lý duyệt lịch phân ca → (5) theo dõi thực tế và điều chỉnh.

**Bottleneck:** Bước 2–4, nhiều yếu tố biến động, dễ lệch dự báo; **giả định 45 phút/lần lập bảng**, chưa xác minh.

**AI hỗ trợ:** ML dự báo theo chuỗi thời gian, rule xếp lịch theo số người tối thiểu và luật lao động; LLM chỉ giải thích các giả định/kịch bản.

**Metric mục tiêu thử nghiệm:** WAPE ≤15% trên tập kiểm thử đủ dài; giảm ≥10% tổng giờ phân ca dư thừa với điều kiện mức phục vụ không suy giảm.

**Quick Architecture:** ☑ **ML + Rule**, ☐ LLM là lõi, ☐ Full Agent.  
**Vì sao không chọn:** Đòi hỏi lịch sử đặt phòng theo mùa đủ dài và trọng tâm Lab là prompt prototype bằng Gemini.

---

## 2.2. Quyết định cá nhân sau QUICK-ASSESS

**Chọn VinFast AI Workshop Copilot** để đưa sang `02-deep-dive-report.md` vì: (1) có luồng nghiệp vụ công khai để bám; (2) phần AI phù hợp với văn bản đầu vào và retrieval có căn cứ; (3) làm prototype trên dữ liệu giả lập mà không cần API xưởng thật; (4) dễ chỉ ra khi nào Rule tốt hơn LLM và khi nào con người bắt buộc phê duyệt. **Chưa kết luận đây là bài toán bức thiết nhất của VinFast trước khi phỏng vấn thực tế.**

## 2.3. Nguồn tham chiếu công khai & phân biệt với giả định

1. **VinFast — Quy trình bảo dưỡng chính thức**: [https://vinfastauto.com/vn_vi/quy-trinh-bao-duong](https://vinfastauto.com/vn_vi/quy-trinh-bao-duong) — mô tả tiếp nhận, báo giá có phê duyệt, sửa chữa, kiểm tra, bàn giao và chăm sóc sau dịch vụ.
2. **VinFast — Đặt lịch dịch vụ bảo dưỡng**: [https://shop.vinfastauto.com/vn_vi/dat-lich-dich-vu-bao-duong.html](https://shop.vinfastauto.com/vn_vi/dat-lich-dich-vu-bao-duong.html) — các trường thông tin xe, dịch vụ, địa điểm, thời gian và ảnh.
3. **VinFast, 11/05/2026 — mở rộng hậu mãi toàn cầu**: [https://vinfastauto.com/vn_vi/vinfast-thuc-day-chien-luoc-hau-mai-toan-cau-mo-rong-mang-luoi-dich-vu-va-doi-tac-quoc-te](https://vinfastauto.com/vn_vi/vinfast-thuc-day-chien-luoc-hau-mai-toan-cau-mo-rong-mang-luoi-dich-vu-va-doi-tac-quoc-te) — số xưởng tính đến cuối 2025 và kế hoạch mở rộng 2026.
4. **VinFast — FAQ chính sách hậu mãi**: [https://vinfastauto.com/vn_vi/cau-hoi-thuong-gap/cau-hoi-xe-o-to/chinh-sach-hau-mai](https://vinfastauto.com/vn_vi/cau-hoi-thuong-gap/cau-hoi-xe-o-to/chinh-sach-hau-mai) — các kênh đặt lịch và phần mô tả/ảnh bổ sung.

**Đề xuất kiểm chứng tiếp theo:** Phỏng vấn cố vấn dịch vụ và kỹ thuật viên để xác định thời gian thực, tỷ lệ phiếu bị trả lại, mức độ đầy đủ của mô tả, danh mục mã lỗi, kho tài liệu và quy trình phê duyệt đang dùng. Điều này thuộc **bước chuẩn bị**, chưa được thực hiện trong bài này.
