########### SCREENS ###########
            
######### PULANG KABAYO #########
default cup_stage_1 = 0

screen beer_button:
                
    add maximo_drinks[cup_stage_1] xpos 0.37 ypos 0.3

    $ tip = GetTooltip()
    if tip:
        text tip xcenter 0.678 ypos 90 size 40 font "Belgan Aesthetic.ttf" color "#ffffff"
                
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.7
        ypos 0.5
    
        tooltip "Beer"
        auto "images/DRINKS/MAXIMO/INGREDIENT/ingredient1_%s.png" #covers idle, hover, selected etc
        action SetVariable("cup_stage_1", cup_stage_1 + 1), [Hide("beer_button"), Return("beer_done")]

######### HONEY #########
screen matcha_button:
    add maximo_drinks[cup_stage_1] xpos 0.37 ypos 0.3

    $ tip = GetTooltip()
                
    if tip:
        text tip xcenter 0.725 ypos 520 size 40 font "Belgan Aesthetic.ttf" color "#ffffff"
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.7
        ypos 0.72

        tooltip "Matcha"
        auto "images/DRINKS/MAXIMO/INGREDIENT/ingredient2_%s.png" #covers idle, hover, selected etc
        action SetVariable("cup_stage_1", cup_stage_1 + 1), [Hide("matcha_button"), Return("matcha_done")]

######### LIME #########
screen shroom_button:
    add maximo_drinks[cup_stage_1] xpos 0.37 ypos 0.3

    $ tip = GetTooltip()
    if tip:
        text tip xcenter 0.689 ypos 650 size 40 font "Belgan Aesthetic.ttf" color "#ffffff"
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.7
        ypos 0.8

        tooltip "Mushroom"
        auto "images/DRINKS/MAXIMO/INGREDIENT/ingredient3_%s.png" #covers idle, hover, selected etc
        action SetVariable("cup_stage_1", cup_stage_1 + 1), [Hide("shroom_button"), Return("shroom_done")]

############# SERVE #############
screen maximo_serve_button:
    add maximo_drinks[cup_stage_1] xpos 0.37 ypos 0.3
    
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.73
        ypos 0.5
        auto "serve_button_%s.png" #covers idle, hover, selected etc
        action [Hide("serve_button"), Return("serve_done")]
