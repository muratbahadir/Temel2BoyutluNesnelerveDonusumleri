import math

genelList = []


def cizgiciz(start, end, image, listeyeEkle):
    x1, y1 = start
    x2, y2 = end
    pikselSayisi = math.sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))
    if pikselSayisi == 0:
        pikselSayisi = 1
    xfark = (x2 - x1) / pikselSayisi
    yfark = (y2 - y1) / pikselSayisi
    liste = []

    xn = x1
    yn = y1
    while True:
        liste.append([xn, yn])
        image.putpixel((int(xn), int(yn)), (60, 255, 60))
        xn = xn + xfark
        yn = yn + yfark
        if x2>x1:
            if xn>x2:
                break
        if x1>x2:
            if xn<x2:
                break
        if y2>y1:
            if yn>y2:
                break
        if y1>y2:
            if yn<y2:
                break

    if listeyeEkle:
        genelList.extend(liste)
    return liste


def egri1(xmerkez, ymerkez, r, image):
    artis_miktari = 1 / (2 * (3.1415922653589 / 180.00) * r)
    aci = 180

    liste = []

    while (aci < 225):
        radyan = aci * 3.1415922653589 / 180.0
        x = xmerkez + r * math.cos(radyan)
        y = ymerkez + r * math.sin(radyan)
        liste.append([x, y])

        aci = aci + artis_miktari
    genelList.extend(liste)
    return liste


def egri2(xmerkez, ymerkez, r, image):
    artis_miktari = 1 / (2 * (3.1415922653589 / 180.00) * r)
    aci = 0
    liste2 = []
    # image.putpixel((int(xmerkez), int(ymerkez)), (255, 255, 255, 255))
    while (aci < 45):
        radyan = aci * 3.1415922653589 / 180.0
        x = xmerkez + r * math.cos(radyan)
        y = ymerkez + r * math.sin(radyan)
        liste2.append([x, y])
        image.putpixel((int(x), int(y)), (255, 255, 255))
        aci = aci + artis_miktari

    return liste2


def egriCiz(merkezx, merkezy, image):
    liste1 = egri1(merkezx, merkezy, 50, image)
    liste2 = egri2(merkezx, merkezy, 50, image)
    liste3 = []
    liste3.extend(liste1)
    fark = liste2[len(liste2) - 1][0] - liste1[len(liste1) - 1][0]
    for i in range(len(liste1)):
        liste1[i][0] = liste1[i][0] + fark
        liste1[i][1] = liste1[i][1] + fark
        genelList.append([liste1[i][0], liste1[i][0]])
        liste3.append([liste1[i][0], liste1[i][0]])
        image.putpixel((int(liste1[i][0]), int(liste1[i][1])), (255, 255, 255))
    return liste3

def yayCiz(xmerkez, ymerkez, aciDerece, r, image):
    artis_miktari = 1 / (2 * (3.1415922653589 / 180.00) * r)
    aci = 0
    liste = []

    while (aci < aciDerece):
        radyan = aci * 3.1415922653589 / 180.0
        x = xmerkez + r * math.cos(radyan)
        y = ymerkez + r * math.sin(radyan)
        liste.append([x, y])
        image.putpixel((int(x), int(y)), (255, 255, 255))
        aci = aci + artis_miktari
    genelList.extend(liste)
    return liste


def cemberciz(merkezx, merkezy, image, r, bos, rgb):
    liste = yayCiz(merkezx, merkezy, 360, r, image)
    liste2 = []

    if bos:
        return liste
    else:
        xmax = merkezx + r
        xmin = merkezx - r
        for x in range(xmin, xmax):
            listesatr = []
            for i in range(len(liste)):
                if x < liste[i][0] < x + 1:
                    listesatr.append(liste[i][1])
            minx = min(listesatr)
            maxx = max(listesatr)
            for k in range(int(minx), int(maxx)):
                liste2.append([x, k])
                genelList.append([x, k])
                image.putpixel((int(x), int(k)), rgb)
    liste2.extend(liste)
    return liste2

def iciDoluCemberciz(merkezx, merkezy, r, image, rgb):
    return cemberciz(merkezx, merkezy, image, r, False, rgb)


