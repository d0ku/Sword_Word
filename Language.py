import os,time

class Language:
    credits=[]
    game=[]
    help_text=[]
    menu=[]
    location=None

    def __init__(self):
        self.load_language()

    def convert_to_Word(self,list):
        for x in list:
            x=Word(x)
    def load_language(self,location="languages/English"):
        self.location=location
        ##self.clean_list(self.credits)
        #self.clean_list(self.game)
        #self.clean_list(self.help_text)
        #self.clean_list(self.menu)

        temp=self.menu[:]
        for x in temp:
            self.menu.remove(x)

        temp=self.credits[:]
        for x in temp:
            self.credits.remove(x)

        temp=self.game[:]
        for x in temp:
            self.game.remove(x)

        temp=self.help_text[:]
        for x in temp:
            self.help_text.remove(x)
        #self.credits=[]
        #self.game=[]
        #self.help=[]
        #self.menu=[]
        with open(location+"/credits.txt","r") as temp:
            self.credits+=temp.read().split("\n")
        with open(location+"/game.txt","r") as temp:
            self.game+=temp.read().split("\n")
        with open(location+"/help.txt","r") as temp:
            self.help_text+=temp.read().split("\n")
        with open(location+"/menu.txt","r") as temp:
            self.menu+=temp.read().split("\n")

        temp=self.menu[:]
        i=0
        for x in temp:
            self.menu.append(Word(x,self,self.menu,i))
            self.menu.remove(x)
            i+=1

        temp=self.game[:]
        i=0
        for x in temp:
            self.game.append(Word(x,self,self.game,i))
            self.game.remove(x)
            i+=1

        temp=self.credits[:]
        i=0
        for x in temp:
            self.credits.append(Word(x,self,self.credits,i))
            self.credits.remove(x)
            i+=1

        temp=self.help_text[:]
        i=0
        for x in temp:
            self.help_text.append(Word(x,self,self.help_text,i))
            self.help_text.remove(x)
            i+=1


        #self.credits=list(map(lambda x: Word(x),self.credits))
        #self.game=list(map(lambda x: Word(x),self.game))
        #self.help_text=list(map(lambda x: Word(x),self.help_text))
        #self.menu=list(map(lambda x: Word(x),self.menu))
        #for x in self.menu:
        #    print(x.word)

class Word:
    word=""
    index=0


    def __init__(self,word,parent,category,index):
        self.word=word
        self.parent=parent
        self.category=category
        self.index=index

    def update(self):
        self.word=str(self.category[self.index])

    def __str__(self):
        return self.word


