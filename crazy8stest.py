import random

#Create Card class which initializes instance of one card
class Card():
    def __init__ (self, suit_id, rank_id):
        self.suit_id = suit_id
        self.rank_id = rank_id
        if self.rank_id == 1:
            self.rank = "Ace"
            self.value = 1
        elif self.rank_id == 11:
            self.rank = "Jack"
            self.value = 10
        elif self.rank_id == 12:
            self.rank = "Queen"
            self.value = 10
        elif self.rank_id == 13:
            self.rank = "King"
            self.value = 10
        elif 2 <= self.rank_id <= 10:
            self.rank = str(self.rank_id)
            self.value = self.rank_id
        else:
            self.rank = "RankError"
            self.value = -1

        if self.suit_id == 1:
            self.suit = "Diamonds"
        elif self.suit_id == 2:
            self.suit = "Hearts"
        elif self.suit_id == 3:
            self.suit = "Spades"
        elif self.suit_id == 4:
            self.suit = "Clubs"
        else:
            self.suit = "SuitError"
        self.short_name = self.rank[0] + self.suit[0]
        if self.rank == '10':
            self.short_name = self.rank + self.suit[0]
        self.long_name = self.rank + " of " + self.suit

    def __str__(self):
        return  self.long_name

def init_cards():
    global deck, p_hand, c_hand
    for suit_id in range(1, 5):
        for rank_id in range(1, 14):
            new_card = Card(suit_id, rank_id)
            if new_card.rank == 8:
                new_card.value = 50
            deck.append(new_card)
    for card in range(7):
        p_card = random.choice(deck)
        deck.remove(p_card)
        p_hand.append(p_card)
    for card in range(7):
        c_card = random.choice(deck)
        deck.remove(c_card)
        c_hand.append(c_card)


def get_new_suit():
    global active_suit
    got_suit = False
    while not got_suit:
        suit = input("Pick a suit: ")
        if suit.lower() == 'd':
            active_suit = "Diamonds"
            got_suit = True
        elif suit.lower() == 'h':
            active_suit = "Hearts"
            got_suit = True
        elif suit.lower() == 's':
            active_suit = "Spades"
            got_suit = True
        elif suit.lower() == 'c':
            active_suit = "Clubs"
            got_suit = True
        else:
            print("Not a valid suit. Try again.")
    print("You picked", active_suit)


def computer_turn():
    global c_hand, up_card, active_suit, deck, blocked
    options = []
    for card in c_hand:
        if card.rank == '8':

            c_hand.remove(card)
            up_card = card
            print("Computer played", card.short_name)
            #suit_totals = [diamonds, spades, hearts, clubs]
            suit_totals = [0, 0, 0, 0]
            for suit in range(1, 5):
                for card in c_hand:
                    if card.suit_id == suit:
                        suit_totals[suit - 1] += 1
            long_suit = 0
            for i in range(4):
                if suit_totals[i] > long_suit:
                    long_suit = i
            if long_suit == 0:
                active_suit = "Diamonds"
            elif long_suit == 1:
                active_suit = "Hearts"
            elif long_suit == 2:
                active_suit = "Spades"
            elif long_suit == 3:
                active_suit = "Clubs"
            print("Computer changed suit to", active_suit)
            return
        else:
            if card.suit == active_suit:
                options.append(card)
            elif card.rank == up_card.rank:
                options.append(card)
    if len(options) > 0:
        best_play = options[0]
        for card in options:
            if card.value > best_play.value:
                best_play = card

        c_hand.remove(best_play)
        up_card = best_play
        active_suit = up_card.suit
        print("Computer played", best_play.short_name)

    else:
        if len(deck) > 0:
            next_card = random.choice(deck)
            c_hand.append(next_card)
            deck.remove(next_card)
            print("Computer drew a card.")
        else:
            print("Computer is blocked.")
            blocked += 1
            print("Computer has %i cards left." % (len(c_hand)))

def player_turn():
    global p_hand, deck, active_suit, up_card, blocked
    valid_play = False
    is_eight = False
    print("\nYour hand: ")
    for card in p_hand:
        print(card.short_name)
    print("Up card:", up_card.short_name)
    if up_card.rank == '8':
        print ("Suit is", active_suit)
    print("What do you want to do?")
    response = input("Type a card to play or 'Draw' to take a card: ")
    while not valid_play:
        selected_card = None
        while selected_card == None:
            if response.lower() == "draw":
                valid_play = True
                if len(deck) > 0:

                    card = random.choice(deck)
                    p_hand.append(card)
                    deck.remove(card)
                    print("You drew:", card.short_name)
                else:
                    print("There are no cards left in the deck.")
                    blocked += 1
                return
            else:
                for card in p_hand:
                    if response.upper() == card.short_name:
                        selected_card = card
                if selected_card == None:
                    response = input("You don't have that card. Try again: ")
        if selected_card.rank == '8':
            valid_play = True
            is_eight = True
            get_new_suit()
        elif selected_card.suit == active_suit:
            valid_play = True
        elif selected_card.rank == up_card.rank:
            valid_play = True

        if valid_play:
            p_hand.remove(selected_card)
            up_card = selected_card
            if not is_eight:
                active_suit = up_card.suit
            print("You played", selected_card.short_name)
        if not valid_play:
            response = input("That's not a legal play. Try again: ")

p_total = c_total = 0
done = False
game_done = False
while not done:
    deck = []
    p_hand = []
    c_hand = []
    init_cards()
    blocked = 0
    up_card = random.choice(deck)
    active_suit = up_card.suit
    while not game_done:
        player_turn()
        if len(p_hand) == 0:
            game_done = True
            print("You won!")
            #display game score here
            p_points = 0
            for card in c_hand:
                p_points += card.value
            p_total += p_points
            print("You got %i points for computer's hand." % p_points)
        if not game_done:
            computer_turn()
        if len(c_hand) == 0:
            game_done = True
            print("Computer won!")
            #display game score here
            c_points = 0
            for card in p_hand:
                c_points += card.value
            c_total += c_points
            print("Computer got %i points for your hand." % c_points)
        if blocked >= 2:
            game_done = True
            print("Both players blocked. GAME OVER.")
            p_points = 0
            for card in c_hand:
                p_points += card.value
            p_total += p_points
            c_points = 0
            for card in p_hand:
                c_points += card.value
            c_total += c_points
            print("You got %i points for computer's hand." % p_points)
            print("Computer got %i points for your hand." % c_points)
    play_again = input("Play again (Y/N)? ")
    if play_again.lower().startswith('y'):
        print("\nSo far, you have %i points" % p_total)
        print(" and the computer has %i points." % c_total)
        game_done = False
    else:
        done = True
print("\nFinal score:")
print("You: %i   Computer: %i" % (p_total, c_total))