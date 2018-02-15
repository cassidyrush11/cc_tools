import test_data
import json


#Creates and returns a GameLibrary object(defined in test_data) from loaded json_data
def make_game_library_from_json(json_data):
    #Initialize a new GameLibrary
    game_library = test_data.GameLibrary()
    for game_data in json_data:
        game = test_data.Game()
        game.title = game_data["title"]
        game.year = game_data["year"]
        platform_data = game_data["platform"]
        platform = test_data.Platform()
        platform.name = platform_data["name"]
        platform.launch_year = platform_data["launch_year"]
        game.platform = platform
        game_library.add_game(game)


    #Loop through the json_data
        #Create a new Game object from the json_data by reading
        #  title
        #  year
        #  platform (which requires reading name and launch_year)
        #Add that Game object to the game_library
    #Return the completed game_library

    return game_library