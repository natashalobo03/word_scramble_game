
def game():
  import random
  word_list=['apple','banana','cherry','strawberry','pineapple','kiwi','mango','jackfruit','orange','grapes']
  choosen_word = random.choice(word_list)
  char_list=list(choosen_word)
  random.shuffle(char_list)
  print(char_list)
  attempts=3
  for attempt in range(attempts):
      guess=input("Guess the scrambled word(HINT : It's a fruit):")
      if guess == choosen_word:
          print("You win")
          return
          
      
      else:
          print("You loose")
      if attempt ==attempts-1:
          print("You are out of moves .The answer was "+ choosen_word)
          break
      
while True:
  game()          
  answer=input("Do you want to play the game again(yes/no):")
  if answer == 'yes' :
      game()
      break
  elif answer =='no':
      print("Thanks for playing!")
      break
