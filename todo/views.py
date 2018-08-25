from django.shortcuts import render , redirect
from .models import Kitaps
from .models import Yayinevi
from django.contrib import messages
from django.shortcuts import get_object_or_404
import json


def index(request):

    tablo = Kitaps.objects.all()

    return render(request,"index.html" , {"tablo": tablo})
def index2(request):

    tablo = Yayinevi.objects.all()

    return render(request,"base.html", {"tablo" : tablo})


# index.html üzerinden models de oluşturduğumuz kitaps(database) sınıfına veri ekleme foksiyonu
def ekle(request):
    if request.method == "GET":
        return redirect("/")


    else:
        kitapadi  = request.POST.get("kitapAdi")
        yazaradi = request.POST.get("yazarAdi")
        yayinevi = request.POST.get("yayinevi")

        newKitaps = Kitaps(kitapAdi=kitapadi , yaazarAdi=yazaradi , yayineviAdi=yayinevi)

        newKitaps.save()

        return redirect("/")

def ekle2(request):
    if request.method == "GET":
        return redirect("/")


    else:
        kitapadi  = request.POST.get("kitapAdi")
        yazaradi = request.POST.get("yazarAdi")
        yayinevi = request.POST.get("yayinevi")

        newKitaps = Kitaps(kitapAdi=kitapadi , yaazarAdi=yazaradi , yayineviAdi_id=yayinevi)

        newKitaps.save()

        tablo =Kitaps.objects.all()

        return render(request, "tablo.html", {"tablo": tablo})

def sil(request , id ):
    sil = Kitaps.objects.filter(id = id)

    sil.delete()
    return redirect('/')

# guncelle ve tamamla fonksiyonları beraber güncelleme işlemini yapmakta

# index.html sayfasından güncellemek istediğimiz veri satırında bulunan güncelle butonu ile update.html sayfasına gidiyoruz

# update.html de bulunan textlere veriler yüklü halde geliyor degiştirmek isteğimiz textin yerine yenisini yazıp tamamla dediğimizde güncellenmiş halde index.html ye dönüyor

def guncelle(request , id):

    guncelle1 = Kitaps.objects.get(id = id)

    return render(request , "update.html" , {"guncelle1": guncelle1})

def tamamla(request, id):
    kitapadi = request.POST.get("kitapAdi")
    yazaradi = request.POST.get("yazarAdi")
    yayinevi = request.POST.get("yayineviAdi")

    newKitaps = Kitaps(id = id,kitapAdi=kitapadi,yaazarAdi=yazaradi,yayineviAdi=yayinevi)

    newKitaps.save()
    messages.success(request, "Seçilen veri güncellendi")
    return redirect("/")

# arama kısmı biraz farklı tüm kolonlar için 1 text alanımız var arama fonksiyonunda önce verinin hangi kolonda olduğunu

# tespit eden 3 tane fonksiyonumuz var

# daha sonra post ile gelen verinin select * from ... where = ? işlemini gerçekleştiriyor ve tüm satırı tabloya yazdırıyor

def arama(request):
    src = request.POST.get("arama")

    if kitapsorgulama(src):
        return render(request, "index.html", {"tablo": kitapsorgulama(src)})
    elif yazarsorgulama(src):
        return render(request, "index.html", {"tablo": yazarsorgulama(src)})
    elif yayinsorgulama(src):
        return render(request, "index.html", {"tablo": yayinsorgulama(src)})
    else:
        messages.warning(request, 'Girilen değer bulunamadı')
        return redirect("/")

def kitapsorgulama(src):
    try:

        return Kitaps.objects.filter(kitapAdi=src).values()
    except Kitaps.DoesNotExist:
        return False


def yazarsorgulama(src):
    try:
        return Kitaps.objects.filter(yaazarAdi=src).values()
    except Kitaps.DoesNotExist:
        return False

def yayinsorgulama(src):
    try:
        return Kitaps.objects.filter(yayineviAdi=src).values()
    except Kitaps.DoesNotExist:
        return False