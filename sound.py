from pygame import mixer

def sound_init():
    mixer.init()

def play_sfx(track, loops=0, channel=1, volume=1):
    chn = mixer.Channel(channel)
    # track_full = "data/sounds/" + str(track) + ".ogg"
    snd = track
    chn.set_volume(volume)
    chn.play(snd, loops)
