import json

with open("basic-game.json", "r") as f:
    game_data = json.load(f)

start_scene = "START"

def game_loop(current_scene):
    while True:
        print(current_scene)
        current_scene = game_data[current_scene]
        print(current_scene["text"])

        if "END" in current_scene:
            print("Game Over")

        user_action = input()
        for action in current_scene["commands"]:
            if user_action == action:
                current_scene = current_scene["commands"][action]

def start_game():
    for scene in game_data:
        if scene == "START":
            game_loop(start_scene)

start_game()