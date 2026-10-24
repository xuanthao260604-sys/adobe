# Sakura — mô hình trang trí EVA, bản thiết kế v1

## Đọc trước
Đây là bản vector giản lược theo ảnh tham khảo do người dùng cung cấp, không phải bản truy nguyên chính xác mẫu gốc. Không có kích thước thật trong ảnh. Các số đo sau là giả định thiết kế, có thể chỉnh trong SVG. Chưa chế tạo thử; chưa chứng nhận sẵn sàng sản xuất.

Ảnh có chuôi chiếm khoảng một phần tư chiều dài, thân cong thanh mảnh, chắn tay dạng cánh hoa, màu tím/trắng/vàng và hoa anh đào. Bản này giữ bảng màu, đường cong và hoa, bỏ các gai vàng nhỏ, hiệu ứng sáng và chi tiết chạm nổi phức tạp. Chuôi thực tế làm thẳng, vỏ kín dán hai mặt, không có khoang tra kiếm. Đầu EVA bo tù; không thêm lõi kim loại hoặc cạnh sắc.

## Các file
- 01_tong_the.svg/pdf/png: tổng thể 420 × 1120 mm, tỷ lệ 1:1.
- 02_mau_cat.svg/pdf/png: mẫu cắt A1, B1/B2, C1, D1, khổ 420 × 1120 mm.
- 03_chuoi_moi_noi.svg/pdf/png: B3, mặt cắt và mẫu thử T1; 420 × 310 mm.
- 04_trang_tri.svg/pdf/png: hoa, cành, thoi trắng, viền vàng, tua; 420 × 304 mm.
- 05_lap_rap.svg/pdf/png: hướng dẫn minh họa, khổ A3 ngang; hình lắp chỉ minh họa, không dùng làm mẫu cắt.
- Sakura_5_trang_vector.pdf: gộp đủ 5 trang, giữ kích thước trang gốc.
- Mau_cat_ghep_A4_100pct.pdf: 27 trang A4 cho trang 2–4, đã chia sẵn, không dùng chức năng Poster thêm lần nữa.
- so_do_ghep_A4.json: ánh xạ trang nguồn, hàng/cột và gốc tọa độ từng mảnh.
- KIEM_TRA.json: kết quả kiểm tra số hóa.
- build.py: mã tạo bản vẽ, không cần chạy để dùng file. Nếu muốn tái tạo cần Python, cairosvg và pypdf.

SVG chứa đường vector và văn bản chỉnh sửa được, không nhúng PNG. Các nhóm có mã nhận diện. Mở bằng File > Open trong Illustrator, sau đó Save As .ai nếu cần. Chưa kiểm tra trực tiếp bằng Illustrator. PDF giữ đường nét vector; chữ vẫn dùng font nhúng của bộ xuất, trong SVG dùng DejaVu Sans (có thể bị thay font nếu máy không có). Chỉ PNG dùng để xem nhanh, không dùng làm mẫu đo.

## Kích thước và số lượng
| Mã | Số | Kích thước mm | Vật liệu |
|---|---:|---|---|
| A1 | 1 | Thân lộ 740; rộng gốc 48; nối 20 × 80; dày 10 | EVA 10 |
| B1/B2 | mỗi mã 1 | 250 × 36 × 5 | EVA 5 |
| B3 | 1 | 250 × 36 × 10; rãnh hở đầu 20,5 × 72,5 | EVA 10 |
| C1 | 1 | Rộng 130, cao xấp xỉ 40; dày 10; lỗ 21 × 11 | EVA 10 |
| C2 | 2 | Khung 100 × 30 danh nghĩa | EVA 1 / giấy màu |
| D1 | 2 | Dài 775; rộng miệng 68; theo đường cong SVG | EVA 5 |
| E1 | 12 | Hoa Ø20 danh nghĩa | EVA 1 / giấy màu |
| E2 | 8 | Hình thoi cao 24 × rộng 16 | Giấy trắng |
| E3 | 1 mẫu, in 2 bản | Bao 120 × 38 xấp xỉ | Giấy nâu |
| E4 | 4 | 150 × 3 | Giấy vàng |
| E5 | 1 | 80 × 60; chừa đầu 10; tua cách 5 | Giấy tím mềm |
| E6 | 1 | 8 × 1200 (cắt bằng thước, không có khuôn dài) | Ruy băng tím |

