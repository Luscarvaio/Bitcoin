from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
 # importando bibliotecas
import requests
import json

co0 = "#444466"  # Preta / black
co1 = "#feffff"  # branca / white 
co2 = "#6f9fbd"  # azul / blue
fundo = "#484f60" # background

# criando janela -------------
janela = Tk()
janela.title('')
janela.geometry('320x350')
janela.configure(bg=fundo)

# dividindo janela em 2 frames-------------
ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=157)



frame_cima = Frame(janela, width=320, height=50, bg=co1, pady=0, padx=0, relief='flat')
frame_cima.grid(row=1, column=0)

frame_baixo = Frame(janela, width=320, height=300, bg=fundo, pady=0, padx=0, relief='flat')
frame_baixo.grid(row=2, column=0, sticky=NW)


def info():
    api_link ='https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD%2CBRL%2CEUR'
    # HTTP requests
    response = requests.get(api_link)

    #-- convertendo os dados em dicionários
    dados = response.json()


    # valor em USD
    valor_usd = float(dados['USD'])
    valor_formatado_usd = "US${:,.3f}".format(valor_usd)
    l_p_usd['text'] = valor_formatado_usd

    frame_baixo.after(100, info)

    # valor em BRL
    valor_brl = float(dados['BRL'])
    valor_formatado_brl = "R$ {:,.3f}".format(valor_brl)
    l_p_brl['text'] = "Reais: "+valor_formatado_brl

    # valor em EUR
    valor_eur = float(dados['EUR'])
    valor_formatado_eur = "€ {:,.3f}".format(valor_eur)
    l_p_eur['text'] = "Euros: "+valor_formatado_eur


# configurando frame cima -------------
imagem = Image.open('images/icons8-bitcoin-48.png')
imagem = imagem.resize((30, 30), Image.Resampling.LANCZOS)
imagem = ImageTk.PhotoImage(imagem)

l_icon = Label(frame_cima, image=imagem, compound=LEFT, bg=co1, relief=FLAT)
l_icon.place(x=10, y=8)

l_nome = Label(frame_cima, text='Bitcoin Price tracker', bg=co1, fg=co2, relief=FLAT, anchor='center', font=('Arial 20'))
l_nome.place(x=50, y=5)

# configurando frame baixo -------------
l_p_usd = Label(frame_baixo, text='', width=14, bg=fundo, fg=co1, relief=FLAT, anchor='center', font=('Arial 20'))
l_p_usd.place(x=0, y=50)

l_p_brl = Label(frame_baixo, text='', bg=fundo, fg=co1, relief=FLAT, anchor='center', font=('Arial 12'))
l_p_brl.place(x=0, y=130)

l_p_eur = Label(frame_baixo, text='', bg=fundo, fg=co1, relief=FLAT, anchor='center', font=('Arial 12'))
l_p_eur.place(x=0, y=160)


info()

janela.mainloop()