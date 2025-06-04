"""
Autores: Vitor Ramos de Farias (RM: 561958) 
Carlos Eduardo Sanches Mariano (RM: 561756)
"""

"""  Este código implementa a lógica do sistema StormShield Sentinel  de acordo com Software and Total Experience, 
com uma interface gráfica utilizando a biblioteca Tkinter. """


"""  == INICIO DO CÓDIGO ==  """

# Importação de bibliotecas necessárias
import tkinter as tk # Responsável pela interface gráfica
from tkinter import messagebox, Toplevel, Label, Entry, Button, Frame, StringVar # Mostra ao python que queremos alguma de suas bibliotecas, como janelas botoes, menus, etc
import random # random == Aleatório
from datetime import datetime, timedelta # Ajuda a lidar com datas, horários, com datetime e timedelta, estou importante uma biblioteca especifica
#date time == Ajuda a saber "Quando" algo aconteceu  
#Exemplo no nosso código: Nós a usamos para saber o momento exato em que um código de confirmação foi gerado (datetime.now()), permitindo-nos calcular quando ele irá expirar.

#Time delta == diferença no tempo
#Exemplo no nosso código: Calcular a expiração de 5 minutos e previsão do tempo

import re
#Import re == importa expressões regulares, usada para encontrar, validar e manipular padrões dentro de textos.



'''# ======================= #'''

# --- Gerenciamento de Dados: Simulação do Banco de Dados ---
# Dicionários e listas para armazenar informações em tempo de execução.
usuarios_cadastrados = {}
alertas_emitidos = []
dados_meteorologicos_simulados = {}
codigos_confirmacao = {}


# --- Modularização: Funções da Lógica Principal ---

def validar_formato_telefone(telefone): 
    """
    Valida se o número de telefone segue o formato (XX) XXXXX-XXXX.
    Usa expressão regular para uma validação mais precisa.
    Critério: Validação de Dados (RF003)
    """
    # Padrão para (XX) XXXXX-XXXX ou (XX)XXXXX-XXXX
    padrao = re.compile(r'^\(\d{2}\) ?\d{5}-?\d{4}$')
    return re.match(padrao, telefone) is not None # a biblioteca re, tenta "casar = match" com o padra se não "match" vai ser igual a None == "Formato de telefone inválido e pede para ele 
                                                  #digitar novamente"


def simular_coleta_dados_meteorologicos(localizacao):
    """
    Simula a coleta de dados de APIs e sensores IoT.
    Critério: Lógica de Processamento (RF008)
    """
    if localizacao not in dados_meteorologicos_simulados:# Garante que, uma vez que os dados para uma localização são gerados, eles permaneçam os mesmos durante a execução do programa
        dados_meteorologicos_simulados[localizacao] = { # esse bloco só vai ser executado caso seja a primeira vez que ele foi chamado para uma localização
            "temperatura": random.uniform(15.0, 30.0), 
            "umidade": random.randint(40, 95), # Randint 
            "precipitacao": random.randint(0, 100),
            "nivel_agua_rio_mm": random.randint(1000, 5000)
        }
    return dados_meteorologicos_simulados[localizacao] #retorna dados metereologicos


def verificar_risco_alagamento(dados):
    """
    Processa os dados coletados para identificar riscos de alagamento.
    Critério: Estruturas de Programação, Lógica de Processamento (RF005)
    """
    if dados["precipitacao"] > 70 or dados["nivel_agua_rio_mm"] > 4500: # Se dados de "precipitacao" for maior que 70 ou dados de "nivel_agua rio_mm" maior que 4500 == "ALTA"
        return "ALTA"
    elif dados["precipitacao"] > 50 or dados["nivel_agua_rio_mm"] > 3500: # Se dados de "precipitacao" for maior que 50 ou dados de "nivel_agua rio_mm" maior que 3500 == "MODERADO"
        return "MODERADO"
    return "BAIXO" # Else = Baixo





# --- Funções da Interface Gráfica (GUI) ---