Các kích thước hoa/cánh/cành là khung danh nghĩa, không phải đường chữ nhật cắt thêm. Cắt theo đường viền hình. D1 dùng một khuôn hai lần. Vật liệu gợi ý: 1 tấm EVA 10 mm 500 × 1000 và 1 tấm EVA 5 mm 500 × 1000; xếp 2 D1 cạnh nhau, chuôi tận dụng phần còn lại. Kiểm tra xếp phôi trước khi cắt vì kích thước tấm bán thực tế có thể khác.

## Mối nối
Tổng dài theo trục dọc: 250 chuôi + 10 chắn + 740 thân = 1000 mm. Thanh nối dài 80 xuyên chắn dày 10, còn 70 nằm trong chuôi. Rãnh sâu 72,5 nên dư 2,5 mm cuối; rộng 20,5 so với nối 20 nên dư tổng 0,5 mm, 0,25 mỗi bên khi căn giữa. Rãnh dày bằng lớp EVA B3 danh nghĩa 10; EVA thật phải đo và thử. Lỗ chắn rộng 21 × dày 11 giúp luồn thanh 20 × 10.

Cắt T1 trên phế liệu cùng tấm, xếp thử giữa hai má EVA 5. Nếu chật nới từng 0,2 mm; nếu lỏng thêm giấy đệm. Đây là mối dán EVA mềm, không phải mối chịu lực. Để rãnh và nối sạch sơn. Dán B3 lên B2, luồn C1 qua nối, thử khô, bôi keo phù hợp EVA, đặt nối vào rãnh rồi đóng B1. Keo theo hướng dẫn hãng; thử trên phế liệu vì một số dung môi làm hỏng EVA. Dán hai D1 thành vỏ kín riêng; sơn gốc nước rồi trang trí.

## In ghép
1. In Mau_cat_ghep_A4_100pct.pdf ở Actual size / 100%, giấy A4, tắt Fit/Shrink. Không in PNG.
2. Kiểm tra ô 100 × 10 mm bằng thước trước. Nếu sai, chỉnh thiết lập máy in, không bù bằng co giãn tùy ý từng trang.
3. Trang 2: 3 cột × 5 hàng = 15 mảnh. Trang 3: 3 × 2 = 6. Trang 4: 3 × 2 = 6. Thứ tự từng bộ là từ trái sang phải rồi xuống hàng.
4. Vùng in mỗi mảnh 190 × 277, lề 10 mm. Bước ghép ngang 180, dọc 267, chồng 10 mm. Cắt bỏ mép trắng theo khung; dấu + trong phần chồng có cùng tọa độ nguồn giữa hai mảnh. Căn dấu + và đường nét trước khi dán băng keo mặt sau.
5. Một số mảnh ít hình do giữ nguyên bố cục nguồn. Không bỏ mảnh nếu chưa đối chiếu sơ đồ.
6. Bản gốc PDF có khổ dài hơn A3; không chọn A4 rồi Fit khi dùng làm khuôn. Tổng thể chỉ xem hoặc in khổ lớn, không có trong bộ A4 để tiết kiệm giấy.

Đường đỏ liền: cắt. Xanh đứt: gấp (tua giấy). Xám chấm: tham chiếu, không cắt đứt gốc nối. Màu sắc thuộc nhóm trang trí; đường viền đỏ là nét hướng dẫn, có thể ẩn/xóa trong bản sao trước khi in trang trí.

## Kiểm tra và giới hạn
Đã xuất và đọc lại SVG/PDF, kiểm tra kích thước trang bằng mm, xác minh PDF không chứa ảnh raster, số mảnh A4 và phép tính mối nối. Đã xem PNG trang cắt và mối nối. Chưa in vật lý, chưa kiểm tra dung sai EVA hoặc độ bền keo, chưa mở bằng Adobe Illustrator. Thử T1 và đo ô chuẩn trước khi làm bản hoàn chỉnh. Chưa xác nhận mọi họa tiết khớp bản gốc; đây là thiết kế thủ công đơn giản hóa.