def diskCiz(merkezx, merkezy, r1, r2, image, rgb1, rgb2):
    liste=iciDoluCemberciz(merkezx, merkezy, r1, image, rgb1)
    iciDoluCemberciz(merkezx, merkezy, r2, image, rgb2)
    return liste

def ucgenCiz(konum1, konum2, konum3, image, bos, rgb):
    konumlarx = [konum1[0], konum2[0], konum3[0]]
    liste = []
    liste.extend(cizgiciz(konum1, konum2, image,True))
    liste.extend(cizgiciz(konum1, konum3, image,True))
    liste.extend(cizgiciz(konum2, konum3, image,True))
    if bos:
        return liste
    else:
        xmax = max(konumlarx)
        xmin = min(konumlarx)
        for x in range(xmin, xmax):
            listedoldurulan = []
            for i in range(len(liste)):
                if x < liste[i][0] < x + 1:
                    listedoldurulan.append(liste[i][1])
            for k in range(int(min(listedoldurulan)), int(max(listedoldurulan))):
                genelList.append([x, k])
                image.putpixel((int(x), int(k)), rgb)
        return liste

def iciDoluUcgen(konum1, konum2, konum3, image, rgb):
    return ucgenCiz(konum1, konum2, konum3, image, False, rgb)


def dikdortgenCiz(konum1, konum2, image, bos, rgb):
    x1, y1 = konum1
    x2, y2 = konum2
    konum3 = x2, y1
    konum4 = x1, y2
    konumlarx = [x1, x2]
    liste = []
    liste.extend(cizgiciz(konum1, konum3, image,True))
    liste.extend(cizgiciz(konum4, konum2, image,True))
    liste.extend(cizgiciz(konum1, konum4, image,True))
    liste.extend(cizgiciz(konum3, konum2, image,True))

    if bos:
        return liste
    else:
        xmax = max(konumlarx)
        xmin = min(konumlarx)
        for x in range(xmin, xmax):
            listedoldurulan = []
            for i in range(len(liste)):
                if x <= liste[i][0] <= x + 1:
                    listedoldurulan.append(liste[i][1])
            for k in range(int(min(listedoldurulan)), int(max(listedoldurulan))):
                genelList.append([x, k])
                liste.append([x, k])
                image.putpixel((int(x), int(k)), rgb)

    return liste

def iciDoluDortgenCiz(konum1, konum2, image, rgb):
    return dikdortgenCiz(konum1, konum2, image, False, rgb)


def kırpma(konum1, konum2, image):
    x1, y1 = konum1
    x2, y2 = konum2
    konum3 = x2, y1
    konum4 = x1, y2
    konumlarx = [x1, x2]
    konumlary = [y1, y2]
    liste = []
    liste.extend(cizgiciz(konum1, konum3, image, False))
    liste.extend(cizgiciz(konum4, konum2, image, False))
    liste.extend(cizgiciz(konum1, konum4, image, False))
    liste.extend(cizgiciz(konum3, konum2, image, False))

    xmax = max(konumlarx)
    xmin = min(konumlarx)
    ymax = max(konumlary)
    ymin = min(konumlary)
    kırpılanPikseller = []
    for x in range(xmin, xmax):
        listedoldurulan = []
        for i in range(len(liste)):
            if x <= liste[i][0] <= x + 1:
                listedoldurulan.append(liste[i][1])
        for k in range(int(min(listedoldurulan)), int(max(listedoldurulan))):
            kırpılanPikseller.append([int(x), int(k)])


    for i in range(len(genelList)):
        if xmin < genelList[i][0] < xmax and ymin < genelList[i][1] < ymax:
            pass
        else:
            image.putpixel((int(genelList[i][0]), int(genelList[i][1])), (0, 0, 0))


