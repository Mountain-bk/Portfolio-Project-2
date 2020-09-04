
from tkinter import *

root = Tk()

canvas = Canvas(root, height="700", width="800")
canvas.pack()



def na_na_na(list_5_4_3):
    remove_list_5_4_3 = ['The Package', 'Dude', 'Private Life', 'Win It All']
    for key in remove_list_5_4_3:
        del list_5_4_3[key]
    suggest_movies(list_5_4_3)

def na_na_youth(list_5_4_2):
    remove_list_5_4_2 = ['Between Two Ferns: The Movie', 'War Machine', 'Private Life', 'Win It All',
                         'Pee-wees Big Holiday', 'Father of the Year', 'Mindhorn', 'Take the 10']
    for key in remove_list_5_4_2:
        del list_5_4_2[key]
    suggest_movies(list_5_4_2)

def na_na_independent(list_5_4_1):
    remove_list_5_4_1 = ['The Package', 'Between Two Ferns: The Movie', 'War Machine', 'Pee-wees Big Holiday',
                         'Father of the Year', 'Mindhorn', 'Take the 10']
    for key in remove_list_5_4_1:
        del list_5_4_1[key]
    suggest_movies(list_5_4_1)

def na_na(list_5_4):
    remove_list_5_4 = ['Sextuplets', 'Unbreakable Kimmy Schmidt: Kimmy vs the Reverend', 'The Ridiculous 6',
                       'The Polka King', 'Bad Moms', 'A Futile and Stupid Gesture', 'Wine Country',
                       'The Meyerowitz Stories', 'The Land of Steady Habits', 'Paddleton', 'Girlfriends Day',
                       'The Laundromat']
    for key in remove_list_5_4:
        del list_5_4[key]

def filter_na_na(filter_5_3_2):
    na_na(filter_5_3_2)
    question(filter_5_3_2)
    btn1.config(text="Independent", command=lambda: na_na_independent(filter_5_3_2))
    btn2.config(text="Youth", command=lambda: na_na_youth(filter_5_3_2))
    btn3.config(text="N/A", command=lambda: na_na_na(filter_5_3_2))
    btn4.config(text="List suggestions", command=lambda: suggest_movies(filter_5_3_2))
    btn5.pack_forget()

def na_witty_cerebral(list_5_3_4):
    remove_list_5_3_4 = ['A Futile and Stupid Gesture', 'Wine Country', 'The Land of Steady Habits',
                         'Paddleton', 'Girlfriends Day']
    for key in remove_list_5_3_4:
        del list_5_3_4[key]
    suggest_movies(list_5_3_4)

def na_witty_dark(list_5_3_3):
    remove_list_5_3_3 = ['A Futile and Stupid Gesture', 'Wine Country', 'The Meyerowitz Stories',
                         'The Land of Steady Habits', 'Paddleton']
    for key in remove_list_5_3_3:
        del list_5_3_3[key]
    suggest_movies(list_5_3_3)

def na_witty_emotional(list_5_3_2):
    remove_list_5_3_2 = ['A Futile and Stupid Gesture', 'Wine Country', 'The Meyerowitz Stories',
                         'Girlfriends Day', 'The Laundromat']
    for key in remove_list_5_3_2:
        del list_5_3_2[key]
    suggest_movies(list_5_3_2)

def na_witty_humorous(list_5_3_1):
    remove_list_5_3_1 = ['The Meyerowitz Stories', 'The Land of Steady Habits', 'Paddleton', 'Girlfriends Day',
                         'The Laundromat']
    for key in remove_list_5_3_1:
        del list_5_3_1[key]
    suggest_movies(list_5_3_1)

def na_witty(list_5_3):
    remove_list_5_3 = ['Sextuplets', 'Unbreakable Kimmy Schmidt: Kimmy vs the Reverend', 'The Ridiculous 6',
                       'The Package', 'The Polka King', 'Bad Moms', 'Between Two Ferns: The Movie',
                       'War Machine', 'Dude', 'Private Life', 'Win It All', 'Pee-wees Big Holiday', 'Father of the Year',
                       'Mindhorn', 'Take the 10']
    for key in remove_list_5_3:
        del list_5_3[key]

