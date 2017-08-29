import os,time,itertools

class Language:
    credits=[]
    game=[]
    help_text=[]
    menu=[]
    location=None
    default_location="languages/English"

    def __init__(self):
        
        self.load_default_words(self.default_location)
        self.load_language()

    def load_default_words(self,location):
        self.location=location
        ##self.clean_list(self.credits)
        #self.clean_list(self.game)
        #self.clean_list(self.help_text)
        #self.clean_list(self.menu)

        self.credits_backup=[]
        self.game_backup=[]
        self.help_text_backup=[]
        self.menu_backup=[]
        
        #self.credits=[]
        #self.game=[]
        #self.help=[]
        #self.menu=[]
        with open(location+"/credits.txt","r") as temp:
            self.credits_backup+=temp.read().split("\n")
        with open(location+"/game.txt","r") as temp:
            self.game_backup+=temp.read().split("\n")
        with open(location+"/help.txt","r") as temp:
            self.help_text_backup+=temp.read().split("\n")
        with open(location+"/menu.txt","r") as temp:
            self.menu_backup+=temp.read().split("\n")

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
        for x,y in itertools.zip_longest(temp,self.menu_backup):
            if x!=None:
                self.menu.append(Word(x,self,self.menu,i))
                self.menu.remove(x)
            else:
                self.menu.append(Word(y,self,self.menu_backup,i))
            i+=1

        temp=self.game[:]
        i=0
        for x,y in itertools.zip_longest(temp,self.game_backup):
            if x!=None:
                self.game.append(Word(x,self,self.game,i))
                self.game.remove(x)
            else:
                self.game.append(Word(y,self,self.game_backup,i))
            i+=1

        temp=self.credits[:]
        i=0
        for x,y in itertools.zip_longest(temp,self.credits_backup):
            if x!=None:
                self.credits.append(Word(x,self,self.credits,i))
                self.credits.remove(x)
            else:
                self.credits.append(Word(y,self,self.credits_backup,i))
            i+=1

        temp=self.help_text[:]
        i=0
        for x,y in itertools.zip_longest(temp,self.help_text):
            if x!=None:
                self.help_text.append(Word(x,self,self.help_text,i))
                self.help_text.remove(x)
            else:
                self.help_text.append(Word(y,self,self.help_text_backup,i))
            i+=1

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


