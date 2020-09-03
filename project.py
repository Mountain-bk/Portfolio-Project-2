


def main():
    intro()
    while True:
        answer = int(input("1.Heartfelt 2.Romantic 3.Action 4.Christmas 5.N/A: "))
        print("")
        # Heartfelt Comedy Movies
        if answer == 1:
            filter_heartfelt_comedies()
            break
        # Romantic Comedy Movies
        elif answer == 2:
            filter_romantic_comedies()
            break
        # Action Comedy Movies
        elif answer == 3:
            filter_action_comedies()
            break
        # Christmas Comedy Movies
        elif answer == 4:
            filter_christmas_comedies()
            break
        # N/A Comedy Movies
        elif answer == 5:
            filter_na_comedies()
            break
        else:
            print("Please choose 1 or 2 or 3 or 4 or 5.")
    print("For your information, numbers are 'Rotten Tomatoes' scores")
    print("Have a nice movie!")

def intro():
    print("I will give you Netflix Original Comedy Movie suggestion")
    print("Select most applicable number you like to watch.")

def question(question_list):
    print("You got " + str(len(question_list)) + " suggestions")
    print("Select most applicable number or list suggestions.")

def suggest_movies(suggestion_list):
    for movies in suggestion_list.keys():
        print(str(movies) + ": " + str(suggestion_list[movies]))
    print("You got " + str(len(suggestion_list)) + " suggested movies")

def filter_na_comedies():
    na_comedies = {'Sextuplets': 14, 'Unbreakable Kimmy Schmidt: Kimmy vs the Reverend': None, 'The Ridiculous 6': None,
                   'The Package': 42, 'The Polka King': 66, 'Bad Moms': 58, 'Between Two Ferns: The Movie': 74,
                   'A Futile and Stupid Gesture': 61, 'Wine Country': 66, 'The Land of Steady Habits': 85,
                   'Paddleton': 90, 'Girlfriends Day': 43, 'The Laundromat': 42, 'The Meyerowitz Stories': 92,
                   'War Machine': 49, 'Dude': None, 'Private Life': 94, 'Win It All': 85, 'Pee-wees Big Holiday': 80,
                   'Father of the Year': None, 'Mindhorn': 92, 'Take the 10': None}
    question(na_comedies)
    while True:
        answer_5 = int(input("1.Goofy 2.Humorous 3.Witty 4.N/A 5.List suggestions: "))
        print("")
        # N/A Goofy Comedy Movies
        if answer_5 == 1:
            na_goofy(na_comedies)
            suggest_movies(na_comedies)
            break
        # N/A Humorous Comedy Movies
        elif answer_5 == 2:
            na_humorous(na_comedies)
            suggest_movies(na_comedies)
            break
        # N/A Witty Comedy Movies
        elif answer_5 == 3:
            filter_na_witty(na_comedies)
            break
        elif answer_5 == 4:
            filter_na_na(na_comedies)
            break
        elif answer_5 == 5:
            suggest_movies(na_comedies)
            break
        else:
            print("Choose 1 or 2 or 3 or 4 or 5.")

def na_goofy(list_5_1):
    remove_list_5_1 = ['The Package', 'The Polka King', 'Bad Moms', 'Between Two Ferns: The Movie',
                       'A Futile and Stupid Gesture', 'Wine Country', 'The Meyerowitz Stories',
                       'The Land of Steady Habits', 'Paddleton', 'Girlfriends Day', 'The Laundromat',
                       'War Machine', 'Dude', 'Private Life', 'Win It All', 'Pee-wees Big Holiday',
                       'Father of the Year', 'Mindhorn', 'Take the 10']
    for key in remove_list_5_1:
        del list_5_1[key]

def na_humorous(list_5_2):
    remove_list_5_2 = ['Sextuplets', 'Unbreakable Kimmy Schmidt: Kimmy vs the Reverend', 'The Ridiculous 6',
                       'The Package', 'Between Two Ferns: The Movie', 'The Meyerowitz Stories',
                       'The Land of Steady Habits', 'Paddleton', 'Girlfriends Day', 'The Laundromat', 'War Machine',
                       'Dude', 'Private Life', 'Win It All', 'Pee-wees Big Holiday', 'Father of the Year',
                       'Mindhorn', 'Take the 10']
    for key in remove_list_5_2:
        del list_5_2[key]

