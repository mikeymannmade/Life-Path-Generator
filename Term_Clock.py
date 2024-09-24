UNIVERSITY = 1
MILITARY_ACADEMY = 2
CAREERS = 3
TRAVELLER = 4

def lifepath():
    term = 1
    age = 18

    while term <= 3:
        precareer_education()

def precareer_education():
    print("Would you like to attend Pre-Career Education this term?\n")
    print("1. Yes \n2. No \n")
    menu_choice = input("Menu Choice: ")


# Precareer Education
#-------------
# University
#
# Entry EDU 6+
#   DM-1 if in Term Two
#   DM-2 if in Term Three 
#   DM+1 if SOC 9 or higher 
#
#Choose a level 0 and a level 1 skill from the following list:
#
#| [[Admin]]                            |
#| ------------------------------------ |
#| [[Advocate]]                         |
#| [[Animals (training or veterinary)]] |
#| [[Art (any)]]                        |
#| [[Astrogation]]                      |
#| [[Electronics (any)]]                |
#| [[Engineer (any)]]                   |
#| [[Language (any)]]                   |
#| [[Medic]]                            |
#| [[Navigation]]                       |
#| [[Professional (any)]]               |
#| [[Science (any)]]                    |
#
# Increase EDU by +1
#
# Pre-Career Events
#| 2D  | Event                          |
#======================================================================
#| 2   | You are approached by an underground (and highly illegal)    
#|     | psionic group who sense potential in you. You may test your
#|     | PSI and attempt to enter the [[Psion]] career in any 
#|     | subsequent term.
#======================================================================
#| 3   | Your time in education is not a happy one and you suffer a
#|     | deep tragedy; perhaps you become hopelessly addicted to 
#|     | drink or drugs, a failed romance leaves you in tatters or a 
#|     | fatal accident involving a close friend shakes your 
#|     | confidence. You crash and fail to graduate.
# =====================================================================
#| 4   | A supposedly harmless prank goes wrong and someone gets hurt, 
#|     | physically or emotionally. Roll SOC 8+. If you succeed, gain a
#|     | [[Rival]]. If you fail, gain an [[Enemy]]. If you roll 2, you 
#|     | fail to graduate and must take the [[Prisoner]] career in your
#|     | next term.
#======================================================================
#| 5   | Taking advantage of youth, you party as much as you study. 
#        Gain [[Carouse]] 1.   
#======================================================================
#| 6   | You become involved in a tightly knit clique or group and make
#        a pact to remain friends forever, wherever in the galaxy you 
#        may end. Gain D3 [[Ally\|Allies]].
#======================================================================
#| 7   | Life Event. Roll on the [[Life Events]] table.
#        become a leading figure. Gain one [[Ally]] within the movement
#        but gain one [[Enemy]] in wider society.
#======================================================================
#| 9   | You develop a healthy interest in a hobby or other area of 
#        study. Gain [[any skill]] of your choice, with the exception 
#        of Jack-of-all-Trades, at level 0.
#======================================================================
#| 10  | A newly arrived tutor rubs you up the wrong way and you work
#        hard to overturn their conclusions. Roll 9+ on any skill you
#        have learned during this term. If successful, you provide a
#        truly elegant proof that soon becomes accepted as the standard
#        approach. Gain a level in the skill you rolled on and the
#        tutor as a [[Rival]].
#======================================================================
#| 11  | War comes and a wide-ranging draft is instigated. You can
#        either flee and join the [[Drifter]] career next term or be
#        [[The Draft\|drafted]]. Either way, you do not graduate this
#        term. However, if you roll SOC 9+, you can get enough strings
#        pulled to avoid the draft and complete your education – you
#        may attempt graduation normally and are not drafted.
#======================================================================
#| 12  | You gain wide-ranging recognition of your initiative and
#        innovative approach to study. Increase your SOC by +1.
#====================================================================== 
# Graduating University
#======================================================================
# | Graduation | INT 6+  |
# | ---------- | ------- |
# | With Honors     | INT 10+ |
# Graduation Benefits
# - Increase both of the skills chosen before by one level. 
# - Increase EDU by an additional +1. 
# - Graduation grants DM+1 (DM+2 if graduation was with honors) to 
#   qualify for the following careers; [[Agent]], [[Army]], 
#   [[Citizen\|Citizen (corporate)]], 
#   [[Entertainer\|Entertainer (journalist)]], [[Marine]], [[Navy]],
#   [[Scholar]], [[Scout]]. 
# - Graduation allows a commission roll to be taken before the first
#   term of a military career, so long as it is the first career chosen
#   after university. Success will mean the Traveller enters the career
#   at officer rank 1. If graduation was with honors, DM+2 is granted
#   on this first commission roll. 
#======================================================================
# MILITARY ACADEMY
#======================================================================
# For those looking to dedicate their lives to military service, there
# is no better option than joining an academy to round out an
# education. This is a popular choice for those coming from ‘military’
# families or those having grown up never considering anything other 
# than a life in uniform. A term within a military academy can set a 
# recruit’s career for great things, so competition to gain one of the 
# limited number of open student slots is fierce. 
#======================================================================
# Before joining a military academy, you must decide whether it is an 
# academy of the [[Army]], [[Marine|Marines]] or [[Navy]]. 
#======================================================================
# Entry to Military Academy
#======================================================================
# | Army | END 7+ |
# | ---- | ---- |
# | Marines | END 8+ |
# | Navy | INT 8+ |
# DM-2 if in Term Two
# DM-4 if in Term Three. 
#======================================================================
# Skills
#======================================================================
# Gain all Service Skills of the military career the academy is tied to
# at level 0, as with basic training. 
#======================================================================
# Pre-Career Event
#======================================================================
#| 2D  | Event                          |
#======================================================================
#| 2   | You are approached by an underground (and highly illegal)    
#|     | psionic group who sense potential in you. You may test your
#|     | PSI and attempt to enter the [[Psion]] career in any 
#|     | subsequent term.
#======================================================================
#| 3   | Your time in education is not a happy one and you suffer a
#|     | deep tragedy; perhaps you become hopelessly addicted to 
#|     | drink or drugs, a failed romance leaves you in tatters or a 
#|     | fatal accident involving a close friend shakes your 
#|     | confidence. You crash and fail to graduate.
# =====================================================================
#| 4   | A supposedly harmless prank goes wrong and someone gets hurt, 
#|     | physically or emotionally. Roll SOC 8+. If you succeed, gain a
#|     | [[Rival]]. If you fail, gain an [[Enemy]]. If you roll 2, you 
#|     | fail to graduate and must take the [[Prisoner]] career in your
#|     | next term.
#======================================================================
#| 5   | Taking advantage of youth, you party as much as you study. 
#        Gain [[Carouse]] 1.   
#======================================================================
#| 6   | You become involved in a tightly knit clique or group and make
#        a pact to remain friends forever, wherever in the galaxy you 
#        may end. Gain D3 [[Ally\|Allies]].
#======================================================================
#| 7   | Life Event. Roll on the [[Life Events]] table.
#        become a leading figure. Gain one [[Ally]] within the movement
#        but gain one [[Enemy]] in wider society.
#======================================================================
#| 9   | You develop a healthy interest in a hobby or other area of 
#        study. Gain [[any skill]] of your choice, with the exception 
#        of Jack-of-all-Trades, at level 0.
#======================================================================
#| 10  | A newly arrived tutor rubs you up the wrong way and you work
#        hard to overturn their conclusions. Roll 9+ on any skill you
#        have learned during this term. If successful, you provide a
#        truly elegant proof that soon becomes accepted as the standard
#        approach. Gain a level in the skill you rolled on and the
#        tutor as a [[Rival]].
#======================================================================
#| 11  | War comes and a wide-ranging draft is instigated. You can
#        either flee and join the [[Drifter]] career next term or be
#        [[The Draft\|drafted]]. Either way, you do not graduate this
#        term. However, if you roll SOC 9+, you can get enough strings
#        pulled to avoid the draft and complete your education – you
#        may attempt graduation normally and are not drafted.
#======================================================================
#| 12  | You gain wide-ranging recognition of your initiative and
#        innovative approach to study. Increase your SOC by +1.
#======================================================================
# Graduating Military Academy
#======================================================================
# | Graduation  | INT 7+  |
# | ----------- | ------- |
# | With Honors | INT 11+ |
# DM+1 if END 8 or higher.
# DM+1 if SOC 8 or higher. 
#======================================================================
# >[!note]
# >If a Traveller attends a military academy but fails to graduate, 
# they may still automatically enter the military career that the 
# academy is tied to, so long as they did not roll 2 or less on the 
# graduation roll. If they choose to enter this career, they may not 
# make a commission roll in the first term. 
#======================================================================
# Graduation Benefits
#======================================================================
# - If entering the same military career the academy is tied to, select
#   any three Service Skills and increase them to level 1. 
# - Increase EDU by +1. 
# - If the Traveller graduated with honors, increase SOC by +1 as well. 
# - Graduation allows automatic entry into the military career the
#   academy is tied to, so long as it is the first career attempted by 
#   the Traveller after graduation
# - Graduation allows a commission roll to be taken before the first 
#   term of a military career, so long as it is the first career chosen
#   after university, with DM+2. Success will mean the Traveller enters
#   the career at officer rank 1. If graduation was with honors, the 
#   Traveller will automatically pass this roll. 



