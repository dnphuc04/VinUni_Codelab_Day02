# Lab 02 — AI Log & Reflection

**Học viên:** Đồng Ngọc Phúc  
**Mã sinh viên:** 2A202603399  
**Công cụ sử dụng:** Trợ lý AI trong ứng dụng Codex  
**Đề tài:** Trợ lý soạn nháp phương án hỗ trợ tài xế Xanh SM gặp sự cố pin.

> Nhật ký này tổng hợp những trao đổi và công việc đã diễn ra trong chat. Các câu đặt trong dấu ngoặc kép ở bảng dưới là yêu cầu đã gửi. Chưa chạy prototype Gemini, chưa có kết quả kiểm thử ranh giới và chưa khảo sát người vận hành thực tế.

## 1. Mục đích sử dụng AI

Tôi sử dụng AI để đọc yêu cầu của bộ lab, xác định các đầu ra cần nộp, hỗ trợ lựa chọn đề tài và xây dựng nội dung báo cáo. Ban đầu tôi yêu cầu AI chỉ khảo sát thư mục và chưa được sửa tệp. Sau khi xem bản nháp, tôi mới yêu cầu ghi nội dung vào từng tệp cụ thể.

AI hỗ trợ đáng kể việc phân tích và soạn thảo. Đây không phải bài viết hoàn toàn do tôi tự soạn rồi chỉ nhờ AI sửa chính tả. Tuy nhiên, các đề xuất của AI vẫn cần được kiểm tra với worksheet, starter code, dữ liệu thử nghiệm và nghiệp vụ thực tế.

## 2. Nhật ký tương tác

| Bước | Yêu cầu đã gửi | AI hỗ trợ gì? | Kết quả và giới hạn |
|---|---|---|---|
| 1. Khảo sát bài lab | “Xem thư mục VinUni_Codelab_Day02 và xác định việc cần làm. Chưa được sửa khi tôi cho phép” | Đọc hướng dẫn, worksheet, ví dụ, starter code và autograder; liệt kê các phần còn thiếu. | Xác định cần 3 báo cáo Markdown, sơ đồ workflow và prototype Python. Ở thời điểm khảo sát, AI chỉ đọc tệp. |
| 2. Chọn đề tài | “chọn đề tài như nào” | Đề xuất tiêu chí chọn tác vụ hẹp, có workflow, bottleneck và metric; so sánh Xanh SM, Vinhomes và Vinpearl. | Đề xuất Xanh SM vì phù hợp starter code và dễ xây dựng ca thử nghiệm. Đây là lựa chọn phục vụ lab, chưa phải kết luận có nhu cầu kinh doanh đã xác nhận. |
| 3. Xây dựng SCAN và Cards | Tôi gửi lại yêu cầu của `01-problem-scan.md`. | Soạn bản nháp gồm 6 bài toán, 3 Quick Problem Cards và lý do chọn đề tài. | Bản nháp được trình bày trong chat trước khi ghi tệp; các mốc thời gian và mục tiêu là giả định thiết kế. |
| 4. Ghi bài SCAN | “điền giúp tôi vào file luôn” | Điền `01-problem-scan.md` bằng nội dung đã đề xuất. | Hoàn thành bản thảo SCAN và 3 cards; không tạo kết quả khảo sát hoặc thử nghiệm. |
| 5. Phân tích sâu | “làm tiếp `02-deep-dive-report.md`” | Xây dựng workflow 5 bước, Problem Statement 6 trường, so sánh Rule/LLM/Agent, future flow, HITL, fallback và kế hoạch kiểm chứng. | Chọn NOT YET do chưa có dữ liệu, baseline thực đo, kết quả prototype hoặc xác nhận của stakeholders. |
| 6. Viết nhật ký | “làm tiếp `03-ai-log.md`” | Tổng hợp quá trình dùng AI và các giới hạn dựa trên chat hiện tại. | Nhật ký chưa bao gồm giai đoạn chạy code; cần cập nhật bằng bằng chứng thực tế khi hoàn thành prototype. |

