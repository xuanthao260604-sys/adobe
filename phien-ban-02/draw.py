from pathlib import Path
import math, random, io
import cairosvg
P=Path(__file__).parent
random.seed(19)
def path(d,f='none',s='none',w=1,extra=''):return f'<path d="{d}" fill="{f}" stroke="{s}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round" {extra}/>'
def g(body,tr=''):return f'<g transform="{tr}">{body}</g>'
def ellipse(x,y,rx,ry,f,s='none',w=.5):return f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="{f}" stroke="{s}" stroke-width="{w}"/>'
def flower(x,y,r=10,angle=0):
 b=''
 for i in range(5):
  b+=g(path(f'M 0 0 C {-r*.7} {-r*.3} {-r*.55} {-r*1.1} {-r*.14} {-r} L 0 {-r*.82} L {r*.14} {-r} C {r*.55} {-r*1.1} {r*.7} {-r*.3} 0 0','url(#petal)','#c67d9e',.45),f'rotate({i*72})')
 for i in range(10):
  a=i*math.pi/5;xx=math.sin(a)*r*.34;yy=math.cos(a)*r*.34
  b+=path(f'M 0 0 L {xx} {yy}','none','#a96985',.35)+ellipse(xx,yy,.6,.6,'#e9c17d')
 return g(b,f'translate({x} {y}) rotate({angle})')
def leaf(d):return path(d,'url(#gold)','#6f472d',.8)
def tassel(x,y,length=110):
 b=path(f'M 0 0 C -25 30 34 45 0 64','none','#594177',3)
 b+=ellipse(0,57,10,12,'url(#gold)','#49334e')+ellipse(0,61,7,3,'#3c2b43')
 b+=ellipse(0,70,5,8,'#45305e','#d4b27c')
 for i in range(17):
  u=(i-8)*.85;end=u*2+25+math.sin(i)*5
  b+=path(f'M {u*.4} 78 C {u-8} 105 {u+5} {length+40} {end} {length+65}','none',['#4e316f','#8761a6','#b49bcc'][i%3],1.1)
 b+=path('M -5 78 h 10','none','#d6b06b',3)
 return g(b,f'translate({x} {y})')
def branch():
 b=path('M -67 693 C -13 570 -43 423 15 297 Q 48 231 20 150','none','#54374b',3)
 for y,x,side in [(185,23,1),(244,24,-1),(316,8,1),(380,-9,-1),(447,-24,1),(520,-33,-1),(590,-43,1),(651,-57,-1)]:
  dx=side*28
  b+=path(f'M {x} {y+19} q {dx*.6} -8 {dx} -40 m {-dx*.5} 18 q {side*12} -1 {side*18} -13','none','#644052',1.5)
  b+=flower(x+dx,y-22,random.choice([9,11,14]),random.randrange(60))
  b+=flower(x+dx*.35,y+3,6,23)
  b+=ellipse(x+dx+side*9,y-38,3,5,'#d78caa','#765169')
 return b
