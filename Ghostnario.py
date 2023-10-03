import tkinter as tk
from tkinter import messagebox
import tkinter.simpledialog

class GhosnarioGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Ghostnario")
        self.master.geometry("500x300")
        self.master.configure(background="#000000")

        self.estado_personagem = "vivo"
        self.fase = 1

        self.label = tk.Label(master, text="GhostNario😱")
        self.label.pack()
        self.button_iniciar = tk.Button(master, text="Iniciar Jogo", command=self.iniciar_jogo)
        self.button_iniciar.pack()
        self.button_sair = tk.Button(master, text="Sair", command=self.sair_jogo)
        self.button_sair.pack()

    def iniciar_jogo(self):
        self.estado_personagem = "vivo"
        self.fase = 1
        self.executar_fase()

    def executar_fase(self):
        if self.estado_personagem == "vivo":
            if self.fase == 1:
                resposta1 = self.pergunta("GhostNario😱\n\nFASE 1\n\nVocê é um desempregado, e esta semana recebeu a notícia de que está no Serasa. Seu locador te expulsa de casa devido a atrasos de pagamento. \nDesesperado, você liga para seu melhor amigo e SUPLICA por abrigo por pelo menos uma noite. Ele aceita, e te passa o endereço. Ao chegar no endereço que Roberto mandou, você percebe que ele te fez de bobo. Você está no meio de uma floresta, e seu 4g não funciona. \nVocê decide descer de seu Corsa Joy 2004 e ir até uma casa que avistou. Ao caminhar até lá, você leva uma pedrada na cabeça e fica inconsciente. De repente você acorda e supõe que está naquela casa que viu anteriormente.\nHavia poucos móveis lá dentro, mas um pequeno armário lhe chama atenção.\nOpções: abrir armário; ficar imóvel")
                if resposta1.lower() == "ficar imóvel":
                    self.mostrar_mensagem("Você leva uma pancada de Ghostnario na cabeça, mas sobrevive.")
                elif resposta1.lower() == "abrir armário":
                    resposta2 = self.pergunta("Você encontrou um estilete. Deseja pegá-lo? (sim/não)")
                    if resposta2.lower() == 'não':
                        self.mostrar_mensagem("Ghostnario percebeu que você não é muito bom em tomar decisões e te matou.")
                        self.estado_personagem = "morto"
                    elif resposta2.lower() == 'sim':
                        self.mostrar_mensagem("Você agora tem um objeto de defesa.")
                else:
                    self.mostrar_mensagem("Você deve ter escrito errado.")
                    self.estado_personagem = "morto"

            if self.estado_personagem == "vivo":
                if self.fase == 1:
                    resposta3 = self.pergunta("FASE 2\n\nAlguns minutos depois, você se assusta com um barulho de telefone tocando. Nem sabia que ali estava um telefone antes. Deseja atendê-lo? (sim/não)")
                    if resposta3.lower() == "não":
                        self.mostrar_mensagem("Ghostnario te acha preguiçoso e te assassina.")
                        self.estado_personagem = "morto"
                    elif resposta3.lower() == "sim":
                        resposta4 = self.pergunta("Você atende o telefone. Uma mulher estava falando desesperadamente para você ir embora. \nVocê fica confuso. \n-vá embora por favor!! Não é seguro, há um espírito nesta floresta. Ele mata todos que aparecem \n-quem está falando? Sua voz me parece familiar. \n-Não temos tempo para isso. \n-ata \n-Vou mandar um exorcista para te ajudar. \n-ok, rápido.")
                        if resposta4.lower() == "não":
                            self.mostrar_mensagem("Ghostnario te assassina.")
                            self.estado_personagem = "morto"
                        elif resposta4.lower() == "sim":
                            self.mostrar_mensagem("Você decide esperar pelo exorcista.")

            if self.estado_personagem == "vivo":
                if self.fase == 1:
                    resposta5 = self.pergunta("FASE 3\n\nSe passou 1 hora desde que falou com Simone. Você fica assustado com muitos barulhos lá fora.\nGostaria de ir ver? (sim/não)")
                    if resposta5.lower() == "não":
                        self.mostrar_mensagem("Ghostnario arranca seus membros e você morre")
                        self.estado_personagem = "morto"
                    elif resposta5.lower() == "sim":
                        self.mostrar_mensagem("Era Alexandre de Moraes, o exorcista.")

            if self.estado_personagem == "vivo":
                if self.fase == 1:
                    resposta6 = self.pergunta("FASE 4\n\nApós a chegada de Alexandre, você percebe que ele surpreendentemente tem graduação em mecânica de Corsas. Pedir para ele consertar seu Corsa? (sim/não)")
                    if resposta6.lower() == "não":
                        self.mostrar_mensagem("Vocês decidem fugir imediatamente. No caminho escutam alguns barulhos mas nem pensam em olhar para trás. Ao chegar no carro de Alexandre, você se vira e não vê Alexandre. Então você abandona Alexandre e vai embora sozinho. Você sobreviveu! Agora lide com as consequências de abandonar Alexandre em Ghosnario 2")
                        
                    elif resposta6.lower() == "sim":
                        self.mostrar_mensagem("Ele não gosta de sua pergunta e vai embora. Você fica sozinho e triste.")
            
            self.fase += 1
            if self.fase > 4:
                self.fase = 1

    def pergunta(self, texto):
        resposta = tkinter.simpledialog.askstring("Pergunta", texto)
        return resposta

    def mostrar_mensagem(self, mensagem):
        tk.messagebox.showinfo("Mensagem", mensagem)

    def sair_jogo(self):
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    game = GhosnarioGame(root)
    root.mainloop()