def filter_na_witty(filter_5_3_1):
    na_witty(filter_5_3_1)
    question(filter_5_3_1)
    while True:
        answer_5_3 = int(input("1.Humorous 2.Emotional 3.Dark-comedy 4.Cerebral 5.List suggestions: "))
        print("")
        # N/A Witty Humorous Comedy Movies
        if answer_5_3 == 1:
            na_witty_humorous(filter_5_3_1)
            suggest_movies(filter_5_3_1)
            break
        # N/A Witty Emotional Comedy Movies
        elif answer_5_3 == 2:
            na_witty_emotional(filter_5_3_1)
            suggest_movies(filter_5_3_1)
            break
        # N/A Witty Dark-Comedy Movies
        elif answer_5_3 == 3:
            na_witty_dark(filter_5_3_1)
            suggest_movies(filter_5_3_1)
            break
        # N/A Witty Cerebral Comedy Movies
        elif answer_5_3 == 4:
            na_witty_cerebral(filter_5_3_1)
            suggest_movies(filter_5_3_1)
            break
        elif answer_5_3 == 5:
            suggest_movies(filter_5_3_1)
            break
        else:
            print("Choose 1 or 2 or 3 or 4 or 5.")

def na_witty(list_5_3):
    remove_list_5_3 = ['Sextuplets', 'Unbreakable Kimmy Schmidt: Kimmy vs the Reverend', 'The Ridiculous 6',
                       'The Package', 'The Polka King', 'Bad Moms', 'Between Two Ferns: The Movie',
                       'War Machine', 'Dude', 'Private Life', 'Win It All', 'Pee-wees Big Holiday', 'Father of the Year',
                       'Mindhorn', 'Take the 10']
    for key in remove_list_5_3:
        del list_5_3[key]

def na_witty_humorous(list_5_3_1):
    remove_list_5_3_1 = ['The Meyerowitz Stories', 'The Land of Steady Habits', 'Paddleton', 'Girlfriends Day',
                         'The Laundromat']
    for key in remove_list_5_3_1:
        del list_5_3_1[key]

def na_witty_emotional(list_5_3_2):
    remove_list_5_3_2 = ['A Futile and Stupid Gesture', 'Wine Country', 'The Meyerowitz Stories',
                         'Girlfriends Day', 'The Laundromat']
    for key in remove_list_5_3_2:
        del list_5_3_2[key]

def na_witty_dark(list_5_3_3):
    remove_list_5_3_3 = ['A Futile and Stupid Gesture', 'Wine Country', 'The Meyerowitz Stories',
                         'The Land of Steady Habits', 'Paddleton']
    for key in remove_list_5_3_3:
        del list_5_3_3[key]

def na_witty_cerebral(list_5_3_4):
    remove_list_5_3_4 = ['A Futile and Stupid Gesture', 'Wine Country', 'The Land of Steady Habits',
                         'Paddleton', 'Girlfriends Day']
    for key in remove_list_5_3_4:
        del list_5_3_4[key]

def filter_na_na(filter_5_3_2):
    na_na(filter_5_3_2)
    question(filter_5_3_2)
    while True:
        answer_5_4 = int(input("1.Independent 2.Youth 3.N/A 4.List suggestions: "))
        print("")
        # N/A N/A Independent Comedy Movies
        if answer_5_4 == 1:
            na_na_independent(filter_5_3_2)
            suggest_movies(filter_5_3_2)
            break
        # N/A N/A Youth Drama Comedy Movies
        elif answer_5_4 == 2:
            na_na_youth(filter_5_3_2)
            suggest_movies(filter_5_3_2)
            break
        elif answer_5_4 == 3:
            na_na_na(filter_5_3_2)
            suggest_movies(filter_5_3_2)
            break
        elif answer_5_4 == 4:
            suggest_movies(filter_5_3_2)
            break
        else:
            print("Choose 1 or 2 or 3 or 4.")

def na_na(list_5_4):
    remove_list_5_4 = ['Sextuplets', 'Unbreakable Kimmy Schmidt: Kimmy vs the Reverend', 'The Ridiculous 6',
                       'The Polka King', 'Bad Moms', 'A Futile and Stupid Gesture', 'Wine Country',
                       'The Meyerowitz Stories', 'The Land of Steady Habits', 'Paddleton', 'Girlfriends Day',
                       'The Laundromat']
    for key in remove_list_5_4:
        del list_5_4[key]

def na_na_independent(list_5_4_1):
    remove_list_5_4_1 = ['The Package', 'Between Two Ferns: The Movie', 'War Machine', 'Pee-wees Big Holiday',
                         'Father of the Year', 'Mindhorn', 'Take the 10']
    for key in remove_list_5_4_1:
        del list_5_4_1[key]