def filter_na_witty(filter_5_3_1):
    na_witty(filter_5_3_1)
    question(filter_5_3_1)
    btn1.config(text="Humorous", command=lambda: na_witty_humorous(filter_5_3_1))
    btn2.config(text="Emotional", command=lambda: na_witty_emotional(filter_5_3_1))
    btn3.config(text="Dark-comedy", command=lambda: na_witty_dark(filter_5_3_1))
    btn4.config(text="Cerebral", command=lambda: na_witty_cerebral(filter_5_3_1))
    btn5.config(text="List suggestions", command=lambda: suggest_movies(filter_5_3_1))

def na_humorous(list_5_2):
    remove_list_5_2 = ['Sextuplets', 'Unbreakable Kimmy Schmidt: Kimmy vs the Reverend', 'The Ridiculous 6',
                       'The Package', 'Between Two Ferns: The Movie', 'The Meyerowitz Stories',
                       'The Land of Steady Habits', 'Paddleton', 'Girlfriends Day', 'The Laundromat', 'War Machine',
                       'Dude', 'Private Life', 'Win It All', 'Pee-wees Big Holiday', 'Father of the Year',
                       'Mindhorn', 'Take the 10']
    for key in remove_list_5_2:
        del list_5_2[key]
    suggest_movies(list_5_2)

def na_goofy(list_5_1):
    remove_list_5_1 = ['The Package', 'The Polka King', 'Bad Moms', 'Between Two Ferns: The Movie',
                       'A Futile and Stupid Gesture', 'Wine Country', 'The Meyerowitz Stories',
                       'The Land of Steady Habits', 'Paddleton', 'Girlfriends Day', 'The Laundromat',
                       'War Machine', 'Dude', 'Private Life', 'Win It All', 'Pee-wees Big Holiday',
                       'Father of the Year', 'Mindhorn', 'Take the 10']
    for key in remove_list_5_1:
        del list_5_1[key]
    suggest_movies(list_5_1)

def filter_na_comedies():
    na_comedies = {'Sextuplets': 14, 'Unbreakable Kimmy Schmidt: Kimmy vs the Reverend': None, 'The Ridiculous 6': None,
                   'The Package': 42, 'The Polka King': 66, 'Bad Moms': 58, 'Between Two Ferns: The Movie': 74,
                   'A Futile and Stupid Gesture': 61, 'Wine Country': 66, 'The Land of Steady Habits': 85,
                   'Paddleton': 90, 'Girlfriends Day': 43, 'The Laundromat': 42, 'The Meyerowitz Stories': 92,
                   'War Machine': 49, 'Dude': None, 'Private Life': 94, 'Win It All': 85, 'Pee-wees Big Holiday': 80,
                   'Father of the Year': None, 'Mindhorn': 92, 'Take the 10': None}
    question(na_comedies)
    btn1.config(text="Goofy", command=lambda: na_goofy(na_comedies))
    btn2.config(text="Humorous", command=lambda: na_humorous(na_comedies))
    btn3.config(text="Witty", command=lambda: filter_na_witty(na_comedies))
    btn4.config(text="N/A", command=lambda: filter_na_na(na_comedies))
    btn5.config(text="List suggestions", command=lambda: suggest_movies(na_comedies))

def christmas_na(list_4_2):
    remove_list_4_2 = ['A Christmas Prince: The Royal Wedding', 'A Christmas Prince: The Royal Baby',
                       'The Knight Before Christmas', 'The Christmas Chronicles', 'The Princess Switch',
                       'The Holiday Calendar', 'Holiday Rush']
    for key in remove_list_4_2:
        del list_4_2[key]
    suggest_movies(list_4_2)

def christmas_family(list_4_1):
    remove_list_4_1 = ['Christmas Inheritance', 'Let It Snow', 'A Christmas Prince']
    for key in remove_list_4_1:
        del list_4_1[key]
    suggest_movies(list_4_1)

