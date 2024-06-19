#**********************************************************************
# Author:       Mikey Mann
# Date:         19-JUN-2024
# Description:  This is my Mongoose Traveller 2nd Edition Life-Path 
#               Character Generator
# Revisions:    v0.01 - Just getting started
#**********************************************************************
import valid as v
import modifier_calculator as modcalc
import random

# Menu Constants
GEN_CHAR = 1
GEN_RANDOM = 2
VIEW_SAVED = 3
QUIT = 4

def main():
    menu_choice = 0
    char_name = ""
    characteristics = ['Strength (STR)', 'Dexterity (DEX)', 
                        'Endurance (END)', 'Intellect (INT)',
                        'Education (EDU)', 'Social Standing (SOC)']
    # (STR): characteristics[0]
    # (DEX): characteristics[1]
    # (END): characteristics[2]
    # (INT): characteristics[3]
    # (EDU): characteristics[4]
    # (SOC): characteristics[5]
    nobility = ""

    print_welcome()

    print_menu()

    menu_choice = get_menu_choice()

    while menu_choice != QUIT:

        if menu_choice == GEN_CHAR:
            char_name = get_char_name(char_name)

            characteristics = get_stats(char_name, characteristics)

            char_name = calc_nobility(char_name, characteristics[5])

            print_background_skills(char_name, characteristics[4])

            get_background_skills(char_name, characteristics[4])

           # life_path(char_name)
        elif menu_choice == GEN_RANDOM:
            print('\nMenu Option Not Yet Avaliable')

        elif menu_choice == VIEW_SAVED:
            print('\nMenu Option Not Yet Avaliable')

        print_menu()

        get_menu_choice()
    
    print_goodbye()

def print_welcome():
    # This is the welcome message
    print('\nWelcome to the Mongoose Traveller 2nd Edition Life-Path'
          +' Character Generator')

def print_menu():
    # These are the menu options
    print('\nMENU')
    print('\n1. Create New Character\n2. Generate Random Character\n'
          +'3. View Saved Characters\n4. Quit')

def get_menu_choice():
    # This is the user input for the menu opitions
    menu_choice = 0
    menu_choice = v.get_integer('\nChoose Menu Option: ')
    while menu_choice < 0 or menu_choice > 4:
        print('Invalid input.')
        print_menu()
        menu_choice = int(input('\nChoose Menu Option: '))
    return menu_choice

def get_char_name(char_name):
    # This is the user input for thier character's name
    char_name = input("What is your Character's name? ")
    return char_name

def get_stats(char_name, characteristics):
    # This is the user input for their characters initial characteristics
    index = 0
    characteristics = ['Strength (STR)', 'Dexterity (DEX)', 
                        'Endurance (END)', 'Intellect (INT)',
                        'Education (EDU)', 'Social Standing (SOC)']
    
    while index < len(characteristics):
        characteristics[index] = v.get_integer(f"Input {char_name}'s"
                                      +" {characteristics[index]}: " )
        index += 1

    print(f"\n{char_name}'s starting characteristics are:"
          +f"\nStrength (STR): {characteristics[0]} "
          +f"\nDexterity (DEX): {characteristics[1]} "
          +f"\nEndurance (END): {characteristics[2]} "
          +f"\nIntellect (INT): {characteristics[3]} "
          +f"\nEducation (EDU): {characteristics[4]} "
          +f"\nSocial Standing (SOC): {characteristics[5]}")
    
    return characteristics

def calc_nobility(char_name, SOC):
    nobility = ''
    SOC = int(SOC)

    if SOC > 10:
        if SOC == 11:
            nobility = 'Knight'
        elif SOC == 12:
            nobility = 'Baron'
        elif SOC == 13:
            nobility = 'Marquis'
        elif SOC == 14:
            nobility = 'Count'
        elif SOC >= 15:
            nobility = 'Duke'
        char_name = nobility + ' ' + char_name

        print("\nDue to your Social Standing your character will be"
              +f" known henseforth as {char_name}.")

    return char_name

def print_background_skills(char_name, EDU):
    # The player can choose EDU DM + 3 background skills
    edu_mod = modcalc.get_modifier(EDU)
    print(f"\n{char_name} is able to choose {edu_mod + 3} level 0 "
          +"background skills from the following list:")
    print("\n1. Admin\n2. Electronics\n3. Science\n4. Animals\n"
          +"5. Flyer\n6. Seafarer\n7. Art\n8. Language\n9. Streetwise"
          +"\n10. Athletics\n11. Mechanic\n12. Survival\n13. Carouse\n"
          +"14. Medic\n15. Vacc Suit\n16. Drive\n17. Profession")

def get_background_skills(char_name, EDU):
    edu_mod = modcalc.get_modifier(EDU)
    skill_count = edu_mod + 3
    while skill_count > 0:
        v.get_integer(f"\n{skill_count} skills remaining."
              +"\nChoose a background skill: ")
        skill_count -= 1
    print(f"\nNow {char_name} is 18 years old and is ready to begin Term 1.")
    

def print_goodbye():
    print('\nThank you for using this program.\n')

main()