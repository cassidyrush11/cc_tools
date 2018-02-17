import cc_data

def make_cc_data_file_from_json(json_data):
    cc_data_file = cc_data.CCDataFile()

    for json_level in json_data:
        cc_level = cc_data.CCLevel()
        cc_level.level_number = json_level["level_number"]
        cc_level.num_chips = json_level["num_chips"]
        cc_level.time = json_level["time"]
        cc_level.upper_layer = json_level["upper_layer"]
        cc_level.lower_layer = json_level["lower_layer"]
        json_fields = json_level["optional_fields"]
        for json_field in json_fields:
            field_type = json_field["type"]
            if (field_type == "title"):
                print("It's a title!")
                title = json_field["title"]
                cc_title_field = cc_data.CCMapTitleField(title)
                cc_level.add_field(cc_title_field)
            elif (field_type == "password"):
                print("It's a password.")
                password = json_field["password"]
                cc_password_field = cc_data.CCEncodedPasswordField(password)
                cc_level.add_field(cc_password_field)
            elif (field_type == "hint"):
                print("It's a hint!")
                hint = json_field["hint"]
                cc_hint_field = cc_data.CCMapHintField(hint)
                cc_level.add_field(cc_hint_field)
            elif (field_type == "mosnters"):
                print("Oh no, a monster.")
                #monsters = json_field["monsters"]
                #cc_monsters_field = cc_data.CCMonsterMovementField(monsters)
                my_coordinates = json_field["monsters"]
                cc_monsters_field = cc_data.CCMonsterMovementField(my_coordinates)
                cc_level.add_field(cc_monsters_field)
            else:
                print("I have no idea what this is.")

        print(cc_level)

        cc_data_file.add_level(cc_level)

    return cc_data_file