def filter_christmas_comedies():
    christmas_comedies = {'Christmas Inheritance': 43, 'Let It Snow': 81, 'A Christmas Prince': 73,
                          'A Christmas Prince: The Royal Wedding': 50, 'A Christmas Prince: The Royal Baby': 33,
                          'The Knight Before Christmas': 68, 'The Christmas Chronicles': 64, 'The Princess Switch': 75,
                          'The Holiday Calendar': 33, 'Holiday Rush': None}
    question(christmas_comedies)
    btn1.config(text="Children & Family", command=lambda: christmas_family(christmas_comedies))
    btn2.config(text="N/A", command=lambda: christmas_na(christmas_comedies))
    btn3.config(text="List suggestions", command=lambda: suggest_movies(christmas_comedies))
    btn4.pack_forget()
    btn5.pack_forget()


def action_na(list_3_2):
    remove_list_3_2 = ['The Do-Over', 'Murder Mystery', 'True Memoirs of an International Assassin',
                       'Coffee and Kareem', 'Game Over, Man!']
    for key in remove_list_3_2:
        del list_3_2[key]
    suggest_movies(list_3_2)

def action_goofy(list_3_1):
    remove_list_3_1 = ['The Hitmans Bodyguard', 'Shaft', 'Spenser Confidential']
    for key in remove_list_3_1:
        del list_3_1[key]
    suggest_movies(list_3_1)

def filter_action_comedies():
    action_comedies = {'The Do-Over': 5, 'Murder Mystery': 44, 'True Memoirs of an International Assassin': None,
                      'Coffee and Kareem': 20, 'Game Over, Man!': 19, 'The Hitmans Bodyguard': 43, 'Shaft': 32,
                      'Spenser Confidential': 38}
    question(action_comedies)
    btn1.config(text="Goofy", command=lambda: action_goofy(action_comedies))
    btn2.config(text="N/A", command=lambda: action_na(action_comedies))
    btn3.config(text="List suggestions", command=lambda: suggest_movies(action_comedies))
    btn4.pack_forget()
    btn5.pack_forget()

def romantic_not_youth_na(list_2_2_2):
    remove_list_2_2_2 = ['Ibiza', 'Love Wedding Repeat', 'Set It Up', 'The Incredible Jessica James',
                         'Always Be My Maybe', 'Someone Great', 'The Breaker Upperers', 'When We First Met']
    for key in remove_list_2_2_2:
        del list_2_2_2[key]
    suggest_movies(list_2_2_2)

def romantic_not_youth_humorous_na(list_2_2_1_2):
    remove_list_2_2_1_2 = ['Ibiza', 'Love Wedding Repeat', 'Set It Up', 'The Incredible Jessica James',
                           'Always Be My Maybe']
    for key in remove_list_2_2_1_2:
        del list_2_2_1_2[key]
    suggest_movies(list_2_2_1_2)

def romantic_not_youth_humorous_witty(list_2_2_1_1):
    remove_list_2_2_1_1 = ['Someone Great', 'The Breaker Upperers', 'When We First Met']
    for key in remove_list_2_2_1_1:
        del list_2_2_1_1[key]
    suggest_movies(list_2_2_1_1)

def romantic_not_youth_humorous(list_2_2_1):
    remove_list_2_2_1 = ['Falling Inn Love', 'Home Again', 'Holiday in the Wild', 'Isnt It Romantic',
                         'Nappily Ever After']
    for key in remove_list_2_2_1:
        del list_2_2_1[key]

def filter_romantic_not_youth_humorous(filter_2_2_1):
    romantic_not_youth_humorous(filter_2_2_1)
    question(filter_2_2_1)
    btn1.config(text="Witty", command=lambda: romantic_not_youth_humorous_witty(filter_2_2_1))
    btn2.config(text="N/A", command=lambda: romantic_not_youth_humorous_na(filter_2_2_1))
    btn3.config(text="List suggestions", command=lambda: suggest_movies(filter_2_2_1))

def romantic_not_youth(list_2_2):
    remove_list_2_2 = ['To All the Boys Ive Loved Before', 'To All the Boys: P.S. I Still Love You', 'Tall Girl',
                       'The Last Summer', 'The Half of It', 'The Kissing Booth', 'Sierra Burgess Is a Loser',
                       'The Perfect Date', 'Candy Jar']
    for key in remove_list_2_2:
        del list_2_2[key]