## 3. AI giúp tôi ở đâu?

AI giúp chuyển một đề bài dài thành các đầu việc cụ thể. Điểm hữu ích là nhận ra phần báo cáo và phần code có những yêu cầu liên quan nhưng không hoàn toàn giống nhau: worksheet yêu cầu ít nhất 3 ca tấn công, trong khi starter code và autograder chỉ đặt ngưỡng tối thiểu 2. Vì vậy bài làm cần theo yêu cầu đầy đủ của worksheet thay vì chỉ cố vượt autograder.

AI cũng giúp thu hẹp đề tài từ “điều vận thông minh” thành “soạn nháp phương án hỗ trợ sự cố pin”. Phạm vi này cho phép tách rõ trách nhiệm: rule xử lý điều kiện xác định, LLM hỗ trợ ngôn ngữ, còn điều phối viên xác minh và phê duyệt. Bản nháp không có quyền tự gửi tin hoặc điều xe.

Trong báo cáo phân tích sâu, AI đề xuất so sánh với rule + template và đo cả thời gian sửa lỗi. Cách đánh giá này giúp tránh kết luận LLM có ích chỉ vì nó tạo được câu trả lời nhanh. Nếu người duyệt phải sửa nhiều hoặc template đơn giản đạt chất lượng tương đương với chi phí thấp hơn, phần LLM có thể không đáng triển khai.

## 4. Điểm AI trả lời chưa chuẩn hoặc có nguy cơ gây hiểu nhầm

### 4.1. Bỏ sót nội dung tệp hiện tại trong lần ghi SCAN

Trước khi ghi `01-problem-scan.md`, AI đã đọc một tệp có sẵn chứa phần hướng dẫn và một dòng bài toán đã điền. Sau khi ghi xong, AI nói “tạo” tệp và mô tả ghi chú giả định như đã được giữ lại, trong khi bản cũ vừa đọc không có ghi chú đó. Mô tả chính xác phải là **đã cập nhật tệp hiện có và bổ sung ghi chú giả định**.

Đây là sai sót trong cách tường thuật thay đổi. Bài học là cần đối chiếu trạng thái tệp trước và sau khi thao tác, không chỉ dựa vào lời báo hoàn thành của AI.

### 4.2. Các con số do AI đề xuất chưa phải bằng chứng

AI đề xuất baseline soạn nháp 5 phút, mục tiêu ≤2 phút và kịch bản 30 lượt/ngày. Những con số này có thể dùng để thiết kế phép thử, nhưng chưa được đo tại Xanh SM. Không được trình bày chúng như thống kê doanh nghiệp hoặc mức tiết kiệm đã đạt được.

Báo cáo deep-dive đã ghi rõ tính giả định và yêu cầu đo lại. Ví dụ, 90 phút công/ngày là phép tính minh họa `30 × (5 − 2)`, chưa trừ công sửa lỗi, chi phí API và duy trì. Tôi chưa có cơ sở để khẳng định ROI thực tế.

### 4.3. Quy tắc của lab dễ bị hiểu thành quy tắc vận hành thực tế

Ngưỡng pin dưới 5% và khoảng cách 5 km xuất phát từ đề bài. Chúng không đủ để kết luận một xe có thể di chuyển an toàn trong điều kiện thực tế. Báo cáo đã giới hạn các ngưỡng này là quy tắc dùng để kiểm thử prototype.

Tương tự, mã `dispatch_mobile_charger` chỉ biểu thị một đề xuất trong bản nháp. Nếu diễn đạt thành “AI đã điều xe” thì sẽ vượt quá phạm vi và không đúng với hệ thống đang có.

### 4.4. Chưa phát hiện lỗi đầu ra Gemini vì chưa chạy Gemini

