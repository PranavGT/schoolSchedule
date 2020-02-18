from PIL import Image, ImageDraw, ImageFont
import math

def vypisTextu(sirka, vyska, premenna, velkost):
    font = ImageFont.truetype("Arial.ttf", velkost)
    draw = ImageDraw.Draw(image)
    draw.text((sirka, vyska), premenna, font=font, fill="black")

def vytvorObrazok(sirka, vyska):
    return Image.new('RGB', (sirka, vyska), "white")

def oneLine(vyskaNadpisovejCiary):
    for y in range(0, 2):
        for x in range(0, sirka):
            image.putpixel((x, vyskaNadpisovejCiary+y), (0, 0, 0))

def vypisStlpce():
    for y in range(0, sirka, sirkaRiadku):
        for x in range(vyskaNadpisovejCiary, vyska):
            image.putpixel((y, x), (0, 0, 0))


def vypisRiadky():
    for y in range(vyskaNadpisovejCiary, vyska, vyskaRiadku):
        for x in range(0, sirka):
            image.putpixel((x, y), (0, 0, 0))

def vypisDni():
    i = 2
    j = 0
    for x in range(0, 5):
        vypisTextu(stredRiadkuS, stredRiadkuV * i, dni[j], 20)
        i += 2
        j += 1

image = vytvorObrazok(1500, 500)
sirka, vyska = image.size
vyskaNadpisovejCiary = 55
vyskaRiadku = math.ceil((vyska - vyskaNadpisovejCiary) / 5)
pocetDni = 5
docasna = vyskaNadpisovejCiary
pocetStvorcovVriadku = 5
pocetHodin = 10
sirkaRiadku = math.ceil(sirka/pocetHodin)
stredRiadkuV = math.ceil(vyskaRiadku/2)
stredRiadkuS = math.ceil(sirkaRiadku/4)
stred = math.ceil(stredRiadkuV * (1.5))

prvyRiadok = vyskaRiadku - (vyskaRiadku/5)
druhyRiadok = vyskaRiadku*2 - (vyskaRiadku/5)
tretiRiadok = vyskaRiadku*3 - (vyskaRiadku/5)
stvrtyRiadok = vyskaRiadku*4 - (vyskaRiadku/5)
piatyRiadok = vyskaRiadku*5 - (vyskaRiadku/5)

prvaHodina = stredRiadkuS
druhaHodina = sirkaRiadku
tretiaHodina = sirkaRiadku*2
stvrtaHodina = sirkaRiadku*3
piataHodina = sirkaRiadku*4
siestaHodina = sirkaRiadku*5
siedmaHodina = sirkaRiadku*6
osmaHodina = sirkaRiadku*7
deviataHodina = sirkaRiadku*8
desiataHodina = sirkaRiadku*9



nadpis = "Rozvrh hodín pre letný semester 2020"

dni = ["Pondelok", "Utorok", "Streda", "Štvrtok", "Piatok"]
# PONDELOK
vypisTextu(siestaHodina, prvyRiadok, "        OpSy1\n   13:00 - 14:20\n          134", 20)
vypisTextu(siedmaHodina, prvyRiadok, "        OpSy1\n   14:35 - 15:55\n          134", 20)
vypisTextu(osmaHodina, prvyRiadok, "         PoGr\n   16:10 - 17:30\n          134", 20)
vypisTextu(deviataHodina, prvyRiadok, "         PoGr\n   16:10 - 17:30\n          134", 20)
# UTOROK
vypisTextu(tretiaHodina, druhyRiadok, "        Prog3\n   11:25 - 12:45\n          134", 20)
vypisTextu(stvrtaHodina, druhyRiadok, "        Prog3\n   11:25 - 12:45\n          134", 20)
vypisTextu(piataHodina, druhyRiadok, "         Web3\n   13:00 - 14:20\n          137", 20)
vypisTextu(siestaHodina, druhyRiadok, "         Web3\n   13:00 - 14:20\n          137", 20)
vypisTextu(osmaHodina, druhyRiadok, "        Prog3\n   16:10 - 17:30\n          134", 20)
vypisTextu(deviataHodina, druhyRiadok, "        Prog3\n   16:10 - 17:30\n          134", 20)
# STREDA
vypisTextu(10, 10, nadpis, 40)
vypisTextu(druhaHodina, tretiRiadok, "   PoGr | PoSy \n    8:15 - 9:35\n     134 | 125", 20)
vypisTextu(tretiaHodina, tretiRiadok, "        PoSy \n    9:35 - 10:30\n      134 | 125", 20)
vypisTextu(stvrtaHodina, tretiRiadok, "       SoftSy\n  10:40 - 11:20\n          125", 20)
vypisTextu(piataHodina, tretiRiadok, "        SoftSy\n  11:25 - 12:05\n          135", 20)
vypisTextu(siestaHodina, tretiRiadok, "      InfoBezp\n   12:15 - 14:20\n          125", 20)
vypisTextu(sirkaRiadku*6, tretiRiadok, "  Mat | InfoBezp\n  13:00 - 15:40\n  235/234 | 125", 20)
# PIATOK
vypisTextu(druhaHodina, piatyRiadok, "          TZI \n    8:15 - 10:25\n          235", 20)
vypisTextu(tretiaHodina, piatyRiadok, "          TZI \n    8:15 - 10:25\n          235", 20)
vypisTextu(stvrtaHodina, piatyRiadok, "          TZI \n    8:15 - 10:25\n          235", 20)



oneLine(vyskaNadpisovejCiary)
vypisStlpce()
vypisRiadky()
vypisDni()


image.show()
image.save("rozvrh.png")