def filter_romantic_not_youth_comedies(filter_2_2):
    romantic_not_youth(filter_2_2)
    question(filter_2_2)
    btn1.config(text="Humorous", command=lambda: filter_romantic_not_youth_humorous(filter_2_2))
    btn2.config(text="N/A", command=lambda: romantic_not_youth_na(filter_2_2))
    btn3.config(text="List suggestions", command=lambda: suggest_movies(filter_2_2))

def romantic_youth_na(list_2_1_3):
    remove_list_2_1_3 = ['Tall Girl', 'The Last Summer', 'The Half of It', 'The Kissing Booth', 'The Perfect Date']
    for key in remove_list_2_1_3:
        del list_2_1_3[key]
    suggest_movies(list_2_1_3)

def romantic_youth_humorous(list_2_1_2):
    remove_list_2_1_2 = ['To All the Boys Ive Loved Before', 'To All the Boys: P.S. I Still Love You',
                         'Sierra Burgess Is a Loser', 'Tall Girl', 'The Last Summer', 'The Half of It', 'Candy Jar']
    for key in remove_list_2_1_2:
        del list_2_1_2[key]
    suggest_movies(list_2_1_2)

def romantic_youth_heartfelt(list_2_1_1):
    remove_list_2_1_1 = ['To All the Boys Ive Loved Before', 'To All the Boys: P.S. I Still Love You',
                         'The Kissing Booth', 'Sierra Burgess Is a Loser', 'The Perfect Date', 'Candy Jar']
    for key in remove_list_2_1_1:
        del list_2_1_1[key]
    suggest_movies(list_2_1_1)

def romantic_youth(list_2_1):
    remove_list_2_1 = ['Ibiza', 'Love Wedding Repeat', 'Set It Up', 'The Incredible Jessica James', 'Always Be My Maybe',
                       'Someone Great', 'The Breaker Upperers', 'When We First Met', 'Falling Inn Love',
                       'Home Again', 'Holiday in the Wild', 'Isnt It Romantic', 'Nappily Ever After']
    for key in remove_list_2_1:
        del list_2_1[key]

def filter_romantic_youth_comedies(filter_2_1):
    romantic_youth(filter_2_1)
    question(filter_2_1)
    btn1.config(text="Heartfelt", command=lambda: romantic_youth_heartfelt(filter_2_1))
    btn2.config(text="Humorous", command=lambda: romantic_youth_humorous(filter_2_1))
    btn3.config(text="N/A", command=lambda: romantic_youth_na(filter_2_1))
    btn4.pack()
    btn4.config(text="List suggestions", command=lambda: suggest_movies(filter_2_1))

def filter_romantic_comedies():
    romantic_comedies = {'To All the Boys Ive Loved Before': 97, 'To All the Boys: P.S. I Still Love You': 75,
                         'Tall Girl': 44, 'The Last Summer': None, 'The Half of It': 96, 'The Kissing Booth': 17,
                         'Sierra Burgess Is a Loser': 61, 'The Perfect Date': 65, 'Candy Jar': 71, 'Ibiza': 67,
                         'Love Wedding Repeat': 31, 'Set It Up': 92, 'The Incredible Jessica James': 88,
                         'Always Be My Maybe': 89, 'Someone Great': 82, 'The Breaker Upperers': 89,
                         'When We First Met': 39, 'Falling Inn Love': 65, 'Home Again': 32, 'Holiday in the Wild': 43,
                         'Isnt It Romantic': 70, 'Nappily Ever After': 71}
    question(romantic_comedies)
    btn1.config(text="Youth", command=lambda: filter_romantic_youth_comedies(romantic_comedies))
    btn2.config(text="Not Youth", command=lambda: filter_romantic_not_youth_comedies(romantic_comedies))
    btn3.config(text="List suggestions", command=lambda: suggest_movies(romantic_comedies))
    btn4.pack_forget()
    btn5.pack_forget()

