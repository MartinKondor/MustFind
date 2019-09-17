"""
Global constants.
"""
import os
from enum import Enum

from pygame import locals as keys


class Screens(Enum):
    EXIT = 0
    LOADING = 1
    MAIN_MENU = 2
    SETTINGS = 3
    GAME = 4


VERSION = 'v0.1.0-beta'
BASE_FOLDER = os.getcwd() + '/bin/'

MAP_FOLDER = BASE_FOLDER + 'maps/'
TILESET_FOLDER = BASE_FOLDER + 'tilesets/'
IMAGE_FOLDER = BASE_FOLDER + 'images/'
SAVE_FOLDER = BASE_FOLDER + 'saves/'

WINDOW_TITLE = 'Must find (' + VERSION + ')'

# Colors: http://paletton.com/#uid=33t0u0k++SpsoZRH8+V+VvU+1p9
BG_COLOR = (0, 151, 230)
BG_COLOR_2 = (255, 186, 0)
BG_COLOR_3 = (255, 80, 29)

GRAVITY_CONST = 0.375
BASE_SPEED = 0.5

KEYBOARD = {
    keys.K_UNKNOWN: 0,
    keys.K_FIRST: 0,
    keys.K_BACKSPACE: 8,
    keys.K_TAB: 9,
    keys.K_CLEAR: 12,
    keys.K_RETURN: 13,
    keys.K_PAUSE: 19,
    keys.K_ESCAPE: 27,
    keys.K_SPACE: 32,
    keys.K_EXCLAIM: 33,
    keys.K_QUOTEDBL: 34,
    keys.K_HASH: 35,
    keys.K_DOLLAR: 36,
    keys.K_AMPERSAND: 38,
    keys.K_QUOTE: 39,
    keys.K_LEFTPAREN: 40,
    keys.K_RIGHTPAREN: 41,
    keys.K_ASTERISK: 42,
    keys.K_PLUS: 43,
    keys.K_COMMA: 44,
    keys.K_MINUS: 45,
    keys.K_PERIOD: 46,
    keys.K_SLASH: 47,
    keys.K_0: 48,
    keys.K_1: 49,
    keys.K_2: 50,
    keys.K_3: 51,
    keys.K_4: 52,
    keys.K_5: 53,
    keys.K_6: 54,
    keys.K_7: 55,
    keys.K_8: 56,
    keys.K_9: 57,
    keys.K_COLON: 58,
    keys.K_SEMICOLON: 59,
    keys.K_LESS: 60,
    keys.K_EQUALS: 61,
    keys.K_GREATER: 62,
    keys.K_QUESTION: 63,
    keys.K_AT: 64,
    keys.K_LEFTBRACKET: 91,
    keys.K_BACKSLASH: 92,
    keys.K_RIGHTBRACKET: 93,
    keys.K_CARET: 94,
    keys.K_UNDERSCORE: 95,
    keys.K_BACKQUOTE: 96,
    keys.K_a: 97,
    keys.K_b: 98,
    keys.K_c: 99,
    keys.K_d: 100,
    keys.K_e: 101,
    keys.K_f: 102,
    keys.K_g: 103,
    keys.K_h: 104,
    keys.K_i: 105,
    keys.K_j: 106,
    keys.K_k: 107,
    keys.K_l: 108,
    keys.K_m: 109,
    keys.K_n: 110,
    keys.K_o: 111,
    keys.K_p: 112,
    keys.K_q: 113,
    keys.K_r: 114,
    keys.K_s: 115,
    keys.K_t: 116,
    keys.K_u: 117,
    keys.K_v: 118,
    keys.K_w: 119,
    keys.K_x: 120,
    keys.K_y: 121,
    keys.K_z: 122,
    keys.K_DELETE: 127,
    keys.K_KP0: 256,
    keys.K_KP1: 257,
    keys.K_KP2: 258,
    keys.K_KP3: 259,
    keys.K_KP4: 260,
    keys.K_KP5: 261,
    keys.K_KP6: 262,
    keys.K_KP7: 263,
    keys.K_KP8: 264,
    keys.K_KP9: 265,
    keys.K_KP_PERIOD: 266,
    keys.K_KP_DIVIDE: 267,
    keys.K_KP_MULTIPLY: 268,
    keys.K_KP_MINUS: 269,
    keys.K_KP_PLUS: 270,
    keys.K_KP_ENTER: 271,
    keys.K_KP_EQUALS: 272,
    keys.K_UP: 273,
    keys.K_DOWN: 274,
    keys.K_RIGHT: 275,
    keys.K_LEFT: 276,
    keys.K_INSERT: 277,
    keys.K_HOME: 278,
    keys.K_END: 279,
    keys.K_PAGEUP: 280,
    keys.K_PAGEDOWN: 281,
    keys.K_F1: 282,
    keys.K_F2: 283,
    keys.K_F3: 284,
    keys.K_F4: 285,
    keys.K_F5: 286,
    keys.K_F6: 287,
    keys.K_F7: 288,
    keys.K_F8: 289,
    keys.K_F9: 290,
    keys.K_F10: 291,
    keys.K_F11: 292,
    keys.K_F12: 293,
    keys.K_F13: 294,
    keys.K_F14: 295,
    keys.K_F15: 296,
    keys.K_NUMLOCK: 300,
    keys.K_CAPSLOCK: 301,
    keys.K_SCROLLOCK: 302,
    keys.K_RSHIFT: 303,
    keys.K_LSHIFT: 304,
    keys.K_RCTRL: 305,
    keys.K_LCTRL: 306,
    keys.K_RALT: 307,
    keys.K_LALT: 308,
    keys.K_RMETA: 309,
    keys.K_LMETA: 310,
    keys.K_LSUPER: 311,
    keys.K_RSUPER: 312,
    keys.K_MODE: 313,
    keys.K_HELP: 315,
    keys.K_PRINT: 316,
    keys.K_SYSREQ: 317,
    keys.K_BREAK: 318,
    keys.K_MENU: 319,
    keys.K_POWER: 320,
    keys.K_EURO: 321,
    keys.K_LAST: 323,
}
