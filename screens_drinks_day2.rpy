########### SCREENS ###########
            
######### MARIO CLARA #########
default cup_stage_2 = 0

screen wine_button:
                
    add ysabel_drinks[cup_stage_2] xpos 0.43 ypos 0.35

    $ tip = GetTooltip()
    if tip:
        text tip xcenter 0.683 ypos 120 size 40 font "Belgan Aesthetic.ttf" color "#ffffff"
                
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.73
        ypos 0.53
    
        tooltip "Wine"
        auto "images/DRINKS/YSABEL/INGREDIENTS/ingredient1_%s.png" #covers idle, hover, selected etc
        action SetVariable("cup_stage_2", cup_stage_2 + 1), [Hide("wine_button"), Return("wine_done")]

######### POMEGRANATE #########
screen pomegranate_button:
    add ysabel_drinks[cup_stage_2] xpos 0.43 ypos 0.35

    $ tip = GetTooltip()
                
    if tip:
        text tip xcenter 0.7 ypos 520 size 40 font "Belgan Aesthetic.ttf" color "#ffffff"
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.76
        ypos 0.77

        tooltip "Pomegranate"
        auto "images/DRINKS/YSABEL/INGREDIENTS/ingredient2_%s.png" #covers idle, hover, selected etc
        action SetVariable("cup_stage_2", cup_stage_2 + 1), [Hide("pomegranate_button"), Return("pomegranate_done")]

######### GUMMY STRIPS #########
screen gum_button:
    add ysabel_drinks[cup_stage_2] xpos 0.43 ypos 0.35

    $ tip = GetTooltip()
    if tip:
        text tip xcenter 0.689 ypos 400 size 40 font "Belgan Aesthetic.ttf" color "#ffffff"
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.717
        ypos 0.669

        tooltip "Sour Strips"
        auto "images/DRINKS/YSABEL/INGREDIENTS/ingredient3_%s.png" #covers idle, hover, selected etc
        action SetVariable("cup_stage_2", cup_stage_2 + 1), [Hide("gum_button"), Return("gum_done")]

############# SERVE #############
screen ysabel_serve_button:
    add ysabel_drinks[cup_stage_2] xpos 0.43 ypos 0.35
    
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.72
        ypos 0.6
        auto "serve_button_%s.png" #covers idle, hover, selected etc
        action [Hide("ysabel_serve_button"), Return("ysabel_serve_done")]
