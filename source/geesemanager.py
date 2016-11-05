#!/usr/bin/python

import goose.entity as entity
import goose.clan as clan

import sys
import os
import json
import cPickle as pickle

WELCOMEMSG = '''
 ____ ____ ____ ____ ____
||G |||E |||E |||S |||E ||
||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|/__\|

   _____ _____ __  __ _    _ _            _______ ____  _____
  / ____|_   _|  \/  | |  | | |        /\|__   __/ __ \|  __ \\
 | (___   | | | \  / | |  | | |       /  \  | | | |  | | |__) |
  \___ \  | | | |\/| | |  | | |      / /\ \ | | | |  | |  _  /
  ____) |_| |_| |  | | |__| | |____ / ____ \| | | |__| | | \ \\
 |_____/|_____|_|  |_|\____/|______/_/    \_\_|  \____/|_|  \_\\
'''


def createClan(size, x, y):
    print 'Use random data? (y/n)'
    if str(raw_input('---> ')) == 'y':
        geesearray = clan.generateRandomClan(size, x, y)
        print 'Finished generating clan.'
        return clan.Clan(geesearray)
    else:
        geesearray = []
        for gooseCount in range(size):
            geesearray.append(createClanGoose(x, y))
        print 'Finished generating clan.'
        return clan.Clan(geesearray)


def createGeese(count):
    print 'Use random data? (y/n)'
    geesearray = []
    if str(raw_input('---> ')) == 'y':
        for gooseCount in range(count):
            geesearray.append(entity.generateRandomGoose())
        return geesearray
        print 'Finished generating ' + count + ' geese.'
    else:
        for gooseCount in range(count):
            geesearray.append(createGoose())
        return geesearray
        print 'Finished generating ' + count + ' geese.'


def createGoose():
    return entity.Goose(str(raw_input('name ---> ')), int(raw_input('age (d) ---> ')), int(raw_input('span (d) ---> ')), int(raw_input('health ---> ')), int(raw_input('hunger ---> ')), entity.Location(int(raw_input('X: ')), int(raw_input('Y: '))), int(raw_input('gender ---> ')), int(raw_input('range ---> ')))


def createClanGoose(x, y):
    return entity.Goose(str(raw_input('name ---> ')), int(raw_input('age (d) ---> ')), int(raw_input('span (d) ---> ')), int(raw_input('health ---> ')), int(raw_input('hunger ---> ')), entity.Location(x, y), int(raw_input('gender ---> ')), int(raw_input('range ---> ')))


def exit():
    print '*quack*'
    print 'The geese will find you!'
    sys.exit()


def clear():
    for i in range(100):
        print
    return


def export(obj, file):
    if mode == 0:
        pickle.dump(obj, open(file, 'wb'))
    elif mode == 1:
        print 'We have no support for JSON, woops!'
    else:
        print 'Wrong mode. Try 0 (pkl) or 1 (json).'


if __name__ == '__main__':
    print WELCOMEMSG
    while(True):
        exec(str(raw_input('>_ ')))