def elipsciz(rx, ry, xc, yc, image):
    x = 0
    y = ry
    liste = []
    d1 = ((ry * ry) - (rx * rx * ry) +
          (0.25 * rx * rx))
    dx = 2 * ry * ry * x
    dy = 2 * rx * rx * y

    while (dx < dy):

        liste.append([x + xc, y + yc])
        liste.append([-x + xc, y + yc])
        liste.append([x + xc, -y + yc])
        liste.append([-x + xc, -y + yc])
        image.putpixel((x + xc, y + yc), (255, 0, 0))
        image.putpixel((-x + xc, y + yc), (255, 0, 0))
        image.putpixel((x + xc, -y + yc), (255, 0, 0))
        image.putpixel((-x + xc, -y + yc), (255, 0, 0))

        if (d1 < 0):
            x += 1
            dx = dx + (2 * ry * ry)
            d1 = d1 + dx + (ry * ry)
        else:
            x += 1
            y -= 1
            dx = dx + (2 * ry * ry)
            dy = dy - (2 * rx * rx)
            d1 = d1 + dx - dy + (ry * ry)

    d2 = (((ry * ry) * ((x + 0.5) * (x + 0.5))) +
          ((rx * rx) * ((y - 1) * (y - 1))) -
          (rx * rx * ry * ry))

    while y >= 0:

        liste.append([x + xc, y + yc])
        liste.append([-x + xc, y + yc])
        liste.append([x + xc, -y + yc])
        liste.append([-x + xc, -y + yc])
        image.putpixel((x + xc, y + yc), (255, 0, 0))
        image.putpixel((-x + xc, y + yc), (255, 0, 0))
        image.putpixel((x + xc, -y + yc), (255, 0, 0))
        image.putpixel((-x + xc, -y + yc), (255, 0, 0))

        if d2 > 0:
            y -= 1
            dy = dy - (2 * rx * rx)
            d2 = d2 + (rx * rx) - dy
        else:
            y -= 1
            x += 1
            dx = dx + (2 * ry * ry)
            dy = dy - (2 * rx * rx)
            d2 = d2 + dx - dy + (rx * rx)
    genelList.extend(liste)
    return liste


def iciDoluElipsCiz(rx, ry, xc, yc, image):
    liste = elipsciz(rx, ry, xc, yc, image)
    xmax = rx + xc
    xmin = xc - rx
    liste2 =[]
    liste2.extend(liste)
    for x in range(xmin, xmax):
        listedoldurulan = []
        for i in range(len(liste)):
            if x <= liste[i][0] <= x + 1:
                listedoldurulan.append(liste[i][1])
        for k in range(int(min(listedoldurulan)), int(max(listedoldurulan))):
            genelList.append([x, k])
            liste2.append([x, k])
            image.putpixel((int(x), int(k)), (255, 0, 0))
    return liste2

def yıldızÇiz(xmerkez,ymerkez,r,image,bos):

    aci = 0
    liste2 = []

    while (aci <= 360):
        radyan = aci * 3.1415922653589 / 180.0
        x = xmerkez + r * math.cos(radyan)
        y = ymerkez + r * math.sin(radyan)
        liste2.append([x, y])
        image.putpixel((int(x), int(y)), (255, 0, 255))
        aci = aci + 72
    liste=[]
    liste.extend(liste2)
    liste.extend(cizgiciz(liste2[0],liste2[2],image,True))
    liste.extend(cizgiciz(liste2[0], liste2[3], image, True))
    liste.extend(cizgiciz(liste2[1], liste2[3], image, True))
    liste.extend(cizgiciz(liste2[1], liste2[4], image, True))
    liste.extend(cizgiciz(liste2[2], liste2[4], image, True))
    if not bos:
        konumlarx = []
        for i in range(len(liste2)):
            konumlarx.append(liste2[i][0])
        xmax = int(max(konumlarx))
        xmin = int(min(konumlarx))
        icerdekibolgelerx=[]
        for x in range(xmin, xmax):
            listedoldurulan = []
            for i in range(len(liste)):

                if x <= liste[i][0] <= x + 1:
                    listedoldurulan.append(liste[i][1])
            for k in range(int(min(listedoldurulan)), int(max(listedoldurulan))):
                icerdekibolgelerx.append([x,k])

        konumlary = []
        for i in range(len(liste2)):
            konumlary.append(liste2[i][1])
        ymax = max(konumlary)
        ymin = min(konumlary)
        icerdekibolgelery = []
        for y in range(int(ymin), int(ymax)):
            listedoldurulan = []
            for i in range(len(liste)):
                if y <= liste[i][1] <= y + 1:
                    listedoldurulan.append(liste[i][0])
            for k in range(int(min(listedoldurulan)), int(max(listedoldurulan))):
                if icerdekibolgelerx.__contains__([k, y]):
                    icerdekibolgelery.extend([k, y])
                    image.putpixel((int(k), int(y)), (255, 0, 0))
        liste.extend(icerdekibolgelery)


    genelList.extend(liste)
    return liste
