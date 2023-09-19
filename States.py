import pygame
from Entities import Player
from WorldTypes import Screen
from Debugging import MapEditor

class State:
    def __init__(self):
        pass
    def update(dt, events):
        pass
    def draw(surface):
        pass

class GameplayState(State):
    def __init__(self):
        super().__init__()

        self.player = Player()
        self.screen = Screen((0, 0))

        self.isEditMode = True
        self.map_editor = MapEditor(self.screen)

    def update(self, dt, events):
        self.screen.update(dt, events)
        
        if self.isEditMode:
            self.map_editor.update(dt, events)
            return
        
        self.player.update(dt, events)
    
    def draw(self, surface):
        self.screen.draw(surface)

        if self.isEditMode:
            self.map_editor.render(surface)
            return
    
        self.player.draw(surface)