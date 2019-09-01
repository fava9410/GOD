class Move():
    """Abstract class"""
    def getStrongVs(self):
        pass
    def getWeakVs(self):
        pass

class Rock(Move):
    def getStrongVs(self):
        return [Scissors]
    def getWeakVs(self):
        return [Paper]

class Scissors(Move):
    def getStrongVs(self):
        return [Paper]
    def getWeakVs(self):
        return [Rock]

class Paper(Move):
    def getStrongVs(self):
        return [Rock]
    def getWeakVs(self):
        return [Scissors]

class MoveFactory():
    """docstring for MoveFactory."""
    def create_move(self, object_type):
        return eval(object_type)()

class Player():
    #def __init__(self,name,score):
    def __init__(self,**entries):
        #self.name = name
        #self.score = score
        #self.choice = None
        self.__dict__.update(entries)

class Round():
    rounds_to_win = 3
    winner = False
    def __init__(self,player1,player2,round,match):
        self.player1 = player1
        self.player2 = player2
        self.round = round
        self.match= match
        self.pwin = None
        self.round_history = None
    def decide_winner(self):
        if type(self.player1.choice) in self.player2.choice.getWeakVs():
            self.pwin = self.player1
        elif type(self.player1.choice) in self.player2.choice.getStrongVs():
            self.pwin = self.player2
        else:
            self.round_history = {'match_id' : self.match,
                            'round':self.round,
                            'round_winner':'-',
                            'winner_move':type(self.player1.choice).__name__}        
        if self.pwin:
            self.round_history = {'match_id' : self.match,
                            'round':self.round,
                            'round_winner':self.pwin.name,
                            'winner_move':type(self.pwin.choice).__name__}
            self.pwin.score += 1
            if self.pwin.score == self.rounds_to_win:
                self.winner = True
    def clean_choices(self):
        self.player1.choice = None
        self.player2.choice = None