def doluYıldızÇiz(xmerkez,ymerkez,r,image):

    return yıldızÇiz(xmerkez,ymerkez,r,image,False)


def poligonciz(konumListesi, image):
    liste = []

    for i in range(0,len(konumListesi)-1):
        liste.extend(cizgiciz((konumListesi[i][0],konumListesi[i][1]),
                              (konumListesi[i+1][0],konumListesi[i+1][1]),image,True))

    liste.extend(cizgiciz((konumListesi[0][0], konumListesi[0][1]),
                          (konumListesi[i + 1][0], konumListesi[i + 1][1]), image, True))
    return liste

def iciDoluPoligon(konumListesi, image):
    liste = poligonciz(konumListesi,image)
    liste2=[]
    liste2.extend(liste)
    konumlarx = []
    for i in range(len(konumListesi)):
        konumlarx .append(konumListesi[i][0])
    xmax = max(konumlarx)
    xmin = min(konumlarx)
    iceridekibolgelerx = []
    for x in range(xmin, xmax):
        listedoldurulan = []
        for i in range(len(liste)):
            if x <= liste[i][0] <= x + 1:
                listedoldurulan.append(liste[i][1])
        for k in range(int(min(listedoldurulan)), int(max(listedoldurulan))):
            iceridekibolgelerx.append([x, k])


        konumlary = []
        for i in range(len(konumListesi)):
            konumlary.append(konumListesi[i][1])
        ymax = max(konumlary)
        ymin = min(konumlary)
        icerdekibolgelery = []
        for y in range(int(ymin), int(ymax)):
            listedoldurulan = []
            for i in range(len(liste)):
                if y <= liste[i][1] <= y + 1:
                    listedoldurulan.append(liste[i][0])
            for k in range(int(min(listedoldurulan)), int(max(listedoldurulan))):
                if iceridekibolgelerx.__contains__([k, y]):
                    icerdekibolgelery.extend([k, y])
                    image.putpixel((int(k), int(y)), (255, 0, 0))
    return liste2

def oteleme(liste,x,y,image):
    liste2=[]

    for i in range(len(liste)):

        liste2.append([liste[i][0] + x,liste[i][1] + y])
        image.putpixel((int(liste[i][0] + x), int(liste[i][1] + y)), (0, 255, 255))
    return liste2

def dondurme(liste,cevrilenNokta,image):
    liste2 = []
    aci = 90
    for i in range(len(liste)):
        radyan = aci * 3.1415922653589 / 180.0
        x = cevrilenNokta[0] + (liste[i][0] - cevrilenNokta[0]) * math.cos(radyan) - (
                    (liste[i][1] - cevrilenNokta[1]) * math.sin(radyan))
        y = cevrilenNokta[1] + (liste[i][0] - cevrilenNokta[0]) * math.sin(radyan) - (
                    (liste[i][1] - cevrilenNokta[1]) * math.cos(radyan))
        liste2.append([x,y])
        image.putpixel((int(x), int(y)), (255, 0, 255))
    return liste2

def olceklendirme(liste,sx,sy,image):
    liste2=[]
    for i in range(len(liste)):
        image.putpixel((int(liste[i][0]), int(liste[i][1])), (0, 0, 0))
        x1=sx*liste[i][0]
        y1 = sy * liste[i][1]
        liste2.append([x1,y1])
        image.putpixel((int(x1), int(y1)), (255, 255, 255))
    genelList.extend(liste2)
    return liste2

def zoomin(nesne,image):

    return olceklendirme(nesne,2,2,image)

def zoomout(nesne,image):

    return olceklendirme(nesne, 0.7, 0.7, image)

def birlesikDonusumler(liste,kombinasyon,image):

    for i in range(len(kombinasyon)):
        if kombinasyon[i]=="ö":
            liste = oteleme(liste,75,95,image)
        if kombinasyon[i] == "d":
            liste = dondurme(liste, (200, 200), image)

