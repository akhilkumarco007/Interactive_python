# Mini-project #6 - Blackjack
import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.hand_list = []

    def __str__(self):
        hand_string = ""
        for i in self.hand_list:
            hand_string += " "+i.__str__()
        return "Hand contains"+hand_string

    def add_card(self, card):
        self.list = self.hand_list.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        sum = 0
        for i in self.hand_list:
            sum += VALUES[i.get_rank()]
        for j in self.hand_list:
            if j.get_rank() == 'A':
                if (sum + 10) <= 21:
                    sum += 10
        return sum
   
    def draw(self, canvas, pos):
        for i in self.hand_list:
            i.draw(canvas, pos)
            pos[0] += 20 + CARD_SIZE[0]
            
# define deck class 
class Deck:
    def __init__(self):
        deck = []
        for i in SUITS:
            for j in RANKS:
                card = Card(i, j)
                deck.append(card)
        self.deck = deck

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.deck)

    def deal_card(self):
        # deal a card object from the deck
        dealt_card = self.deck[-1]
        self.deck.pop(-1)
        return dealt_card
    
    def __str__(self):
        # return a string representing the deck
        deck_string = ""
        for i in self.deck:
            deck_string += " "+i.__str__()
        return "Deck contains"+deck_string

#define event handlers for buttons
def deal():
    global outcome, in_play, deck, player_hand, dealer_hand, action, score
    outcome = ""
    if in_play:
        outcome = "You Lose."
        score -= 1
        in_play = False
    else:
        deck = Deck()
        deck.shuffle()
        player_hand = Hand()
        dealer_hand = Hand()
        player_hand.add_card(deck.deal_card())
        player_hand.add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())
        action = "Hit or Stand?"
        in_play = True

def hit():
    global outcome, action, in_play, score
    # if the hand is in play, hit the player
    if in_play:
        if player_hand.get_value() <= 21:
            player_hand.add_card(deck.deal_card())
    # if busted, assign a message to outcome, update in_play and score
        if player_hand.get_value() > 21:
            outcome = "You went Bust and Lose."
            action = "New Deal?"
            in_play = False
            score -= 1
        
def stand():
    global outcome, action, in_play, score
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if in_play:
        if player_hand.get_value() > 21:
            outcome = "You Lose."
            score -= 1
        if player_hand.get_value() <= 21:
            while (dealer_hand.get_value() <= 17):
                dealer_hand.add_card(deck.deal_card())
            if dealer_hand.get_value() > 21:
                outcome = "You Win."
                score += 1
            else:
                if player_hand.get_value() > dealer_hand.get_value():
                    outcome = "You Win."
                    score += 1
                else:
                    outcome = "You Lose."
                    score -= 1
    # assign a message to outcome, update in_play and score
    action = "New Deal?"
    in_play = False
    
# draw handler    
def draw(canvas):
    canvas.draw_text("Blackjack", [40, 60], 50, 'Aqua')
    canvas.draw_text("Dealer", [40, 120], 25, 'Black')
    canvas.draw_text(outcome, [200, 120], 25, 'Black')
    canvas.draw_text("Player", [40, 350], 25, 'Black')
    canvas.draw_text(action, [200, 350], 25, 'Black')
    player_hand.draw(canvas, [40, 400])
    dealer_hand.draw(canvas, [40, 152])
    if in_play == True:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [76, 200], CARD_BACK_SIZE)
    canvas.draw_text("Score", [450, 60], 25, 'Black')
    canvas.draw_text(str(score), [530, 60], 25, 'Black')

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric
