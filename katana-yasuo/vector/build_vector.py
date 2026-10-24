from pathlib import Path
import math,random,io,json,zipfile,xml.etree.ElementTree as ET
import cairosvg
from pypdf import PdfReader,PdfWriter
P=Path(__file__).parent
random.seed(21)
def path(d,f='none',s='none',w=.6,extra=''):
 return f'<path d="{d}" fill="{f}" stroke="{s}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round" {extra}/>'
COUNTS={}
def g(id,b,tr=''):
 COUNTS[id]=COUNTS.get(id,0)+1
 uid=id if COUNTS[id]==1 else id+'_'+str(COUNTS[id])
 return f'<g id="{uid}" inkscape:label="{id}" transform="{tr}">{b}</g>'
def txt(x,y,t,size=5):return f'<text x="{x}" y="{y}" font-family="DejaVu Sans" font-size="{size}" fill="#3f4b5c">{t}</text>'
def ellipse(x,y,rx,ry,f,s='none',w=.5):return f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="{f}" stroke="{s}" stroke-width="{w}"/>'
B='M -22 0 L 23 0 C -5 194 -42 412 -43 605 C -44 696 -36 752 -18 780 C -63 754 -76 682 -76 599 C -77 396 -44 183 -22 0 Z'
D='M -30 0 Q 0 -14 30 0 C 15 229 0 520 13 752 Q 16 808 6 826 Q -13 813 -26 780 C -60 551 -54 269 -30 0 Z'
DEFS='''<defs><linearGradient id="gold"><stop stop-color="#352c24"/><stop offset=".2" stop-color="#83704b"/><stop offset=".43" stop-color="#e7d4a0"/><stop offset=".55" stop-color="#ac9060"/><stop offset=".8" stop-color="#55442e"/><stop offset="1" stop-color="#cbb27c"/></linearGradient><linearGradient id="steel"><stop stop-color="#26394c"/><stop offset=".3" stop-color="#7f91a4"/><stop offset=".65" stop-color="#b9c2cd"/><stop offset=".84" stop-color="#edf3f5"/><stop offset="1" stop-color="#c5d4de"/></linearGradient><linearGradient id="blue"><stop stop-color="#121f30"/><stop offset=".45" stop-color="#314c6a"/><stop offset=".7" stop-color="#23394f"/><stop offset="1" stop-color="#0d1929"/></linearGradient><linearGradient id="ivory"><stop stop-color="#716c61"/><stop offset=".55" stop-color="#c7c6b5"/><stop offset="1" stop-color="#7e827e"/></linearGradient><clipPath id="bc">'''+path(B)+'''</clipPath><clipPath id="dc">'''+path(D)+'''</clipPath><clipPath id="hc"><rect x="-17" y="0" width="34" height="190"/></clipPath></defs>'''
parts={}
parts['01_Than_kiem']=path(B,'url(#steel)','#596b79',.65)
# Sharp tip retained. No rounding of outline.
b=path('M 16 1 C -12 210 -48 416 -49 604 C -49 693 -39 750 -18 780 C -45 751 -57 690 -57 605 C -58 416 -22 190 7 1 Z','#e5edf0')
b+=path('M -21 0 C -45 187 -78 399 -76 599 C -76 682 -63 754 -18 780','none','#b5eaff',1.4)
# irregular hamon line follows inside edge
pts=[]
for i in range(111):
 t=i/110;y=t*758;xx=-1-62*math.sin(t*math.pi*.57)+math.sin(i*2.7)*1.6
 pts.append(f'{xx:.3f} {y:.3f}')
b+=path('M '+' L '.join(pts),'none','#f5f6ee',.7)
parts['02_Vien_luoi_Hamon']=b
b=''
for k in range(7):
 x=-18+k*3
 b+=path(f'M {x} 8 C {x+29} 50 {x-36} 75 {x-5} 130 S {x-50} 245 {x-29} 310 S {x-65} 425 {x-45} 486','none',['#edf0e6','#798994','#c8d2d6'][k%3],.45)
b+=path('M -8 20 C 17 45 -31 56 -9 74 C 12 87 -17 110 -29 124 M -31 141 Q -1 116 -17 106 M -45 250 C -5 217 -20 204 -29 220 C -42 239 -20 253 -46 272','none','#f1f2df',.8)
parts['03_Hoa_van_khac_than']=f'<g clip-path="url(#bc)">{b}</g>'
parts['04_Loi_chuoi']='<rect x="-17" y="0" width="34" height="190" fill="url(#ivory)" stroke="#4a5559" stroke-width=".7"/>'
b=''
for y in range(-12,190,22):
 for side in [-1,1]:
  b+=g('wrap',path(f'M -19 {y} L 19 {y+23} L 19 {y+33} L -19 {y+10} Z','url(#blue)','#101e2b',.5)+path(f'M -18 {y+2} L 18 {y+24}','none','#6e8492',.65)+path(f'M -18 {y+7} L 18 {y+29}','none','#1b2b40',.5),f'scale({side} 1)')