def na_na_youth(list_5_4_2):
    remove_list_5_4_2 = ['Between Two Ferns: The Movie', 'War Machine', 'Private Life', 'Win It All',
                         'Pee-wees Big Holiday', 'Father of the Year', 'Mindhorn', 'Take the 10']
    for key in remove_list_5_4_2:
        del list_5_4_2[key]

def na_na_na(list_5_4_3):
    remove_list_5_4_3 = ['The Package', 'Dude', 'Private Life', 'Win It All']
    for key in remove_list_5_4_3:
        del list_5_4_3[key]

def filter_christmas_comedies():
    christmas_comedies = {'Christmas Inheritance': 43, 'Let It Snow': 81, 'A Christmas Prince': 73,
                          'A Christmas Prince: The Royal Wedding': 50, 'A Christmas Prince: The Royal Baby': 33,
                          'The Knight Before Christmas': 68, 'The Christmas Chronicles': 64, 'The Princess Switch': 75,
                          'The Holiday Calendar': 33, 'Holiday Rush': None}
    question(christmas_comedies)
    while True:
        answer_4 = int(input("1.Children & Family 2.N/A 3.List suggestion: "))
        print("")
        # Christmas Children & Family Comedy Movies
        if answer_4 == 1:
            christmas_family(christmas_comedies)
            suggest_movies(christmas_comedies)
            break
        elif answer_4 == 2:
            christmas_na(christmas_comedies)
            suggest_movies(christmas_comedies)
            break
        elif answer_4 == 3:
            suggest_movies(christmas_comedies)
            break
        else:
            print("Choose 1 or 2 or 3.")

def christmas_family(list_4_1):
    remove_list_4_1 = ['Christmas Inheritance', 'Let It Snow', 'A Christmas Prince']
    for key in remove_list_4_1:
        del list_4_1[key]

def christmas_na(list_4_2):
    remove_list_4_2 = ['A Christmas Prince: The Royal Wedding', 'A Christmas Prince: The Royal Baby',
                       'The Knight Before Christmas', 'The Christmas Chronicles', 'The Princess Switch',
                       'The Holiday Calendar', 'Holiday Rush']
    for key in remove_list_4_2:
        del list_4_2[key]

def filter_action_comedies():
    action_comedies = {'The Do-Over': 5, 'Murder Mystery': 44, 'True Memoirs of an International Assassin': None,
                      'Coffee and Kareem': 20, 'Game Over, Man!': 19, 'The Hitmans Bodyguard': 43, 'Shaft': 32,
                      'Spenser Confidential': 38}
    question(action_comedies)
    while True:
        answer_3 = int(input("1.Goofy 2.N/A 3.List suggestion: "))
        print("")
        # Action Goofy Movies
        if answer_3 == 1:
            action_goofy(action_comedies)
            suggest_movies(action_comedies)
            break
        # Action Witty Comedy Movies
        elif answer_3 == 2:
            action_na(action_comedies)
            suggest_movies(action_comedies)
            break
        # Action Comedy Movies
        elif answer_3 == 3:
            suggest_movies(action_comedies)
            break
        else:
            print("Choose 1 or 2 or 3.")

def action_goofy(list_3_1):
    remove_list_3_1 = ['The Hitmans Bodyguard', 'Shaft', 'Spenser Confidential']
    for key in remove_list_3_1:
        del list_3_1[key]

def action_na(list_3_2):
    remove_list_3_2 = ['The Do-Over', 'Murder Mystery', 'True Memoirs of an International Assassin',
                       'Coffee and Kareem', 'Game Over, Man!']
    for key in remove_list_3_2:
        del list_3_2[key]

def filter_romantic_comedies():
    romantic_comedies = {'To All the Boys Ive Loved Before': 97, 'To All the Boys: P.S. I Still Love You': 75,
                         'Tall Girl': 44, 'The Last Summer': None, 'The Half of It': 96, 'The Kissing Booth': 17,
                         'Sierra Burgess Is a Loser': 61, 'The Perfect Date': 65, 'Candy Jar': 71, 'Ibiza': 67,
                         'Love Wedding Repeat': 31, 'Set It Up': 92, 'The Incredible Jessica James': 88,
                         'Always Be My Maybe': 89, 'Someone Great': 82, 'The Breaker Upperers': 89,
                         'When We First Met': 39, 'Falling Inn Love': 65, 'Home Again': 32, 'Holiday in the Wild': 43,
                         'Isnt It Romantic': 70, 'Nappily Ever After': 71}
    question(romantic_comedies)
    while True:
        answer_2 = int(input("1.Youth 2.Not Youth 3.List suggestions: "))
        print("")
        # Romantic Youth Comedy Movies
        if answer_2 == 1:
            filter_romantic_youth_comedies(romantic_comedies)
            break
        # Romantic Not Youth Comedy Movies
        elif answer_2 == 2:
            filter_romantic_not_youth_comedies(romantic_comedies)
            break
        # Romantic Comedy Movies
        elif answer_2 == 3:
            suggest_movies(romantic_comedies)
            break
        else:
            print("Choose 1 or 2 or 3.")