Chưa có bằng chứng mô hình đã bỏ thẻ `[DRAFT_ONLY]`, bịa trạm sạc hoặc đề xuất trạm quá xa trong một lần chạy thực tế. Đây mới là các nguy cơ cần kiểm thử. Tôi không ghi chúng thành những hallucination đã quan sát và cũng không nhận rằng mọi ca tấn công đã vượt qua.

## 5. Tôi đã điều chỉnh yêu cầu và ranh giới như thế nào?

Trong trao đổi thực tế, tôi điều chỉnh yêu cầu theo từng bước: bắt đầu bằng khảo sát chỉ đọc, hỏi cách chọn đề tài, đưa lại tiêu chí SCAN/Cards, rồi yêu cầu ghi từng báo cáo. Cách làm này giúp kiểm soát phạm vi thay đổi và có bản nháp để xem trước khi ghi tệp.

Các ranh giới dưới đây đã được đưa vào **thiết kế báo cáo**, chưa phải kết quả đã kiểm chứng trong system prompt chạy thật:

- Chỉ dùng dữ kiện được cung cấp hoặc đã xác minh; thiếu dữ liệu thì hỏi lại hoặc chuyển người xử lý.
- Giữ `[DRAFT_ONLY]` ở đầu output và yêu cầu phê duyệt của con người.
- Áp dụng quy tắc pin của lab bằng code, không chỉ dựa vào lời nhắc trong prompt.
- Không cho nội dung tài xế gửi thay đổi chỉ thị hệ thống hoặc cấp quyền tự gửi tin.
- Chặn output sai định dạng hoặc trái ranh giới và quay về template hoặc workflow thủ công.

Tôi chưa thực hiện vòng lặp “chạy Gemini → thấy lỗi → sửa system prompt → chạy lại”. Phần này cần được bổ sung vào nhật ký sau khi có output thực tế; không nên viết trước một câu chuyện sửa prompt chưa diễn ra.

## 6. Tự đánh giá và bài học

Qua phần scoping, tôi thấy AI hữu ích nhất khi giúp cấu trúc bài toán và chỉ ra điều kiện cần kiểm chứng. Một báo cáo có nhiều chi tiết và metric vẫn có thể thiếu bằng chứng nếu quy trình, baseline và nhu cầu của người dùng mới chỉ là giả định.

Tôi cũng nhận ra cần phân biệt ba mức: thiết kế được một ranh giới, triển khai được cơ chế kiểm tra và chứng minh cơ chế đó hoạt động trên bộ thử nghiệm. Hiện tại bài làm chủ yếu đạt mức thiết kế; chưa đủ cơ sở để nhận rằng prototype an toàn hoặc sẵn sàng triển khai. Vì vậy quyết định NOT YET phù hợp hơn GO ở giai đoạn này.

## 7. Những việc cần bổ sung sau khi chạy prototype

| Nội dung cần ghi lại | Bằng chứng cần có |
|---|---|
| System prompt và cấu hình thực tế | Nội dung prompt, model và cấu hình đã dùng |
| Các ca kiểm thử | Đầu vào, kỳ vọng và output nguyên bản; ít nhất 3 ca tấn công |
| Lỗi quan sát được | Trường hợp sai định dạng, sai dữ kiện hoặc vượt ranh giới, nếu có |
| Cách sửa | Thay đổi prompt hoặc code cụ thể và lý do |
| Kết quả chạy lại | So sánh trước/sau, gồm cả lỗi vẫn còn |
| Hiệu quả và chi phí | Thời gian có tính sửa lỗi, tỷ lệ chấp nhận, độ trễ và lượng sử dụng API |

**Cập nhật giai đoạn hoàn thiện:** Đã tạo sơ đồ PNG, thử phong cách dạng bảng rồi khôi phục phiên bản xếp dọc theo yêu cầu. AI đã hoàn thiện code gọi Gemini, loader `.env`, 9 ca kiểm thử và lớp rule/validator/fallback. Đã chạy 22 kiểm thử cục bộ: 22 đạt. Có kiểm thử giả lập lỗi API và output sai để bảo đảm fallback không bị báo là Gemini thành công.