parts['05_Day_quan_chuoi']=f'<g clip-path="url(#hc)">{b}</g>'
# wind spiral metal fitting, same visual language on guard, pommel and sheath
spiral='M -17 7 C -39 0 -33 -20 -14 -25 C 13 -38 40 -15 24 4 C 14 15 -8 8 -3 -5 C 0 -13 15 -10 13 -3 C 24 -10 11 -22 -1 -15 C -21 -2 2 22 21 14 C 0 33 -25 22 -17 7 Z'
parts['06_Dau_chuoi']=path('M -22 11 Q -25 -22 -1 -29 Q 25 -32 24 10 Z','url(#gold)','#4c402d',.8)+g('spiral_pommel',path(spiral,'url(#gold)','#342e25',.7),'translate(0 -4) scale(.65)')
# guard asymmetric swirling ring with open negative spaces
b=ellipse(0,0,53,24,'url(#gold)','#403428',.9)+ellipse(0,0,43,16,'#edf0f0','#947e52',.6)
b+=path('M -48 -3 Q -63 -12 -53 -31 Q -56 -12 -29 -13 Q -3 -44 27 -20 Q 57 -6 40 16 Q 31 29 5 21 C 38 20 35 -6 13 -12 Q -6 -20 -17 -2 Q -28 19 -49 9 Q -57 6 -48 -3 Z','url(#gold)','#473a2b',.9)
b+=g('central_spiral',path(spiral,'url(#gold)','#3b3127',.8),'translate(2 0) scale(.8)')
b+=path('M -10 7 Q 6 7 19 19 Q 15 39 -13 54 Q -24 61 -27 76 Q -32 49 -11 35 Q 7 26 -10 7 Z','url(#gold)','#4a3c2b',.8)
b+=path('M -12 17 Q 20 30 -15 49','none','#eadbb3',.9)
parts['07_Chan_tay_xoay_gio']=b
# flowing ragged blue cloth
r='M -15 0 C -59 14 -81 67 -137 55 C -183 44 -200 58 -235 78 Q -200 47 -166 46 C -105 76 -92 4 -15 -7 Z'
b=path(r,'url(#blue)','#30485d',.65)+path('M -20 -2 C -86 29 -86 77 -140 83 Q -169 90 -191 69 L -183 88 L -168 91 L -179 98 Q -137 113 -102 78 Q -61 38 -20 2 Z','url(#blue)','#32485a',.6)
b+=path('M -111 80 C -151 110 -123 146 -155 163 L -166 145 L -161 166 L -175 160 L -176 173 Q -131 184 -126 143 Q -129 111 -100 84 Z','url(#blue)','#314a60',.7)
b+=path('M -22 -2 C -82 22 -93 77 -143 64 M -119 90 Q -149 133 -158 151','none','#738a99',.7)
b+=ellipse(-17,0,8,10,'url(#blue)','#1d2937',1)
parts['08_Dai_vai_xanh']=b
parts['09_Than_vo']=path(D,'url(#blue)','#59616a',.7)
b=''
for k in range(6):
 b+=path(f'M {-12+k*3} 150 C {28+k*2} 278 {-47+k*2} 310 {-19+k*2} 408 C {27+k*2} 490 {-30+k*3} 553 {-8+k*2} 679 Q {18+k} 737 {-8+k} 782','none',['#b9b9ac','#837655','#d2cab4'][k%3],.5)
for y,x in [(300,-9),(368,-12),(550,-10),(710,-6)]:
 b+=path(f'M {x} {y} c 25 -18 27 27 7 18 c -10 -6 3 -19 8 -8 c -1 -18 -21 -9 -13 4 q 24 37 3 68','none','#d3d0bb',.9)
for i in range(65):
 y=random.uniform(24,790);x=random.uniform(-28,23)-22*math.sin(y/826*math.pi)
 b+=path(f'M {x} {y} l {random.uniform(-2,2)} {random.uniform(2,5)}','none','#62717a',.25)
parts['10_Hoa_van_vo']=f'<g clip-path="url(#dc)">{b}</g>'
b=path('M -31 5 Q -39 -15 -14 -28 Q 14 -35 31 -11 L 30 18 Q 3 1 -31 5 Z','url(#gold)','#493d2b',.7)
b+=g('sheath_spiral_top',path(spiral,'url(#gold)','#382f23',.8),'translate(0 -5) scale(.7)')
b+=path('M -36 313 Q -8 289 17 321 L 15 355 Q -12 331 -39 359 Z','url(#gold)','#46392a',.7)
b+=g('sheath_spiral_mid',path(spiral,'url(#gold)','#443627',.6),'translate(-13 327) scale(.65)')
b+=path('M -28 774 Q -15 791 12 778 Q 18 810 6 826 Q -18 814 -28 774 Z','url(#gold)','#463929',.7)
b+=path('M -21 786 Q 4 792 5 818','none','#dec99a',1)
parts['11_Dai_kim_loai_vo']=b
b=''
for i in range(7):
 y=66+i*12
 b+=path(f'M -32 {y} Q -8 {y+14} 22 {y+2} L 23 {y+8} Q -10 {y+20} -33 {y+6} Z','url(#gold)','#342f26',.6)