def filter_romantic_youth_comedies(filter_2_1):
    romantic_youth(filter_2_1)
    question(filter_2_1)
    while True:
        answer_2_1 = int(input("1.Heartfelt 2.Humorous 3.N/A 4.List suggestions: "))
        print("")
        # Romantic Youth Heartfelt Comedy Movies
        if answer_2_1 == 1:
            romantic_youth_heartfelt(filter_2_1)
            suggest_movies(filter_2_1)
            break
        # Romantic Youth Humorous Comedy Movies
        elif answer_2_1 == 2:
            romantic_youth_humorous(filter_2_1)
            suggest_movies(filter_2_1)
            break
        # Romantic Youth N/A Comedy Movies
        elif answer_2_1 == 3:
            romantic_youth_na(filter_2_1)
            suggest_movies(filter_2_1)
            break
        # Romantic Youth Comedy Movies
        elif answer_2_1 == 4:
            suggest_movies(filter_2_1)
            break
        else:
            print("Please choose 1 or 2 or 3 or 4.")

def romantic_youth(list_2_1):
    remove_list_2_1 = ['Ibiza', 'Love Wedding Repeat', 'Set It Up', 'The Incredible Jessica James', 'Always Be My Maybe',
                       'Someone Great', 'The Breaker Upperers', 'When We First Met', 'Falling Inn Love',
                       'Home Again', 'Holiday in the Wild', 'Isnt It Romantic', 'Nappily Ever After']
    for key in remove_list_2_1:
        del list_2_1[key]

def romantic_youth_heartfelt(list_2_1_1):
    remove_list_2_1_1 = ['To All the Boys Ive Loved Before', 'To All the Boys: P.S. I Still Love You',
                         'The Kissing Booth', 'Sierra Burgess Is a Loser', 'The Perfect Date', 'Candy Jar']
    for key in remove_list_2_1_1:
        del list_2_1_1[key]

def romantic_youth_humorous(list_2_1_2):
    remove_list_2_1_2 = ['To All the Boys Ive Loved Before', 'To All the Boys: P.S. I Still Love You',
                         'Sierra Burgess Is a Loser', 'Tall Girl', 'The Last Summer', 'The Half of It', 'Candy Jar']
    for key in remove_list_2_1_2:
        del list_2_1_2[key]

def romantic_youth_na(list_2_1_3):
    remove_list_2_1_3 = ['Tall Girl', 'The Last Summer', 'The Half of It', 'The Kissing Booth', 'The Perfect Date']
    for key in remove_list_2_1_3:
        del list_2_1_3[key]

def filter_romantic_not_youth_comedies(filter_2_2):
    romantic_not_youth(filter_2_2)
    question(filter_2_2)
    while True:
        answer_2_2 = int(input("1.Humorous 2.N/A 3.List suggestions: "))
        print("")
        # Romantic Not Youth Humorous Comedy Movies
        if answer_2_2 == 1:
            filter_romantic_not_youth_humorous(filter_2_2)
            break
        # Romantic Not Youth Not Humorous Movies
        elif answer_2_2 == 2:
            romantic_not_youth_na(filter_2_2)
            suggest_movies(filter_2_2)
            break
        # Romantic Not Youth Comedies Movies
        elif answer_2_2 == 3:
            suggest_movies(filter_2_2)
            break
        else:
            print("Please choose 1 or 2 or 3.")

def romantic_not_youth(list_2_2):
    remove_list_2_2 = ['To All the Boys Ive Loved Before', 'To All the Boys: P.S. I Still Love You', 'Tall Girl',
                       'The Last Summer', 'The Half of It', 'The Kissing Booth', 'Sierra Burgess Is a Loser',
                       'The Perfect Date', 'Candy Jar']
    for key in remove_list_2_2:
        del list_2_2[key]

