import os, math, io, json, xml.etree.ElementTree as ET
from pathlib import Path
import cairosvg
from pypdf import PdfReader,PdfWriter
O=Path(__file__).parent
PUR='#49346c'; GOLD='#ba8b44'; WHITE='#f5eef8'; PINK='#efa9c6'; CUT='#d52648'
blade='M -24 0 L 24 0 C 33 240 12 550 -49 726 Q -56 740 -64 740 Q -70 739 -65 726 C -17 535 -18 238 -24 0 Z'
sheath='M -34 0 L 34 0 C 46 260 13 597 -57 760 Q -64 775 -70 775 Q -85 775 -80 749 C -28 540 -25 232 -34 0 Z'
# All drawing coordinates are millimetres. No embedded raster images.
def text(x,y,s,size=4,color='#302d3c'):
 import html
 return f'<text x="{x}" y="{y}" font-family="DejaVu Sans" font-size="{size}" fill="{color}">{html.escape(s)}</text>'
def path(d,fill='none',stroke=CUT,sw=.45,extra=''):
 return f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" {extra}/>'
def rect(x,y,w,h,fill='none',stroke=CUT,r=0):
 return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}" stroke-width="0.4"/>'
def group(id,s,tr=''):
 return f'<g id="{id}" inkscape:groupmode="layer" inkscape:label="{id}" transform="{tr}">{s}</g>'
def dim(x,y,h,label):
 return path(f'M {x} {y} v {h} m -3 {-h} h 6 m -6 {h} h 6','none','#777',.3)+text(x+3,y+h/2,label,3.5)
def flower(x,y,r=9):
 s=''
 for i in range(5):
  a=i*72
  s+=f'<ellipse cx="0" cy="{-r*.55}" rx="{r*.39}" ry="{r*.60}" fill="{PINK}" stroke="#ba668e" stroke-width=".3" transform="translate({x} {y}) rotate({a})"/>'
 return s+f'<circle cx="{x}" cy="{y}" r="{r*.19}" fill="{GOLD}"/>'
def guard(x,y,filled=False):
 d='M -65 0 Q -56 -18 -31 -13 Q -18 -26 0 -14 Q 18 -26 31 -13 Q 56 -18 65 0 Q 56 18 31 13 Q 18 26 0 14 Q -18 26 -31 13 Q -56 18 -65 0 Z'
 return group('C1_guard',path(d,GOLD if filled else 'none')+rect(-10.5,-5.5,21,11),f'translate({x} {y})')
def heading(n,title,w,h):
 return text(12,15,f'SAKURA / {n:02d} — {title}',6)+text(12,24,f'Đơn vị mm • Bản mẫu thủ công EVA • Khổ {w} × {h} mm',3.5)
def legend(y):
 return text(12,y,'Đỏ liền: CẮT • Xanh đứt: GẤP • Xám chấm: THAM CHIẾU',3.3)+path(f'M 12 {y+5} h 45','none','#278dba',.4,'stroke-dasharray="4 2"')+path(f'M 70 {y+5} h 45','none','#888',.4,'stroke-dasharray="1 2"')+rect(12,y+12,100,10)+text(12,y+28,'Ô kiểm tra: 100 × 10 mm. In 100%, không Fit to page.',3.3)
def svg(w,h,s):
 return f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape" width="{w}mm" height="{h}mm" viewBox="0 0 {w} {h}"><rect width="{w}" height="{h}" fill="white"/>{s}</svg>'
pages=[]
# Overview — assembly at true scale, guard is 10 mm thick along length.
s=heading(1,'TỔNG THỂ',420,1120)
s+=group('A_body',path(blade,PUR,GOLD), 'translate(150 310)')
s+=group('B_handle',rect(132,50,36,250,PUR,GOLD,8))
for y in range(66,285,24):
 s+=path(f'M 133 {y} L 167 {y+17} L 167 {y+25} L 133 {y+8} Z',WHITE,GOLD,.25)
