import pygame,time

class Music:

    music_enabled=True
    sound_enabled=True
    music_position_menu=0
    music_position_game=0
    music_location="music/default/"
    default_music_location="music/default/"

    def __init__(self):
        pygame.mixer.pre_init(44100, -16, 4, 2048)
        pygame.mixer.init()
        pygame.mixer.music.set_volume(0.2)
        pygame.init()

    def load_music_pack(self,location):
        self.music_location=location+"/"

    def play_music(self,filename,times=-1):
        if self.music_enabled==True:
            try:
                pygame.mixer.music.load(self.music_location+filename)
                pygame.mixer.music.play(times)
            except pygame.error:
                pygame.mixer.music.load(self.default_music_location+filename)
                pygame.mixer.music.play(times)


    def pause_music(self):
        pygame.mixer.music.pause()

    def reset(self):
        self.music_position_menu=0
        self.music_position_game=0

    def stop_remember(self,game_location):
        if game_location=="Menu":
            self.music_position_menu=pygame.mixer.music.get_pos()


        if game_location=="Game":
            self.music_position_game=pygame.mixer.music.get_pos()

        pygame.mixer.music.stop()

    def play_remember(self,game_location):
        if self.music_enabled:
            try:
                if game_location=="Menu":
                    pygame.mixer.music.load(self.music_location+ "menu_music.ogg")
                    #pygame.mixer.music.set_pos(self.music_position_menu)
                    pygame.mixer.music.play(-1,self.music_position_menu/1000)
                if game_location=="Game":
                    pygame.mixer.music.load(self.music_location+ "game_music.ogg")
                    #pygame.mixer.music.set_pos(self.music_position_game)
                    pygame.mixer.music.play(-1,self.music_position_game/1000)
            except pygame.error:
                if game_location=="Menu":
                    pygame.mixer.music.load(self.default_music_location+ "menu_music.ogg")
                    #pygame.mixer.music.set_pos(self.music_position_menu)
                    pygame.mixer.music.play(-1,self.music_position_menu/1000)
                if game_location=="Game":
                    pygame.mixer.music.load(self.default_music_location+ "game_music.ogg")
                    #pygame.mixer.music.set_pos(self.music_position_game)
                    pygame.mixer.music.play(-1,self.music_position_game/1000)


    def unpause_music(self):
        pygame.mixer.music.unpause()

    def stop_music(self):
        pygame.mixer.music.stop()

    def change_volume(self,value):
        pygame.mixes.music.set_volume(value)


    def play_sound(self,filename,canal=0):

        if self.sound_enabled==True:
            try:
                pygame.mixer.Channel(canal).play(pygame.mixer.Sound(self.music_location+filename))
            except pygame.error:
                pygame.mixer.Channel(canal).play(pygame.mixer.Sound(self.default_music_location+filename))
            
    def enable_music(self,bool):
        self.music_enabled=bool

    def switch_sound(self):
        if self.sound_enabled==True:
            self.sound_enabled=False
        else:
            self.sound_enabled=True
            #self.play_file("music/music_on.ogg")
    def switch_music(self):
        if self.music_enabled==True:
            self.stop_remember("Menu")
            self.music_enabled=False
        else:
            self.music_enabled=True
            self.play_remember("Menu")
            #self.play_file("music/music_on.ogg")