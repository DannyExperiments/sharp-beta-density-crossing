"""Render the a=2, b=0 beta-density example and package its offline explorer."""

import math
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

from PIL import Image, ImageDraw, ImageFont


HERE = Path(__file__).resolve().parent
W,H = 704,835
BG,PANEL,EDGE = "#101b32","#162640","#3c5577"
TEXT,MUTED = "#f7faff","#c1cee2"
MINT,AMBER,BLUE = "#6aead7","#ffd086","#a9bdfb"


def label(draw, xy, message, size, color=TEXT, anchor="lt"):
    draw.text(xy,message,font=ImageFont.load_default(size=size),fill=color,anchor=anchor)


def density(t,k,p):
    return (t+1)*math.comb(t,k)*p**k*(1-p)**(t-k)


def plot(draw, f, phase):
    t = 2+f
    top = t+1
    odds = 1/math.sqrt(math.comb(t,2))
    theta = odds/(1+odds)
    height = density(t,0,theta)
    assert math.isclose(height,density(t,2,theta),rel_tol=1e-12)
    yaw = .37*math.sin(phase)

    def project(p,value,depth=0):
        x = p-.5
        return 353+500*(x*math.cos(yaw)+depth*math.sin(yaw)), 532-209*value/top-50*x*math.sin(yaw)-35*depth

    edges = [project(0,0),project(1,0),project(1,top),project(0,top)]
    shadow = [project(0,0,.16),project(1,0,.16),project(1,top,.16),project(0,top,.16)]
    draw.polygon(shadow,fill="#1b304e",outline=EDGE)
    draw.polygon(edges,fill="#192a45",outline=EDGE)
    for y in (0,top/2,top):
        draw.line((project(0,y),project(1,y)),fill="#334a69",width=2)
    for j in range(22):
        draw.line((project(j/22,.75),project((j+.55)/22,.75)),fill="#e5eaf4",width=2)
    for k,color in ((0,BLUE),(2,AMBER)):
        draw.line([project(i/100,density(t,k,i/100)) for i in range(101)],fill=color,width=3)
    envelope = [i/100 for i in range(101)] + [theta]
    draw.line([project(p,min(density(t,0,p),density(t,2,p))) for p in sorted(envelope)],fill=MINT,width=5)
    x,y = project(theta,height)
    draw.ellipse((x-8,y-8,x+8,y+8),fill=MINT,outline="#0b1627",width=2)
    left_floor,right_floor = project(0,0),project(1,0)
    label(draw,(left_floor[0],left_floor[1]+12),"0",22,MUTED,"mt")
    label(draw,(right_floor[0],right_floor[1]+12),"1",22,MUTED,"mt")
    max_y = project(0,top)
    label(draw,(max_y[0]-13,max_y[1]+1),str(top),21,MUTED,"rm")
    label(draw,(350,558),"Probability p",22,MUTED,"mt")
    return theta,height


def frame(phase,f):
    image=Image.new("RGB",(W,H),BG)
    draw=ImageDraw.Draw(image)
    label(draw,(36,37),"PAC MODE ESTIMATION",24,MINT)
    label(draw,(34,83),"Two densities cross",56)
    label(draw,(36,160),"Keep the two counts fixed at 2 and 0.",29,MUTED)
    draw.rounded_rectangle((32,214,672,593),21,fill=PANEL,outline=EDGE,width=2)
    label(draw,(55,240),"COUNT 2",22,AMBER)
    label(draw,(218,240),"COUNT 0",22,BLUE)
    label(draw,(644,240),"SMALLER DENSITY",22,MINT,"rt")
    theta,height=plot(draw,f,phase)
    draw.rounded_rectangle((32,614,672,803),21,fill=PANEL,outline=EDGE,width=2)
    label(draw,(55,633),f"Other observations  {f}",31)
    theta_label={0:"1/2",7:"1/7"}.get(f,f"{theta:.4f}")
    label(draw,(648,633),f"Crossing at {theta_label}",27,MUTED,"rt")
    label(draw,(55,691),f"Height  {height:.3f}",35,MINT)
    label(draw,(646,693),"Binary baseline  0.750",29,TEXT,"rt")
    label(draw,(55,751),"Equality with no other observations." if f==0 else "Crossing height is above the baseline.",26,MUTED)
    return image.convert("P",palette=Image.Palette.ADAPTIVE,colors=64)


def main():
    total=75
    frames=[frame(2*math.pi*i/total,(0,3,7)[i//25]) for i in range(total)]
    frames[0].save(HERE/"beta-crossing.gif",save_all=True,append_images=frames[1:],
                   loop=0,duration=180,optimize=True)
    with ZipFile(HERE/"beta-crossing-explorer.zip","w") as archive:
        for name in ("README.md","index.html"):
            info=ZipInfo(name,(1980,1,1,0,0,0))
            info.create_system=3
            info.external_attr=0o100644<<16
            archive.writestr(info,(HERE/name).read_bytes(),ZIP_DEFLATED,compresslevel=9)


if __name__=="__main__":
    main()
