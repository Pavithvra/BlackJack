import random
import art
from replit import clear



def deal_card():
  cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
  card=random.choice(cards)
  return card

def calculate_score(cards):
  if sum(cards)==21 and len(cards)==2:
    return 0

  if 11 in cards and sum(cards)>21:
    cards.remove(11)
    cards.append(1)

  return sum(cards)

def compare(user_score,computer_score):
  if user_score==computer_score:
    return "Its a draw"
  elif computer_score==0:
    return "You lose,caz the dealer has a blackjack"
  elif user_score==0:
    return "you win,caz you have a blackjack"
  elif user_score>21:
    return "Your score exeeds"
  elif computer_score>21:
    return "Opponent lose caz his score exeeds"
  elif user_score>computer_score:
    return "You win"
  else:
    return "You lose"


def play_game():
  print(art.logo)
  
  is_game_over=False
  user_card=[]
  dealers_card=[]

  for i in range(0,2):
      user_card.append(deal_card())
      dealers_card.append(deal_card())
  
  while not is_game_over:
    user_score=calculate_score(user_card)
    computer_score=calculate_score(dealers_card)
    print(f"Your cards: {user_card}, current score: {user_score}")
    print(f"Computer's first card: {dealers_card[0]}")
  
    if user_score==0 or computer_score==0 or user_score>21:
      is_game_over=True
    
    else:
      choice=input("Type 'y' to get another card, type 'n' to pass: ")
      if choice=="y":
        user_card.append(deal_card())
    
      else:
        is_game_over=True
  
  while computer_score!=0 and computer_score<17:
    dealers_card.append(deal_card())
    computer_score=calculate_score(dealers_card)
  
  print(f"The final user cards: {user_card}, final score: {user_score}")
  print(f"The final dealer cards: {dealers_card}, final score: {computer_score}")
  print(compare(user_score,computer_score))
  play_again=input("Do you want to play again? Type 'y' or 'n'")
  if play_again=="y":
    is_game_over=False
    clear()
    play_game()

play_game()
