#==============================Credits================================#
# Author:       Mikey Mann
# Date:         19-JUN-2024
# Description:  This is my Mongoose Traveller 2nd Edition Life-Path 
#               Character Generator
# Revisions:    v0.01 - Just getting started
#====================Traveller Life Path Generator====================#

# Term 0 - Background
# - Name
# - Stats
# - Nobility Title (SOC11+)
# - Background Skills
# - +18 years 

# Term 1-3 - Early Years
# - Pre-Career Education (optional)
# - - University
# - - - Application
# - - - - +Accepted
# - - - - -Apply to career
# - - - Skill Selection
# - - - EDU + 1
# - - - Precareer Event
# - - - Graduation Attempt
# - - - - +Graduate 
# - - - - -End Term
# - - - Graduation Benefits
# - - - End Term 
# - - Military Academy
# - - - Application to Navy, Marines, or Army
# - - - - +Go to Bootcamp 
# - - - - -Apply to career
# - - - Bootcamp
# - - - Precareer Event
# - - - Graduation Attempt
# - - - - +Graduate 
# - - - - -End Term
# - - - Graduation Benefits
# - - - End Term 
# - Career
# - - Application Attempt
# - - - +Hired 
# - - - -Sign up for the draft of become a drifter
# - - Basic Training
# - - Career Survival
# - - - +Career Event and attempt Career Advancement 
# - - - -Career Mishap - If laid off muster out and End Term
# - - Career Event
# - - Career Mishap
# - - Career Advancement
# - - - +Rank up in career and End Term
# - - - -No Promotion and End Term - If roll is less than total 
#       terms in career, cannot choose current career next term
# - End Term 
# - +4 years

# Term 4+ - Aging
# - Antagathics (optional)
# - Career
# - - Application Attempt
# - - - +Hired 
# - - - -Sign up for the draft of become a drifter
# - - Training
# - - Career Survival
# - - - +Career Event and attempt Career Advancement 
# - - - -Career Mishap - If laid off muster out and End Term
# - - Career Event
# - - Career Mishap
# - - Career Advancement
# - - - +Rank up in career and End Term
# - - - -No Promotion and End Term - If roll is less than total 
#       terms in career, cannot choose current career next term
# - Aging
# - End Term
# - +4 years
# - Begin next term or Become a Traveller

#====================Traveller Life Path Generator====================#


import valid as v
import precareer as pce
import background as getback
# Menu Constants
GEN_CHAR = 1
GEN_RANDOM = 2
VIEW_SAVED = 3
QUIT = 4

def main():
    term = 0
    age = 0
    menu_choice = 0
    char_name = ""
    characters = []
    characteristics = []
    # (STR): characteristics[0]
    # (DEX): characteristics[1]
    # (END): characteristics[2]
    # (INT): characteristics[3]
    # (EDU): characteristics[4]
    # (SOC): characteristics[5]
    nobility = ""

    print_welcome()

    print_menu(characters)

    menu_choice = get_menu_choice(characters)

    while menu_choice != QUIT:
        if menu_choice == GEN_CHAR:
            #getback.background(char_name)
            menu_choice = 0
            print("\n********************\n"
                + " Option Unavaliable"
                + "\n********************\n")
            print_menu(characters)
            get_menu_choice(characters)
        
        elif menu_choice == GEN_RANDOM:
            menu_choice = 0
            print("\n********************\n"
                + " Option Unavaliable"
                + "\n********************\n")
            print_menu(characters)
            get_menu_choice(characters)

        elif menu_choice == VIEW_SAVED:
            #print_saved_list(characters)
            menu_choice = 0
            print("\n********************\n"
                + " Option Unavaliable"
                + "\n********************\n")
            print_menu(characters)
            get_menu_choice(characters)
        
        else:
            return menu_choice
    print_goodbye()

# This is the welcome message
def print_welcome():
    print('\nWelcome to the Mongoose Traveller 2nd Edition Life-Path'
          +' Character Generator')

# These are the menu options
def print_menu(characters):
    print('\nMENU')
    print(f'\n1. Begin Character Creation'
         +f'\n2. Generate Random Character'
         +f'\n3. View Saved ({int(len(characters))}) Characters'
         +f'\n4. Quit')

# This is the user input for the menu opitions
def get_menu_choice(characters):
    menu_choice = 0
    menu_choice = v.get_integer('\nChoose Menu Option: ')
    while menu_choice < 1 or menu_choice > 4:
        print('Invalid input.')
        print_menu(characters)
        menu_choice = v.get_integer('\nChoose Menu Option: ')
    return menu_choice 

'''def print_saved_list(characters):
    index = 0
    if len(characters) == 0:
        print("\nYou havent made any characters yet...")
    
    else: 
        print("poopie")'''

# This is the goodbye message
def print_goodbye():
    print("\nThank you for using the level one hp calculator!\n")


main()