def filter_romantic_not_youth_humorous(filter_2_2_1):
    romantic_not_youth_humorous(filter_2_2_1)
    question(filter_2_2_1)
    while True:
        answer_2_2_1 = int(input("1.Witty 2. N/A 3. List suggestions: "))
        print("")
        # Romantic Not Youth Humorous Witty Comedy Movies
        if answer_2_2_1 == 1:
            romantic_not_youth_humorous_witty(filter_2_2_1)
            suggest_movies(filter_2_2_1)
            break
        # Romantic Not Youth Humorous Not Witty Comedy Movies
        elif answer_2_2_1 == 2:
            romantic_not_youth_humorous_na(filter_2_2_1)
            suggest_movies(filter_2_2_1)
            break
        # Romantic Not Youth Comedy Movies
        elif answer_2_2_1 == 3:
            suggest_movies(filter_2_2_1)
            break
        else:
            print("Please Choose 1 or 2 or 3.")

def romantic_not_youth_humorous(list_2_2_1):
    remove_list_2_2_1 = ['Falling Inn Love', 'Home Again', 'Holiday in the Wild', 'Isnt It Romantic',
                         'Nappily Ever After']
    for key in remove_list_2_2_1:
        del list_2_2_1[key]

def romantic_not_youth_humorous_witty(list_2_2_1_1):
    remove_list_2_2_1_1 = ['Someone Great', 'The Breaker Upperers', 'When We First Met']
    for key in remove_list_2_2_1_1:
        del list_2_2_1_1[key]

def romantic_not_youth_humorous_na(list_2_2_1_2):
    remove_list_2_2_1_2 = ['Ibiza', 'Love Wedding Repeat', 'Set It Up', 'The Incredible Jessica James',
                           'Always Be My Maybe']
    for key in remove_list_2_2_1_2:
        del list_2_2_1_2[key]

def romantic_not_youth_na(list_2_2_2):
    remove_list_2_2_2 = ['Ibiza', 'Love Wedding Repeat', 'Set It Up', 'The Incredible Jessica James',
                         'Always Be My Maybe', 'Someone Great', 'The Breaker Upperers', 'When We First Met']
    for key in remove_list_2_2_2:
        del list_2_2_2[key]


def filter_heartfelt_comedies():
    heartfelt_comedies = {'The Fundamentals of Caring': 78, 'The Two Popes': 89, 'Otherhood': 25, 'The Last Laugh': 53,
                          'Unicorn Store': 64, 'Dolemite Is My Name': 97, 'Like Father': 46, '#realityhigh': 40,
                          'Dumplin': 85, 'Deidra & Laney Rob a Train': 92, 'The Main Event': 28, 'Sandy Wexler': 27,
                          'The Half of It': 96, 'To All the Boys Ive Loved Before': 97,
                          'To All the Boys P.S. I Still Love You': 75, 'The Last Summer': None,
                          'Tall Girl': 44, 'Love Wedding Repeat': 31, 'Falling Inn Love': 65,
                          'Holiday in the Wild': 43}
    question(heartfelt_comedies)
    while True:
        answer_1 = int(input("1.Romantic 2.Humorous 3.N/A 4.List suggestions: "))
        print("")
        # Heartfelt Romantic Comedy Movies
        if answer_1 == 1:
            filter_heartfelt_romantic_comedies(heartfelt_comedies)
            break
        # Heartfelt Humorous Comedy Movies
        elif answer_1 == 2:
            filter_heartfelt_humorous_comedies(heartfelt_comedies)
            break
        # Heartfelt N/A Comedy Movies
        elif answer_1 == 3:
            heartfelt_na(heartfelt_comedies)
            suggest_movies(heartfelt_comedies)
            break
        # Heartfelt Comedy Movies
        elif answer_1 == 4:
            suggest_movies(heartfelt_comedies)
            break
        else:
            print("Please choose 1 or 2 or 3 or 4")


def filter_heartfelt_romantic_comedies(filter_1_1):
    heartfelt_romantic(filter_1_1)
    question(filter_1_1)
    while True:
        answer_1_1 = int(input("1.Youth 2.Not Youth 3.List suggestions: "))
        print("")
        # Heartfelt Romantic Youth Comedy Movies
        if answer_1_1 == 1:
            heartfelt_romantic_youth(filter_1_1)
            suggest_movies(filter_1_1)
            break
        # Heartfelt Romantic Not Youth Comedy Movies
        elif answer_1_1 == 2:
            heartfelt_romantic_not_youth(filter_1_1)
            suggest_movies(filter_1_1)
            break
        # Heartfelt Romantic Comedy Movies
        elif answer_1_1 == 3:
            suggest_movies(filter_1_1)
            break
        else:
            print("Please choose 1 or 2 or 3.")

