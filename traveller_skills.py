
def get_traveller_skills():
    i = 0
    traveller_skills = [
                        "Admin","Advocate","Animals","Art","Astrogation",
                        "Athletics","Broker","Carouse","Deception",
                        "Diplomat","Drive","Electronics","Engineer",
                        "Explosives","Flyer","Gambler","Gun Combat",
                        "Gunner","Heavy Weapons","Investigate",
                        "Jack Of All Trades","Language","Leadership",
                        "Mechanic","Medic","Melee","Navigation",
                        "Persuade","Pilot","Profession","Recon",
                        "Science","Seafarer","Stealth","Steward",
                        "Streetwise","Survival","Tactics","Vacc Suit"
                        ]
    traveller_skill_scrores = [
                                -3, -3, -3, -3, -3, -3, -3, -3, -3, -3,
                                -3, -3, -3, -3, -3, -3, -3, -3, -3, -3,
                                -3, -3, -3, -3, -3, -3, -3, -3, -3, -3,
                                -3, -3, -3, -3, -3, -3, -3, -3, -3
                                ]
    
    print(len(traveller_skills))

    while i < len(traveller_skills):
    
        a = "'"
        print(f"# traveller_skills[{i}] - ", end='')
        print(f'"{traveller_skills[i]}"')
        #print(traveller_skill_scrores[i])
        i += 1


get_traveller_skills()