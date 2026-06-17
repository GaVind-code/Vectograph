import board 

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scaners import DiodeOrientation
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.encoder import EmcoderHandler
from kmk.extensions.RGB import RGB

emcoder_handler = EmcoderHandler()

keyboard = KMKKeyboard()
keyboard.extensions.append(MediaKeys())

keyboard.modules = [emcoder_handler]

COL0 = board.D10
COL1 = board.D9
COL2 = board.D8
COL3 = board.D7
ROW0 = board.D3
ROW1 = board.D6

col_pins = (COL0, COL1, COL2, COL3)
row_pins = (ROW0, ROW1)

keyboard.col_pins = col_pins
keyboard.row_pins = row_pins
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [
        KC.MUTE, KC.VOLD, VOLU, KC.MUTE,
        KC.MRWD, KC.MPLY, KC.MFFD, KC.NO,
    ],
]

emcoder_handler.pins = (
    (board.D1, board.D2, None,),
)

emcoder_handler.map = [
    (
        (KC.VOLD, KC.VOLU, KC.NO),
    ),
]

rgb = RGB(pixel_pin=board.D0, num_pixels=10)
keybroad.extensions.append(rgb)