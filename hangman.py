#"Виселица - gallows, hangman"
import random
HANGMAN = (
    #отвратительно огромный кортеж
    '''
    -------
    |     |
    |     
    |   
    |     
    |    
    |    
    ''',
    '''
    -------
    |     |
    |     o
    |   
    |    
    |    
    |    
    ''',
    '''
    -------
    |     |
    |     o
    |   \-+-/
    |    
    |    
    |    
    ''',
    '''
    -------
    |     |
    |     o
    |   \-+-/
    |     |
    |    
    |    
    ''',
    '''
    -------
    |     |
    |     o
    |   \-+-/
    |     |
    |    | |
    |    
    ''',
    '''
    -------
    |     |
    |     o
    |   \-+-/
    |     |
    |    | |
    |    | |
    '''
    )
MAX_WRONG = len(HANGMAN) - 1 #макс. число возможных ошибок (6-1=5)
WORDS = ("HELLO", "WORLD", "PYTHON", "TORCH", "ROTTEN", "PINEAPPLE") #загаданные слова
word = random.choice(WORDS) #выбор одного значения из кортежа со словами
so_far = "-" * len(word) #заменяем последовательность символов переменной world "-"
wrong = 0 #количество ошибок
used = [] #список для уже использованных букв
print ("Welcome to the game")
print(MAX_WRONG)
while wrong < MAX_WRONG and so_far != word: #пока ошибок <= 5 и отгаданное слово не равно загаданному
    print(HANGMAN[wrong]) #вывод позиции из кортежа Hangman (0-1-2-3-4-5)
    print("Вы уже предлагали: ", used) #вывод уже использованных букв
    print("Состояние слова: ", so_far) #вывод отгаданых букв/слова
    quess = input("Введите букву: ") #получение ввода
    quess = quess.upper() #приравнивание к верх. регистру
    while quess in used: #пока ввод находится в списке used
        quess = input("Уже было. Введите другую букву: ") #требовать другую букыву
        quess = quess.upper()
    used.append(quess) #добавить ввод к списку used
    if quess in word: #проверка нахождения буквы в слове
        print("Да, буква", quess, "есть в слове! =)")
        new = ""
        for i in range(len(word)): #i принимает значения последовательности из индесов слова в переменной world
            if quess == word[i]:   #проверка наличиия буквы в слове по индексу
                new += quess #к переменной new прибавить значение quess
            else:
                new += so_far[i] #иначе (если буква не содержится) к переменной new добавить значение so_far по индексу
        so_far = new #обновить so_far. Цикл выполняется столько раз, сколько индексов есть в загадоном слове, в результате формируется новая последовательность.
    else:
        print("Такой буквы нет =(")
        wrong += 1
    print ("У вас ещё ", MAX_WRONG - wrong, "попыток")
if wrong >= MAX_WRONG: #почему-то не работает
    print(HANGMAN[wrong])
    print("Game over")
else:
    print("You win!")
    print("Было загадано слово", word)# Quess-the-word
