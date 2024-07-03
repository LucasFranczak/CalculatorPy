from tkinter import *
import itertools
import math

class Calculadora:
    def __init__(self, raiz):
        self.input_ = ""
        self.operacao_atual = ""
        self.operacoes_realizadas = [] 
        self.caixa_operacao = Texto(raiz, "", 0, 1, 6)
        self.soma = Celula()

        self.quadro_operacoes = Frame(raiz, bd=2, relief=SUNKEN)
        self.quadro_operacoes.grid(row=0, column=0, rowspan=7, padx=10, pady=10, sticky=N+S)

        def novo_botao(text, row, column, function, color="grey"):
            return Botao(raiz, text, row, column, function, color)

        def input_numero(numero):
            return lambda: self.Numero(numero)

        buttons = {}

        numbers_positions = list(itertools.product([4, 5, 6], [1, 2, 3]))
        for numero in range(1, 9):
            buttons.update({str(numero): (*numbers_positions[numero - 1], input_numero(numero))})

        buttons.update({"0": (6, 3, input_numero(0))})

        buttons.update({
            "pi()": (2, 1, self.Pi),
            "x²": (2, 2, self.Pow),
            "log10()": (2, 3, self.Log10),
            "%": (2, 4, self.Percentual),
            "raiz()": (2, 5, self.Raiz_Quadrada),
            "clear": (5, 5, self.clear_, "blue"),
            "sen()": (3, 1, self.Seno),
            "cos()": (3, 2, self.Cosseno),
            "tg()": (3, 3, self.Tangente),
            "+": (3, 4, self.Soma),
            "-": (4, 4, self.Subtracao),
            "*": (5, 4, self.Multiplicacao),
            "/": (6, 4, self.Divisao),
            "=": (6, 5, self.Igual, "orange"),
            " ": (4, 5, lambda: None),
            "  ": (3, 5, lambda: None)
        })

        for button in buttons.keys():
            if len(buttons[button]) == 4:
                novo_botao(button, *buttons[button])
            else:
                novo_botao(button, *buttons[button], "grey")

    def clear_(self):
        self.input_ = ""
        self.operacao_atual = ""
        self.caixa_operacao.atualiza_texto("0")

    def Raiz_Quadrada(self):
        self.operacao_atual += "√"
        self.input_ = ""
        self.caixa_operacao.atualiza_texto(self.operacao_atual)

    def Seno(self):
        self.operacao_atual += "sin("
        self.input_ = ""
        self.caixa_operacao.atualiza_texto(self.operacao_atual)

    def Cosseno(self):
        self.operacao_atual += "cos("
        self.input_ = ""
        self.caixa_operacao.atualiza_texto(self.operacao_atual)

    def Tangente(self):
        self.operacao_atual += "tan("
        self.input_ = ""
        self.caixa_operacao.atualiza_texto(self.operacao_atual)

    def Log10(self):
        self.operacao_atual += "log10("
        self.input_ = ""
        self.caixa_operacao.atualiza_texto(self.operacao_atual)

    def Pi(self):
        self.operacao_atual += str(math.pi)
        self.input_ = ""
        self.caixa_operacao.atualiza_texto(self.operacao_atual)

    def Pow(self):
        self.operacao_atual += "**2"
        self.input_ = ""
        self.caixa_operacao.atualiza_texto(self.operacao_atual)

    def Percentual(self):
        self.operacao_atual += "/100"
        self.input_ = ""
        self.caixa_operacao.atualiza_texto(self.operacao_atual)

    def Igual(self):
        try:
            resultado = eval(self.operacao_atual)
            self.input_ = str(resultado)
            # Adiciona a operação à lista de operações realizadas
            self.operacoes_realizadas.append(self.operacao_atual + " = " + self.input_)
            # Atualiza o quadro de operações realizadas
            self.atualiza_quadro_operacoes()
        except Exception as e:
            self.input_ = "Erro"
        self.operacao_atual = self.input_
        self.caixa_operacao.atualiza_texto(self.operacao_atual)

    def Soma(self):
        self.operacao_atual += "+"
        self.input_ = ""
        self.caixa_operacao.atualiza_texto(self.operacao_atual)

    def Multiplicacao(self):
        self.operacao_atual += "*"
        self.input_ = ""
        self.caixa_operacao.atualiza_texto(self.operacao_atual)

    def Divisao(self):
        self.operacao_atual += "/"
        self.input_ = ""
        self.caixa_operacao.atualiza_texto(self.operacao_atual)

    def Subtracao(self):
        self.operacao_atual += "-"
        self.input_ = ""
        self.caixa_operacao.atualiza_texto(self.operacao_atual)

    def Numero(self, numero):
        self.input_ += str(numero)
        self.operacao_atual += str(numero)
        self.caixa_operacao.atualiza_texto(self.operacao_atual)

    def atualiza_quadro_operacoes(self):
        # Limpa o quadro atual
        for widget in self.quadro_operacoes.winfo_children():
            widget.destroy()

        # Exibe as operações realizadas no quadro
        for index, operacao in enumerate(self.operacoes_realizadas):
            label_operacao = Label(self.quadro_operacoes, text=operacao, font=("Arial", 12))
            label_operacao.grid(row=index, column=0, sticky=W)

class Botao:
    def __init__(self, frame, text_botao, linha, coluna, comando, color="grey"):
        self.button = Button(frame, text=text_botao, fg="black", bg=color, command=comando, font=("Arial", "20", "bold"))
        self.button["width"] = 5
        self.button["height"] = 1
        self.button.grid(row=linha, column=coluna)


class Texto:
    def __init__(self, raiz, texto, row, column, columnspan):
        self.texto = Label(raiz, text=texto, font=("Arial", "24", "bold"))
        self.texto["height"] = 2
        self.texto["width"] = 20
        self.texto.grid(row=row, column=column, columnspan=columnspan, sticky=W + E + N + S)

    def atualiza_texto(self, novo_texto):
        self.texto.config(text=novo_texto)


class Celula:
    def __init__(self):
        self._numero_A = None
        self._numero_B = None
        self._sinal = None

    def soma(self):
        return float(self._numero_A) + float(self._numero_B)

    def subtracao(self):
        return float(self._numero_A) - float(self._numero_B)

    def multiplicacao(self):
        return float(self._numero_A) * float(self._numero_B)

    def divisao(self):
        return float(self._numero_A) / float(self._numero_B)


raiz = Tk()
raiz.title("Calculadora")
raiz.geometry("670x400")
m = Calculadora(raiz)
raiz.mainloop()
