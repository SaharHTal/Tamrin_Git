#import matplotlib.pyplot as plt
try:
    names = input().split()
    player1 = names[0]
    player2 = names[1]
    healths = input().split()
    health1 = int(healths[0])
    health2 = int(healths[1])
    damages = input().split()
    damage_a = int(damages[0])
    damage_b = int(damages[1])
    damage_c = int(damages[2])
    score1 = 0
    score2 = 0
    damage1 = 0
    damage2 = 0
    first_round = input().split()

    if first_round[1] == "A":
        damage2 = damage_a
        health1 -= damage_a
    elif first_round[1] == "B":
        damage2 = damage_b
        health1 -= damage_b
    elif first_round[1] == "C":
        damage2 = damage_c
        health1 -= damage_c
    if first_round[0] == "A":
        damage1 = damage_a
        health2 -= damage_a
    elif first_round[0] == "B":
        damage1 = damage_b
        health2 -= damage_b
    elif first_round[0] == "C":
        damage1 = damage_c
        health2 -= damage_c
    if damage2 > damage1:
        score2 += 1
    elif damage2 < damage1:
        score1 +=1
    second_round = input().split()

    if second_round[1] == "A":
        damage2 = damage_a
        health1 -= damage_a
    elif second_round[1] == "B":
        damage2 = damage_b
        health1 -= damage_b
    elif second_round[1] == "C":
        damage2 = damage_c
        health1 -= damage_c
    if second_round[0] == "A":
        damage1 = damage_a
        health2 -= damage_a
    elif second_round[0] == "B":
        damage1 = damage_b
        health2 -= damage_b
    elif second_round[0] == "C":
        damage1 = damage_c
        health2 -= damage_c
    if damage2 > damage1:
        score2 += 1
    elif damage2 < damage1:
        score1 +=1
    third_round = input().split()
    if third_round[1] == "A":
        damage2 = damage_a
        health1 -= damage_a
    elif third_round[1] == "B":
        damage2 = damage_b
        health1 -= damage_b
    elif third_round[1] == "C":
        damage2 = damage_c
        health1 -= damage_c
    if third_round[0] == "A":
        damage1 = damage_a
        health2 -= damage_a
    elif third_round[0] == "B":
        damage1 = damage_b
        health2 -= damage_b
    elif third_round[0] == "C":
        damage1 = damage_c
        health2 -= damage_c
    if damage2 > damage1:
        score2 += 1
    elif damage2 < damage1:
        score1 +=1
    result1 = f"{player1} -> Score: {score1}, Health: {health1}"
    result2 = f"{player2} -> Score: {score2}, Health: {health2}"
    print(result1)
    print(result2)
    #f = open("result.txt", "w")
    #f.write(f"{result1}\n{result2}")
    #f.close()
    #final_scores = [score1, score2]
    #plt.bar(names, final_scores)
    #plt.xlabel("Players")
    #plt.ylabel("Scores")
    #plt.title("Player's Scores")
    #plt.show
except ValueError:
    print("Invalid Command.")
    #f = open("result.txt", "w")
    #f.write("Invalid Command.")
    #f.close()
except IndexError:
    print("Invalid Command.")
    #f = open("result.txt", "w")
    #f.write("Invalid Command.")
    #f.close()