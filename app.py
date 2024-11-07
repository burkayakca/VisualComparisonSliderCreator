import gradio as gr
import leafmap.foliumap as leafmap
from bs4 import BeautifulSoup

def sliderCreator(title, img1, img2, label1, label2, description=" ", filename="slider.html", starting_position=50, isResponsive=True):
    try:
        # Creating the Comparison slider
        leafmap.image_comparison(
            img1=img1,
            img2=img2,
            label1=label1,
            label2=label2,
            starting_position=starting_position,
            make_responsive=isResponsive,
            out_html=filename
        )

        # Settings of the Slider page
        with open(filename, "r", encoding="utf-8") as f:
            sliderHtml = f.read()

        soup = BeautifulSoup(sliderHtml, "html.parser")
        divClassFoo = soup.find("div")
        _head = soup.head

        # Style settings
        style = _head.style
        style.string = "h1 {font-family: Arial, sans-serif; margin: 0.5em} body { margin: unset; display: flex; flex-direction: column; justify-content: center; align-items: center;} p {margin: 0.5em}"

        # Turkish character support and HTML Title
        metaTag = soup.new_tag("meta")
        metaTag.attrs["charset"] = "utf-8"
        titleTag = soup.new_tag("title")
        titleTag.string = title
        style.insert_before(titleTag)
        style.insert_before(metaTag)

        # Slider Name/Explanation
        h1Tag = soup.new_tag("h1")
        h1Tag.string = title
        divClassFoo.insert_before(h1Tag)

        pTag = soup.new_tag("p")
        pTag.string = description
        h1Tag.insert_after(pTag)

        # Saving changes
        with open(filename, "w", encoding="utf-8") as f:
            f.write(str(soup))

        return filename  # Return the filename for download

    except Exception as e:
        return str(e)  # Return the error message

# Interface
interface = gr.Interface(
    fn=sliderCreator,
    inputs=[
        gr.Textbox(label="Başlık: "),
        gr.Image(type="filepath", label="İlk resim"),
        gr.Image(type="filepath", label="İkinci Resim"),
        gr.Textbox(label="İlk resimin açıklaması: (ör. Önce, Eskiden"),
        gr.Textbox(label="İkinci resimin açıklaması: (ör. Sonra, Günümüzde"),
        gr.TextArea(label="Açıklama: "),
    ],
    outputs=gr.File(label="İndir"),
    title="Görsel Kaydırıcı Oluşturucu",
    description='Bu yazılım, yükleyeceğiniz iki farklı görseli kıyaslamanıza yardımcı olan bir etkileşimli kaydırıcı içeren bir HTML dosyası oluşturur. Bu tür kaydırıcılar en çok "Öncesi-Sonrası" tarzında temalı iki görselin kıyaslamasında kullanılır. JPG veya JPEG formatında görseller sunmak kaydıydla istediğiniz görselleri kıyaslayan bir kaydırıcı oluşturup kullanabilirsiniz. Programdan en iyi verimi almak için: 1) Tüm alanları doldurun. Yazı alanlarını fazla doldurmamaya özen gösterin. 2) Kaydırıcı, ilk resim kısmına girdiğiniz görselin boyut ve en boy oranında olacaktır. Mümkün olduğunca birbirine yakın boyut ve en-boy oranına sahip görselleri tercih ediniz | Program tamamlandığında İndir kısmında slider.html görünecektir.\nDosya boyutunun üzerine sol tıklayarak yada sağ tıklayarak "farklı kaydet" seçerek kaydırıcıyı içeren slider.html dosyasını indirebilirsiniz.'
)

interface.launch()
