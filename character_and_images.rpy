###################### CHARACTERS ######################
define m = Character("Mom", color="#ffffff")
define d = Character("Diego", color="#ffffff")
define y = Character("Ysabel", color="#ffffff")
define c1m = Character("Maximo", color="#ffffff")
define c2d = Character("Dawani", color="#ffffff")

define narrate = Character(None, what_italic=True)

define unknown = Character ("???", color="#ffffff")
define cus1 = Character ("Customer 1", color="#ffffff")
define c2 = Character ("Customer 2", color="#ffffff")
define c3 = Character ("Customer 3", color="#ffffff")
########################################################

######################## IMAGES ########################

# BACKGROUNDS
image hospital = "hospital.png"
image forest = "forest_1.png"
image forest_door = "forest_2.png"
image bar_inside = "bar_inside.png"
image bar_counter = "bar_counter.png"
image bg black = Solid("#000")

# FOREGROUND
image bar_table = "bar_table.png"

# INSERT PHOTOS
image cut1 = "cutscene.png"
image cut2 = "cutscene2.png"
image cut3 = "cutscene3.png"
image hand = "hand.png"
image day1 = "d1.png"
image day2 = "d2.png"
image day3 = "d3.png"
image day4 = "d4.png"
image bottle = "bottle.png"
image lana = "lana.png"


# CUP IMAGES 
# DIEGO/TUTORIAL(DRINK 1)
init python:
    diego_drinks = [
        "images/DRINKS/DIEGO/DRINK/cup_empty.png",
        "images/DRINKS/DIEGO/DRINK/cup_1.png",
        "images/DRINKS/DIEGO/DRINK/cup_2.png",
        "images/DRINKS/DIEGO/DRINK/cup_3.png"
    ]

#  MAXIMO (DRINK 2)
init python:
    maximo_drinks = [
        "images/DRINKS/MAXIMO/DRINK/m_glass_0.png",
        "images/DRINKS/MAXIMO/DRINK/m_glass_1.png",
        "images/DRINKS/MAXIMO/DRINK/m_glass_2.png",
        "images/DRINKS/MAXIMO/DRINK/m_glass_3.png"
    ]

#  YSABEL (DRINK 3)
init python:
    ysabel_drinks = [
        "images/DRINKS/YSABEL/DRINK/y_glass_0.png",
        "images/DRINKS/YSABEL/DRINK/y_glass_1.png",
        "images/DRINKS/YSABEL/DRINK/y_glass_2.png",
        "images/DRINKS/YSABEL/DRINK/y_glass_3.png"
    ]

# DAWANI (DRINK 4)
init python:
    dawani_drinks = [
        "images/DRINKS/DAWANI/DRINK/glass_0.png",
        "images/DRINKS/DAWANI/DRINK/glass_1.png",
        "images/DRINKS/DAWANI/DRINK/glass_2.png",
        "images/DRINKS/DAWANI/DRINK/glass_3.png"
    ]

# LIFE/HEART IMAGES
image heart_full = "images/heart_full.png"
image heart_empty = "images/heart_empty.png"

# JUMPSCARE/GAME OVER IMAGES
image jumpscare_max = "images/MAXIMO/1_jumpscare.png"
image jumpscare_ysa = "images/YSABEL/2_jumpscare.png"
image jumpscare_daw = "images/DAWANI/3_jumpscare.png"
image gameover_txt = "images/game_over.png"

####################### SPRITE #########################

# DIEGO
image dieg_shadow = "images/DIEGO/diego_shadow.png"
image dieg_default = "images/DIEGO/diego_default.png"
image dieg_close_eye = "images/DIEGO/diego_default-closedeyes.png"
image dieg_open_mouth = "images/DIEGO/diego_default-mouthopen.png"
image dieg_laugh = "images/DIEGO/diego_diego_laugh.png"
image dieg_serious = "images/DIEGO/diego_serious.png"
image dieg_serious_open = "images/DIEGO/diego_serious-mouthopen.png"