def definir_estilos(): # Aqui estou definindo uma função de cores padroes e fontes utilizadas
    """Retorna um dicionário com as cores e fontes padrão do aplicativo."""
    
    estilos = {
        "cor_borda": "#0078D7",        # Azul brilhante da borda
        "cor_fundo": "#0A1921",        # Azul escuro do fundo
        "cor_botao_bg": "#B2F0E8",       # Ciano claro do fundo do botão
        "cor_botao_texto": "#000000",   # Preto para o texto do botão
        "cor_branca": "#FFFFFF",       # Branco para o texto do título
        "cor_ciano_texto": "#79FBFD",   # Ciano para "StormShield"
        "fonte_titulo": ("Garamond", 24), # Fonte que nós escolhemos
        "fonte_botao": ("Montsserat", 11, "bold") # Fonte texto do botão
    }
    return estilos


class StormShieldApp(tk.Tk):  # Criando a janela principal do aplicativo com tkinter # tk. tk é uma classe que existe dentro da biblioteca do tkinter
     
    def __init__(self): # inicio de execucao, uso de self para saber com "QUEM" cada um vai ser trabalhado, "Nome de quem?" "Idade de quem?"
        super().__init__() # A função "Super" da acesso a classe pai (tk.tk) do tkinter

        # Carrega os estilos do nosso tema
        estilos = definir_estilos()

        # --- Configurações da Janela Principal ---
        self.title("StormShield Sentinel") # Titulo
        self.geometry("600x450") # Qual o tamanho da tela?
        self.resizable(False, False) # Para que nao possa alterar o dimensionamento da janela, para manter um padrao
        
        # Usando o valor do dicionário, para isso deixamos entre [] para chamar o indice
        self.configure(bg=estilos["cor_borda"])

        # Frame principal que cria o efeito de borda
        main_frame = Frame(self, bg=estilos["cor_fundo"]) # bg = Define a cor de fundo, frame = cria um container
        main_frame.pack(pady=2, padx=2, fill="both", expand=True) # Torna o Frame visível e o posiciona na tela usando o gerenciador .pack() biblioteca especifica do tkinter
        # fill="both": Faz o Frame se expandir para preencher todo o espaço disponível

        # --- Layout do Título ---
        title_frame = Frame(main_frame, bg=estilos["cor_fundo"]) # Frame, cria um novo frame e define a cor de fundo, sendo pega do dicionario estilos
        title_frame.pack(pady=(40, 20)) # faz com que o title_frame possa ser visivel

        Label(title_frame, text="Bem vindo", font=estilos["fonte_titulo"], fg=estilos["cor_branca"], bg=estilos["cor_fundo"]).pack()
        second_line_frame = Frame(title_frame, bg=estilos["cor_fundo"])
        second_line_frame.pack()
        Label(second_line_frame, text="ao ", font=estilos["fonte_titulo"], fg=estilos["cor_branca"], bg=estilos["cor_fundo"]).pack(side="left")
        Label(second_line_frame, text="StormShield", font=(estilos["fonte_titulo"][0], estilos["fonte_titulo"][1], "bold"), fg=estilos["cor_ciano_texto"], bg=estilos["cor_fundo"]).pack(side="left")

        # --- Estilizando os Botões ---
        buttons_frame = Frame(main_frame, bg=estilos["cor_fundo"])
        buttons_frame.pack(pady=20)
        
        # Propriedades comuns dos botões
        button_opts = {
            "bg": estilos["cor_botao_bg"],
            "fg": estilos["cor_botao_texto"],
            "font": estilos["fonte_botao"],
            "width": 25,
            "relief": 'flat',
            "pady": 5
        }

        # Estilizando os Botões     texto dentro do botão     exibir janela que foi chamada       armazenar conjuntos
        Button(buttons_frame, text="Cadastrar Novo Usuário", command=self.abrir_janela_cadastro, **button_opts).pack(pady=5)
        Button(buttons_frame, text="Ver Previsão do Tempo", command=self.exibir_previsao_semanal, **button_opts).pack(pady=5)
        Button(buttons_frame, text="Ver Mapa Meteorológico", command=self.exibir_mapa_meteorologico, **button_opts).pack(pady=5)
        Button(buttons_frame, text="Ver Números de Emergência", command=self.exibir_numero_emergencia, **button_opts).pack(pady=5)
        Button(buttons_frame, text="Sair", command=self.quit, **button_opts).pack(pady=5)

        # --- Configurações Finais ---
        self.usuario_logado = None # Começa com None, porque nenhum usario foi logado antes de iniciar o programa
        self.verificar_alertas_periodicamente()


    def abrir_janela_cadastro(self): 

        # Carrega os estilos para usar nesta janela
        estilos = definir_estilos()

        # Janela de Toplevel para o cadastro
        self.janela_cadastro = Toplevel(self, bg=estilos["cor_borda"]) # Cor de fundo
        self.janela_cadastro.title("Cadastro de Usuário") # Titulo da pagina
        self.janela_cadastro.geometry("500x400") # Dimensão da janela
        self.janela_cadastro.resizable(False, False) # Impede que os úsuarios possam redimensionar a janela
        

        # Frame principal que cria a área de conteúdo e o efeito da borda
        cadastro_container = Frame(self.janela_cadastro, bg=estilos["cor_fundo"])
        cadastro_container.pack(pady=2, padx=2, fill="both", expand=True)

        # --- Título da Janela de Cadastro ---
        Label(
            cadastro_container, 
            text="Novo Cadastro", 
            font=(estilos["fonte_titulo"][0], 18), # Pega a fonte indice 0 de estilos, e tamanho 18
            fg=estilos["cor_branca"],
            bg=estilos["cor_fundo"]
        ).pack(pady=(20, 25))

        # --- Campos de Entrada ---

        label_opts = {
            'font': (estilos["fonte_botao"][0], 10), 
            'fg': estilos["cor_branca"], 
            'bg': estilos["cor_fundo"]
        }
        
        # Opções de estilo para as caixas de texto 
        entry_opts = {
            'font': (estilos["fonte_botao"][0], 12),
            'width': 35,
            'bg': estilos["cor_botao_bg"],  
            'fg': estilos["cor_botao_texto"], 
            'relief': 'flat',               # Usamos para remover a borda 3D
            'bd': 12,                       # Criar um padding interno horizontal
            'insertbackground': estilos["cor_branca"] # Cor do cursor de digitação
        }

        Label(cadastro_container, text="Nome Completo:", **label_opts).pack(pady=(10, 2)) # Criar Nome completo == Label(Criar rotulo)
        self.entry_nome = Entry(cadastro_container, **entry_opts) # Entry = Criar uma caixa de texto pro úsuario poder se cadastrar #cadastrar_container fala que label deve ser colocada dentro do frame cadastrar
        self.entry_nome.pack()

        Label(cadastro_container, text="Telefone (XX) XXXXX-XXXX:", **label_opts).pack(pady=(15, 2)) # Criar label telefone e mostra o text "exemplo"
        self.entry_telefone = Entry(cadastro_container, **entry_opts)
        self.entry_telefone.pack() # pac serve para "enpacotar" o conteudo e colocalo na tela
        
        # --- Botões de Ação ---
        buttons_frame = Frame(cadastro_container, bg=estilos["cor_fundo"])
        buttons_frame.pack(pady=30)
        
        button_opts_cadastro = {
            'bg': estilos["cor_botao_bg"], 'fg': estilos["cor_botao_texto"], 
            'font': estilos["fonte_botao"], 'relief': 'flat', 'pady': 5, 'width': 12
        }
        
        Button(buttons_frame, text="Cadastrar", command=self.realizar_cadastro, **button_opts_cadastro).pack(side="left", padx=10) # Command=self serve para interatividade do botao, dar vida a ele
        
        # Adicionando um botão de "Voltar" para fechar a janela
        Button(buttons_frame, text="Voltar", command=self.janela_cadastro.destroy, **button_opts_cadastro).pack(side="left", padx=10)

    def realizar_cadastro(self):
        nome = self.entry_nome.get() # Self serve para se direcionar a quela certa "coisa", "pessoa"
        telefone = self.entry_telefone.get() # Self serve para buscar o numero de entrada 

        if not nome or not telefone:
            messagebox.showerror("Erro de Cadastro", "Todos os campos são obrigatórios.", parent=self.janela_cadastro)
            return

        if not validar_formato_telefone(telefone):
            messagebox.showerror("Erro de Cadastro", "Formato de telefone inválido. Use (XX) XXXXX-XXXX.",
                                 parent=self.janela_cadastro)
            return

        # Lógica de confirmação do número
        if self.confirmar_numero_telefone_gui(telefone):
            usuarios_cadastrados[telefone] = {"nome": nome, "localizacao_atual": "Osasco, SP"} # Usando exemplo de que a pessoa esteja em "Osasco, SP"
            self.usuario_logado = telefone  # Simula login após cadastro
            messagebox.showinfo("Sucesso", f"Usuário {nome} cadastrado com sucesso!", parent=self.janela_cadastro)
            self.janela_cadastro.destroy() # self.janela_cadastr == Janela secundaria(toplevel) .destroy() remove a janela e tudo dentro dela
        else: 
            messagebox.showerror("Erro de Validação", "Não foi possível validar seu número de telefone.", # messagebox.showerror, serve para criar um popup mostrando a menssagem
                                 parent=self.janela_cadastro)

    def confirmar_numero_telefone_gui(self, telefone):

        # Gera código de confirmação
        codigo = str(random.randint(100000, 999999)) # usando a biblioteca random == numeros aleatorios
        expiracao = datetime.now() + timedelta(minutes=5) # A hora de expiração é igual a hora exata de agora mais cinco minutos, em resumo tem 5 minutos pra expirar
        codigos_confirmacao[telefone] = {'codigo': codigo, 'expiracao': expiracao}

        # Janela para inserir o código
        janela_confirmacao = Toplevel(self.janela_cadastro)
        janela_confirmacao.title("Confirmação de Número")
        janela_confirmacao.geometry("350x150") # Tamanho da janela

        Label(janela_confirmacao, text=f"Enviamos um código para {telefone}.\n(Simulação) Código: {codigo}").pack(
            pady=10)
        entry_codigo = Entry(janela_confirmacao, width=20)
        entry_codigo.pack()

        resultado = tk.BooleanVar()  # Para aguardar o resultado da confirmação

        def validar():
            # A linha abaixo é a condição principal, que precisa ser 100% verdadeira para o código funcionar.
            # Ela tem duas checagens, unidas pelo "and" (E).
            if entry_codigo.get() == codigo and datetime.now() < codigos_confirmacao[telefone]['expiracao']:
                # Se a validação for um sucesso, as duas linhas abaixo são executadas.
                resultado.set(True)
                janela_confirmacao.destroy()
            else: # Se não
                messagebox.showerror("Erro", "Código inválido ou expirado.", parent=janela_confirmacao) # Menssagme de erro
                resultado.set(False)

        Button(janela_confirmacao, text="Validar", command=validar).pack(pady=10)
        self.wait_window(janela_confirmacao)  # Aguarda o fechamento da janela de confirmação
        return resultado.get()

    def verificar_alertas_periodicamente(self):
        """ Simula a verificação de alertas em background. """
        if self.usuario_logado:
            usuario = usuarios_cadastrados[self.usuario_logado]
            localizacao = usuario['localizacao_atual']
            dados = simular_coleta_dados_meteorologicos(localizacao)
            risco = verificar_risco_alagamento(dados)

            if risco in ["ALTA", "MODERADO"]:
                mensagem = f"Risco de alagamento {risco} em {localizacao}.\nConsulte as rotas de fuga no mapa."
                # RN003 e RN004: Mostra um alerta visual que simula SMS/Ligação
                messagebox.showwarning("Alerta de Emergência!", mensagem)
                alertas_emitidos.append({
                    "telefone": self.usuario_logado, "data_hora": datetime.now().isoformat(), "risco": risco
                })

        # Agenda a próxima verificação para daqui a 30 segundos (30000 ms)
        self.after(30000, self.verificar_alertas_periodicamente)

    def exibir_previsao_semanal(self):
        if not self.usuario_logado:
            messagebox.showinfo("Informação", "Por favor, cadastre um usuário para ver a previsão.")
            return

        previsao_texto = f"--- Previsão do Tempo para 7 Dias em {usuarios_cadastrados[self.usuario_logado]['localizacao_atual']} ---\n\n" # Mostra a previsao de 7 dias do Usuario cadastrado Especifico "Self".usuario logado, com base na localizao de exmplo "Osasco"
        for i in range(7): # por indice de 0 a 7 == dias da semana
            dia = datetime.now() + timedelta(days=i)
            # Simula dados diferentes para cada dia
            dados_dia = simular_coleta_dados_meteorologicos(f"local_{i}")
            previsao_texto += f"{dia.strftime('%d/%m/%Y')} - Temp: {dados_dia['temperatura']:.1f}°C, " \
                              f"Umidade: {dados_dia['umidade']}%, Precipitação: {dados_dia['precipitacao']}%\n"

        messagebox.showinfo("Previsão Semanal", previsao_texto)

    def exibir_mapa_meteorologico(self):
        if not self.usuario_logado: # SE nao tiver nenhum usuario cadastrado 
            messagebox.showinfo("Informação", "Por favor, cadastre um usuário para ver o mapa.") # Menssagem popup
            return

        mapa_texto = f"--- Mapa Meteorológico para {usuarios_cadastrados[self.usuario_logado]['localizacao_atual']} ---\n" # Cria o cabecaloho do texto
        mapa_texto += "[Legenda: '=' Chuva Leve, '*' Chuva Forte, 'o' Nuvens]\n\n" # Adiciona uma legenda ao mapa
        for _ in range(5): # loop de 0 a 5
            linha_mapa = "".join(random.choice([" = ", " * ", " o ", "   "]) for _ in range(10)) # 4. Cria uma única linha do mapa com 10 símbolos aleatórios usando random
            mapa_texto += linha_mapa + "\n"   # Adiciona a linha recém-criada ao texto final do mapa

        messagebox.showinfo("Mapa Meteorológico", mapa_texto) # pop up

    




    
    def exibir_numero_emergencia(self):
        """
        Exibe os principais números de emergência em uma janela de informação.
        """
        estilos = definir_estilos()

        janela_emergencia = Toplevel(self, bg=estilos["cor_borda"])
        janela_emergencia.title("Números em caso de Emergência")
        janela_emergencia.geometry("450x350")


        container = Frame(janela_emergencia, bg=estilos["cor_fundo"])
        container.pack(padx=2, pady=2, fill="both", expand=True)


        Label( # TITULO
            container,
            text="Números de Emergência",
            font=(estilos["fonte_titulo"][0], 22, "bold"), # Usando a nossa fonte, em negrito
            fg=estilos["cor_ciano_texto"], # PEgando cor do texto de estilos
            bg=estilos["cor_fundo"]
        ).pack(pady=(20, 15)) # pady=(20, 15) -> 20px de espaço em cima, 15px embaixo


        # Criando um dicionario para simplificar a escolha utilizando um loop ofr
        lista_de_numeros = [
            "Defesa Civil: 199",
            "Corpo de Bombeiros: 193",
            "Polícia Militar: 190",
            "SAMU (Ambulância): 192",
        ]

        label_opts = {
            'font': (estilos["fonte_botao"][0], 14), 
            'fg': estilos["cor_branca"], 
            'bg': estilos["cor_fundo"]
        }


        for costumizacao in lista_de_numeros:
            Label(
                container,
                text=costumizacao,
                **label_opts  # Desempacota o dicionário de opções aqui
            ).pack(pady=8)

        # 4. Adicionar um botão de "Fechar" estilizado
        btn_fechar = Button(
            container,
            text="Fechar",
            command=janela_emergencia.destroy, # Comando para destruir ESTA janela
            bg=estilos["cor_botao_bg"],
            fg=estilos["cor_botao_texto"],
            font=estilos["fonte_botao"],
            width=10,
            relief='flat', # relief = relevo ; remove qualquer efeito de borda 3D, fazendo com que o widget pareça estar completamente nivelado com o fundo
            pady=5
        )
        btn_fechar.pack(pady=(25, 0)) # Espaçamento para o botão

        # Garante que a janela fique "modal" (foco nela) sobre a janela de cadastro, se aberta
        janela_emergencia.transient(self)
        janela_emergencia.grab_set()
                                                

# --- Ponto de Entrada da Aplicação ---

if __name__ == "__main__":
    app = StormShieldApp()
    app.mainloop()