def yansima(liste,eksen,image):
    liste2=[]
    if eksen=="x":
        for i in range(len(liste)):
            liste2.append([liste[i][0]*-1,liste[i][1]])
            image.putpixel((int(liste[i][0]*-1),int(liste[i][1])),(255,255,50))
    if eksen == "y":
        for i in range(len(liste)):
            liste2.append([liste[i][0] , liste[i][1]*-1])
            image.putpixel((int(liste[i][0] ), int(liste[i][1]*-1)), (255, 255, 50))
    genelList.extend(liste2)
    return liste2

def nesneciz():

    print("ÇİZGİ            = 1")
    print("EĞRİ             = 2")
    print("YAY              = 3")
    print("DİSK             = 4")
    print("ÜÇGEN(BOŞ)       = 5")
    print("ÜÇGEN(DOLU)      = 6")
    print("DİKDÖRTGEN(BOŞ)  = 7")
    print("DİKDÖRTGEN(DOLU) = 8")
    print("KARE(BOŞ)        = 9")
    print("KARE(DOLU)       = 10")
    print("ÇEMBER(BOŞ)      = 11")
    print("ÇEMBER(DOLU)     = 12")
    print("ELİPS(BOŞ)       = 13")
    print("ELİPS(DOLU)      = 14")
    print("POLİGON(BOŞ)     = 15")
    print("POLİGON(DOLU)    = 16")
    print("YILDIZ(BOŞ)      = 17")
    print("YILDIZ(DOLU)     = 18")
    secim=int(input("Çizmek istediğiniz şeklin kodunu giriniz:"))
    if secim==1:
        cizgiciz((100,100),(200,200),image,True)
    if secim==2:
        egriCiz(250,250,image)
    if secim==3:
        yayCiz(250,250,135,50,image)
    if secim==4:
        diskCiz(250,250,100,50,image,(255,255,0),(0,0,0))
    if secim==5:
        ucgenCiz((250,100),(350,80),(450,150),image,True,(255,0,0))
    if secim==6:
        iciDoluUcgen((250,100),(350,80),(450,150),image,(255,0,0))
    if secim==7:
        dikdortgenCiz((250,250),(350,390),image,True,(255,0,0))
    if secim==8:
        iciDoluDortgenCiz((250,250),(350,390),image,(255,0,0))
    if secim == 9:
        dikdortgenCiz((50, 250), (150,350), image, True, (255, 0, 0))
    if secim == 10:
        iciDoluDortgenCiz((50, 250), (150, 350), image, (255, 0, 0))
    if secim == 11:
        cemberciz(250,250,image,50,True,(255,0,0))
    if secim == 12:
        iciDoluCemberciz(250,250,50,image,(255,0,0))
    if secim == 13:
        elipsciz(125, 75, 250, 250,image)
    if secim == 14:
        iciDoluElipsCiz(125,75,250,250,image)
    if secim == 15:
        poligonciz([[250,150],[250,135],[275,150],[255,175],[260,190],[250,250],[240,220],[245,200]], image)
    if secim == 16:
        iciDoluPoligon([[250,150],[250,135],[275,150],[255,175],[260,190],[250,250],[240,220],[245,200]],image)
    if secim == 17:
        yıldızÇiz(250,250,30,image,True)
    if secim == 18:
        doluYıldızÇiz(250,250,30,image)

    image.show()
    secim2=int(input("Yeni çizim yaptırmak için 1 , Çıkış için -1 giriniz."))
    if secim2 == 1:
        nesneciz()
    if secim2 == -1:
        pass