#MAXIMO
image maximo_default = "images/MAXIMO/maximo_default.png"
image maximo_defopen = "images/MAXIMO/maximo_default-mouthopen.png"
image maximo_annoyed = "images/MAXIMO/maximo_annoyed.png"
image maximo_annoyedopen = "images/MAXIMO/maximo_annoyed-mouthopen.png"
image maximo_blush = "images/MAXIMO/maximo_blush.png"
image maximo_blushopen = "images/MAXIMO/maximo_blush-mouthopen.png"
image maximo_smileblush = "images/MAXIMO/maximo_smileblush.png"
image maximo_smileblushopen = "images/MAXIMO/maximo_smileblush-mouthopen.png"
image maximo_soft = "images/MAXIMO/maximo_soft.png"
image maximo_softopen = "images/MAXIMO/maximo_soft-mouthopen.png"
image maximo_glitch = "images/MAXIMO/maximo_glitch.png"
image maximo_nervous = "images/MAXIMO/maximo_nervous.png"

#YSABEL
image ysa_default = "images/YSABEL/ysabel_default.png"
image ysa_defopen = "images/YSABEL/ysabel_default-mouthopen.png"
image ysa_annoyed = "images/YSABEL/ysabel_annoyed.png"
image ysa_annoyedopen = "images/YSABEL/ysabel_annoyed-mouthopen.png"
image ysa_mad = "images/YSABEL/ysabel_annoyed2.png"
image ysa_madopen = "images/YSABEL/ysabel_annoyed2-mouthopen.png"
image ysa_sad = "images/YSABEL/ysabel_sad.png"
image ysa_sadopen = "images/YSABEL/ysabel_sad-mouthopen.png"
image ysa_red = "images/YSABEL/ysabel_red.png"
image ysa_redopen = "images/YSABEL/ysabel_red-mouthopen.png"
image ysa_glitch_pic = "images/YSABEL/ysabel_glitch.png"

#DAWANI
image daw_default = "images/DAWANI/dawani_default.png"
image daw_defopen = "images/DAWANI/dawani_default-mouthopen.png"
image daw_annoyed = "images/DAWANI/dawani_annoyed.png"
image daw_annoyedopen = "images/DAWANI/dawani_annoyed-mouthopen.png"
image daw_mad = "images/DAWANI/dawani_annoyed2.png"
image daw_madopen = "images/DAWANI/dawani_annoyed2-mouth open.png"
image daw_sad = "images/DAWANI/dawani_sad.png"
image daw_sadopen = "images/DAWANI/dawani_sad-mouthopen.png"
image daw_happy = "images/DAWANI/dawani_happy.png"
image daw_happyopen = "images/DAWANI/dawani_happy-mouthopen.png"
image daw_glitch = "images/DAWANI/dawani_glitch1.png"
image daw_glitch = "images/DAWANI/dawani_glitch2.png"
#########################################################

################### IMAGE ANIMATION #####################

#DIEGO
image dieg_talk_normal:
    "images/DIEGO/diego_default.png"
    0.2
    "images/DIEGO/diego_default-mouthopen.png"
    0.2
    repeat
image dieg_serious_talk:
    "images/DIEGO/diego_serious.png"
    0.2
    "images/DIEGO/diego_serious-mouthopen.png"
    0.2
    repeat
image dieg_laugh_talk:
    "images/DIEGO/diego_laugh.png"
    0.2
    "images/DIEGO/diego_default-closedeyes.png"
    0.2
    repeat

#MAXIMO
image max_talk_normal:
    "images/MAXIMO/maximo_default.png"
    0.2
    "images/MAXIMO/maximo_default-mouthopen.png"
    0.2
    repeat
image max_talk_soft:
    "images/MAXIMO/maximo_soft.png"
    0.2
    "images/MAXIMO/maximo_soft-mouthopen.png"
    0.2
    repeat
