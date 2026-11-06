# Lab 02 — Problem Scan & Quick Assessment

> Bộ tài liệu nhóm được chọn lọc từ bài của Đồng Ngọc Phúc. Việc sử dụng làm bài nhóm không đồng nghĩa mọi thành viên đã thực hiện cùng một thử nghiệm. [Bài nguồn và bằng chứng cá nhân](https://github.com/dnphuc04/VinUni_Codelab_Day02/tree/398cf61c0e05594e0acd30d20fe081224bbddb96). Code và thư mục `evidence/` được giữ trên nhánh cá nhân, không đưa vào `main`.

**Hình thức:** Bài báo cáo nhóm — Lab 02  
**Đại diện tổng hợp:** Đồng Ngọc Phúc — 2A202603399  

> Các bài toán, workflow, baseline và mục tiêu định lượng là giả định phục vụ lab, chưa được xác nhận bằng khảo sát doanh nghiệp.

## Phase 1 — SCAN: Quét cơ hội (bản tổng hợp nhóm)

Sử dụng 4 lenses: **Lặp lại**, **Tốn thời gian**, **AI có thể tốt hơn**, **Pain từ người khác**.

| # | Công ty | Lens | Bài toán / Điểm nghẽn |
|---|---|---|---|
| 1 | Xanh SM | Tốn thời gian | Khi tài xế báo sự cố pin bằng tin nhắn tự do, điều phối viên phải đọc, hỏi lại thông tin thiếu, tra cứu dữ liệu và soạn hướng dẫn thủ công. |
| 2 | Vinhomes | Lặp lại | Nhân viên tiếp nhận phải đọc và phân loại nhiều phản ánh cư dân, xác định tòa nhà và chuyển đến bộ phận phụ trách; tin nhắn thiếu thông tin dễ bị chuyển sai hoặc phải hỏi lại. |
| 3 | Vinpearl | AI có thể tốt hơn | Nhân viên phải soạn phản hồi cho nhiều đánh giá của khách; câu trả lời mẫu có thể chưa phản ánh đúng vấn đề và cảm xúc trong từng đánh giá. |
| 4 | VinFast | Lặp lại | Nhân viên tài chính đối chiếu bảng kê phiên sạc với hóa đơn đối tác, xử lý thủ công các chênh lệch về mã giao dịch, số tiền hoặc dữ liệu thiếu. |
| 5 | Vinmec | Tốn thời gian | Nhân viên phụ trách lịch hẹn đọc yêu cầu qua tin nhắn, trích xuất chuyên khoa khách muốn đặt, thời gian mong muốn và thông tin liên hệ rồi nhập lại vào hệ thống. |
| 6 | Xanh SM | Pain từ người khác | Ghi chú hủy chuyến của tài xế có cách diễn đạt không thống nhất, khiến bộ phận vận hành mất thời gian tổng hợp nguyên nhân và phát hiện vấn đề lặp lại. |

**Sàng lọc ban đầu:**

- Chọn **#1, #2 và #3** để phân tích nhanh vì có đầu vào ngôn ngữ tự nhiên, đầu ra dễ kiểm tra và có thể giữ bước phê duyệt của con người.
- Với **#4**, nên thử đối chiếu bằng rule trước; chỉ cân nhắc AI khi phải xử lý chứng từ hoặc mô tả không có cấu trúc.
- Với **#5**, cần kiểm soát dữ liệu cá nhân và giới hạn rõ chức năng hành chính, không suy luận chẩn đoán.
- Với **#6**, cần tập dữ liệu có nhãn đáng tin cậy để đánh giá chất lượng phân loại.

## Phase 2 — QUICK-ASSESS: 3 Quick Problem Cards

### Card #1 — Trợ lý soạn nháp hỗ trợ sự cố pin

| Trường | Nội dung |
|---|---|
| **Bài toán trong một câu** | Hỗ trợ điều phối viên soạn nháp phương án xử lý khi tài xế báo sự cố pin, dựa trên thông tin đã được xác minh. |
| **Công ty thành viên** | Xanh SM |
| **Actor** | Điều phối viên xử lý sự cố; tài xế là người chờ hỗ trợ. |
| **Workflow hiện tại — giả định** | 1. Nhận tin nhắn tài xế → 2. Xác minh mức pin, vị trí và thông tin xe → 3. Tra cứu phương án hỗ trợ → 4. Soạn hướng dẫn → 5. Kiểm tra và gửi cho tài xế. |
| **Bottleneck** | Tổng hợp thông tin rời rạc và soạn hướng dẫn phù hợp từng tình huống; giả định mất **5 phút/lượt** ở bước soạn nháp. |
| **AI Solution** | LLM trích xuất thông tin từ báo cáo, chỉ ra dữ liệu thiếu và soạn nháp dựa trên dữ liệu được cung cấp. Code áp dụng quy tắc ngưỡng pin và kiểm tra output. |
| **Metric mục tiêu** | Trên 30 tình huống giả lập: giảm trung vị thời gian soạn nháp từ **5 phút xuống ≤2 phút**; **≥90%** bản nháp được người đánh giá chấp nhận mà không sửa nội dung chính; **0 vi phạm** ranh giới trong bộ test. |
| **Quick Architecture** | **Rule + LLM Feature**. Rule xử lý ngưỡng pin và điều kiện bắt buộc; LLM hỗ trợ ngôn ngữ. |
| **Operational Boundary** | Output bắt đầu bằng `[DRAFT_ONLY]`; không tự gửi tin hoặc điều xe. Theo quy tắc lab, pin dưới 5% phải đề xuất `dispatch_mobile_charger`, không đề xuất trạm xa hơn 5 km. Không tự bịa vị trí hay trạng thái trạm sạc. |
| **HITL / Fallback** | Điều phối viên xác minh và duyệt trước khi hành động. Thiếu dữ liệu, output lỗi hoặc tình huống ngoài phạm vi thì chuyển sang xử lý thủ công. |

### Card #2 — Phân loại và đề xuất chuyển phản ánh cư dân

| Trường | Nội dung |
|---|---|
| **Bài toán trong một câu** | Hỗ trợ nhân viên phân loại phản ánh cư dân và đề xuất bộ phận tiếp nhận dựa trên danh mục trách nhiệm có sẵn. |
| **Công ty thành viên** | Vinhomes |
| **Actor** | Nhân viên chăm sóc cư dân và bộ phận vận hành tòa nhà. |
| **Workflow hiện tại — giả định** | 1. Nhận phản ánh → 2. Đọc và xác định vấn đề, địa điểm → 3. Hỏi bổ sung thông tin → 4. Chọn bộ phận phụ trách → 5. Tạo phiếu và chuyển xử lý. |
| **Bottleneck** | Đọc nội dung tự do và xác định nhóm xử lý; giả định mất **4 phút/phiếu**, đặc biệt với phản ánh chứa nhiều vấn đề. |
| **AI Solution** | LLM đề xuất nhãn, trích xuất địa điểm và tóm tắt yêu cầu. Rule ánh xạ nhãn sang bộ phận theo danh mục được cung cấp. |
| **Metric mục tiêu** | Trên 50 phản ánh giả lập có nhãn tham chiếu: phân loại đúng **≥90%**; giảm trung vị thời gian phân loại từ **4 phút xuống ≤1,5 phút**; **100%** trường hợp thiếu địa điểm được đánh dấu cần bổ sung. |
| **Quick Architecture** | **Rule + LLM Feature**. LLM hiểu nội dung; rule giới hạn nhãn và tuyến chuyển. |
| **Operational Boundary** | Chỉ đề xuất phân loại và bản nháp phiếu; không tự đóng phiếu, cam kết thời hạn hoặc quyết định bồi thường. Các tình huống khẩn cấp phải được chuyển cho người phụ trách theo quy trình có sẵn. |
| **HITL / Fallback** | Nhân viên duyệt tuyến chuyển. Phản ánh nhiều vấn đề, mơ hồ hoặc ngoài danh mục được đưa vào hàng chờ xử lý thủ công. |

### Card #3 — Soạn nháp phản hồi đánh giá khách sạn

| Trường | Nội dung |
|---|---|
| **Bài toán trong một câu** | Hỗ trợ nhân viên soạn phản hồi phù hợp với nội dung đánh giá của khách, tuân thủ hướng dẫn và chính sách được cung cấp. |
| **Công ty thành viên** | Vinpearl |
| **Actor** | Nhân viên chăm sóc khách hàng hoặc quản lý phụ trách phản hồi đánh giá. |
| **Workflow hiện tại — giả định** | 1. Đọc đánh giá → 2. Xác định vấn đề chính → 3. Kiểm tra thông tin và chính sách liên quan → 4. Soạn phản hồi → 5. Quản lý duyệt và đăng. |
| **Bottleneck** | Viết phản hồi vừa đúng vấn đề vừa phù hợp giọng điệu thương hiệu; giả định mất **8 phút/đánh giá** ở bước soạn. |
| **AI Solution** | LLM tóm tắt các vấn đề và soạn phản hồi dựa trên đánh giá, dữ kiện đã xác minh và chính sách được cung cấp. |
| **Metric mục tiêu** | Trên 30 đánh giá giả lập: giảm trung vị thời gian soạn từ **8 phút xuống ≤3 phút**; **≥90%** bản nháp đề cập đầy đủ vấn đề chính theo checklist của người đánh giá; **0 cam kết bồi thường trái chính sách** trong bộ test. |
| **Quick Architecture** | **LLM Feature** kết hợp kiểm tra các nội dung bị cấm. Không cần Agent vì tác vụ chỉ tạo bản nháp từ đầu vào có sẵn. |
| **Operational Boundary** | Không tự đăng phản hồi; không bịa kết quả điều tra, tiết lộ dữ liệu khách hoặc tự hứa hoàn tiền, nâng hạng, tặng voucher. |
| **HITL / Fallback** | Nhân viên duyệt mọi bản nháp. Phản ánh nghiêm trọng hoặc thiếu căn cứ trả lời được chuyển cho quản lý xử lý. |

## Lựa chọn để Deep-Dive của bài nhóm

Chọn **Card #1 — Trợ lý soạn nháp hỗ trợ sự cố pin Xanh SM**.

Lý do lựa chọn:

1. Khớp với bài tập Python và các ranh giới trong starter code.
2. Phạm vi đủ hẹp để hoàn thành prototype bằng dữ liệu giả lập.
3. Có thể phân chia rõ nhiệm vụ giữa rule, LLM và người phê duyệt.
4. Có thể kiểm thử cụ thể bằng các tình huống dụ bỏ thẻ nháp, đề xuất trạm quá xa hoặc yêu cầu tự động gửi tin.

Card #2 và #3 vẫn có tiềm năng, nhưng cần bổ sung danh mục phân tuyến hoặc chính sách phản hồi để đánh giá đáng tin cậy.

**Bước kiểm chứng tiếp theo:** xây dựng bộ tình huống giả lập có đáp án kỳ vọng, đo baseline thủ công và thử prototype. Kết quả trên dữ liệu giả lập chỉ chứng minh khả năng của bản mẫu trong phạm vi thử nghiệm, chưa đủ để kết luận sẵn sàng triển khai thực tế.
