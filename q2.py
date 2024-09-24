import statistics
# start

NBA_player: list[float] = []
bigger_Than_2: int = 0
heights: int = 0
SENTINEL: int = -999
player: int = 0
while True:
    player_height: float = float(input("Enter your height :"))
    if player_height == SENTINEL:
        break
    if not 1.60 < player_height < 3.0:
        continue
    player += 1
    NBA_player.append(player_height)
    if player_height > 2.0:
        bigger_Than_2 += 1
for i in range(len(NBA_player)):
    if NBA_player[i] > statistics.mean(NBA_player):
        heights += 1

if len(NBA_player) > 1.60:
    print(f"The highest player : {max(NBA_player)}")
    print(f"The smallest player : {min(NBA_player)}")
    print(f"The average is : {statistics.mean(NBA_player)}")
    print(f"How many players are bigger than 2.0 meter?  : {bigger_Than_2}")
    print(f"How many players are bigger than avg?  : {heights}")

# end