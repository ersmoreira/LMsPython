class Participant:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.choice = ""

    def choose(self):
        self.choice = input(
            '{name}, escolhe pedra, papel, tesoura, lagarto, spock: '.format(name=self.name))
        print('{name} escolheu {choice}'.format(
            name=self.name, choice=self.choice))

    def toNumericalChoice(self):
        switcher = {
            "pedra": 0,
            "papel": 1,
            "tesoura": 2,
            "lagarto": 3,
            "spock": 4
        }
        return switcher[self.choice]

    def incrementPoint(self):
        self.points += 1


class GameRound:
    def __init__(self, p1, p2):
        self.rules = [
            [0, -1, 1, 1, -1],
            [1, 0, -1, -1, 1],
            [-1, 1, 0, 1, -1],
            [-1, 1, -1, 0, 1],
            [1, -1, 1, -1, 0]
        ]
        p1.choose()
        p2.choose()
        result = self.compareChoices(p1, p2)
        print('A jogada resultou em {result}'.format(
            result=self.getResultAsString(result)))

        if result > 0:
            p1.incrementPoint()
        elif result < 0:
            p2.incrementPoint()

    def compareChoices(self, p1, p2):
        return self.rules[p1.toNumericalChoice()][p2.toNumericalChoice()]

    def awardPoints(self):
        print('Implement')

    def getResultAsString(self, result):
        res = {
            0: 'Empate',
            1: 'Vitória',
            -1: 'Derrota'
        }
        return res[result]


class Game:
    def __init__(self):
        self.endGame = False
        self.participant = Participant('Jogador1')
        self.secondParticipant = Participant('JOgador2')

    def start(self):
        while not self.endGame:
            gameRound = GameRound(self.participant, self.secondParticipant)
            self.checkEndCondition()

    def checkEndCondition(self):
        resposta = input('Continuar o jogo (s/n)? ')
        if resposta == 's':
            GameRound(self.participant, self.secondParticipant)
            self.checkEndCondition()
        else:
            print(
                'O jogo acabou.\n{p1name} tem {p1points} pontos.\n{p2name} tem {p2points} pontos.'.format(p1name=self.participant.name, p1points=self.participant.points, p2name=self.secondParticipant.name, p2points=self.secondParticipant.points))
            self.determineWinner()
            self.endGame = True

    def determineWinner(self):
        resultString = 'It\'s a Draw'
        if self.participant.points > self.secondParticipant.points:
            resultString = 'O vencedor é o {name}.'.format(
                name=self.participant.name)
        elif self.secondParticipant.points > self.participant.points:
            resultString = 'O vencedor é o {name}.'.format(
                name=self.secondParticipant.name)
        print(resultString)


game = Game()
game.start()
