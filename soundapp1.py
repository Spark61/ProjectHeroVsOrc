from pygame import mixer

# Starting the mixer
mixer.init()

# Loading the song
mixer.music.load("smd/Messersmith.mp3")

# Setting the volume
mixer.music.set_volume(0.7)


def startPlay(mixer):
    mixer.music.play()


def resumePlay(mixer):
    mixer.music.unpause()


def pausePlay(mixer):
    mixer.music.pause()


def optionsPlay(mixer):
    pass


def mediumPlay(mixer):
    mixer.music.set_volume(0.5)


startPlay(mixer)

# infinite loop
while True:

    print("Press 'p' to pause, 'r' to resume")
    print("Press 'e' to exit the program")
    query = input("  ")

    if query == 'p':

        # Pausing the music
        pausePlay(mixer)
    elif query == 'r':

        # Resuming the music
        resumePlay(mixer)
    elif query == 'o':

        # Resuming the music
        optionsPlay(mixer)
    elif query == 'm':

        # Resuming the music
        mediumPlay(mixer)
    elif query == 'e':

        # Stop the mixer
        mixer.music.stop()
        break
