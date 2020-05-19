letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
letter_to_points={key:value for key,value in zip(letters,points)}
letter_to_points[" "]=0
letter_to_points_temp={}
for letter,value in letter_to_points.items():
  letter_to_points_temp[letter.lower()]=value
for letter,value in letter_to_points_temp.items():
  letter_to_points[letter]=value
#print(letter_to_points)

def score_word(word):
  point_total=0
  for letter in word:
    for key in letter_to_points.keys():
      if letter==key:
        value=letter_to_points[key]
        point_total+=value  
  return point_total

brownie_points=score_word("BROWNIE")
print(brownie_points)

player_to_words={"player1":["BLUE","TENNIS","EXIT"], "wordNerd":["EARTH","EYES","MACHINE"], "Lexi Con":["ERASER","BELLY","HUSKY"], "Prof Reader":["ZAP","COMA","PERIOD"]}

player_to_points={}

def update_point_totals():
  for player,words in player_to_words.items():
    player_points=0
    for word in words:
      player_points+=score_word(word)
      player_to_points[player]=player_points
  return player_to_points

def play_word(player,word):
  for key,value in player_to_words.items():
    if player==key:
      value=value.append(word)
  update_point_totals()
  return player_to_words

play_word("player1","Paparazzi")
update_point_totals()
print(player_to_words)
print(player_to_points)






