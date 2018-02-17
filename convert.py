import cc_dat_utils
import test_data
import test_json_utils
import json
import cc_data
import cc_json_utils


#cc_dat_utils.make_cc_data_from_dat("C:/Users/cassi/Documents/GitHub/cc_tools/data/pfgd_test.dat")
#print(cc_dat_utils.make_cc_data_from_dat("C:/Users/cassi/Documents/GitHub/cc_tools/data/pfgd_test.dat"))

#Part 1
#Use cc_data_utils.make_cc_data_from_dat() to load pfgd_test.dat
#print the resulting data


#Part 2
#input_json_file = "data/test_data.json"

### Begin Add Code Here ###


#with open("C:/Users/cassi/Documents/GitHub/cc_tools/test_data.json", 'r') as reader:
    #game_data = json.load(reader)
#game_library = test_json_utils.make_game_library_from_json(game_data)
#print(game_library)



#Open the file specified by input_json_file
#Use the json module to load the data from the file
#Use make_game_library_from_json(json_data) to convert the data to GameLibrary data
#Print out the resulting GameLibrary data using print_game_library(game_library_data) in test_data.py
### End Add Code Here ###


#Part 3
#Load your custom JSON file
#Convert JSON data to cc_data
#Save converted data to DAT file

with open("C:/Users/cassi/Documents/GitHub/cc_tools/data/cassidyrcc1.json", 'r') as reader:
    level_data = json.load(reader)
cc_data_file = cc_json_utils.make_cc_data_file_from_json(level_data)
print(cc_data_file)

cc_dat_utils.write_cc_data_to_dat(cc_data_file, "C:/Users/cassi/Documents/GitHub/cc_tools/data/cassidyrcc1.dat")
dat_check = cc_dat_utils.make_cc_data_from_dat("C:/Users/cassi/Documents/GitHub/cc_tools/data/cassidyrcc1.dat")
print(dat_check)