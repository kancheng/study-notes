from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A4
from pathlib import Path
pdfmetrics.registerFont(TTFont('DejaVu','/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('Chinese',str(Path(__file__).parent/'NotoSansTC.ttf')))
out=Path(__file__).parent.parent/'fr/bonjour-verbes/Bonjour-Verbes-A1.pdf'
c=canvas.Canvas(str(out),pagesize=A4); W,H=A4
navy=HexColor('#17365e'); muted=HexColor('#53677c'); pale=HexColor('#eaf0f9')
def text(x,y,s,size=10,color=navy,font='DejaVu'):
 c.setFillColor(color);c.setFont(font,size);c.drawString(x,y,s)
def cn(x,y,s,size=10,color=navy):text(x,y,s,size,color,'Chinese')
def line(y):c.setStrokeColor(HexColor('#dae2ed'));c.line(42,y,W-42,y)
def heading(title,sub):
 global y
 c.setFillColor(navy);c.rect(0,H-94,W,94,fill=1,stroke=0);text(42,H-49,title,20,HexColor('#ffffff'));cn(43,H-74,sub,11,HexColor('#dde9ff'));y=H-123
heading('Bonjour Verbes - French A1', '三個必背動詞：現在式、例句、中文翻譯')
groups=[('ETRE (être)','是／處於',[('je','je suis','我是'),('tu','tu es','你是'),('il / elle','il / elle est','他／她是'),('nous','nous sommes','我們是'),('vous','vous êtes','您／你們是'),('ils / elles','ils / elles sont','他們／她們是')],[('Je suis étudiant.','我是學生。'),('Tu es prêt ?','你準備好了嗎？'),('Elle est française.','她是法國人。'),('Nous sommes à Taipei.','我們在台北。'),('Vous êtes professeur ?','您是老師嗎？'),('Ils sont ici.','他們在這裡。')]),('AVOIR','有；表達年齡',[('je','j’ai','我有'),('tu','tu as','你有'),('il / elle','il / elle a','他／她有'),('nous','nous avons','我們有'),('vous','vous avez','您／你們有'),('ils / elles','ils / elles ont','他們／她們有')],[('J’ai 25 ans.','我 25 歲。'),('Tu as un livre.','你有一本書。'),('Il a un frère.','他有一個兄弟。'),('Nous avons un cours.','我們有一堂課。'),('Vous avez une question ?','您有問題嗎？'),('Elles ont des amis.','她們有朋友。')]),("S’APPELER",'叫做／名字是',[('je','je m’appelle','我叫'),('tu','tu t’appelles','你叫'),('il / elle','il / elle s’appelle','他／她叫'),('nous','nous nous appelons','我們叫'),('vous','vous vous appelez','您／你們叫'),('ils / elles','ils / elles s’appellent','他們／她們叫')],[('Je m’appelle Hao-Cheng.','我叫 Hao-Cheng。'),('Tu t’appelles comment ?','你叫什麼名字？'),('Elle s’appelle Marie.','她叫 Marie。'),('Nous nous appelons les Bleus.','我們叫做「藍隊」。'),('Vous vous appelez comment ?','您叫什麼名字？'),('Ils s’appellent Paul et Marc.','他們叫 Paul 和 Marc。')])]
for i,(title,meaning,rows,examples) in enumerate(groups):
 if i:
  c.showPage();heading('Bonjour Verbes - French A1','現在式變位與跟讀例句')
 text(42,y,title,18);cn(265,y,meaning,12,muted);y-=30
 c.setFillColor(pale);c.roundRect(42,y-5,W-84,25,5,fill=1,stroke=0)
 cn(55,y+3,'人稱',10);cn(190,y+3,'現在式',10);cn(390,y+3,'中文',10);y-=23
 for subject,form,zh in rows:
  text(55,y,subject,10);text(190,y,form,10);cn(390,y,zh,10);line(y-9);y-=30
 y-=18;cn(42,y,'例句與翻譯',13);y-=25
 for fr,zh in examples:
  text(55,y,fr,10);cn(55,y-18,zh,10,muted);y-=45
 if i==2:
  y-=5;cn(42,y,'拼字：vous êtes、ils / elles sont、s’appeler。年齡用 avoir。',10,muted)
 c.setFont('DejaVu',8);c.setFillColor(muted);c.drawRightString(W-42,28,f'{i+1} / 3')
c.save();print(out)
