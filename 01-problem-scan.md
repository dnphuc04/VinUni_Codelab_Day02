
**Học viên** Nguyễn Việt Hưng
**MSV** 2A202603411

# 🔍 Phase 1 — SCAN: Quét cơ hội 
Sử dụng 4 lenses: **Lặp lại**, **Tốn thời gian**, **AI có thể tốt hơn**, **Pain từ người khác**

### 📝 List bài toán của tôi:
| # | Subsidiary (VinFast/Xanh SM...) | Lens | Mô tả ngắn bài toán |
|---|----------------------------------|------|---------------------|
| 1 |VINMEC |AI có thể tốt hơn| Tự động hóa ghi chép hồ sơ bệnh án và nhập liệu lâm sàng|
| 2 |VINMEC|Pain từ người khác| Bệnh nhân quên uống thuốc hoặc không tuân thủ liệu trình|
| 3 |VINMEC |Lặp lại| Tiếp nhận bệnh nhân, đặt lịch và điều phối lịch khám|
| 4 |VINMEC |Lặp lại| Xử lý bảo hiểm, phê duyệt dịch vụ và đối soát hồ sơ thanh toán|
| 5 |VINMEC |AI có thể tốt hơn|Quản lý tồn kho thuốc, vật tư y tế và dự báo nhu cầu sử dụng|

---

# 🃏 Phase 2 — QUICK-ASSESS 

Chọn **top 3 bài toán** là bài toán **1**, **2** và **3** từ list bài toán trên.

### Card 1: Tự động hóa ghi chép hồ sơ bệnh án và nhập liệu lâm sàng (AI Medical Scribe)

