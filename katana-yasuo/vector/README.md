# Katana Yasuo — bóc tách vector chỉnh sửa

Dựng lại bằng đường vector từ ảnh katana đã tạo, giữ xanh chàm, thép bạc, vàng cổ và hoa văn gió. Đây là diễn giải 2D của ảnh, không phải tách chính xác mọi điểm ảnh hoặc bản render 3D. Không bo tù đầu kiếm, không đặt bán kính bo tự động lên góc hình học. Các đường cong trang trí và dáng cong katana vẫn giữ.

## Mở trong Adobe Illustrator
1. Tải ZIP bên dưới, giải nén.
2. File > Open > `Yasuo_vector_tong_the.svg` để sửa bản lắp, hoặc `Yasuo_boc_tach.svg` để xem các phần đặt riêng.
3. Trong Layers, mở các Group theo mã. Illustrator có thể nhập SVG thành các group dưới một layer; kéo nhóm ra layer riêng nếu cần. Không khẳng định nhóm SVG tự động trở thành 13 layer Illustrator.
4. Dùng Direct Selection (A) chỉnh node; Object > Ungroup khi cần. Hoa văn có clipping group; vào Isolation Mode hoặc Object > Clipping Mask > Release để sửa ngoài khung. Việc release có thể làm lộ nét ngoài viền.
5. File > Save As > Adobe Illustrator (.ai). Môi trường này không xuất trực tiếp .ai gốc và chưa kiểm tra bằng ứng dụng Illustrator.
6. Có PDF vector thay thế để mở trực tiếp. Không dùng PNG làm file chỉnh sửa chính.

## Nội dung
- `Yasuo_vector_tong_the.svg/pdf/png`: bản lắp ráp mỹ thuật với nhóm nền có thể xóa.
- `Yasuo_boc_tach.svg/pdf/png`: trang xem các bộ phận rời. Các nhóm có tỷ lệ bố trí khác nhau, không dùng đo hoặc in cắt.
- `01` thân; `02` viền sáng và hamon; `03` khắc trên thân; `04` lõi chuôi; `05` dây quấn; `06` đầu chuôi; `07` chắn tay xoáy; `08` dải vải; `09` thân vỏ; `10` hoa văn vỏ; `11` đai kim loại; `12` dây buộc; `13` gió.
- Mỗi nhóm có SVG độc lập; nhóm viền/hoa văn/gió có nền trong, có thể trông ít hình khi mở riêng.
- Màu sắc dùng gradient vector, không nhúng ảnh. Bản tổng thể dùng phối cảnh tương đối giống ảnh gốc; không phải hình chiếu kỹ thuật.

## Phạm vi
Theo yêu cầu lần này: chỉ bóc tách hình ảnh để chỉnh trong Illustrator. Không có thanh nối, rãnh, độ dày, dung sai hoặc tỷ lệ gia công 1:1. Đơn vị hiện tại là đơn vị đồ họa px; hãy đặt kích thước mong muốn trong Illustrator. Các nét trang trí không tự động là đường cắt. Hiệu ứng chất liệu, ánh sáng và độ chi tiết không giống hoàn toàn ảnh raster.

Đã kiểm tra XML SVG, ID không trùng, số nhóm và PDF không chứa ảnh raster. Đã xem ảnh xuất từ bản tổng thể. Chưa thử mở bằng Illustrator.