def heartfelt_na(list_1_3):
    remove_list_1_3 = ['The Half of It', 'To All the Boys Ive Loved Before', 'To All the Boys P.S. I Still Love You',
                       'The Last Summer', 'Tall Girl', 'Love Wedding Repeat', 'Falling Inn Love', 'Holiday in the Wild',
                       'The Fundamentals of Caring', 'The Two Popes', 'Otherhood', 'The Last Laugh', 'Unicorn Store',
                       'Dolemite Is My Name', 'Like Father', '#realityhigh', 'Dumplin', 'Deidra & Laney Rob a Train']
    for key in remove_list_1_3:
        del list_1_3[key]
    suggest_movies(list_1_3)

def heartfelt_humorous_na(list_1_2_3):
    remove_list_1_2_3 = ['The Two Popes', 'Otherhood', 'The Last Laugh', 'Unicorn Store', 'Dolemite Is My Name',
                         'Like Father', '#realityhigh', 'Dumplin', 'Deidra & Laney Rob a Train']
    for key in remove_list_1_2_3:
        del list_1_2_3[key]
    suggest_movies(list_1_2_3)

def heartfelt_humorous_not_youth(list_1_2_2):
    remove_list_1_2_2 = ['The Fundamentals of Caring', '#realityhigh', 'Dumplin', 'Deidra & Laney Rob a Train']
    for key in remove_list_1_2_2:
        del list_1_2_2[key]
    suggest_movies(list_1_2_2)

def heartfelt_humorous_youth(list_1_2_1):
    remove_list_1_2_1 = ['The Fundamentals of Caring', 'The Two Popes', 'Otherhood', 'The Last Laugh',
                         'Unicorn Store', 'Dolemite Is My Name', 'Like Father']
    for key in remove_list_1_2_1:
        del list_1_2_1[key]
    suggest_movies(list_1_2_1)

def heartfelt_humorous(list_1_2):
    remove_list_1_2 = ['The Main Event', 'Sandy Wexler', 'The Half of It', 'To All the Boys Ive Loved Before',
                       'To All the Boys P.S. I Still Love You', 'The Last Summer', 'Tall Girl',
                       'Love Wedding Repeat', 'Falling Inn Love', 'Holiday in the Wild']
    for key in remove_list_1_2:
        del list_1_2[key]

def filter_heartfelt_humorous_comedies(filter_1_2):
    heartfelt_humorous(filter_1_2)
    question(filter_1_2)
    btn1.config(text="Youth", command=lambda: heartfelt_humorous_youth(filter_1_2))
    btn2.config(text="Not Youth", command=lambda: heartfelt_humorous_not_youth(filter_1_2))
    btn3.config(text="N/A", command=lambda: heartfelt_humorous_na(filter_1_2))
    btn4.config(text="List suggestions", command=lambda: suggest_movies(filter_1_2))

def heartfelt_romantic_not_youth(list_1_1_2):
    remove_list_1_1_2 = ['The Half of It', 'To All the Boys Ive Loved Before', 'To All the Boys P.S. I Still Love You',
                         'The Last Summer', 'Tall Girl']
    for key in remove_list_1_1_2:
        del list_1_1_2[key]
    suggest_movies(list_1_1_2)

def heartfelt_romantic_youth(list_1_1_1):
    remove_list_1_1_1 = ['Love Wedding Repeat', 'Falling Inn Love', 'Holiday in the Wild']
    for key in remove_list_1_1_1:
        del list_1_1_1[key]
    suggest_movies(list_1_1_1)

def heartfelt_romantic(list_1_1):
    remove_list_1_1 = ['The Fundamentals of Caring', 'The Two Popes', 'Otherhood', 'The Last Laugh', 'Unicorn Store',
                       'Dolemite Is My Name', 'Like Father', '#realityhigh', 'Dumplin', 'Deidra & Laney Rob a Train',
                       'The Main Event', 'Sandy Wexler']
    for key in remove_list_1_1:
        del list_1_1[key]

def filter_heartfelt_romantic_comedies(filter_1_1):
    heartfelt_romantic(filter_1_1)
    question(filter_1_1)
    btn1.config(text="Youth", command=lambda: heartfelt_romantic_youth(filter_1_1))
    btn2.config(text="Not Youth", command=lambda: heartfelt_romantic_not_youth(filter_1_1))
    btn3.config(text="List suggestions", command=lambda: suggest_movies(filter_1_1))
    btn4.pack_forget()


