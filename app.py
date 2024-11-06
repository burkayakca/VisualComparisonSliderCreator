import gradio as gr
import leafmap.foliumap as leafmap
from bs4 import BeautifulSoup
import os
import re

def sliderCreator(title, img1, img2, label1, label2, description =" ", filename = "slider",starting_position=50,isResponsive=True):
    
    import leafmap.foliumap as leafmap
    from bs4 import BeautifulSoup 

    try:
        ### Creating the Comparison slider ###
        ### Karşılaştırma kaydırıcısını oluştur ###
        leafmap.image_comparison(
            img1 = img1,
            img2 = img2,
            label1 = label1,
            label2 = label2,
            starting_position = starting_position,
            make_responsive = isResponsive,
            out_html = f'{filename}.html'
        )

        ### Settings of the Slider page ###
        ### Karşılaştırıcı sayfası ayarları ###

        with open(f"{filename}.html","r",encoding="utf-8") as f:
            sliderHtml = f.read()

        soup = BeautifulSoup(sliderHtml, "html.parser")
        divClassFoo = soup.find("div")
        _head = soup.head

        #style settings
        #stil ayarları
        style = _head.style
        style.string = "h1 {font-family: Arial, sans-serif; margin: 0.5em} body { margin: unset; display: flex; flex-direction: column; justify-content: center; align-items: center;} p {margin: 0.5em}"

        #Turkish character support and HTML Title
        #Türkçe karakter desteği ve HTML başlığı
        metaTag = soup.new_tag("meta")
        metaTag.attrs["charset"] = "utf-8"
        titleTag = soup.new_tag("title")
        titleTag.string = title
        style.insert_before(titleTag)
        style.insert_before(metaTag)

        #Slider Name/Explanation
        #Kaydırıcı açıklaması/adı
        h1Tag = soup.new_tag("h1")
        h1Tag.string = title
        divClassFoo.insert_before(h1Tag)

        pTag = soup.new_tag("p")
        pTag.string = description
        h1Tag.insert_after(pTag)

        #Saving changes
        #Değişikliklerin kaydedilmesi
        with open(f"{filename}.html","w",encoding="utf-8") as f:
            f.write(str(soup))

        return f"Görsel kaydırıcınız {filename}.html adlı dosya içerisine başarıyla aktarılmıştır."       

    except:
        return "Bir hata meydana geldi. Lütfen terkar deneyin"


#sliderCreator("Deprem karşılaştırma kaydırıcısı","d_once.jpg","d_sonra.jpg","sonra","önce","deneme")

#Arayüz
interface = gr.Interface(
    fn = sliderCreator,
    inputs = [
    gr.Textbox(label = "Başlık: "),
    gr.Image(type="filepath",label ="İlk resim"), gr.Image(type="filepath",label ="İkinci Resim"),
    gr.Textbox(label="İlk resimin açıklaması: "), gr.Textbox(label="İkinci resimin açıklaması: "),
    gr.TextArea(label="Açıklama: "),
    gr.Textbox(label="Dosya adı: ")
    ],
    outputs = "text",
    title="Görsel Kaydırıcı Oluşturucu",
    description = "JPG/JPEG/SVG Dosyalarıyla çalışır. Kaydırıcı ilk resmin boyutunda olacaktır"
)

interface.launch()