import keyboard
from sound import *

def main():
    sound_init()
    snd_key = mixer.Sound("keystroke.ogg")
    snd_newline = mixer.Sound("newline.ogg")

    disabled_keys = ["up", "down", "left", "right", "backspace"]

    print("\nTypewriter initialized.")
    print("\nDisabled keys:")
    for i in disabled_keys:
        print(i)

    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            if keyboard.is_pressed("enter"):
                play_sfx(snd_newline)
            elif keyboard.read_key() in disabled_keys:
                pass
            else:
                play_sfx(snd_key)

main()
