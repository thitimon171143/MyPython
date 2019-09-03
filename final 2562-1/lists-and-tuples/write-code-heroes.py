heroes_1 = ['Ironman','Thor','Hulk','Superman','Spiderman']

def main():
    again = 'y'
    while again == 'y' or again == 'Y' :
        print(' 1.Display','\n','2.AddHeroes','\n','3.InsertHeroes','\n','4.RemoveHeroes','\n','5.DisplaySortedHeoroes_Ascending','\n')
        choose = input('Choose function : ')
        if choose == '1' :
            DisplayHeroes()
        elif choose == '2' :
            AddHeroes()
        elif choose == '3' :
            InsertHeroes()
        elif choose == '4' :
            RemoveHeroes()
        elif choose == '5' :
            DisplaySortedHeoroes_A()
        else :
            print('ERROR')
        again = input('Do you want try again ? : ')

def DisplayHeroes():
    global heroes_1
    print('---Display---')
    for i in heroes_1:
        print(i)

def AddHeroes():
    global heroes_1
    print('---AddHeroes---')
    new_heroes = input('Enter your sentence : ')
    heroes_1.append(new_heroes)
    print(heroes_1)

def InsertHeroes():
    global heroes_1
    print('---InsertHeroes---')
    heroes = input('Enter heroes : ')
    new_heroes = input('Enter your new heroes : ')
    heroes_1.insert(heroes_1.index(heroes),new_heroes)
    print(heroes_1)

def RemoveHeroes():
    global heroes_1
    print('---RemoveHeroes---')
    new_heroes = input('Enter your sentence : ')
    heroes_1.remove(new_heroes)
    print(heroes_1)

def DisplaySortedHeoroes_A():
    global heroes_1
    print('---DisplaySortedHeoroes_Ascending---')
    heroes_1.sort()
    print(heroes_1)

main()