image max_talk_blush:
    "images/MAXIMO/maximo_blush.png"
    0.2
    "images/MAXIMO/maximo_blush-mouthopen.png"
    0.2
    repeat
image max_talk_smileblush:
    "images/MAXIMO/maximo_smileblush.png"
    0.2
    "images/MAXIMO/maximo_smileblush-mouthopen.png"
    0.2
    repeat
image max_talk_mad:
    "images/MAXIMO/maximo_annoyed.png"
    0.2
    "images/MAXIMO/maximo_annoyed-mouthopen.png"
    0.2
    repeat

#YSABEL
image ysa_talk_def:
    "images/YSABEL/ysabel_default-mouthopen.png"
    0.2
    "images/YSABEL/ysabel_default.png"
    0.2
    repeat
image ysa_talk_annoy:
    "images/YSABEL/ysabel_annoyed-mouthopen.png"
    0.2
    "images/YSABEL/ysabel_annoyed.png"
    0.2
    repeat
image ysa_talk_mad:
    "images/YSABEL/ysabel_annoyed2-mouthopen.png"
    0.2
    "images/YSABEL/ysabel_annoyed2.png"
    0.2
    repeat
image ysa_talk_sad:
    "images/YSABEL/ysabel_sad-mouthopen.png"
    0.2
    "images/YSABEL/ysabel_sad.png"
    0.2
    repeat
image ysa_talk_red:
    "images/YSABEL/ysabel_red-mouthopen.png"
    0.2
    "images/YSABEL/ysabel_red.png"
    0.2
    repeat

#DAWANI
image daw_talk_def:
    "images/DAWANI/dawani_default-mouthopen.png"
    0.2
    "images/DAWANI/dawani_default.png"
    0.2
    repeat
image daw_talk_annoy:
    "images/DAWANI/dawani_annoyed-mouthopen.png"
    0.2
    "images/DAWANI/dawani_annoyed.png"
    0.2
    repeat
image daw_talk_mad:
    "images/DAWANI/dawani_annoyed2-mouth open.png"
    0.2
    "images/DAWANI/dawani_annoyed2.png"
    0.2
    repeat
image daw_talk_sad:
    "images/DAWANI/dawani_sad-mouthopen.png"
    0.2
    "images/DAWANI/dawani_sad.png"
    0.2
    repeat
image daw_talk_happy:
    "images/DAWANI/dawani_happy-mouthopen.png"
    0.2
    "images/DAWANI/dawani_happy.png"
    0.2
    repeat
#########################################################


#IMAGE TRANSFORM
transform SPRITE1_pos:
    xpos 0.1      # Horizontal position (0.0 = far left, 1.0 = far right)
    ypos 1.0        # Vertical position relative to screen
    xanchor 0.0     # Align sprite from left edge
    yanchor 1.0     # Align sprite from bottom

transform SPRITE2_pos:
    xpos 0.6     # Horizontal position (0.0 = far left, 1.0 = far right)
    ypos 1.0        # Vertical position relative to screen
    xanchor 0.0     # Align sprite from left edge
    yanchor 1.0     # Align sprite from bottom

transform drink_pos:
    xpos 0.667      # Horizontal position (0.0 = far left, 1.0 = far right)
    ypos 0.84        # Vertical position relative to screen
    xanchor 0.0     # Align sprite from left edge
    yanchor 1.0     # Align sprite from bottom
    zoom 0.64

transform drink_pos1:
    xpos 0.4     # Horizontal position (0.0 = far left, 1.0 = far right)
    ypos 0.84        # Vertical position relative to screen
    xanchor 0.0     # Align sprite from left edge
    yanchor 1.0     # Align sprite from bottom
    zoom 0.64

transform bottle_pos:
    xpos 0.0    # Horizontal position (0.0 = far left, 1.0 = far right)
    ypos 1.0        # Vertical position relative to screen
    xanchor 0.0     # Align sprite from left edge
    yanchor 1.0     # Align sprite from bottom
