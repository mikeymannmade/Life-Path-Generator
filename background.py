import valid as v
import modifier_calculator as modcalc
import random

def background(char_name):
    characteristics = ['Strength (STR)', 'Dexterity (DEX)', 
                        'Endurance (END)', 'Intellect (INT)',
                        'Education (EDU)', 'Social Standing (SOC)', 
                        'Psionics (PSI)']
                    # (STR): characteristics[0]
                    # (DEX): characteristics[1]
                    # (END): characteristics[2]
                    # (INT): characteristics[3]
                    # (EDU): characteristics[4]
                    # (SOC): characteristics[5]
                    # (PSI): characteristics[6] 
    nobility = ""

    char_name = get_char_name(char_name)

    characteristics = get_stats(char_name, characteristics)

    char_name = calc_nobility(char_name, characteristics[5])

    print_background_skills(char_name, characteristics[4])

    get_background_skills(char_name, characteristics[4])


def get_char_name(char_name):
    # This is the user input for thier character's name
    char_name = input("What Is Your Name? ")
    return char_name

def get_stats(char_name, characteristics):
    # This is the user input for their characters initial stats
    index = 0
    characteristics = ['Strength (STR)', 'Dexterity (DEX)', 
                        'Endurance (END)', 'Intellect (INT)',
                        'Education (EDU)', 'Social Standing (SOC)']
    
    while index < len(characteristics):
        characteristics[index] = v.get_integer(f"Input {char_name}'s"
            +f" {characteristics[index]}: " )
        if characteristics[index] > 15:
            print("\nERROR: Ability Score Over 15!\n")
            print("\nAbility Scores Cannot Exceed 15 In Character"
                    +" Creation Unless Otherwise Specified\n")
            print(f"\nReenter Valid Score for {characteristics[index]}")
            index -= 1
        index += 1

    print(f"\n{char_name}'s starting characteristics are:"
          +f"\nStrength (STR): {characteristics[0]}"
          +f"\nDexterity (DEX): {characteristics[1]}"
          +f"\nEndurance (END): {characteristics[2]}"
          +f"\nIntellect (INT): {characteristics[3]}"
          +f"\nEducation (EDU): {characteristics[4]}"
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

        print("\nDue to your Social Standing your character will now "
              +f"be known henseforth as {char_name}.")

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
    print(f"\nNow {char_name} is 18 years old and is ready to"
          +" begin Term 1.")
    
#=============================Skills==================================#
# Skills can be listed with or without an associated level. If no
# specific level is listed, then you gain that skill at level 1 if you
# do not have it already, or increase its level by +1 if you are
# already trained in that field. If a level is listed, then you gain
# the skill at that level so long as it is higher than your current
# level in the skill.
# 
# For example, "Gambler 0" would mean you receive the Gambler skill
# at level 0. This is of benefit to you only if you have no Gambler
# skill.
# 
# "Vacc Suit" would mean you increase your Vacc Suit skill by +1 or
# gain it at level 1 if you have no Vacc Suit skill to begin with. If
# you have Vacc Suit 0, it increases to 1, if you have Vacc Suit 2 it
# rises to 3 and so forth.
# 
# "Streetwise 1" would mean you get the Streetwise skill at level 1.
# If your Streetwise skill is already 1 or more, then this is of no
# benefit to you. If you have no Streetwise skill, or it is only at 0,
# you jump straight to Streetwise 1. 
# 
# A skill may never be increased beyond level 4 during Traveller
# creation. Once a skill has reached level 4, any additional
# increases are lost. In addition, a Traveller may never have a
# total number of skill levels higher than three times their
# combined INT and EDU.
#=====================================================================#

def print_goodbye():
    print('\nThank you for using this program.\n')