| Trường | Nội dung |
|---|---|
| **Bài toán** | Ứng dụng AI để tự động ghi nhận, chuyển đổi và cấu trúc hóa nội dung trao đổi giữa bác sĩ và bệnh nhân thành bản nháp hồ sơ bệnh án điện tử (EMR), giảm thời gian ghi chép và nhập liệu thủ công cho đội ngũ y tế. |
| **Công ty thành viên** | VINMEC |
| **Actor** | Bác sĩ khám bệnh; điều dưỡng và nhân viên y tế; bộ phận quản lý hồ sơ bệnh án; bệnh nhân. |
| **Workflow hiện tại** | 1. Bác sĩ tiếp nhận và trao đổi với bệnh nhân trong quá trình khám. <br> 2. Bác sĩ ghi nhận triệu chứng, tiền sử bệnh, kết quả thăm khám và các thông tin lâm sàng. <br> 3. Bác sĩ nhập các thông tin này vào hệ thống HIS/EMR, thường kết hợp giữa nhập liệu thủ công và lựa chọn biểu mẫu có sẵn. <br> 4. Bác sĩ hoàn thiện hồ sơ, chỉ định xét nghiệm, chẩn đoán và kế hoạch điều trị. <br> 5. Bác sĩ kiểm tra, chỉnh sửa và xác nhận hồ sơ bệnh án. |
| **Bước nào tốn thời gian nhất / kém hiệu quả nhất?** | **Bước 2 và 3:** Bác sĩ phải vừa tập trung trao đổi, thăm khám bệnh nhân vừa ghi chép và nhập liệu vào hệ thống. Việc nhập lại thông tin từ ghi chú hoặc biểu mẫu, cập nhật các trường dữ liệu và hoàn thiện nội dung hồ sơ có thể làm tăng thời gian hành chính, giảm thời gian tương tác trực tiếp với bệnh nhân và phát sinh nguy cơ thiếu sót thông tin. |
| **AI có thể hỗ trợ bước nào?** | **Bước 1, 2 và 3:** <br> - Sử dụng Speech-to-Text để chuyển đổi hội thoại giữa bác sĩ và bệnh nhân thành văn bản. <br> - Sử dụng Medical NLP/LLM để nhận diện và trích xuất thông tin lâm sàng như triệu chứng, tiền sử bệnh, thuốc đang sử dụng, kết quả thăm khám và chỉ định. <br> - Tự động phân loại và cấu trúc hóa thông tin theo các trường trong mẫu hồ sơ bệnh án . <br> - Tạo bản nháp ghi chép lâm sàng và đề xuất điền các trường tương ứng trên hệ thống HIS/EMR. <br> - Phát hiện thông tin còn thiếu, nội dung không nhất quán hoặc các trường chưa được hoàn thiện để bác sĩ kiểm tra. <br> - Bác sĩ rà soát, chỉnh sửa và xác nhận trước khi lưu chính thức vào hồ sơ bệnh án. |
| **Metric để đo lường hiệu quả** | - **Documentation Time:** Thời gian trung bình bác sĩ dành cho việc hoàn thiện hồ sơ bệnh án trên mỗi lượt khám. <br>  - **Documentation Completeness:** Tỷ lệ hồ sơ có đầy đủ các trường thông tin bắt buộc. <br> - **AI Suggestion Acceptance Rate:** Tỷ lệ nội dung do AI đề xuất được bác sĩ chấp nhận sau khi rà soát. <br> - **Correction Rate:** Tỷ lệ nội dung AI tạo ra cần bác sĩ chỉnh sửa. <br> - **Physician Satisfaction:** Mức độ hài lòng của bác sĩ khi sử dụng hệ thống. <br> - **Clinical Safety:** Tỷ lệ lỗi nghiêm trọng liên quan đến sai lệch thông tin lâm sàng trong bản nháp được AI tạo ra. |
| **Quick Architecture** | **Ambient AI Scribe + Medical NLP/LLM + HIS/EMR Integration:** <br> - **Audio Capture:** Thu nhận hội thoại giữa bác sĩ và bệnh nhân theo cơ chế được bệnh nhân đồng ý. <br> - **Speech-to-Text (STT):** Chuyển đổi giọng nói thành văn bản, hỗ trợ nhận diện thuật ngữ y khoa. <br> - **Medical NLP/LLM:** Trích xuất thông tin lâm sàng, nhận diện thực thể y tế và cấu trúc hóa nội dung theo mẫu hồ sơ. <br> - **Clinical Validation Layer:** Kiểm tra tính đầy đủ, nhất quán và đánh dấu các thông tin chưa rõ ràng để bác sĩ xác minh. <br> - **EMR Integration:** Đưa bản nháp vào các trường tương ứng trên hệ thống HIS/EMR thông qua API hoặc giao diện tích hợp. <br> - **Physician Review & Approval:** Bác sĩ kiểm tra, chỉnh sửa và xác nhận trước khi lưu hồ sơ chính thức. <br> - **Audit Log:** Lưu vết nội dung AI đề xuất, nội dung được chỉnh sửa và người xác nhận. |

**KPI mục tiêu đề xuất:**
- Giảm ít nhất 20% thời gian hoàn thiện hồ sơ trên mỗi lượt khám.
- Documentation Completeness đạt ≥ 95% đối với các trường thông tin thuộc phạm vi thử nghiệm.
- AI Suggestion Acceptance Rate đạt ≥ 80%.
- 0 lỗi nghiêm trọng được AI tự động ghi vào hồ sơ chính thức mà không qua xác nhận của bác sĩ.


### Card 2: AI Medication Reminder Assistant – Trợ lý AI nhắc nhở và theo dõi việc sử dụng thuốc

