import random

''' 
Handles the random drawing of cards
'''
def draw_new_card(color=None) -> int:
    def _generate_value() -> int:
        return random.randint(1,10)

    def _generate_color() -> int:
        if color == "black":
            return 1
        return random.choice([1, 1, -1])

    return _generate_value() * _generate_color()

class Player:
    def __init__(self):
        self.score = draw_new_card(color="black")
    
    ''' Has the side effect of changing score state of player, and returns the value'''
    def hit(self):
        self.score += draw_new_card()
        return self.score

class Easy21:
    '''An instance of the easy 21 game'''
    def __init__(self):
        self.player1 = Player()
        self.dealer = Player()
        self._terminated = False
        self._state = (self.dealer.score, self.get_player1_score)

    def reset(self):
        self.__init__()

    def get_state(self):
        return self._state

    def terminate(self):
        self._terminated = True

    def get_player1_score(self):
        return self.player1.score
    
    def get_dealer_score(self):
        return self.dealer.score
    
    def get_reward(self):
        if self._terminated:
            if self.player1.score > 21 or self.player1.score < 1:
                return -1
            if self.dealer.score > 21 or self.dealer.score < 1:
                return 1
            if self.player1.score > self.dealer.score:
                return 1
            elif self.player1.score < self.dealer.score:
                return -1
            else:
                return 0
        return 0
 
    '''
    Unpacked version of the function
    hit is a boolean representing the action
    dealer_frist, player_score is the state
    '''
    def step(self, dealer_first, player_score, hit):
        if self._terminated:
            # raise GameCompletedError
            return

        if hit:
            player_score = self.player1.hit()
            if (player_score > 21 or player_score < 1):
                self.terminate()
            return ((dealer_first, player_score), self.get_reward())
        else:
            while self.get_dealer_score() < 17 and self.get_dealer_score > 0:
                dealer_score = self.dealer.hit()
            self.terminate()
            return ((dealer_first, player_score), self.get_reward())



