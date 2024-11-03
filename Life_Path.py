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
import modifier_calculator as modcalc

def main():

    term = 0
    age = 0
    name = ""
    home_world = ""
    characteristics = []
    # (STR): characteristics[0]
    # (DEX): characteristics[1]
    # (END): characteristics[2]
    # (INT): characteristics[3]
    # (EDU): characteristics[4]
    # (SOC): characteristics[5]
    # (PSI): characteristics[6]
    nobility = ""
    background_skills = []
    skills_list = []
    term_history = []
    precareer_choice = 0

    welcome_user()
    name = get_name(name)
    home_world = get_home_world(name, home_world)
    characteristics = get_characteristics(name, characteristics)
    nobility = calc_nobility(name, characteristics[5], home_world)
    background_skills = get_background_skills(name, characteristics[4], background_skills)
    
    print("\nEnd Of Term 0")
    age += 18
    term += 1

    # TERM 1
    print(f"\nTerm {term}\n")

    if term < 4:
        precareer_choice = get_precareer_choice(name, precareer_choice, term)

def welcome_user():
    print("\nWelcome Traveller\n")
    print("New User Detected")
    print("\nEnter Traveller Profile Data\n")

def get_name(name):
    # This is the user input for thier character's name
    name = input("Enter Your Name: ")
    return name

def get_home_world(name, home_world):
    print("Enter Your Home World Name ")
    home_world = input(f"{name}: ")
    return home_world

def get_characteristics(name, characteristics):
    # This is the user input for their characters initial stats
    index = 0
    score = 0
    characteristics = ['Strength (STR)', 'Dexterity (DEX)', 
                        'Endurance (END)', 'Intellect (INT)',
                        'Education (EDU)', 'Social Standing (SOC)']
    
    while index < len(characteristics):
        print(f"Input Your {characteristics[index]}" )
        score = v.get_integer(f"{name}: ")
        if score > 15:
            print("\nERROR: Ability Score Over 15!")
            print("\nAbility Scores Cannot Exceed 15 In Character"
                    +" Creation Unless Later Specified\n")
            print(f"Reenter a Valid Score\n")
            index -= 1
        else:
            characteristics[index] = score
        index += 1

    print(f"\nYour starting characteristics are:"
          +f"\nStrength (STR): {characteristics[0]}"
          +f"\nDexterity (DEX): {characteristics[1]}"
          +f"\nEndurance (END): {characteristics[2]}"
          +f"\nIntellect (INT): {characteristics[3]}"
          +f"\nEducation (EDU): {characteristics[4]}"
          +f"\nSocial Standing (SOC): {characteristics[5]}")
    
    return characteristics

def calc_nobility(name, SOC, home_world):
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

        print(f"\nTAS Records Will Show You As {nobility} {name} Of {home_world}.")
    return nobility

def get_background_skills(name, EDU, background_skills):

    # This is proving challenging... I think I may need to make a list
    # of all the skills in a seperate modiual to reffer to... And a 
    # second list with the players skill points and to modify that list
    # only as far as skills are concerned.
    # 
    # Ive found out about dictionaries but Im still not sure how to
    # impliment them... 

    edu_mod = modcalc.get_modifier(EDU)
    skill_count = edu_mod + 3
    background_skills = []
    index = 0

    print(f"\nYou Are Able To Choose {edu_mod + 3} Level 0 "
          +"Background Skills From The Following List:")
    print("\n1. Admin\n2. Electronics\n3. Science\n4. Animals\n"
          +"5. Flyer\n6. Seafarer\n7. Art\n8. Language\n9. Streetwise"
          +"\n10. Athletics\n11. Mechanic\n12. Survival\n13. Carouse\n"
          +"14. Medic\n15. Vacc Suit\n16. Drive\n17. Profession")
    while skill_count > 0:
        print(f"\n{skill_count} skills remaining."
              +"\nChoose a background skill")
        background_skills[index] = v.get_integer(f"{name}: ")
        index += 1
        skill_count -= 1
    print(background_skills)
    return background_skills

#=============================Term 1-3================================#

def get_precareer_choice(name, precareer_choice, term):
    precareer_choice = 0
    print(f"\nDid You Apply For Pre-Career Education In Term {term}?"
          +"\nOnly Avaliable In Terms 1-3.")
    print("\nChoose From The Following:"
        +"\n1. Apply To University"
        +"\n2. Apply To Military Academy"
        +"\n3. Skip Pre-Career Education")
    precareer_choice = input(f"{name}: ")
    return precareer_choice

main() 