s+=guard(150,305,True)+flower(150,305,12)
s+=group('D_sheath',path(sheath,WHITE,GOLD),'translate(315 280)')
s+=path('M 323 285 C 344 530 309 812 245 1033 L 237 1025 C 291 780 309 492 298 284 Z',PUR,GOLD)
for x,y in [(320,390),(310,520),(290,650),(278,785),(250,930)]: s+=flower(x,y,12)
s+=path('M 245 970 C 300 750 274 610 327 365','none','#795064',2)
s+=dim(55,50,1000,'1.000 mm')+dim(190,50,250,'250 chuôi')+dim(190,300,10,'10 chắn')+dim(190,310,740,'740 thân')
s+=text(230,1068,'D: vỏ trang trí kín, dài 775 mm',3.7)+text(12,1090,'Tỷ lệ suy luận từ ảnh; hoa văn giản lược. Vỏ đặt cạnh, không dùng để tra kiếm.',3.5)
pages.append(('01_tong_the',420,1120,s))
# Cut parts packed at actual scale
s=heading(2,'MẪU CẮT KẾT CẤU 1:1',420,1120)
s+=text(22,40,'A1 × 1 / EVA 10 mm / thân 740 + nối 80',3.7)
s+=group('A1_cut',path(blade.replace('M -24 0 L 24 0', 'M -24 0 L -10 0 L -10 -80 L 10 -80 L 10 0 L 24 0')), 'translate(100 135)')
s+=path('M 76 135 h 48','none','#888',.3,'stroke-dasharray="1 2"')
s+=dim(145,55,80,'nối 20 × 80 × 10')+dim(145,135,740,'740')
s+=text(208,40,'D1 × 2 / EVA 5 mm / cao 775',3.7)
s+=group('D1_cut',path(sheath),'translate(300 60)')
s+=text(208,850,'Dán 2 mặt kín; tổng dày 10 mm.',3.6)
s+=text(22,908,'B1 / B2: 2 má chuôi, EVA 5 mm',3.5)
s+=rect(22,920,36,250,r=0) if False else ''
# Horizontal handle blanks fit below blade
s+=rect(22,922,250,36)+text(25,943,'B1: 250 × 36 × 5 — mặt trước',3.5)
s+=rect(22,968,250,36)+text(25,989,'B2: 250 × 36 × 5 — mặt sau',3.5)
s+=guard(340,930)+text(278,965,'C1: 130 × ~40 × 10',3.2)+text(278,973,'Lỗ 21 × 11 xuyên dày 10',3.2)
s+=text(22,1020,'B3 lớp giữa: xem trang 3. A1: nối liền thân, không cắt rời thanh nối.',3.5)
s+=text(22,1028,'Đầu thân bo tù ~R6; toàn bộ cạnh EVA được làm tròn bằng giấy nhám nhẹ.',3.5)
s+=legend(1050)
pages.append(('02_mau_cat',420,1120,s))
# Joint page: horizontal dimensions to fit
s=heading(3,'CHUÔI & MỐI NỐI 1:1',420,310)
s+=text(12,36,'Chọn thanh nối trước: A1 = 20 rộng × 10 dày × 80 dài mm.',4)
s+=text(12,44,'Qua chắn C1 dày 10 → phần ngậm trong chuôi 70 mm.',3.8)
s+=rect(20,65,250,36)+rect(197.5,72.75,72.5,20.5)
s+=text(22,60,'B3 / EVA 10 mm / 250 × 36; cắt bỏ rãnh đỏ bên phải',3.5)
s+=text(24,88,'Phần giữ lại: 177,5 × 36',3.2)
s+=text(177,111,'Rãnh hở đầu: 20,5 × 72,5 × 10',3.5)
s+=text(12,126,'Mặt cắt lắp: B1 5 mm + B3 10 mm + B2 5 mm = chuôi dày 20 mm',3.5)
s+=rect(20,137,250,5,WHITE)+rect(20,142,177.5,10,PUR)+rect(20,152,250,5,WHITE)
s+=rect(200,142,70,10,'#bd9cd7')+rect(270,137,10,20,GOLD)+rect(280,142,45,10,PUR)
s+=text(25,168,'Chừa 2,5 mm cuối rãnh; khe rộng dư 0,5 mm tổng.',3.4)
s+=text(25,177,'Chiều dày rãnh = EVA đo thực tế; chỉnh lớp đệm trước khi dán kín.',3.4)
s+=text(12,194,'T1 thử khớp: cắt từ phế liệu cùng tấm trước khi làm chuôi.',3.7)
s+=rect(20,205,20,40)+text(18,253,'Nối thử 20 × 40',3)
s+=rect(85,205,36,45)+rect(92.75,215,20.5,35)+text(80,258,'Rãnh thử 20,5',3)
s+=text(145,213,'1. Thử khô; phải trượt vào bằng tay, không ép mạnh.',3.4)
s+=text(145,224,'2. Chật: nới rãnh từng 0,2 mm; lỏng: thêm giấy đệm.',3.4)
s+=text(145,235,'3. Keo thủ công tương thích EVA; thử trên phế liệu.',3.4)
s+=text(145,246,'4. Không sơn hoặc dán phủ bề mặt mối nối trước thử khít.',3.4)
s+=legend(267)
pages.append(('03_chuoi_moi_noi',420,310,s))
# Decor sheet
s=heading(4,'HỌA TIẾT CẮT RỜI 1:1',420,304)
s+=text(12,37,'E1 hoa anh đào Ø20 / 12 bông; giấy màu hoặc EVA 1 mm',3.5)
for i in range(12): s+=flower(25+(i%6)*29,55+(i//6)*28,10)
s+=text(210,38,'E2 / 8 hình thoi trắng 24 × 16',3.5)
for i in range(8):
 x=225+(i%4)*42;y=55+(i//4)*30
 s+=path(f'M {x} {y-12} l 8 12 l -8 12 l -8 -12 Z',WHITE)
s+=text(12,110,'E3 / cành đơn giản 120 × 35 / in 2 bản',3.5)
s+=group('E3_branch',path('M 15 151 Q 70 140 135 116 L 133 120 Q 72 145 15 154 Z','#795064')+path('M 55 143 l -10 -22 l 4 0 l 12 20 Z','#795064')+path('M 95 132 l 9 17 l 3 -1 l -8 -19 Z','#795064'))
s+=text(210,110,'E4 / 4 viền vàng 150 × 3',3.5)
for i in range(4): s+=rect(210,119+i*8,150,3,GOLD)
s+=text(12,174,'C2 / 2 lớp cánh vàng 100 × 30 / EVA 1 mm',3.5)
for x in [70,175]:
 s+=group('C2_petals_'+str(x),path('M -50 0 Q -40 -15 -20 -8 Q 0 -22 20 -8 Q 40 -15 50 0 Q 30 15 0 9 Q -30 15 -50 0 Z',GOLD),f'translate({x} 195)')
s+=text(242,174,'E5 tua giấy 80 × 60',3.5)+rect(250,182,80,60,PUR)
for x in range(255,330,5): s+=path(f'M {x} 192 v 50')
s+=path('M 250 192 h 80','none','#278dba',.4,'stroke-dasharray="4 2"')
s+=text(12,224,'E6 / dây tím mềm 8 × 1.200 mm: cắt từ ruy băng, không phải mẫu trên trang.',3.5)
s+=text(12,234,'Nền trắng/tím: sơn theo tổng thể hoặc dùng đường viền A1/D1 làm mẫu giấy bọc.',3.5)
s+=text(12,244,'Hoa/cành rời là chi tiết bổ sung; không phải khuôn bọc toàn bộ vỏ.',3.5)
s+=legend(261)
pages.append(('04_trang_tri',420,304,s))
# Assembly illustrated
s=heading(5,'LẮP RÁP & VẬT LIỆU',420,297)
steps=[('01 / CẮT & THỬ', 'Cắt A1 liền nối. Thử T1, đo EVA thực tế.'),('02 / DÁN CHUÔI','Dán B3 lên B2, giữ rãnh sạch keo.'),('03 / GHÉP NỐI','Luồn C1, đưa nối vào rãnh, dán B1.'),('04 / TRANG TRÍ','Dán C2, quấn dây, dán hoa và viền.'),('05 / LÀM VỎ KÍN','Dán D1 × 2; sơn, thêm cành hoa.'),('06 / TRƯNG BÀY','Để keo khô theo nhãn; đỡ cả thân và chuôi.')]
for i,(title,desc) in enumerate(steps):
 x=12+(i%3)*135;y=44+(i//3)*86
 s+=text(x,y,title,4)+text(x,y+9,desc,2.9)
 if i==0:s+=rect(x+15,y+20,20,35,PUR)+rect(x+50,y+20,36,35,WHITE)+rect(x+57.75,y+25,20.5,30)
 elif i==1:
  for j in range(3):s+=rect(x+10+j*8,y+20+j*9,90,6,[WHITE,PUR,WHITE][j])
 elif i==2:s+=rect(x+10,y+27,50,20,WHITE)+rect(x+66,y+20,10,34,GOLD)+rect(x+83,y+32,35,10,PUR)+path(f'M {x+110} {y+57} h -70 l 5 -3 m -5 3 l 5 3','none','#777')
 elif i==3:s+=guard(x+62,y+33,True)+flower(x+62,y+33)
 elif i==4:s+=rect(x+10,y+25,100,13,WHITE,GOLD,5)+flower(x+45,y+31,8)
 else:s+=path(f'M {x+15} {y+40} h 95 m -80 0 v 12 m 65 -12 v 12','none',GOLD,2)+rect(x+10,y+25,105,10,PUR,GOLD,4)
s+=text(12,223,'Vật liệu dự kiến: EVA 10 mm (1 tấm 500 × 1.000); EVA 5 mm (1 tấm 500 × 1.000).',3.4)
s+=text(12,233,'EVA 1 mm/giấy màu; ruy băng 8 mm × 1,2 m; keo tương thích EVA; sơn gốc nước.',3.4)
s+=text(12,243,'Không dùng lõi kim loại, không mài sắc. Mô hình mềm chỉ dùng trang trí.',3.4)
s+=text(12,253,'Vỏ kín độc lập: KHÔNG tra thân vào. Muốn vỏ rỗng cần bản thiết kế khác.',3.4)
s+=text(12,263,'Kiểm tra in 100 mm → thử T1 → cắt kết cấu → thử khô → dán → trang trí.',3.4)
s+=text(12,277,'Đã kiểm tra hình học số; chưa chế tạo thử, chưa xác nhận độ khít vật liệu thật.',3.4)
pages.append(('05_lap_rap',420,297,s))
writer=PdfWriter()
for name,w,h,s in pages:
 data=svg(w,h,s).encode(); (O/(name+'.svg')).write_bytes(data)
 pdf=cairosvg.svg2pdf(bytestring=data); (O/(name+'.pdf')).write_bytes(pdf)
 writer.add_page(PdfReader(io.BytesIO(pdf)).pages[0])
 cairosvg.svg2png(bytestring=data,write_to=str(O/(name+'.png')),output_width=1000)
with open(O/'Sakura_5_trang_vector.pdf','wb') as f:writer.write(f)
# Vector-only A4 tiles: 10 mm overlap; 190 x277 mm printable area with 10 mm borders.
tiles=PdfWriter(); manifest=[]
for name,w,h,s in pages[1:4]:
 nx=math.ceil(max(0,w-190)/180)+1;ny=math.ceil(max(0,h-277)/267)+1
 for row in range(ny):
  for col in range(nx):
   x=col*180;y=row*267
   nested=f'<svg x="10" y="10" width="190" height="277" viewBox="{x} {y} 190 277">{s}</svg>'
   marks=''
   for mx,my in [(10,10),(200,10),(10,287),(200,287)]:marks+=path(f'M {mx-2} {my} h 4 m -2 -2 v 4','none','#111',.2)
   # Interior crosses coincide with neighbouring tile's overlap boundaries.
   for mx in [10,20,190,200]:
    for my in [10,20,277,287]:marks+=path(f'M {mx-1.5} {my} h 3 m -1.5 -1.5 v 3','none','#999',.15)
   label=text(10,6,f'{name} / hàng {row+1}-{ny} / cột {col+1}-{nx} / gốc {x},{y} mm',2.5)
   label+=text(10,293,'100% • Chồng 10 mm • Cắt mép trắng; căn nét và dấu + trong vùng chồng',2.5)
   pdf=cairosvg.svg2pdf(bytestring=svg(210,297,nested+marks+label).encode())
   tiles.add_page(PdfReader(io.BytesIO(pdf)).pages[0]);manifest.append({'sheet':name,'row':row+1,'column':col+1,'origin_mm':[x,y]})
with open(O/'Mau_cat_ghep_A4_100pct.pdf','wb') as f:tiles.write(f)
(O/'so_do_ghep_A4.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
print('Created',len(pages),'SVG sheets;',len(tiles.pages),'A4 vector tiles')