def heartfelt_romantic(list_1_1):
    remove_list_1_1 = ['The Fundamentals of Caring', 'The Two Popes', 'Otherhood', 'The Last Laugh', 'Unicorn Store',
                       'Dolemite Is My Name', 'Like Father', '#realityhigh', 'Dumplin', 'Deidra & Laney Rob a Train',
                       'The Main Event', 'Sandy Wexler']
    for key in remove_list_1_1:
        del list_1_1[key]

def heartfelt_romantic_youth(list_1_1_1):
    remove_list_1_1_1 = ['Love Wedding Repeat', 'Falling Inn Love', 'Holiday in the Wild']
    for key in remove_list_1_1_1:
        del list_1_1_1[key]

def heartfelt_romantic_not_youth(list_1_1_2):
    remove_list_1_1_2 = ['The Half of It', 'To All the Boys Ive Loved Before', 'To All the Boys P.S. I Still Love You',
                         'The Last Summer', 'Tall Girl']
    for key in remove_list_1_1_2:
        del list_1_1_2[key]

def filter_heartfelt_humorous_comedies(filter_1_2):
    heartfelt_humorous(filter_1_2)
    question(filter_1_2)
    while True:
        answer_1_2 = int(input("1.Youth 2.Not Youth 3.N/A 4.List suggestions: "))
        print("")
        # Heartfelt Humorous Youth Comedy Movies
        if answer_1_2 == 1:
            heartfelt_humorous_youth(filter_1_2)
            suggest_movies(filter_1_2)
            break
        # Heartfelt Humorous Not Youth Comedy Movies
        elif answer_1_2 == 2:
            heartfelt_humorous_not_youth(filter_1_2)
            suggest_movies(filter_1_2)
            break
        # Heartfelt Humorous N/A Comedy Movies
        elif answer_1_2 == 3:
            heartfelt_humorous_na(filter_1_2)
            suggest_movies(filter_1_2)
            break
        # Heartfelt Humorous Comedy Movies
        elif answer_1_2 == 4:
            suggest_movies(filter_1_2)
            break
        else:
            print("Please choose 1 or 2 or 3 or 4.")

def heartfelt_humorous(list_1_2):
    remove_list_1_2 = ['The Main Event', 'Sandy Wexler', 'The Half of It', 'To All the Boys Ive Loved Before',
                       'To All the Boys P.S. I Still Love You', 'The Last Summer', 'Tall Girl',
                       'Love Wedding Repeat', 'Falling Inn Love', 'Holiday in the Wild']
    for key in remove_list_1_2:
        del list_1_2[key]

def heartfelt_humorous_youth(list_1_2_1):
    remove_list_1_2_1 = ['The Fundamentals of Caring', 'The Two Popes', 'Otherhood', 'The Last Laugh',
                         'Unicorn Store', 'Dolemite Is My Name', 'Like Father']
    for key in remove_list_1_2_1:
        del list_1_2_1[key]

def heartfelt_humorous_not_youth(list_1_2_2):
    remove_list_1_2_2 = ['The Fundamentals of Caring', '#realityhigh', 'Dumplin', 'Deidra & Laney Rob a Train']
    for key in remove_list_1_2_2:
        del list_1_2_2[key]

def heartfelt_humorous_na(list_1_2_3):
    remove_list_1_2_3 = ['The Two Popes', 'Otherhood', 'The Last Laugh', 'Unicorn Store', 'Dolemite Is My Name',
                         'Like Father', '#realityhigh', 'Dumplin', 'Deidra & Laney Rob a Train']
    for key in remove_list_1_2_3:
        del list_1_2_3[key]

def heartfelt_na(list_1_3):
    remove_list_1_3 = ['The Half of It', 'To All the Boys Ive Loved Before', 'To All the Boys P.S. I Still Love You',
                       'The Last Summer', 'Tall Girl', 'Love Wedding Repeat', 'Falling Inn Love', 'Holiday in the Wild',
                       'The Fundamentals of Caring', 'The Two Popes', 'Otherhood', 'The Last Laugh', 'Unicorn Store',
                       'Dolemite Is My Name', 'Like Father', '#realityhigh', 'Dumplin', 'Deidra & Laney Rob a Train']
    for key in remove_list_1_3:
        del list_1_3[key]

if __name__ == '__main__':
    main()