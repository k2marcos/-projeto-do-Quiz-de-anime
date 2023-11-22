class Pergunta:
    def __init__(self, enunciado, alternativas):
        self.enunciado = enunciado
        self.alternativas = alternativas 

class Alternativa: 
    def __init__(self, texto, correta):
        self.texto = texto
        self.correta = correta

PERGUNTAS = [
    Pergunta("Quem é o irmão de Kokoshibo em Demon Slayer?",[
        Alternativa("Tanjiro",False),
        Alternativa("Zenitsu",False),
        Alternativa("Yoriichi",True),
        Alternativa(" Naruto",False),
    ]),
    Pergunta("Qual é o personagem mais forte de Jujutsu Kaisen?",[
        Alternativa(" Gojo",True),
        Alternativa("Sukuna",False),
        Alternativa("Goku",False),
        Alternativa(" Naruto",False),
    ]),
    Pergunta("Quem é o protagonista de Black Clover?",[
        Alternativa("Seya",False),
        Alternativa("Saitama",False),
        Alternativa("Asta",True),
        Alternativa(" Deku",False),
    ]),
     Pergunta("Quem é o super-herói mais conhecido do mundo?",[
        Alternativa("Homem-Aranha",False),
        Alternativa("Homem de Ferro",False),
        Alternativa("Super-Homem",True),
        Alternativa(" Batman",False),
    ]),
     Pergunta("Qual é o vilão mais famoso do mundo?",[
        Alternativa("Lord Voldemort",True),
        Alternativa("Coringa",False),
        Alternativa("Freeza",False),
        Alternativa("Darth Vader",False),
    ]),
    Pergunta("Quantos filhos o Rei Demônio de Nanatsu no Taizai tem?",[
        Alternativa("3",False),
        Alternativa("2",False),
        Alternativa("10",True),
        Alternativa("0",False),
    ]),
    Pergunta("Quantas vezes Kuririn morreu para Freeza em Dragon Ball?",[
        Alternativa("0",False),
        Alternativa("5",False),
        Alternativa("3",True),
        Alternativa("6",False),
    ]),
     Pergunta("Quem é o protagonista em Naruto?",[
        Alternativa("Naruto Shipuden",False),
        Alternativa("Naruto Uzumaki",False),
        Alternativa("Ichigo",True),
        Alternativa("Goku",False),
    ]),
]
