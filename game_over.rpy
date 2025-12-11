#============================================================
# GAME OVER
#============================================================

label game_over_maximo:
    pause 1.5
    play sound "heartbeat.mp3"
    $ renpy.pause(4.0, hard=True)
    play sound "jumpscare.mp3" volume 1.0
    scene jumpscare_max
    with vpunch
    pause 1.0
    show gameover_txt at truecenter with dissolve
    $ renpy.pause(5.75, hard=True)
    scene black with dissolve
    menu:
        "Retry First Shift":
            $ renpy.load("day2_checkpoint")
        "Main Menu":
            $ renpy.full_restart()
    return

label game_over_ysabel:
    pause 1.5
    play sound "heartbeat.mp3"
    $ renpy.pause(4.0, hard=True)
    play sound "jumpscare.mp3" volume 1.0
    scene jumpscare_ysa
    with vpunch
    pause 1.0
    show gameover_txt at truecenter with dissolve
    $ renpy.pause(5.75, hard=True)
    scene black with dissolve
    menu:
        "Retry Second Shift":
            $ renpy.load("day3_checkpoint")
        "Main Menu":
            $ renpy.full_restart()

    return

label game_over_dawani:
    pause 1.5
    play sound "heartbeat.mp3"
    $ renpy.pause(4.0, hard=True)
    play sound "jumpscare.mp3" volume 1.0
    scene jumpscare_daw
    with vpunch
    pause 1.0
    show gameover_txt at truecenter with dissolve
    $ renpy.pause(5.75, hard=True)
    scene black with dissolve
    menu:
        "Retry Third Shift":
            $ renpy.load("day4_checkpoint")
        "Main Menu":
            $ renpy.full_restart()

    return