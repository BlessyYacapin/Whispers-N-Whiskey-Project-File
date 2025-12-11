#============================================================
# GLITCH LABEL
#============================================================

label maximo_glitch:
    image maximo_glitched:
        glitch("images/MAXIMO/maximo_annoyed.png", offset=60)
        pause 0.1
        glitch("images/MAXIMO/maximo_annoyed.png", offset=20, chroma=True)
        pause 0.07
        glitch("images/MAXIMO/maximo_glitch.png", offset=30)
        pause 0.1
        glitch("images/MAXIMO/maximo_annoyed.png", offset=80, chroma=True)
        pause 0.07
        glitch("images/MAXIMO/maximo_annoyed.png", offset=40)
        pause 0.1
        glitch("images/MAXIMO/maximo_glitch.png", offset=20, chroma=True)
        pause 0.07
        repeat
    show maximo_glitched with hpunch
    pause 1.3
    hide maximo_glitched

label ysabel_glitch:
    image ysabel_glitched:
        glitch("images/YSABEL/ysabel_red.png", offset=60)
        pause 0.1
        glitch("images/YSABEL/ysabel_red.png", offset=20, chroma=True)
        pause 0.07
        glitch("images/YSABEL/ysabel_glitch.png", offset=30)
        pause 0.1
        glitch("images/YSABEL/ysabel_red.png", offset=80, chroma=True)
        pause 0.07
        glitch("images/YSABEL/ysabel_red.png", offset=40)
        pause 0.1
        glitch("images/YSABEL/ysabel_red.png", offset=20, chroma=True)
        pause 0.07
        repeat
    show ysabel_glitched with hpunch
    pause 1.3
    hide ysabel_glitched

label dawani_glitch:
    image dawani_glitched:
        glitch("images/DAWANI/dawani_annoyed2.png", offset=60)
        pause 0.1
        glitch("images/DAWANI/dawani_annoyed2.png", offset=20, chroma=True)
        pause 0.07
        glitch("images/DAWANI/dawani_glitch.png", offset=30)
        pause 0.1
        glitch("images/DAWANI/dawani_annoyed2.png", offset=80, chroma=True)
        pause 0.07
        glitch("images/DAWANI/dawani_annoyed2.png", offset=40)
        pause 0.1
        glitch("images/DAWANI/dawani_glitch2.png", offset=20, chroma=True)
        pause 0.07
        repeat
    show dawani_glitched with hpunch
    pause 1.3
    hide dawani_glitched