b+=path('M 19 133 C 55 151 70 134 90 155 L 85 155 L 91 164 L 79 158 L 82 167 Q 53 141 19 143 Z','url(#gold)','#3d3529',.7)
b+=path('M 21 141 C 29 182 63 193 51 241 L 46 229 L 43 237 Q 48 187 15 145 Z','url(#gold)','#3d3529',.7)
parts['12_Day_buoc_vo']=b
# separate editable transparent wind paths
b=''
for i in range(8):
 off=i*2
 b+=path(f'M {25+off} 30 C 210 132 -181 210 -9 322 C 165 430 -221 444 -75 563 C 41 651 273 633 241 748','none','#bce7ed',.4+i*.07,extra=f'opacity="{.17+i*.05}"')
parts['13_Hieu_ung_gio']=b
# General SVG with named groups and no raster. Coordinates in design units (not fabrication templates).
def document(w,h,body):return f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape" width="{w}px" height="{h}px" viewBox="0 0 {w} {h}">{DEFS}{body}</svg>'
assembled=g('00_Nen_co_the_xoa','<rect width="620" height="1140" fill="#edf0f0"/>')
assembled+=txt(30,35,'WINDWALKER / YASUO-INSPIRED KATANA',10)+txt(30,52,'VECTOR REDRAW • EDITABLE PARTS',4)
for key in ['01_Than_kiem','02_Vien_luoi_Hamon','03_Hoa_van_khac_than']:
 assembled+=g(key,parts[key],'translate(240 292)')
for key in ['04_Loi_chuoi','05_Day_quan_chuoi','06_Dau_chuoi']:
 assembled+=g(key,parts[key],'translate(272 92) rotate(10)')
assembled+=g('07_Chan_tay_xoay_gio',parts['07_Chan_tay_xoay_gio'],'translate(240 290)')
assembled+=g('08_Dai_vai_xanh',parts['08_Dai_vai_xanh'],'translate(267 110) scale(.86)')
for key in ['09_Than_vo','10_Hoa_van_vo','11_Dai_kim_loai_vo','12_Day_buoc_vo']:
 assembled+=g(key,parts[key],'translate(440 245)')
assembled+=g('13_Hieu_ung_gio',parts['13_Hieu_ung_gio'],'translate(240 280)')
assembled+=txt(30,1115,'2D vector interpretation of the generated image. Not a physical cutting template.',4)
# Component contact sheet, each editable group independent; scaled only here for convenient inspection.
exploded='<rect width="1000" height="1100" fill="#f5f6f6"/>'+txt(25,30,'EDITABLE PARTS / 13 GROUPS',13)
positions=[(130,100,.8),(280,100,.8),(430,100,.8),(555,95,1),(635,95,1),(760,125,1.5),(600,430,1.25),(370,850,.9),(830,140,.8),(930,140,.8),(600,610,.45),(630,850,1),(50,850,.25)]
for (key,b),(x,y,sc) in zip(parts.items(),positions):
 exploded+=g(key,b,f'translate({x} {y}) scale({sc})')
 exploded+=txt(x-25,y-35,key,4)
# Individual files preserve local coordinate system; several overlays are mostly transparent by design.
boxes=[(-90,-10,140,800),(-90,-10,140,800),(-90,-10,140,800),(-25,-10,50,210),(-25,-10,50,210),(-40,-45,80,70),(-70,-50,140,140),(-250,-20,270,210),(-70,-40,120,880),(-70,-40,120,880),(-70,-40,120,880),(-50,40,160,220),(-160,0,450,800)]
for (key,b),(x,y,w,h) in zip(parts.items(),boxes):
 data=document(w,h,g(key,b,f'translate({-x} {-y})')).encode();(P/(key+'.svg')).write_bytes(data)
for name,w,h,b in [('Yasuo_vector_tong_the',620,1140,assembled),('Yasuo_boc_tach',1000,1100,exploded)]:
 data=document(w,h,b).encode();(P/(name+'.svg')).write_bytes(data)
 cairosvg.svg2pdf(bytestring=data,write_to=str(P/(name+'.pdf')))
 cairosvg.svg2png(bytestring=data,write_to=str(P/(name+'.png')),output_width=1240)
print('Created 15 SVGs, 2 PDFs, 2 previews')
