import random
import copy
import time

# set up of the game cards - note: 1 = ace, 11 = jack, 12 = queen, 13 = king
clubs = ['c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 
          'c10', 'c11', 'c12', 'c13']
diamonds = ['d1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9', 
          'd10', 'd11', 'd12', 'd13']
hearts = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8', 'h9', 
          'h10', 'h11', 'h12', 'h13']
spades = ['s1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 
          's10', 's11', 's12', 's13']
red_cards = diamonds + hearts
black_cards = clubs + spades
deck = red_cards + black_cards


num_players = int(input("\nPlease enter the number of players: [1-13] "))
game_cards = random.sample(deck, 4 * num_players)


def split(lst, partition_len):
  for i in range(0, len(lst), partition_len):
    yield lst[i:i + partition_len]

hands = list(split(game_cards, 4))
scores = [[0] * 4 for _ in range(num_players)]

# obtain the game cards but only the values and not the suit
values = copy.deepcopy(game_cards)
mapping_table = str.maketrans({'c': '', 'd': '', 'h': '', 's': ''})
for _ in range(len(values)):
   values[_] = values[_].translate(mapping_table)
values = [int(i) for i in values]
values = list(split(values, 4))

# ROUND 1
def red_or_black():
    for _ in range(num_players):
        colour = input("\nPlayer " + str(_ + 1) + ": Guess the suit colour, red (R) or black (B): ")
        if 'h' in hands[_][0] or 'd' in hands[_][0]:
           if colour.lower() == 'r':
              print(f"\nCorrect! Your card was {hands[_][0]}")
              time.sleep(1)
              scores[_][0] = 1
           else:
              print(f"\nIncorrect! Your card was {hands[_][0]}")
              time.sleep(1)
        elif 'c' in hands[_][0] or 's' in hands[_][0]:
           if colour.lower() == 'b':
              print(f"\nCorrect! Your card was {hands[_][0]}")
              time.sleep(1)
              scores[_][0] = 1
           else:
              print(f"\nIncorrect! Your card was {hands[_][0]}")
              time.sleep(1)

# ROUND 2
def high_or_low():
   for _ in range(num_players):
      print("\nPlayer " + str(_ + 1) + ":")
      print(f"\nYour first card was {hands[_][0]}")      
      guess = input("\nGuess either higher (H) or lower (L): ")
      if guess.lower() == 'h': 
         if values[_][1] >= values[_][0]:
            print(f"\nCorrect! Your second card was {hands[_][1]}")
            time.sleep(1)
            scores[_][1] = 1
         elif values[_][1] < values[_][0]:
            print(f"\nIncorrect! Your second card was {hands[_][1]}")
            time.sleep(1)
      elif guess.lower() == 'l':
         if values[_][1] <= values[_][0]:
            print(f"\nCorrect! Your second card was {hands[_][1]}")
            time.sleep(1)
            scores[_][1] = 1
         elif values[_][1] < values[_][0]:
            print(f"\nIncorrect! Your second card was {hands[_][1]}")
            time.sleep(1)

# ROUND 3
def in_or_out():
   for _ in range(num_players):
    print("\nPlayer " + str(_ + 1) + ":")
    print(f"\nYour first card was {hands[_][0]}")
    print(f"\nYour second card was {hands[_][1]}")
    guess = input("\nGuess either inside (I) or outside (O): ")
# the third card is inside cards one and two (note same value counts as inside)
    if values[_][2] <= max(values[_][0], values[_][1]) and values[_][2] >= min(values[_][0], values[_][1]):
       if guess.lower() == 'i':
         print(f"\nCorrect! Your third card was {hands[_][2]}")
         time.sleep(1)
         scores[_][2] = 1
       elif guess.lower() == 'o':
         print(f"\nIncorrect! Your third card was {hands[_][2]}")
         time.sleep(1)
# the third card is outside cards one and two 
    elif values[_][2] > max(values[_][0], values[_][1]) or values[_][2] < min(values[_][0], values[_][1]):
       if guess.lower() == 'o':
         print(f"\nCorrect! Your third card was {hands[_][2]}")
         time.sleep(1)
         scores[_][2] = 1
       elif guess.lower() == 'i':
         print(f"\nIncorrect! Your third card was {hands[_][2]}")
         time.sleep(1)


# ROUND 4
def suit():
   for _ in range(num_players):
      guess = input("\nPlayer " + str(_ + 1) + ": Guess the suit of the fourth card - clubs (C), diamonds (D), hearts (H), spades (S): ")
      if 'c' in hands[_][3] and guess.lower() == 'c':
         print(f"\nCorrect! Your fourth card was {hands[_][3]}")
         time.sleep(1)
         scores[_][3] = 2
      elif 'd' in hands[_][3] and guess.lower() == 'd':
         print(f"\nCorrect! Your fourth card was {hands[_][3]}")
         time.sleep(1)
         scores[_][3] = 2
      elif 'h' in hands[_][3] and guess.lower() == 'h':
         print(f"\nCorrect! Your fourth card was {hands[_][3]}")
         time.sleep(1)
         scores[_][3] = 2
      elif 's' in hands[_][3] and guess.lower() == 's':
         print(f"\nCorrect! Your fourth card was {hands[_][3]}")
         time.sleep(1)
         scores[_][3] = 2
      else:
         print(f"\nIncorrect! Your fourth card was {hands[_][3]}")
         time.sleep(1)

def main():
# play the rounds 
   red_or_black()
   high_or_low()
   in_or_out()
   suit()
   print("\n")
# add up the round scores for each player 
   total_scores = [sum(i) for i in scores]
   for _ in range(num_players):
      print(f"Player {_ + 1} score: {total_scores[_]}")

# runs the entire game from start to finish
main()      
          




   