| Trường | Nội dung |
|---|---|
| **Bài toán** | Xây dựng trợ lý AI hỗ trợ bệnh nhân ghi nhớ lịch uống thuốc, hiểu hướng dẫn sử dụng và theo dõi việc tuân thủ điều trị sau khi khám tại VINMEC. |
| **Công ty thành viên** | VINMEC |
| **Actor** | Bệnh nhân sau khám và được kê đơn; người nhà/người chăm sóc; bác sĩ và dược sĩ theo dõi điều trị. |
| **Workflow hiện tại** | 1. Bệnh nhân khám và nhận đơn thuốc từ bác sĩ. <br> 2. Bệnh nhân tự ghi nhớ hoặc tự thiết lập lịch uống thuốc. <br> 3. Bệnh nhân mua thuốc và sử dụng tại nhà theo hướng dẫn. <br> 4. Bệnh nhân tự theo dõi việc uống thuốc, dễ quên liều hoặc sai thời điểm. <br> 5. Khi có thắc mắc hoặc vấn đề phát sinh, bệnh nhân chủ động liên hệ bác sĩ/dược sĩ. <br> 6. Bệnh nhân tái khám theo lịch hẹn. |
| **Bước nào tốn thời gian nhất / kém hiệu quả nhất?** | **Bước 2, 3, 4 và 5:** Bệnh nhân phải tự quản lý nhiều loại thuốc với liều lượng, tần suất và thời gian sử dụng khác nhau. Việc ghi nhớ thủ công dễ dẫn đến quên liều, dùng thuốc không đúng lịch hoặc không hiểu rõ hướng dẫn. Nhân viên y tế có thể phát sinh thêm thời gian giải đáp các câu hỏi lặp lại về cách sử dụng thuốc. |
| **AI có thể hỗ trợ bước nào?** | **Bước 2, 3, 4 và 5:** <br> - Tự động tiếp nhận và trích xuất thông tin từ đơn thuốc điện tử đã được bác sĩ xác nhận. <br> - Tạo lịch uống thuốc dựa trên chỉ định đã kê bằng Rule-based Schedule Engine. <br> - Gửi thông báo nhắc uống thuốc qua ứng dụng, SMS hoặc Zalo. <br> - Cho phép bệnh nhân xác nhận đã uống, hoãn nhắc hoặc báo bỏ lỡ liều. <br> - Sử dụng LLM kết hợp RAG để giải thích đơn thuốc và trả lời câu hỏi dựa trên nguồn thông tin y khoa được VINMEC phê duyệt. <br> - Phát hiện tình trạng bỏ lỡ nhiều liều hoặc dấu hiệu bất thường được bệnh nhân khai báo để chuyển tiếp cho nhân viên y tế. |
| **Metric để đo lường hiệu quả** | - **Medication Adherence Rate:** Tỷ lệ liều thuốc bệnh nhân tự xác nhận đã uống trên tổng số liều đến hạn. <br> - **Patient Activation Rate:** Tỷ lệ bệnh nhân kích hoạt và thiết lập thành công trợ lý. <br> - **Support Call Reduction:** Mức giảm số lượng cuộc gọi hỏi đáp về hướng dẫn sử dụng thuốc. <br> - **Patient Satisfaction:** Mức độ hài lòng của bệnh nhân. <br> - **Medication Safety:** Số lỗi nghiêm trọng trong việc tạo lịch nhắc thuốc; mục tiêu là 0 lỗi do hệ thống tự ý thay đổi liều hoặc chỉ định. |
| **Quick Architecture** | **Hybrid AI + Deterministic Workflow:** <br> - **HIS/EMR Integration:** Đồng bộ đơn thuốc đã được bác sĩ xác nhận. <br> - **OCR / Medical NLP:** Trích xuất và chuẩn hóa thông tin thuốc từ đơn thuốc. <br> - **Rule-based Schedule Engine:** Tạo lịch uống thuốc chính xác theo chỉ định. <br> - **Notification Service:** Gửi thông báo nhắc thuốc qua App/SMS/Zalo. <br> - **LLM + RAG:** Giải thích đơn thuốc và trả lời câu hỏi dựa trên kho tri thức y khoa được phê duyệt. <br> - **Adherence Dashboard:** Theo dõi lịch sử xác nhận uống thuốc và mức độ tuân thủ điều trị. |
**KPI mục tiêu đề xuất:**
- Patient Activation Rate ≥ 60%.
- Medication Adherence Rate tăng ít nhất 10 điểm phần trăm so với baseline hoặc nhóm đối chứng.
- Notification Delivery Rate ≥ 99%.
- 0 lỗi nghiêm trọng trong việc tạo lịch nhắc thuốc.

