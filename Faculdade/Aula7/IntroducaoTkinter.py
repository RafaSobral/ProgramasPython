from tkinter import *

# Cria a janela principal (raiz)
i = Tk()

# # Configurações iniciais da janela
# i.title('Testando')  # Título da janela
# i.geometry('600x300')  # Tamanho da janela
# i['bg'] = 'red'  # Cor de fundo da janela
# # i.wm_iconbitmap('Estrela_pt.ico')  # Ícone da janela

# # Caixa de entrada de dados
# e = Entry(i)  
# e.pack()  # Empacota a caixa de entrada

# # Função do botão
# def botao_clicado():
#     # Modifica o texto do label
#     label.config(text='Você clicou no botão!')

# # Botão
# btn1 = Button(i,
#               text='Clique',
#               font='Arial 10 italic',
#               fg='white',  # Cor da fonte
#               bg='#4CAF50',  # Cor do fundo
#               relief='raised',  # Borda do botão
#               bd=5,  # Tamanho da borda
#               padx=20,  # Espaço entre o conteúdo e a borda na horizontal
#               activebackground='#45A049',  # Cor de fundo ao clicar
#               activeforeground='yellow',  # Cor da fonte ao clicar
#               command=botao_clicado  # Ação a ser realizada ao clicar
# )
# btn1.pack(pady=20)

# # Label (inicializada com texto vazio)
# label = Label(i,
#               bg="#CECECE",  # Cor de fundo da label
#               fg='silver'  # Cor da fonte
# )
# label.pack()


#Sistema grid(linha e coluna)-----------------------------------------------------------------


# x1 = Label(i,text='Teste1',bg='red')
# x2 = Label(i,text='Teste1',bg='green')
# x3 = Label(i,text='Teste1',bg='blue')

# x1.grid(row=0,column=0, padx=10)
# x2.grid(row=0,column=1, padx=10)
# x3.grid(row=0,column=2, padx=10)

# label_nome = Label(i,text='Nome:',font='Arial 10',bg='lightgreen')
# label_nome.grid(row=0,column=0,padx=10,pady=10)

# entry_nome = Entry(i)
# entry_nome.grid(row=0,column=1,padx=10,pady=10)

# label_idade = Label(i,text='Idade:',font='Arial 10',bg='lightgreen')
# label_idade.grid(row=1,column=0,padx=10,pady=10)

# entry_idade = Entry(i)
# entry_idade.grid(row=1,column=1,padx=10,pady=10)

# def informacoes():
#     nome = entry_nome.get()
#     idade = entry_idade.get()
#     r_Label.config(text=f'Nome: {nome}\nIdade: {idade}')

# btn2 = Button(i,text='Cadastrar', command=informacoes)
# btn2.grid(row=2,column=0,columnspan=2,pady=20)

# r_Label = Label(i,bg='lightblue')
# r_Label.grid(row=3,column=0,columnspan=2)


#Checkbutton() - Selecao multipla ---------------------------------------------------------------

def mostrar_selecionados():
    selecionados = []
    if futebol_var.get():
        selecionados.append('Futebol:')
    if volei_var.get():
        selecionados.append('Volei:')
    if natacao_var.get():
        selecionados.append('Natacao:')
    if tenis_var.get():
        selecionados.append('Tenis:')
    if basquete_var.get():
        selecionados.append('Basquete:')
    if surf_var.get():
        selecionados.append('Surf:')

    r_label.config(text='Esporte(s) selecionado(): '+' '.join(selecionados))

futebol_var = IntVar()
volei_var = IntVar()
natacao_var = IntVar()
tenis_var = IntVar()
basquete_var = IntVar()
surf_var = IntVar()

t = Label(i,text='Qual seu esporte favorito', bg='lightblue')
a1 = Checkbutton(i,text='Futebol',bg='Lightgreen', variable=futebol_var)
a2 = Checkbutton(i,text='Volei',bg='Lightgreen', variable=volei_var)
a3 = Checkbutton(i,text='Natacao',bg='Lightgreen', variable= natacao_var)
a4 = Checkbutton(i,text='Tenis',bg='Lightgreen', variable= tenis_var)
a5 = Checkbutton(i,text='Basquete',bg='Lightgreen', variable= basquete_var)
a6 = Checkbutton(i,text='Surf',bg='Lightgreen', variable= surf_var)

t.place(x=10,y=20)
a1.place(x=10,y=60)
a2.place(x=90,y=60)
a3.place(x=170,y=60)
a4.place(x=250,y=60)
a5.place(x=330,y=60)
a6.place(x=410,y=60)


btn = Button(i,text='Clique aqui', command=mostrar_selecionados)
btn.place(x=10, y=90)

r_label =Label(i,text='Esportes Selecionados: nenhum')
r_label.place(x=10, y=20)




# Inicia o loop da interface gráfica
i.mainloop()