D='M -34 0 L 34 0 C 46 260 13 597 -57 760 Q -64 775 -70 775 Q -85 775 -80 749 C -28 540 -25 232 -34 0 Z'
B='M -24 0 L 24 0 C 33 240 12 550 -49 726 Q -56 740 -64 740 Q -70 739 -65 726 C -17 535 -18 238 -24 0 Z'
defs='''<defs>
<linearGradient id="gold" x1="0" x2="1"><stop stop-color="#41273a"/><stop offset=".22" stop-color="#b38452"/><stop offset=".42" stop-color="#fff0c8"/><stop offset=".6" stop-color="#bd915d"/><stop offset=".8" stop-color="#765039"/><stop offset="1" stop-color="#f7dca0"/></linearGradient>
<linearGradient id="silk"><stop stop-color="#a79abc"/><stop offset=".45" stop-color="#fff9ff"/><stop offset=".7" stop-color="#ece4f0"/><stop offset="1" stop-color="#aa9ab8"/></linearGradient>
<linearGradient id="purple"><stop stop-color="#181b39"/><stop offset=".45" stop-color="#3d2b62"/><stop offset=".75" stop-color="#75528c"/><stop offset="1" stop-color="#25213e"/></linearGradient>
<linearGradient id="steel"><stop stop-color="#171e4b"/><stop offset=".45" stop-color="#6556bc"/><stop offset=".68" stop-color="#bba8f4"/><stop offset=".86" stop-color="#eefaff"/><stop offset="1" stop-color="#a3e5fa"/></linearGradient>
<radialGradient id="petal" cx=".5" cy="1" r="1"><stop stop-color="#b76496"/><stop offset=".4" stop-color="#f0afce"/><stop offset="1" stop-color="#ffedf3"/></radialGradient>
<radialGradient id="bg"><stop stop-color="#f1eaf1"/><stop offset="1" stop-color="#bbb1c4"/></radialGradient>
<clipPath id="bladeClip">'''+path(B)+'''</clipPath><clipPath id="sheathClip">'''+path(D)+'''</clipPath></defs>'''
s='<rect width="700" height="1220" fill="url(#bg)"/>'
s+=ellipse(354,555,279,480,'none','#d4c9d5',1)
s+='<text x="49" y="51" font-family="DejaVu Sans" font-size="23" letter-spacing="8" fill="#463852">SAKURA</text><text x="50" y="72" font-family="DejaVu Sans" font-size="8" letter-spacing="2" fill="#786581">02 / VECTOR ARTWORK</text>'
# sword blade
b=path(B,'url(#steel)','#bceeff',.8)
b+='<g clip-path="url(#bladeClip)">'
b+=path('M -13 0 C -4 290 -1 535 -61 737 L -70 748 L -83 727 C -23 525 -24 239 -24 0 Z','url(#purple)')
b+=path('M 16 5 C 29 278 2 562 -60 735','none','#f3feff',2)
b+=path('M 2 5 C 15 270 -7 554 -62 732','none','#8cd8ff',.7)
for i in range(65):
 y=random.uniform(25,711);x= -12 -45*(y/740)**3+random.uniform(-8,11)
 b+=flower(x,y,random.uniform(2,5),random.randrange(360))
for y in range(30,720,95):
 x=-4-44*(y/740)**3
 b+=path(f'M {x} {y} q -10 29 0 52 q 8 22 -9 45','none','#ddc7ff',.6)
b+='</g>'
s+=g(b,'translate(254 358)')
# handle wrapped with cross bands and diamond openings
h='<rect x="-18" y="0" width="36" height="250" rx="7" fill="url(#purple)" stroke="#97744f"/>'
for y in range(0,232,28):
 h+=path(f'M -18 {y} L 18 {y+20} L 18 {y+30} L -18 {y+10} Z','url(#silk)','#a69ab5',.45)
 h+=path(f'M 18 {y} L -18 {y+20} L -18 {y+30} L 18 {y+10} Z','url(#silk)','#a69ab5',.45)
 for dy in [3,5,7]:h+=path(f'M -17 {y+dy} L 17 {y+dy+19}','none','#d0c5da',.3)
 h+=ellipse(0,y+14,1.8,2,'url(#gold)')
# gold end fittings: curved swept petals
for base in [0,242]:
 h+=path(f'M -21 {base+2} Q 0 {base-5} 21 {base+2} L 21 {base+10} Q 0 {base+4} -21 {base+10} Z','url(#gold)','#684735',.6)
for i in range(4):
 h+=g(leaf('M -2 5 C -23 -10 -17 -26 -4 -37 C -12 -17 1 -19 7 -31 C 8 -10 16 -5 7 6 Z'),f'translate({-13+i*8} 0) rotate({-28+i*19})')
h+=flower(13,206,7)
s+=g(h,'translate(254 98)')
# elaborate layered guard and downward collar
q=''
for angle in [-160,-135,-108,-72,-45,-20,20,45,72,108,135,160]:
 q+=g(leaf('M 0 0 C 14 -13 45 -17 60 -8 Q 47 -8 51 0 Q 34 13 0 0 Z')+path('M 5 0 Q 27 -8 48 -4','none','#f8dfb2',.5),f'rotate({angle}) scale(1 .63)')
q=g(q,'scale(1 .36)')
q+=ellipse(0,0,42,10,'url(#purple)','#e2c084',1.8)
for angle in range(0,360,45):q+=g(leaf('M 0 0 Q 14 -22 38 -3 Q 19 8 0 0 Z'),f'rotate({angle}) scale(1 .5)')
q+=flower(0,-3,13)
for side in [-1,1]:
 q+=g(leaf('M 0 9 Q 18 17 23 51 Q 6 46 2 32 Q -5 43 -8 63 Q -14 37 0 9 Z')+path('M 2 16 Q 10 35 15 44','none','#fff0c7',.7),f'scale({side} 1)')
