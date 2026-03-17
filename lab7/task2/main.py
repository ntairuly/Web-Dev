from models import Character, Protagonist, Antagonist, SideCharacter


characters = [Antagonist("Kaiba", "Yu-Gi-Oh!", 17, 
                         "Male", "To fight with the best duelist in the world"),
              Protagonist("Yugi", "Yu-Gi-Oh!", 15, "Male", 
                          "To become the strongest duelist"), 
              SideCharacter("Joey", "Yu-Gi-Oh!", 16, "Male", 
                            "Yugi's best friend and rival"),
              Character("Nursat", "None", 18, "Male")]

characters[0].add_loved_phrase("My pride and my soul, my Blue-Eyes White Dragon!")
characters[1].add_friend(characters[0])
characters[1].add_friend(characters[2])
characters[0].add_main_enemy(characters[1])
characters[1].add_main_enemy(characters[0])

print()
for character in characters:
    print(character)
    print()

    if isinstance(character, Protagonist) or isinstance(character, Antagonist):
        print(character.main_enemy() + "\n")
    
    if isinstance(character, Protagonist):
        print(f"{character.name}'s friends:")
        for friend in character.get_friends():
            print(f" {friend.name}")
        print()
    
    if isinstance(character, Antagonist):
        print(f"{character.name}'s loved phrase: {character.get_loved_phrase()}\n")
    
    if isinstance(character, SideCharacter):
        print(character.describe_role() + "\n")