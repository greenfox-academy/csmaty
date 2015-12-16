from pregame_operations import *
from menu_classes import *
import os

def newgamemenu():
    newgamemenu_itemlist = [
        MenuItem('1','Start New Game', namemenu),
        MenuItem('2', 'Back to Main Menu', mainmenu.main)
        ]
    newgamemenu = Menu(newgamemenu_itemlist)
    newgamemenu.main()

def loadmenu():
    loadmenu_itemlist = [
        MenuItem('1','Choose from Saved Games', mainmenu.main),
        MenuItem('2', 'Back to Main Menu', mainmenu.main),
        ]
    loadmenu = Menu(loadmenu_itemlist)
    loadmenu.main()



def namemenu():
    hero.enter_name()
    namemenu_itemlist = [
        MenuItem('1','I would like to use a different name', hero.enter_name),
        MenuItem('2', 'Save Name and Continue', statsmenu),
        MenuItem('3', 'Save Name', mainmenu.main),
        MenuItem('4', 'Quit', mainmenu.main)
        ]
    namemenu = Menu(namemenu_itemlist)
    namemenu.main()

def statsmenu():
    hero.roll_stats()
    statsmenu_itemlist = [
        MenuItem('1','I would like to roll for new stats', hero.roll_stats),
        MenuItem('2', 'Save Stats and Continue', potion_select),
        MenuItem('3', 'Save Stats', mainmenu.main),
        MenuItem('4', 'Quit', mainmenu.main)
        ]
    statsmenu = Menu(statsmenu_itemlist)
    statsmenu.main()

def potion_select():
    print('\nSelect one potion to take with youself: \n\n')
    potionlist = [
        MenuItem('1','Potion of Health', reconsider_potion, 'Potion of Health'),
        MenuItem('2', 'Potion of Dexterity', reconsider_potion, 'Potion of Dexterity'),
        MenuItem('3', 'Potion of Luck', reconsider_potion, 'Potion of Luck'),
        MenuItem('4', 'Quit', mainmenu.main)
        ]
    potions = Menu(potionlist)
    potions.main()

def reconsider_potion(potion):
    hero.add_potion(potion)
    potionmenu_itemlist = [
        MenuItem('1','Select another potion', potion_select),
        MenuItem('2', 'Continue', begin_game_screen),
        MenuItem('3', 'Quit', mainmenu.main)
        ]
    potionmenu = Menu(potionmenu_itemlist)
    potionmenu.main()

def begin_game_screen():
    hero.display_character()
    begingamemenu_itemlist = [
        MenuItem('1','Begin Game',  round_one____fight),
        MenuItem('2', 'Save',  mainmenu.main),
        MenuItem('3', 'Quit', mainmenu.main)
        ]
    begingamemenu = Menu(begingamemenu_itemlist)
    begingamemenu.main()


def round_one____fight():
    print("Test your Sword in a test fight")
    hero.show_fight_stats()
    print('\n****')
    monster.show_enemy_fight_stats()
    fightmenu()

def fightmenu():
    fightmenu_itemlist = [
        MenuItem('1','Strike',  fight_hit),
        MenuItem('2', 'Retreat',  mainmenu.main),
        MenuItem('3', 'Quit', mainmenu.main)
        ]
    fightmenu = Menu(fightmenu_itemlist)
    fightmenu.main()


def fight_hit():
    hero.roll_for_strike_dexterity()
    monster.roll_for_strike_dexterity()
    strikemenu_itemlist = [
        MenuItem('1','Continue',  mainmenu.main),
        MenuItem('2', 'Try your Luck', mainmenu.main),
        MenuItem('3', 'Retreat', mainmenu.main),
        MenuItem('4', 'Quit', mainmenu.main)
        ]
    strikemenu = Menu(strikemenu_itemlist)
    if hero.dexterity > monster.dexterity:
        print('\n\n  You Strike!')
    else:
        print('\n\n  Unfortunately the opponent strikes')
    strikemenu.main()




mainmenu_itemlist = [
    MenuItem('1','New game', newgamemenu),
    MenuItem('2', 'Load Game', loadmenu),
    MenuItem('3', 'Exit', exit),
    MenuItem('000', 'Exit without Saving', exit)
    ]
mainmenu = Menu(mainmenu_itemlist)