s+=g(q,'translate(254 353)')
s+=tassel(220,126,104)
# scabbard white with purple flame-shaped inlays, gilded curved lines
v=path(D,'url(#silk)','#9b744a',1)
v+='<g clip-path="url(#sheathClip)">'
v+=path('M -35 -5 L 36 -5 C 56 81 -22 99 -13 188 C 8 280 36 314 -6 403 C -37 482 -9 583 -52 681 Q -90 777 -66 790 L -105 790 C -51 637 -61 516 -32 422 C 5 306 -29 295 -31 216 C -40 126 -2 80 -35 -5 Z','url(#purple)','url(#gold)',1.2)
v+=path('M 32 170 C -27 219 41 328 -26 408 C -55 458 -5 529 -43 608 C -17 496 -70 466 -37 405 C 18 304 -41 235 32 170 Z','url(#purple)','url(#gold)',1)
v+=path('M -88 705 Q -29 660 -31 578 C 1 663 -42 723 -70 777 Z','url(#purple)','url(#gold)',1)
for k in range(5):
 v+=path(f'M {22-k*3} 28 C {45-k*4} 135 {-23-k*3} 129 {-18-k*2} 207 C {-10-k*2} 283 {39-k*3} 325 {-13-k*2} 417 C {-52-k*2} 488 {3-k*3} 543 {-48-k*3} 686','none',['#b18a5a','#d9bf94','#c5b8ce','#bfa6ca','#e7d4e6'][k],.55)
for i in range(95):
 y=random.uniform(5,760);x=random.uniform(-22,30)-70*(y/775)**2
 v+=ellipse(x,y,random.uniform(.2,.6),random.uniform(.4,1),'#c2a180')
v+='</g>'
# mouth and toe caps
v+=leaf('M -36 0 Q -6 11 35 0 L 35 15 Q 0 24 -35 13 Z')
for side in [-1,1]:v+=g(leaf('M -30 9 Q -43 27 -22 66 Q -22 36 4 29 Q -19 31 -30 9 Z'),f'scale({side} 1)')
v+=leaf('M -83 741 Q -58 758 -49 727 Q -43 758 -66 780 Q -88 786 -83 741 Z')
v+=path('M -78 751 Q -65 766 -55 746','none','#f2d39a',1)
v+=branch()
# tied purple rope
for k in range(3):
 v+=path(f'M -35 {93+k*7} Q 0 {120+k*7} 36 {91+k*7}','none','#2e2048',5)
 v+=path(f'M -35 {92+k*7} Q 0 {119+k*7} 36 {90+k*7}','none','#86629b',2)
for side in [-1,1]:
 v+=g(path('M 0 114 C -65 63 -70 144 0 114 C -63 154 -60 175 0 118','none','#38244f',7)+path('M 0 113 C -65 62 -70 143 0 113 C -63 153 -60 174 0 117','none','#9c77af',2),f'scale({side} 1)')
v+=ellipse(0,116,9,10,'url(#purple)','#ad8ac0',2)
v+=tassel(29,124,85)
s+=g(v,'translate(495 300)')
s+='<text x="50" y="1165" font-family="DejaVu Sans" font-size="9" fill="#665574">TÍM THẠCH ANH / TRẮNG NGỌC / VÀNG CỔ / HOA ANH ĐÀO</text><text x="50" y="1183" font-family="DejaVu Sans" font-size="7" fill="#786581">Bản mỹ thuật 2D • Không dùng trang này làm khuôn cắt • Chưa chế tạo thử</text>'
svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="700mm" height="1220mm" viewBox="0 0 700 1220">{defs}{s}</svg>'
(P/'Sakura_v2_my_thuat.svg').write_text(svg)
cairosvg.svg2pdf(bytestring=svg.encode(),write_to=str(P/'Sakura_v2_my_thuat.pdf'))
cairosvg.svg2png(bytestring=svg.encode(),write_to=str(P/'Sakura_v2_my_thuat.png'),output_width=1400)
print('v2 artwork created')
