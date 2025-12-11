########### SCREENS ###########
            
######### SPARKLING WATER #########
default cup_stage_3 = 0

screen water_button:
                
    add dawani_drinks[cup_stage_3] xpos 0.48 ypos 0.25

    $ tip = GetTooltip()
    if tip:
        text tip xcenter 0.685 ypos 350 size 40 font "Belgan Aesthetic.ttf" color "#ffffff"
                
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.71
        ypos 0.647
    
        tooltip "Sparkling Water"
        auto "images/DRINKS/DAWANI/INGREDIENT/ingredient1_%s.png" #covers idle, hover, selected etc
        action SetVariable("cup_stage_3", cup_stage_3 + 1), [Hide("water_button"), Return("water_done")]

######### GIN #########
screen gins_button:
    add dawani_drinks[cup_stage_3] xpos 0.48 ypos 0.25

    $ tip = GetTooltip()
                
    if tip:
        text tip xcenter 0.682 ypos 110 size 40 font "Belgan Aesthetic.ttf" color "#ffffff"
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.71
        ypos 0.53

        tooltip "Gin"
        auto "images/DRINKS/DAWANI/INGREDIENT/ingredient2_%s.png" #covers idle, hover, selected etc
        action SetVariable("cup_stage_3", cup_stage_3 + 1), [Hide("gins_button"), Return("gins_done")]

######### FLOWER #########
screen flower_button:
    add dawani_drinks[cup_stage_3] xpos 0.48 ypos 0.25

    $ tip = GetTooltip()
    if tip:
        text tip xcenter 0.708 ypos 110 size 40 font "Belgan Aesthetic.ttf" color "#ffffff"
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.71
        ypos 0.53

        tooltip "Chrysanthemum"
        auto "images/DRINKS/DAWANI/INGREDIENT/ingredient3_%s.png" #covers idle, hover, selected etc
        action SetVariable("cup_stage_3", cup_stage_3 + 1), [Hide("flower_button"), Return("flower_done")]

############# SERVE #############
screen dawani_serve_button:
    add dawani_drinks[cup_stage_3] xpos 0.48 ypos 0.25
    
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.7
        ypos 0.5
        auto "serve_button_%s.png" #covers idle, hover, selected etc
        action [Hide("serve_button"), Return("serve_done")]
