import tkinter
import requests

window=tkinter.Tk()
window.title("Pokemon")
window.geometry("400x415")
url = "https://pokeapi.co/api/v2/pokemon?limit=100000"

def goster():
    for i in pokemonlar:
        print(i)
        text.insert("1.0",i+"\n")
def veriyi_cek():
    istek = requests.get(url)
    if istek.status_code==200:
        return istek.json()

pokemonlar=[]
pokemon_veri = veriyi_cek()
pokemon_sonuc = pokemon_veri["results"]

for i in pokemon_sonuc:
    pokemonlar.append(i.get("name"))

# Bir adet text box'a scroll bağlama işlemi
scroll=tkinter.Scrollbar(window,orient="vertical")
scroll.pack(side="right",fill="y")
text= tkinter.Text(yscrollcommand=scroll.set)
text.config()
text.pack()
scroll.config(command=text.yview)

pokemon_isim_getir= tkinter.Button(text="pokemon isimlerini getir",command=goster)
pokemon_isim_getir.pack()


window.mainloop()