"""news-23 b30 front-page-dense: draw THE WORLD TODAY, Monday 23 November 2026.
1024x1024 front page, 31 stories. Drawn illustrations, not photographs."""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
FD = "/usr/share/fonts/truetype/dejavu/"
SERIF_B = FD + "DejaVuSerif-Bold.ttf"
SANS = FD + "DejaVuSans.ttf"
SANS_B = FD + "DejaVuSans-Bold.ttf"


def F(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, font, max_w):
    """Greedy word wrap, returns list of lines that fit max_w."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=font) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def fit(draw, text, font, max_w):
    """Shrink text with ellipsis until it fits max_w (single line)."""
    if draw.textlength(text, font=font) <= max_w:
        return text
    while len(text) > 1 and draw.textlength(text + "\u2026", font=font) > max_w:
        text = text[:-1]
    return text + "\u2026"


def chip(draw, x, y, label, kind):
    """Small REPORTED (navy) / CLAIM (red) chip; returns width used."""
    f = F(SANS_B, 9)
    w = int(draw.textlength(label, font=f)) + 10
    col = (16, 42, 90) if kind == "REPORTED" else (178, 34, 34)
    draw.rounded_rectangle([x, y, x + w, y + 14], radius=3, fill=col)
    draw.text((x + 5, y + 2), label, font=f, fill="white")
    return w


img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

# ---------------------------------------------------------------- masthead
d.rectangle([0, 0, W, 56], fill=(12, 12, 12))
d.text((10, 8), "THE WORLD TODAY", font=F(SERIF_B, 40), fill="white")
d.text((W - 10, 18), "MONDAY  23 NOVEMBER 2026", font=F(SANS_B, 19),
       fill=(255, 196, 0), anchor="ra")

# ---------------------------------------------------------------- kicker
d.text((10, 60), "AI rout hits Asia  \u00b7  UN chief urges AI rules  \u00b7  "
       "US lead over China at record low  \u00b7  Anthropic IPO $107.3B",
       font=F(SANS_B, 13), fill=(178, 34, 34))

# ---------------------------------------------------------------- number strip (2 rows x 5 cols)
strip = [
    ("-3.3%", "KOSPI", (178, 34, 34)),
    ("5.3", "US-CHINA POWER GAP", (16, 42, 90)),
    ("11,762", "EBOLA CASES, DRC", (110, 90, 0)),
    ("10T won", "SEOUL STABILISATION FUND", (120, 72, 0)),
    ("2%", "BILLIONAIRE TAX IN PARIS", (0, 110, 60)),
    ("$450M", "SKUBAL DEAL", (128, 0, 128)),
    ("165", "RUSSIAN MISSILES IN A WEEK", (178, 34, 34)),
    ("12,000", "CLEARED IN MANCHESTER", (16, 42, 90)),
    ("264 kg", "EXPLOSIVES SEIZED IN LEBANON", (110, 90, 0)),
    ("$107.3B", "ANTHROPIC IPO \u2014 LARGEST EVER", (128, 0, 128)),
]
col_w = 202
for i, (num, lab, col) in enumerate(strip):
    r, c = divmod(i, 5)
    x = 10 + c * col_w
    y = 80 + r * 30
    d.text((x, y), num, font=F(SANS_B, 21), fill=col)
    d.text((x, y + 21), fit(d, lab, F(SANS_B, 9), col_w - 6),
           font=F(SANS_B, 9), fill=(40, 40, 40))

# ---------------------------------------------------------------- region bar
regions = [("ASIA-PACIFIC 7", (0, 128, 128)), ("AMERICAS 8", (16, 42, 90)),
           ("MIDDLE EAST 6", (168, 130, 20)), ("EUROPE 5", (110, 60, 160)),
           ("AFRICA 3", (150, 60, 60)), ("WORLD 2", (110, 110, 110))]
rx = 8
for name, col in regions:
    w = 169 if name != "WORLD 2" else 168
    d.rectangle([rx, 142, rx + w, 158], fill=col)
    d.text((rx + w / 2, 145), name, font=F(SANS_B, 10), fill="white",
           anchor="ma")
    rx += w

# ---------------------------------------------------------------- UTC strip
d.rectangle([8, 162, 1016, 178], fill=(10, 24, 60))
d.text((12, 166), "THE DAY IN UTC", font=F(SANS_B, 10), fill=(255, 196, 0))
d.text((120, 166), "~00:00 Kospi dives  \u00b7  ~06:30 Guterres opens  \u00b7  "
       "~09:00 Power Index  \u00b7  ~12:00 Paris 2% tax  \u00b7  "
       "~15:00 Kyiv missiles  \u00b7  ~18:00 Anthropic $97.17",
       font=F(SANS, 10), fill="white")
d.text((1012, 166), "~ APPROX", font=F(SANS, 10), fill=(170, 190, 220),
       anchor="ra")

# ---------------------------------------------------------------- heroes
HX = [8, 350, 692]          # hero panel x
HW = 324                    # hero panel width
SC_Y, SC_H = 182, 118       # scene area

# --- hero 1: Kospi skyline + falling chart
x0 = HX[0]
d.rectangle([x0, SC_Y, x0 + HW, SC_Y + SC_H], fill=(8, 20, 60))
# buildings
import random
random.seed(23)
for bx in range(x0 + 8, x0 + HW - 8, 22):
    bh = random.randint(28, 62)
    d.rectangle([bx, SC_Y + SC_H - 22 - bh, bx + 16, SC_Y + SC_H - 22],
                fill=(24, 48, 96))
    for wy in range(SC_Y + SC_H - 18 - bh, SC_Y + SC_H - 24, 9):
        for wx in (bx + 3, bx + 9):
            d.rectangle([wx, wy, wx + 3, wy + 4], fill=(255, 210, 90))
d.text((x0 + 8, SC_Y + 4), "-3.3%", font=F(SANS_B, 30), fill=(255, 60, 60))
pts = [(x0 + 14 + i * 30, SC_Y + 46 + i * 5 + (0 if i % 2 else 3))
       for i in range(10)]
d.line(pts, fill=(255, 80, 80), width=3)
for px, py in pts:
    d.ellipse([px - 3, py - 3, px + 3, py + 3], fill=(255, 210, 90))
d.rectangle([x0, SC_Y + SC_H - 22, x0 + HW, SC_Y + SC_H], fill=(0, 0, 0))
d.text((x0 + 8, SC_Y + SC_H - 19), "KOSPI  4,708.54  \u00b7  -161 PTS",
       font=F(SANS_B, 11), fill="white")

# --- hero 2: Guterres / 150 delegates
x0 = HX[1]
d.rectangle([x0, SC_Y, x0 + HW, SC_Y + SC_H], fill=(0, 128, 128))
d.text((x0 + 10, SC_Y + 6), "150 DELEGATES", font=F(SANS_B, 27),
       fill=(255, 220, 0))
d.text((x0 + 10, SC_Y + 36), "BACK A RISK", font=F(SANS_B, 27), fill="white")
d.text((x0 + 10, SC_Y + 66), "FRAMEWORK", font=F(SANS_B, 27), fill="white")
# small globe, bottom-right, clear of FRAMEWORK text
gx, gy, gr = x0 + HW - 34, SC_Y + SC_H - 36, 20
d.ellipse([gx - gr, gy - gr, gx + gr, gy + gr], fill=(170, 230, 200),
          outline=(255, 255, 255), width=2)
d.ellipse([gx - 8, gy - 10, gx + 2, gy + 2], fill=(60, 160, 90))
d.ellipse([gx + 2, gy + 4, gx + 10, gy + 12], fill=(60, 160, 90))
# tiny flags row, bottom-left of scene
for i, fc in enumerate([(200, 40, 40), (40, 90, 200), (255, 210, 0),
                        (40, 160, 80), (220, 120, 40)]):
    fx = x0 + 12 + i * 18
    d.polygon([(fx, SC_Y + SC_H - 16), (fx + 12, SC_Y + SC_H - 12),
               (fx, SC_Y + SC_H - 8)], fill=fc)
d.rectangle([x0, SC_Y + SC_H - 22, x0 + HW, SC_Y + SC_H], fill=(0, 0, 0))
d.text((x0 + 8, SC_Y + SC_H - 19), "UN  \u00b7  BRIDGETOWN",
       font=F(SANS_B, 11), fill="white")

# --- hero 3: Asia Power Index bars
x0 = HX[2]
d.rectangle([x0, SC_Y, x0 + HW, SC_Y + SC_H], fill=(245, 240, 225))
d.text((x0 + 8, SC_Y + 4), "NARROWEST SINCE 2018", font=F(SANS_B, 11),
       fill=(60, 60, 60))
d.text((x0 + HW - 8, SC_Y + 4), "GAP 5.3", font=F(SANS_B, 11),
       fill=(168, 130, 20), anchor="ra")
bars = [("78.9", "US", (16, 42, 90), 48), ("73.6", "CHINA", (178, 34, 34), 45),
        ("40.5", "INDIA", (190, 160, 20), 25)]
bw, gap = 62, 34
bx = x0 + 22
base = SC_Y + SC_H - 40
for val, name, col, bh in bars:
    d.rectangle([bx, base - bh, bx + bw, base], fill=col)
    d.text((bx + bw / 2, base - bh + 4), val, font=F(SANS_B, 13),
           fill="white", anchor="ma")
    d.text((bx + bw / 2, base + 3), name, font=F(SANS_B, 10),
           fill=(20, 20, 20), anchor="ma")
    bx += bw + gap
d.rectangle([x0, SC_Y + SC_H - 22, x0 + HW, SC_Y + SC_H], fill=(0, 0, 0))
d.text((x0 + 8, SC_Y + SC_H - 19), "ASIA POWER INDEX 2026",
       font=F(SANS_B, 11), fill="white")

# --- hero text blocks (headline / body / source+chip)
heroes = [
    ("1  AI ROUT HITS ASIA",
     "Kospi closes -3.3% to 4,708.54, sheds 161 pts; intraday -5.8%. "
     "Samsung -3.1%, SK Hynix -2.5.", "KOREA EXCHANGE", "REPORTED"),
    ("2  GUTERRES: REGULATE AI BEFORE IT'S TOO LATE",
     "UN chief urges global AI safety rules at the Bridgetown summit; "
     "150 delegates back a risk framework.", "UNITED NATIONS", "REPORTED"),
    ("3  US LEAD OVER CHINA AT RECORD LOW",
     "Asia Power Index 2026: US 78.9, China 73.6 \u2014 gap 5.3, narrowest "
     "since 2018. India third at 40.5.", "LOWY INSTITUTE", "REPORTED"),
]
for i, (head, body, src, kind) in enumerate(heroes):
    x0 = HX[i]
    hl = wrap(d, head, F(SANS_B, 15), HW - 4)
    y = SC_Y + SC_H + 6
    for ln in hl[:2]:
        d.text((x0, y), ln, font=F(SANS_B, 15), fill=(10, 10, 10))
        y += 18
    bl = wrap(d, body, F(SANS, 11), HW - 4)
    y += 2
    for ln in bl[:2]:
        d.text((x0, y), ln, font=F(SANS, 11), fill=(40, 40, 40))
        y += 14
    d.text((x0, y + 2), src, font=F(SANS, 9), fill=(110, 110, 110))
    chip(d, x0 + HW - 62, y, kind, kind)

# ---------------------------------------------------------------- 10 cards
d.text((8, 402), "MORE OF THE DAY  \u2014  10 STORIES", font=F(SANS_B, 14),
       fill=(10, 10, 10))
d.line([(8, 420), (1016, 420)], fill=(10, 10, 10), width=2)

cards = [
    ("AMERICAS", (16, 42, 90), "BESSENT: NVIDIA ANSWERS",
     "Treasury chief wants China answers.", "Reuters", "REPORTED"),
    ("FBI", (110, 60, 160), "FBI PROBES NCIC HACK",
     "Hackers hit police NCIC database.", "AP", "REPORTED"),
    ("WHITE HOUSE", (168, 130, 20), "TRUMP: IRAN STRIKES MAY RESUME",
     "Strikes could resume in New Year.", "Reuters", "REPORTED"),
    ("MARKETS", (0, 128, 128), "US FUTURES JUMP 3%",
     "Holiday rally lifts Nasdaq futures 3%.", "Bloomberg", "REPORTED"),
    ("SPORT", (178, 34, 34), "SKUBAL'S $450M METS DEAL",
     "Nine-year deal, largest ever.", "AP", "REPORTED"),
    ("SPORT", (0, 128, 128), "TOM JACKSON DIES AT 75",
     "Broncos LB turned ESPN voice dies.", "ESPN", "REPORTED"),
    ("LEGAL", (110, 60, 160), "STATES SUE SPACEX",
     "Ten states challenge AI safety claims.", "AP", "REPORTED"),
    ("TECH", (16, 42, 90), "ANTHROPIC IPO: $107.3B",
     "Raised at $83; debut closes $97.17.", "WSJ", "REPORTED"),
    ("EUROPE", (178, 34, 34), "POLAND: 3 MISSILES CROSSED AIRSPACE",
     "Kyiv: three Kh-101s crossed airspace.", "AP", "CLAIM"),
    ("SPACE", (110, 110, 110), "RUSSIAN NUCLEAR SATELLITE",
     "Intel: satellite built to carry a nuke.", "Reuters", "CLAIM"),
]
CW, CH = 200, 86
for i, (cat, col, head, body, src, kind) in enumerate(cards):
    r, c = divmod(i, 5)
    x = 8 + c * 202
    y = 426 + r * 92
    d.rectangle([x, y, x + CW, y + 16], fill=col)
    d.text((x + 4, y + 2), cat, font=F(SANS_B, 9), fill="white")
    d.text((x + CW - 4, y + 2), str(i + 4), font=F(SANS_B, 9),
           fill="white", anchor="ra")
    hl = wrap(d, head, F(SANS_B, 11), CW - 8)
    yy = y + 19
    for ln in hl[:2]:
        d.text((x + 4, yy), ln, font=F(SANS_B, 11), fill=(10, 10, 10))
        yy += 13
    d.text((x + 4, yy + 1), fit(d, body, F(SANS, 10), CW - 12),
           font=F(SANS, 10), fill=(40, 40, 40))
    d.text((x + 4, y + CH - 15), src, font=F(SANS, 9), fill=(110, 110, 110))
    chip(d, x + CW - 62, y + CH - 16, kind, kind)

# ---------------------------------------------------------------- map + ALSO
d.text((8, 616), "WHERE IT HAPPENED", font=F(SANS_B, 14), fill=(10, 10, 10))
d.line([(8, 634), (1016, 634)], fill=(10, 10, 10), width=2)
# map canvas
mx, my, mw, mh = 8, 640, 408, 190
d.rectangle([mx, my, mx + mw, my + mh], fill=(215, 232, 245))
for gx in range(mx, mx + mw, 16):
    d.line([(gx, my), (gx, my + mh)], fill=(190, 210, 230))
for gy in range(my, my + mh, 16):
    d.line([(mx, gy), (mx + mw, gy)], fill=(190, 210, 230))
# stylised continents (green blobs)
d.polygon([(mx + 18, my + 40), (mx + 90, my + 18), (mx + 150, my + 30),
           (mx + 165, my + 70), (mx + 120, my + 105), (mx + 60, my + 100),
           (mx + 25, my + 75)], fill=(150, 200, 130))            # N America
d.polygon([(mx + 95, my + 118), (mx + 125, my + 112), (mx + 140, my + 140),
           (mx + 120, my + 175), (mx + 100, my + 160)], fill=(150, 200, 130))
d.polygon([(mx + 195, my + 45), (mx + 235, my + 30), (mx + 260, my + 55),
           (mx + 245, my + 95), (mx + 210, my + 90)], fill=(150, 200, 130))
d.polygon([(mx + 275, my + 35), (mx + 340, my + 20), (mx + 395, my + 40),
           (mx + 385, my + 95), (mx + 320, my + 105), (mx + 285, my + 80)],
          fill=(150, 200, 130))                                     # Asia
d.polygon([(mx + 300, my + 118), (mx + 330, my + 112), (mx + 345, my + 140),
           (mx + 320, my + 165), (mx + 300, my + 145)], fill=(150, 200, 130))
# pins (spread so none overlap)
pins = [(330, 30), (118, 158), (360, 55), (95, 62), (128, 52), (268, 78),
        (72, 48), (38, 62), (88, 92), (105, 100), (222, 42), (238, 58),
        (255, 34)]
for i, (px, py) in enumerate(pins, start=1):
    cx, cy = mx + px, my + py
    d.ellipse([cx - 8, cy - 8, cx + 8, cy + 8], fill=(178, 34, 34),
              outline="white", width=1)
    d.text((cx, cy - 1), str(i), font=F(SANS_B, 9), fill="white",
           anchor="mm")
d.text((mx, my + mh + 4),
       "Pins 1\u201313: 1 Seoul \u00b7 2 Bridgetown \u00b7 3 Beijing \u00b7 "
       "4 Washington \u00b7 5 New York \u00b7 6 Tehran",
       font=F(SANS, 9), fill=(60, 60, 60))
d.text((mx, my + mh + 16),
       "7 Chicago \u00b7 8 San Francisco \u00b7 9 Denver \u00b7 10 Austin \u00b7 "
       "11 Warsaw \u00b7 12 Kyiv \u00b7 13 Moscow",
       font=F(SANS, 9), fill=(60, 60, 60))

# ALSO list, two columns
d.text((432, 616), "ALSO ON MONDAY", font=F(SANS_B, 14), fill=(10, 10, 10))
also = [
    "Paris: 100+ back 2% billionaire tax",
    "Manchester: 12,000 cleared",
    "Zelenskyy: 165 missiles in a week",
    "COP31: the day after pact rejected",
    "Benghazi: UN demands port probe",
    "Israel unity talks resume",
    "Gaza: two killed in Israeli strike",
    "West Bank settler attacks",
    "Iran war: no deal in sight",
    "Lebanon seizes 264 kg explosives",
    "Bahrain: strike hits plant, 2 hurt",
    "Sudan: defences down drones",
    "DRC: fighting traps Ebola teams",
    "Bangladesh: Hasina jailed if she returns",
    "Seoul minister quits in exam row",
    "SK Telecom -7.3% as hype cools",
    "China eases margin rules",
    "Seoul readies 10T-won fund",
]
for i, item in enumerate(also):
    col, row = divmod(i, 9)
    x = 432 + col * 296
    y = 642 + row * 20
    d.text((x, y), f"{14 + i}. {item}", font=F(SANS, 11),
           fill=(20, 20, 20))

# ---------------------------------------------------------------- DATE CHECK
d.rectangle([8, 868, 1016, 946], outline=(178, 34, 34), width=2)
d.text((16, 874), "DATE CHECK", font=F(SANS_B, 13), fill=(178, 34, 34))
d.text((1010, 874), "READ 23 NOV 2026, 23:59 UTC \u2014 STORIES DATED 23 NOV ONLY",
       font=F(SANS_B, 10), fill=(178, 34, 34), anchor="ra")
dc1 = ("LEFT OUT \u2014 NOT 23 NOV: Democrats reach 258 seats (22 Nov) \u00b7 "
       "Sparta II fire (22 Nov) \u00b7 El Chapo Isidro captured (22 Nov) \u00b7 "
       "EU-Indonesia pact (21 Nov) \u00b7 Nigeria boat (21 Nov) \u00b7 "
       "ICJ Myanmar ruling (19 Nov)")
for j, ln in enumerate(wrap(d, dc1, F(SANS, 11), 992)):
    d.text((16, 894 + j * 14), ln, font=F(SANS, 11), fill=(20, 20, 20))
dc2 = ("NOT YET: Dymer search continues (14 missing) \u00b7 4 House races "
       "uncalled \u00b7 COP32 venue not set \u00b7 WHO evacuating trapped "
       "Ebola staff")
d.text((16, 926), dc2, font=F(SANS, 11), fill=(20, 20, 20))

# ---------------------------------------------------------------- footer
d.text((8, 954), "Sources: Reuters \u00b7 AP \u00b7 Bloomberg \u00b7 AFP \u00b7 "
       "Yonhap \u00b7 BBC \u00b7 WSJ \u00b7 NYT \u00b7 ESPN \u00b7 Lowy Institute "
       "(Asia Power Index 2026).", font=F(SANS, 9), fill=(90, 90, 90))
d.text((8, 966), "CHIPS: REPORTED = confirmed by wires \u00b7 CLAIM = one "
       "side's claim, not independently confirmed \u00b7 ONGOING = still "
       "developing", font=F(SANS, 9), fill=(90, 90, 90))
d.rectangle([0, 984, W, H], fill=(12, 12, 12))
d.text((W / 2, 996), "Scenes are drawn illustrations, not photographs.  "
       "\u00b7  THE WORLD TODAY \u2014 Monday 23 November 2026  \u00b7  "
       "31 stories  \u00b7  6 regions", font=F(SANS_B, 11),
       fill=(255, 196, 0), anchor="ma")

img.save("entry.png", optimize=True)
print("saved entry.png", img.size)
