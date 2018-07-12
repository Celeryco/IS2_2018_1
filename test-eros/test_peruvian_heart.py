import os
import pygame as pg
from data import tools, settings
from data.libraries import button, input
from data.models import player, character, bomb, map, wall, powerup, enemy, obstacle
from data.views import character_view, bomb_view, fire_view, map_view, wall_view, powerup_view, enemy_view

def setup_module(module):
    global map

    pg.init()
    os.environ['SDL_VIDEO_CENTERED'] = "TRUE"
    pg.display.set_caption("prueba")
    SCREEN = pg.display.set_mode((800, 640))

    game_folder = os.path.dirname(__file__)
    #self.map = map_view.MapView(path.join(game_folder, 'map.txt'))
    map_folder = os.path.join(game_folder,'maps') #
    map = map_view.TiledMap(os.path.join(map_folder, 'tiles1-bomberman.tmx')) #

def test_get_mapdata():
    inst = isinstance(map, map_view.TiledMap)
    assert inst

def test_get_GFX():
    GFX = tools.load_all_gfx(os.path.join("resources", "graphics"))
    conditional = True
    for index, value in GFX.items():
        pic = isinstance(value, pg.Surface)
        if not pic:
            conditional = False
    assert conditional

def test_get_music():
    GFX = tools.load_all_music(os.path.join("resources", "music"))
    conditional = True
    suffix = ".wav";
    for index, value in GFX.items():
        iswav = value.endswith(suffix)
        if not iswav:
            conditional = False
    assert conditional

def test_get_fonts():
    FONTS = tools.load_all_fonts(os.path.join("resources", "fonts"))
    conditional = True
    suffix = ".ttf";
    for index, value in FONTS.items():
        correct_font = value.endswith(suffix)
        if not correct_font:
            conditional = False
    assert conditional

def test_map_characters():
    conditional = True
    for tile_object in map.tmxdata.objects: #
        if tile_object.name == 'player':   #
            charac = character.Character(settings.GFX['quintana'], settings.SFX['death_sound'])
            ischara = isinstance(charac, character.Character)
            if not ischara:
                conditional = False
    assert conditional

def test_map_objects():
    conditional = True
    for tile_object in map.tmxdata.objects: #
        if tile_object.name == 'roca' : #
            obst = obstacle.Obstacle(tile_object.name) #
        isobstacle = isinstance(obst, obstacle.Obstacle)
        if not isobstacle:
            conditional = False
    assert conditional

def test_map_powerups():
    conditional = True
    for tile_object in map.tmxdata.objects: #
        if tile_object.name == 'fire':   #
            powerup_model = powerup.Powerup(settings.GFX['fire-up'], "fire", 1)
            ispower = isinstance(powerup_model, powerup.Powerup)
            if not power:
                conditional = False
    assert conditional

def test_map_enemy():
    conditional = True
    for tile_object in map.tmxdata.objects: #
        if tile_object.name == 'enemigo':   #
            enemy_model = enemy.Enemy(settings.GFX['inca'])
            isenemy = isinstance(enemy_model, enemy.Enemy)
            if not isenemy:
                conditional = False
    assert conditional

def test_library_button():
    button_model = button.Button("boton", 10, 10, 50, 20, 5, 2, 2)
    isbutton = isinstance(button_model, button.Button)
    assert isbutton

def test_library_input():
    input_model = input.Input("Input", 30, 30, 30, 30, 10, 4, 3, 10)
    isinput = isinstance(input_model, input.Input)
    assert isinput
