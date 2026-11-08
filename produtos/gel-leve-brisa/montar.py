# Monta as fotos de marketplace do Gel Adesivo Leve Brisa a partir dos recortes (rembg).
from PIL import Image, ImageOps, ImageEnhance, ImageFilter, ImageDraw, ImageFont
S='/tmp/claude-0/-home-user-EliLimpa/00423cff-6e31-5dc4-938c-0de550a8c578/scratchpad/'
F='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'; FR='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
NAVY=(31,42,107); PINK=(214,32,125); W=1500
def font(s,b=True): return ImageFont.truetype(F if b else FR,s)
def cut(n):
    im=Image.open(S+f'cut_{n}.png').convert('RGBA')
    a=im.getchannel('A').point(lambda v:0 if v<40 else v); im.putalpha(a)
    im=im.crop(a.point(lambda v:255 if v>120 else 0).getbbox())
    rgb=im.convert('RGB'); rgb=ImageEnhance.Brightness(rgb).enhance(1.08); rgb=ImageEnhance.Contrast(rgb).enhance(1.06)
    rgb=rgb.filter(ImageFilter.UnsharpMask(2,60,3)); rgb.putalpha(im.getchannel('A')); return rgb
def place(canvas,im,box,shadow=True):
    x0,y0,x1,y1=box; t=im.copy(); t.thumbnail((x1-x0,y1-y0),Image.LANCZOS)
    x=x0+(x1-x0-t.width)//2; y=y0+(y1-y0-t.height)//2
    if shadow:
        sh=Image.new('L',canvas.size,0); d=ImageDraw.Draw(sh)
        d.ellipse([x+t.width*0.08,y+t.height-18,x+t.width*0.92,y+t.height+22],fill=70)
        sh=sh.filter(ImageFilter.GaussianBlur(18)); canvas.paste((150,150,150),(0,0),sh)
    canvas.paste(t,(x,y),t)
def blank(): return Image.new('RGB',(W,W),(255,255,255))
def principal(n,out):
    c=blank(); m=int(W*0.075); place(c,cut(n),(m,m,W-m,W-m)); c.save(out,quality=90)
principal('17','fotos/refil_01_principal.jpg')
principal('12','fotos/aplicador_01_principal.jpg')
principal('05','fotos/kit_01_principal.jpg')
def wrap(d,text,f,width):
    words=text.split(); lines=[]; cur=''
    for w in words:
        t=(cur+' '+w).strip()
        if d.textlength(t,font=f)<=width: cur=t
        else: lines.append(cur); cur=w
    lines.append(cur); return lines
def infografico(n,titulo,itens,out,nota=None):
    c=blank(); d=ImageDraw.Draw(c)
    d.rectangle([0,0,W,170],fill=PINK); d.text((W//2,85),titulo,font=font(64),fill='white',anchor='mm')
    place(c,cut(n),(60,230,640,1380))
    y=260
    for big,small in itens:
        d.ellipse([700,y+8,744,y+52],fill=PINK); d.text((722,y+30),'✓',font=font(30),fill='white',anchor='mm')
        d.text((770,y),big,font=font(50),fill=NAVY); yy=y+64
        for l in wrap(d,small,font(36,False),680): d.text((770,yy),l,font=font(36,False),fill=(70,70,70)); yy+=46
        y=yy+34
    if nota:
        d.rounded_rectangle([700,y,1440,y+110],radius=20,fill=(255,236,150))
        for i,l in enumerate(wrap(d,nota,font(32),700)): d.text((725,y+18+i*40),l,font=font(32),fill=NAVY)
    c.save(out,quality=90)
infografico('17','Limpa e perfuma a cada descarga',[
 ('6 aplicações','6 discos de gel em um refil de 36g'),
 ('Até 7 dias cada','Até 6 semanas de vaso perfumado'),
 ('Sem suporte na borda','O gel gruda direto na parede do vaso'),
 ('Fragrância Lavanda','Perfume duradouro no banheiro')],
 'fotos/refil_02_caracteristicas.jpg','REFIL: aplicador não incluso')
infografico('12','Aplicador + Refil: comece hoje',[
 ('Aplicador reutilizável','Encaixe o refil, aplique e guarde para o próximo'),
 ('6 aplicações','Refil de 36g com 6 discos de gel'),
 ('Até 7 dias cada','Até 6 semanas de vaso perfumado'),
 ('Mais higiênico','Você não encosta a mão no vaso')],
 'fotos/aplicador_02_caracteristicas.jpg')
# kit
c=blank(); d=ImageDraw.Draw(c)
d.rectangle([0,0,W,170],fill=PINK); d.text((W//2,85),'Kit 1 Aplicador + 2 Refis',font=font(66),fill='white',anchor='mm')
place(c,cut('05'),(80,220,W-80,980))
d.rounded_rectangle([90,1030,W-90,1440],radius=30,fill=(246,240,248))
cols=[('18','aplicações'),('até 18','semanas perfumado'),('3 x 36g','de gel Lavanda')]
for i,(a,b) in enumerate(cols):
    cx=90+(W-180)//6*(2*i+1)
    d.text((cx,1170),a,font=font(96),fill=PINK,anchor='mm'); d.text((cx,1270),b,font=font(36),fill=NAVY,anchor='mm')
d.text((W//2,1375),'O aplicador é reutilizável: use os 2 refis depois do primeiro',font=font(30,False),fill=(70,70,70),anchor='mm')
c.save('fotos/kit_02_rendimento.jpg',quality=90)
# como usar: painel do verso (foto 09)
o=ImageOps.exif_transpose(Image.open('originais/09.jpg')).convert('RGB')
pw,ph=o.size; p=o.crop((int(pw*0.258),int(ph*0.503),int(pw*0.69),int(ph*0.612)))
p=ImageEnhance.Brightness(p).enhance(1.12); p=ImageEnhance.Contrast(p).enhance(1.15); p=p.filter(ImageFilter.UnsharpMask(2,80,3))
c=blank(); d=ImageDraw.Draw(c)
d.rectangle([0,0,W,170],fill=NAVY); d.text((W//2,85),'Como usar em 4 passos',font=font(64),fill='white',anchor='mm')
p.thumbnail((W-80,700),Image.LANCZOS); c.paste(p,((W-p.width)//2,230))
passos=['1. Encaixe o refil no aplicador e tire a tampa.','2. Encoste a ponta na parede do vaso, perto da borda.','3. Pressione até a próxima trava: o disco de gel fica grudado.','4. Tampe, guarde e dê descarga para ativar o gel.']
y=230+p.height+60
for t in passos:
    for l in wrap(d,t,font(40),W-200): d.text((100,y),l,font=font(40),fill=NAVY); y+=54
    y+=14
d.text((W//2,W-70),'Antes de aplicar, o vaso deve estar limpo.',font=font(34,False),fill=(90,90,90),anchor='mm')
c.save('fotos/comum_03_como_usar.jpg',quality=90)
# laterais com as partes
for n,out in (('10','fotos/aplicador_04_partes.jpg'),('16','fotos/refil_04_partes.jpg')):
    c=blank(); m=int(W*0.075); place(c,cut(n),(m,m,W-m,W-m)); c.save(out,quality=90)
print('ok')
