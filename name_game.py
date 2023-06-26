players = {}

while True:
       command = input()
       if command == "Stop":
           break
       
       players[command] = 0
       for i in range(len(command)):
           letter = int(input())
           if letter == ord(command[i]):
               players[command] += 10
           else:
               players[command] += 2
               
current_winner = ["", 0]           
for k, v in players.items():
    if v >= current_winner[1]:
        current_winner = k, v
        
print(f"The winner is {current_winner[0]} with {current_winner[1]} points!")