def filter_heartfelt_comedies():
    heartfelt_comedies = {'The Fundamentals of Caring': 78, 'The Two Popes': 89, 'Otherhood': 25, 'The Last Laugh': 53,
                          'Unicorn Store': 64, 'Dolemite Is My Name': 97, 'Like Father': 46, '#realityhigh': 40,
                          'Dumplin': 85, 'Deidra & Laney Rob a Train': 92, 'The Main Event': 28, 'Sandy Wexler': 27,
                          'The Half of It': 96, 'To All the Boys Ive Loved Before': 97,
                          'To All the Boys P.S. I Still Love You': 75, 'The Last Summer': None,
                          'Tall Girl': 44, 'Love Wedding Repeat': 31, 'Falling Inn Love': 65,
                          'Holiday in the Wild': 43}

    question(heartfelt_comedies)
    btn1.config(text="Romantic", command=lambda: filter_heartfelt_romantic_comedies(heartfelt_comedies))
    btn2.config(text="Humorous", command=lambda: filter_heartfelt_humorous_comedies(heartfelt_comedies))
    btn3.config(text="N/A", command=lambda: heartfelt_na(heartfelt_comedies))
    btn4.config(text="List suggestions", command=lambda: suggest_movies(heartfelt_comedies))
    btn5.pack_forget()


def start():
    intro.pack_forget()
    startBtn.pack_forget()
    intro1.pack(pady=(100, 0))
    intro2.pack(pady=50)
    btn1.pack()
    btn2.pack()
    btn3.pack()
    btn4.pack()
    btn5.pack()

def all_children (window) :
    _list = window.winfo_children()

    for item in _list :
        if item.winfo_children() :
            _list.extend(item.winfo_children())

    return _list

def suggest_movies(suggestion_list):
    widget_list = all_children(frame)
    for item in widget_list:
        item.pack_forget()

    movie_frame = LabelFrame(frame)
    movie_frame.pack(pady=50)

    for movies in suggestion_list.keys():
        movie = Label(movie_frame, text=str(movies) + ": " + str(suggestion_list[movies]), height="2", width="100", bg="#141414", fg="white")
        movie.pack()
    list = Label(frame, text="You got " + str(len(suggestion_list)) + " suggested movies", bg="#141414", fg="white")
    list.pack()

    conclusion()

def conclusion():
    lastMessage1 = Label(frame, text="For your information, numbers are 'Rotten Tomatoes' scores",  bg="#141414", fg="white")
    lastMessage2 = Label(frame, text="Have a nice movie!", bg="#141414", fg="white")
    lastMessage1.pack(pady=(50, 0))
    lastMessage2.pack(pady=50)


def question(question_list):
    intro1.config(text="You got " + str(len(question_list)) + " suggestions")
    intro2.config(text="Select most applicable genre or list suggestions.")


frame = LabelFrame(root, bg="#141414")
frame.place(relwidth=1, relheight=1)


# button lists
btn1 = Button(frame, text="Heartfelt", height="2", width="20", command=filter_heartfelt_comedies)
btn2 = Button(frame, text="Romantic", height="2", width="20", command=filter_romantic_comedies)
btn3 = Button(frame, text="Action", height="2", width="20", command=filter_action_comedies)
btn4 = Button(frame, text="Christmas", height="2", width="20", command=filter_christmas_comedies)
btn5 = Button(frame, text="NA", height="2", width="20", command=filter_na_comedies)


intro1 = Label(frame, text="I will give you Netflix Original Comedy Movie suggestion", bg="#141414", fg="white")
intro2 = Label(frame, text="Select most applicable number you like to watch.", bg="#141414", fg="white")


intro = Label(frame, text="Netflix Comedy Movie Suggestor", padx=50, pady=100, bg="#141414", fg="white")
intro.pack()

startBtn = Button(frame, text="start", padx="100", pady="50", bg="#E50914", fg="white", command=start)
startBtn.pack()



root.mainloop()