### Card 3: Tiếp nhận bệnh nhân, đặt lịch và điều phối lịch khám (AI Patient Access & Appointment Scheduling)

| Trường | Nội dung |
|---|---|
| **Bài toán** | Ứng dụng AI để tự động hóa quy trình tiếp nhận yêu cầu khám bệnh, tư vấn thông tin dịch vụ, đặt lịch và hỗ trợ điều phối lịch khám, giúp giảm thời gian chờ đợi của bệnh nhân và tối ưu hiệu suất sử dụng nguồn lực y tế tại VINMEC. |
| **Công ty thành viên** | VINMEC |
| **Actor** | Bệnh nhân; nhân viên tổng đài (Call Center); nhân viên lễ tân/tiếp đón; bác sĩ; điều dưỡng; nhân viên điều phối lịch khám. |
| **Workflow hiện tại** | 1. Bệnh nhân tìm kiếm thông tin về chuyên khoa, bác sĩ, dịch vụ khám và chi phí. <br> 2. Bệnh nhân liên hệ VINMEC qua hotline, website, ứng dụng hoặc trực tiếp tại bệnh viện để yêu cầu đặt lịch. <br> 3. Nhân viên tiếp nhận xác định nhu cầu khám, thông tin bệnh nhân, chuyên khoa và bác sĩ phù hợp. <br> 4. Nhân viên kiểm tra lịch làm việc, khung giờ trống và khả năng tiếp nhận của bác sĩ/phòng khám trên hệ thống. <br> 5. Nhân viên xác nhận lịch hẹn, hướng dẫn bệnh nhân chuẩn bị trước khi khám. <br> 6. Bệnh nhân đến bệnh viện, thực hiện thủ tục tiếp đón và chờ đến lượt khám. <br> 7. Khi có thay đổi lịch hoặc bệnh nhân hủy/không đến, nhân viên cần cập nhật và điều phối lại lịch khám. |
| **Bước nào tốn thời gian nhất / kém hiệu quả nhất?** | **Bước 2, 3, 4 và 7:** Nhân viên phải xử lý nhiều yêu cầu đặt lịch qua các kênh khác nhau, lặp lại các thao tác hỏi thông tin, xác định nhu cầu và kiểm tra lịch bác sĩ. Việc điều phối thủ công khi có lịch hủy, thay đổi hoặc bệnh nhân không đến có thể khiến khung giờ khám bị bỏ trống, tăng thời gian chờ và làm giảm hiệu suất sử dụng nguồn lực y tế. |
| **AI có thể hỗ trợ bước nào?** | **Bước 1, 2, 3, 4, 5 và 7:** <br> - Sử dụng AI Chatbot/Voicebot để tiếp nhận yêu cầu đặt lịch 24/7 qua website, ứng dụng hoặc hotline. <br> - Sử dụng NLP/LLM để nhận diện nhu cầu khám, chuyên khoa, triệu chứng ban đầu và các yêu cầu về thời gian, địa điểm của bệnh nhân. <br> - Đề xuất chuyên khoa hoặc loại dịch vụ phù hợp dựa trên danh mục dịch vụ và quy tắc phân luồng đã được VINMEC phê duyệt; không thay thế chẩn đoán của bác sĩ. <br> - Kết nối hệ thống HIS/Appointment để truy vấn lịch trống theo bác sĩ, chuyên khoa, cơ sở và thời gian. <br> - Tự động đề xuất các khung giờ phù hợp và hỗ trợ bệnh nhân đặt, đổi hoặc hủy lịch. <br> - Gửi xác nhận lịch hẹn, hướng dẫn chuẩn bị trước khi khám và thông báo nhắc lịch qua App/SMS/Zalo. <br> - Phân tích lịch sử đặt lịch và tỷ lệ bệnh nhân không đến (No-show) để dự báo nguy cơ bỏ hẹn, hỗ trợ gửi nhắc lịch hoặc xác nhận lại lịch hẹn. <br> - Hỗ trợ điều phối lại các khung giờ bị hủy, đưa bệnh nhân trong danh sách chờ vào các slot còn trống theo quy tắc ưu tiên. |
| **Metric để đo lường hiệu quả** | - **Appointment Booking Time:** Thời gian trung bình để hoàn tất một yêu cầu đặt lịch. <br> - **Booking Automation Rate:** Tỷ lệ yêu cầu đặt lịch được xử lý hoàn toàn hoặc phần lớn bởi hệ thống mà không cần nhân viên can thiệp. <br> - **Patient Waiting Time:** Thời gian bệnh nhân chờ từ khi đến bệnh viện đến khi được khám. <br> - **No-show Rate:** Tỷ lệ bệnh nhân không đến theo lịch đã đặt. <br> - **Slot Utilization Rate:** Tỷ lệ khung giờ khám được sử dụng trên tổng số khung giờ có thể cung cấp. <br> - **Rescheduling Success Rate:** Tỷ lệ yêu cầu đổi lịch được xử lý thành công. <br> - **Patient Satisfaction:** Mức độ hài lòng của bệnh nhân với quy trình đặt lịch và tiếp nhận. <br> - **Call Center Workload Reduction:** Mức giảm số lượng yêu cầu đặt lịch và hỏi đáp thông tin cần nhân viên xử lý thủ công. |
| **Quick Architecture** | **AI Patient Access Agent + Appointment Optimization Engine + HIS Integration:** <br> - **Omnichannel Interface:** Tiếp nhận yêu cầu qua Website, Mobile App, Hotline, Chatbot và các kênh giao tiếp khác. <br> - **Speech-to-Text (STT):** Chuyển đổi yêu cầu bằng giọng nói thành văn bản đối với kênh Voicebot. <br> - **LLM + NLP:** Phân tích ý định, trích xuất thông tin bệnh nhân, nhu cầu khám, chuyên khoa và thời gian mong muốn. <br> - **Medical Service Knowledge Base (RAG):** Cung cấp thông tin về chuyên khoa, bác sĩ, dịch vụ, chi phí và hướng dẫn trước khi khám từ nguồn dữ liệu chính thức của VINMEC. <br> - **Appointment Engine:** Truy vấn lịch trống, kiểm tra điều kiện đặt lịch và xử lý đặt/đổi/hủy lịch theo quy tắc nghiệp vụ. <br> - **Scheduling Optimization:** Đề xuất phân bổ lịch khám dựa trên khả năng tiếp nhận, thời lượng khám, lịch làm việc và mức độ ưu tiên đã được quy định. <br> - **Notification Service:** Gửi xác nhận, nhắc lịch và thông báo thay đổi lịch khám. <br> - **HIS/CRM Integration:** Đồng bộ thông tin bệnh nhân, lịch hẹn và trạng thái tiếp nhận với các hệ thống hiện có. <br> - **Human Handover:** Chuyển tiếp cho nhân viên khi yêu cầu phức tạp, thông tin không đủ hoặc có dấu hiệu cần xử lý y tế khẩn cấp. |

**KPI mục tiêu đề xuất cho giai đoạn Pilot (cần xác nhận bằng baseline thực tế):**
- Giảm ít nhất 30% thời gian xử lý trung bình một yêu cầu đặt lịch.
- Booking Automation Rate đạt ≥ 50% đối với các yêu cầu đặt lịch đơn giản.
- Giảm ít nhất 10% tỷ lệ No-show so với baseline hoặc nhóm đối chứng.
- Appointment Booking Success Rate đạt ≥ 95%.
- 0 trường hợp hệ thống tự ý đặt lịch sai bác sĩ, chuyên khoa hoặc khung giờ do lỗi xử lý nghiệp vụ.

**Giá trị kỳ vọng:** Chuyển đổi quy trình tiếp nhận và đặt lịch từ mô hình xử lý thủ công, phân tán qua nhiều kênh sang mô hình Patient Access đa kênh, tự động hóa và điều phối thông minh; giúp bệnh nhân tiếp cận dịch vụ thuận tiện hơn, đồng thời tối ưu công suất sử dụng bác sĩ và phòng khám.

