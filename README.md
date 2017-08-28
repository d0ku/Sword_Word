# Sword_Word
Typing training program (game), to be used in terminal

Aim of this program is to help you develop keyboard typing skill, without looking at keys

It's just a simple training program, i plan to add training modes in future



HOW TO RUN:

Clone this repo or download as zip, unpack and run "python3 Run.py" in root folder

In order to run this program you have to install pygame:

To do so run in console "pip install pygame", if it doesn't work after this try "pip3 install pygame"

INFO:

Supported languages:

- Polish

- English

Program is in its alpha stage, everything should work like it should (except Game Options). Feel free to contact me, if you have some ideas or questions.

Dictionaries, Languages and Sound Packs are designed to be modular, you can create new folder in specified places, add files which fullfill naming conventions, and load packs in the game,

I will add further info for this in the future.

Supported text formats is UTF-8

That's the first project ever finished by me so be nice :D

Currently works as it should only on UNIX systems.

TODO:

- add Game Options Menu positions

- improve input in Game.py class (change timeouted getch to something better)

- add (create) game modes

- fullfill documentation  -> First created in Alpha 1.0.1.doc, needs to be written though

- create full license/credits list

- change lists into dictionaries in Languages.py and its childrens

- load default english word, if word in chosen language cannot be loaded  -> Done in Alpha 1.0.1

- create sound loading in folder mode (easier music packs making), add menu entry for soundpacks, auto load default music if chosen pack can't be opened  -> Done in Alpha 1.0.2

- configuration files (save at exit, load at startup)

- first time game run, run language choose, display license and help

- CLEAN AND RETHINK SOME PIECES OF CODE

- Add Windows compability (Getch module timeout)  Getch timeout functionality provided in Alpha 1.0.3


LICENSE:

You can check the whole license and/or credits in licenses/full_license.txt

Simple credits are available in program under Credits menu entry.


CHANGELOG:

27 of August 2017 - Alpha and initial release 

27 of August 2017 - Alpha 1.0.1

	- load default english word, if word in chosen language cannot be loaded

27 of August 2017 - Alpha 1.0.1.doc

	- documentation created(Sphinx), needs to be fullfilled

28 of August 2017 - Alpha 1.0.2

	- sound loading module style, added Sound Packs options in menu

28 of August 2017 - Alpha 1.0.3

	- Getch timeout for Windows implemented

	- Basic Windows support added, colors in terminal are not supported, it has some bugs, and those probably won't be corrected till Beta release

	- time flow changed in Game.py (now game.timeout is real time beetwen words moves)

	- added linear read option in Language.py (useful if you want to add e.g. a book , the words will be loaded one after another into game)

	- some functions added to Game.py (basis of future game modes)
