import test_data
import json
with open("C:/Users/cassi/Documents/GitHub/cc_tools/test_data.json", 'r') as reader:
    json_data = json.load(reader)

#Creates and returns a GameLibrary object(defined in test_data) from loaded json_data
def make_game_library_from_json(json_data):
    #Initialize a new GameLibrary
    game_library = test_data.GameLibrary()
    for game_data in json_data["game 1"]:
        game = test_data.Game()
        game.title = game_data["title"]
        game.year = game_data["year"]
        game.platform = game_data["platform"]
        for platform_data in json_data["game 1"]:
            platform = test_data.Platform()
            platform.launch_year = platform_data["launch_year"]
            platform.name = platform_data["name"]
            game_library.add_game(game)


    #Loop through the json_data
        #Create a new Game object from the json_data by reading
        #  title
        #  year
        #  platform (which requires reading name and launch_year)
        #Add that Game object to the game_library
    #Return the completed game_library

    return game_library