Lỗi môi trường quan sát được: lệnh `python` không nằm trong PATH; môi trường ảo có sẵn chạy được khi dùng đường dẫn `.venv/Scripts/python.exe` với quyền thực thi phù hợp. Lần chạy prototype trực tiếp dừng do không nhận API key. Không có output Gemini để đánh giá hallucination hoặc vòng sửa prompt dựa trên kết quả thật.

**Trạng thái cuối nhật ký:** đã hoàn thiện tài liệu, sơ đồ và code; kiểm thử cục bộ đạt, vẫn cần xác nhận chạy Gemini và cập nhật bằng chứng. Chưa triển khai nghiệp vụ thực tế.


## 8. Cập nhật thực nghiệm sau khi cấu hình API key

Các phần ghi “chưa chạy Gemini” phía trên phản ánh giai đoạn soạn tài liệu ban đầu. Sau đó đã lưu key trong `.env` bị Git bỏ qua và gọi API thật. Không đưa key vào bài nộp.

Model 2.5 Flash trả 404, API đề xuất 3.8 Flash nhưng lời gọi gặp 504. Chuyển sang 3.1 Flash Lite có trong danh sách model. Lần đầu có 6/9 ca vượt kiểm tra tự động; review phát hiện diễn đạt như đã ghi nhận yêu cầu, tự gọi trạm là gần nhất và suy diễn thiếu dữ liệu. Prompt được sửa để bắt đầu bản nháp bằng lời đề xuất chờ duyệt và cấm các khẳng định chưa có căn cứ.

Lần tiếp theo đạt 8/9 kiểm tra: ca dữ liệu mâu thuẫn chọn điều phối sạc thay vì hỏi lại; lớp rule phát hiện action sai và dùng fallback, không báo là mô hình đạt. Tôi bổ sung vào system prompt thứ tự ưu tiên: dữ liệu thiếu/mâu thuẫn phải xác minh trước khi xét ngưỡng pin. Lần chạy sau gặp thêm lỗi 429, nên chuyển lời gọi từ song song sang tuần tự. Đây là lỗi API, không phải hallucination.

Bằng chứng input/output trước và sau được lưu trong `evidence/`. Chưa đo baseline người dùng hoặc lợi ích kinh doanh; quyết định NOT YET được giữ nguyên. Kết quả cấu trúc/action tự động không thay thế người duyệt toàn bộ câu văn.


### Kết quả chạy lại cuối cùng

Kết quả cuối: 3/3 ca tấn công bắt buộc và 9/9 ca mở rộng vượt kiểm tra cấu trúc/action; Gemini 3.1 Flash Lite, không dùng fallback trong lần chạy cuối. Độ trễ từng ca mở rộng: 0.941–3.587 giây; tổng thời gian lời gọi tuần tự 13.704 giây. Đây là thời gian API, không phải thời gian thao tác nghiệp vụ có người duyệt.

AI hỗ trợ review thấy B6 vẫn gán nguồn dữ liệu chưa được xác minh cho hai mức pin. Điểm này cho thấy vượt kiểm tra tự động không đồng nghĩa đúng mọi câu văn. Chưa có xác nhận review nghiệp vụ của điều phối viên thật. Các output gốc được giữ nguyên, không chỉnh thành kết quả đẹp hơn.

**Xác nhận cuối:** Autograder đầy đủ đạt 10.00/10.00 sau khi chạy lại vì một lần lỗi API tạm thời. Kết quả này không thay thế chấm nội dung của giảng viên. `.env` được Git bỏ qua; chưa commit/push bài. Những đoạn ghi trạng thái chưa chạy ở các mục trước là lịch sử quá trình, đã được cập nhật bằng kết quả ở mục 8.
