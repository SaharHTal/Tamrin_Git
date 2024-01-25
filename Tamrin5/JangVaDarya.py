import re


class Soldier:
    def __init__(self, soldier_type, soldier_id, x, y):
        self.soldier_type = soldier_type
        self.soldier_id = soldier_id
        self.x = x
        self.y = y
        self.health = 100


class Game:

    def __init__(self, n):
        self.n = n

    soldiers_team1 = []
    soldiers_team2 = []
    turn = 0

    def add_soldier(self, soldier_type, soldier_id, x, y):
        if self.turn == 0:
            for soldier in self.soldiers_team1:
                if soldier.soldier_id == soldier_id:
                    print("duplicate tag")
                    return
            self.soldiers_team1.append(Soldier(soldier_type, soldier_id, x, y))
            self.turn = 1
        elif self.turn == 1:
            for soldier in self.soldiers_team2:
                if soldier.soldier_id == soldier_id:
                    print("duplicate tag")
                    return
            self.soldiers_team2.append(Soldier(soldier_type, soldier_id, x, y))
            self.turn = 0

    def move(self, soldier_id, direction):
        if self.turn == 0:
            for soldier in self.soldiers_team1:
                if soldier.soldier_id == soldier_id:
                    if direction == "up":
                        if soldier.y - 1 == -1:
                            print("out of bounds")
                        else:
                            soldier.y -= 1
                            self.turn = 1
                    elif direction == "down":
                        if soldier.y + 1 == self.n:
                            print("out of bounds")
                        else:
                            soldier.y += 1
                            self.turn = 1
                    elif direction == "right":
                        if soldier.x + 1 == self.n:
                            print("out of bounds")
                        else:
                            soldier.x += 1
                            self.turn = 1
                    elif direction == "left":
                        if soldier.x - 1 == -1:
                            print("out of bounds")
                        else:
                            soldier.x -= 1
                            self.turn = 1
        else:
            for soldier in self.soldiers_team2:
                if soldier.soldier_id == soldier_id:
                    if direction == "up":
                        if soldier.y - 1 == -1:
                            print("out of bounds")
                        else:
                            soldier.y -= 1
                            self.turn = 0
                    elif direction == "down":
                        if soldier.y + 1 == self.n:
                            print("out of bounds")
                        else:
                            soldier.y += 1
                            self.turn = 0
                    elif direction == "right":
                        if soldier.x + 1 == self.n:
                            print("out of bounds")
                        else:
                            soldier.x += 1
                            self.turn = 0
                    elif direction == "left":
                        if soldier.x - 1 == -1:
                            print("out of bounds")
                        else:
                            soldier.x -= 1
                            self.turn = 0

    def distance(self, x1, y1, x2, y2):
        return abs(x1 - x2) + abs(y1 - y2)

    def attack(self, attacker_id, target_id):
        if self.turn == 0:
            for attacker in self.soldiers_team1:
                if attacker.soldier_id == attacker_id:
                    for target in self.soldiers_team2:
                        if target.soldier_id == target_id:
                            if attacker.soldier_type == "archer":
                                if self.distance(attacker.x, attacker.y, target.x, target.y) < 3:
                                    if target.health - 10 <= 0:
                                        self.soldiers_team2.remove(target)
                                        print("target eliminated")
                                        self.turn = 1
                                        return
                                    else:
                                        target.health -= 10
                                        self.turn = 1
                                        return
                                else:
                                    print("the target is too far")
                                    return
                            else:
                                if self.distance(attacker.x, attacker.y, target.x, target.y) < 2:
                                    if target.health - 20 <= 0:
                                        self.soldiers_team2.remove(target)
                                        print("target eliminated")
                                        self.turn = 1
                                        return
                                    else:
                                        target.health -= 20
                                        self.turn = 1
                                        return
                                else:
                                    print("the target is too far")
                                    return
        else:
            for attacker in self.soldiers_team2:
                if attacker.soldier_id == attacker_id:
                    for target in self.soldiers_team1:
                        if target.soldier_id == target_id:
                            if attacker.soldier_type == "archer":
                                if self.distance(attacker.x, attacker.y, target.x, target.y) < 3:
                                    if attacker.health - 10 <= 0:
                                        self.soldiers_team1.remove(target)
                                        print("target eliminated")
                                        self.turn = 0
                                        return
                                    else:
                                        target.health -= 10
                                        self.turn = 0
                                        return
                                else:
                                    print("the target is too far")
                                    return
                            else:
                                if self.distance(attacker.x, attacker.y, target.x, target.y) < 2:
                                    if attacker.health - 20 <= 0:
                                        self.soldiers_team1.remove(target)
                                        print("target eliminated")
                                        self.turn = 0
                                        return
                                    else:
                                        target.health -= 20
                                        self.turn = 0
                                        return
                                else:
                                    print("the target is too far")
                                    return

    def info(self, soldier_id):
        if self.turn == 0:
            for soldier in self.soldiers_team1:
                if soldier.soldier_id == soldier_id:
                    print("health:", soldier.health)
                    print("location:", soldier.x, soldier.y)
                    self.turn = 1
                    return
            print("soldier does not exist")
        elif self.turn == 1:
            for soldier in self.soldiers_team2:
                if soldier.soldier_id == soldier_id:
                    print("health:", soldier.health)
                    print("location:", soldier.x, soldier.y)
                    self.turn = 0
                    return
            print("soldier does not exist")

    def who_in_lead(self):
        health1 = health2 = 0
        for soldier1 in self.soldiers_team1:
            health1 += soldier1.health
        for soldier2 in self.soldiers_team2:
            health2 += soldier2.health
        if health1 > health2:
            print("player  1")
        elif health2 > health1:
            print("player  2")
        else:
            print("draw")


n = int(input())
game = Game(n)

while True:
    command = input()
    if re.match("^new (.+) (.+) (.+) (.+)$", command):
        match = re.match("^new (.+) (.+) (.+) (.+)$", command)
        game.add_soldier(match.group(1), int(match.group(2)), int(match.group(3)), int(match.group(4)))
    elif re.match("move (.+) (.+)", command):
        match = re.match("move (.+) (.+)", command)
        game.move(int(match.group(1)), match.group(2))
    elif re.match("attack (.+) (.+)", command):
        match = re.match("attack (.+) (.+)", command)
        game.attack(int(match.group(1)), int(match. group(2)))
    elif re.match(r"info (\d+)", command):
        match = re.match(r"info (\d+)", command)
        game.info(int(match.group(1)))
    elif command == "who is in the lead?":
        game.who_in_lead()
    elif command == "end":
        break