def nesneDonusumleri():
    nesneListe = []
    while True:
        image = Image.open('resimler/black.png')
        print("ÇİZGİ            = 1")
        print("EĞRİ             = 2")
        print("YAY              = 3")
        print("DİSK             = 4")
        print("ÜÇGEN(BOŞ)       = 5")
        print("ÜÇGEN(DOLU)      = 6")
        print("DİKDÖRTGEN(BOŞ)  = 7")
        print("DİKDÖRTGEN(DOLU) = 8")
        print("KARE(BOŞ)        = 9")
        print("KARE(DOLU)       = 10")
        print("ÇEMBER(BOŞ)      = 11")
        print("ÇEMBER(DOLU)     = 12")
        print("ELİPS(BOŞ)       = 13")
        print("ELİPS(DOLU)      = 14")
        print("POLİGON(BOŞ)     = 15")
        print("POLİGON(DOLU)    = 16")
        print("YILDIZ(BOŞ)      = 17")
        print("YILDIZ(DOLU)     = 18")
        secim = int(input("Dönüşüm uygulanacak şeklin kodunu giriniz:"))

        if secim == 1:
            nesneListe.extend(cizgiciz((100, 100), (200, 200), image, True))
        if secim == 2:
            nesneListe.extend(egriCiz(250, 250, image))
        if secim == 3:
            nesneListe.extend(yayCiz(250, 250, 135, 50, image))
        if secim == 4:
            nesneListe.extend(diskCiz(250, 250, 100, 50, image, (255, 255, 0), (0, 0, 0)))
        if secim == 5:
            nesneListe.extend(ucgenCiz((250, 100), (350, 80), (450, 150), image, True, (255, 0, 0)))
        if secim == 6:
            nesneListe.extend(iciDoluUcgen((250, 100), (350, 80), (450, 150), image, (255, 0, 0)))
        if secim == 7:
            nesneListe.extend(dikdortgenCiz((250, 250), (350, 390), image, True, (255, 0, 0)))
        if secim == 8:
            nesneListe.extend(iciDoluDortgenCiz((250, 250), (350, 390), image, (255, 0, 0)))
        if secim == 9:
            nesneListe.extend(dikdortgenCiz((250, 250), (350, 350), image, True, (255, 0, 0)))
        if secim == 10:
            nesneListe.extend(iciDoluDortgenCiz((250, 250), (350, 350), image, (255, 0, 0)))
        if secim == 11:
            nesneListe.extend(cemberciz(250, 250, image, 50, True, (255, 0, 0)))
        if secim == 12:
            nesneListe.extend(iciDoluCemberciz(250, 250, 50, image, (255, 0, 0)))
        if secim == 13:
            nesneListe.extend(elipsciz(125, 75, 250, 250, image))
        if secim == 14:
            nesneListe.extend(iciDoluElipsCiz(125, 75, 250, 250, image))
        if secim == 15:
            nesneListe.extend(poligonciz([[250, 150], [250, 50], [400, 150], [400, 50], [280, 285]], image))
        if secim == 16:
            nesneListe.extend(iciDoluPoligon([[250, 150], [250, 135], [275, 150], [255, 175], [260, 190], [250, 250], [240, 220], [245, 200]],
                           image))
        if secim == 17:
            nesneListe.extend(yıldızÇiz(250, 250, 50, image, True))
        if secim == 18:
            nesneListe.extend(doluYıldızÇiz(250, 250, 30, image))

        image.show()

        print("Nesneleri Döndür           =1")
        print("Olceklendirme Uygula       =2")
        print("Zoom in                    =3")
        print("Zoom out                   =4")
        print("Öteleme Uygula             =5")
        print("Birleşik Dönüşümler Uygula =6")
        print("Yansıma Uygula             =7")
        secim = int(input("Uygulanacak dönüşümün kodunu giriniz:"))

        if secim==1:
            dondurme(nesneListe,(250,250),image)
        if secim==2:
            olceklendirme(nesneListe,2,2,image)
        if secim==3:
            zoomin(nesneListe,image)
        if secim==4:
            zoomout(nesneListe,image)
        if secim==5:
            oteleme(nesneListe,50,100,image)
        if secim==6:
            birlesikDonusumler(nesneListe,["ö","d","ö"],image)
        if secim==7:
            yansima(nesneListe,"x",image)

        image.show()

        secim = int(input("Yeniden dönüşüm için 1 ,menüye dönüş için -1 giriniz:"))
        if secim==1:
            pass
        if secim==-1:
            return nesneListe



from PIL import Image

image = Image.open('resimler/black.png')

print("Nesne Çiz         = 1")
print("Nesne Dönüşümleri = 2")
print("Kırpma İşlemi     = 3")
secim =int(input("Yapmak istediğiniz eylemin kodunu giriniz:"))
if secim==1:
    nesneciz()
if secim == 2:
    nesneDonusumleri()
if secim == 3:
    print("Kırpılma öncesi ekranda çizimler olması gerekiyor.Çizimleri bitirdikten sonra -1'e basınız.")
    nesneciz()
    kırpma([150,150],[350,250],image)
    image.show()

