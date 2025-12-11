########### SCREENS ###########
            
######### GIN #########
default cup_stage_tut = 0

screen gin_button:
                
    add diego_drinks[cup_stage_tut] xpos 0.45 ypos 0.34 zoom 1.1

    $ tip = GetTooltip()
    if tip:
        text tip xcenter 0.689 ypos 67 size 40 font "Belgan Aesthetic.ttf" color "#ffffff"
                
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.7
        ypos 0.48
    
        tooltip "Gin"
        auto "images/DRINKS/DIEGO/INGREDIENT/gin_%s.png" #covers idle, hover, selected etc
        action SetVariable("cup_stage_tut", cup_stage_tut + 1), [Hide("gin_button"), Return("gin_done")]

######### HONEY #########
screen honey_button:
    add diego_drinks[cup_stage_tut] xpos 0.45 ypos 0.34 zoom 1.1

    $ tip = GetTooltip()
                
    if tip:
        text tip xcenter 0.673 ypos 640 size 40 font "Belgan Aesthetic.ttf" color "#ffffff"
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.68
        ypos 0.747

        tooltip "Honey"
        auto "images/DRINKS/DIEGO/INGREDIENT/honey_%s.png" #covers idle, hover, selected etc
        action SetVariable("cup_stage_tut", cup_stage_tut + 1), [Hide("honey_button"), Return("honey_done")]

######### LIME #########
screen lime_button:
    add diego_drinks[cup_stage_tut] xpos 0.45 ypos 0.34 zoom 1.1

    $ tip = GetTooltip()
    if tip:
        text tip xcenter 0.687 ypos 670 size 40 font "Belgan Aesthetic.ttf" color "#ffffff"
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.7
        ypos 0.77

        tooltip "Lime"
        auto "images/DRINKS/DIEGO/INGREDIENT/lime_%s.png" #covers idle, hover, selected etc
        action SetVariable("cup_stage_tut", cup_stage_tut + 1), [Hide("lime_button"), Return("lime_done")]

############# SERVE #############
screen serve_button:
    add diego_drinks[cup_stage_tut] xpos 0.45 ypos 0.34 zoom 1.1
    
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.7
        ypos 0.5
        auto "serve_button_%s.png" #covers idle, hover, selected etc
        action [Hide("serve_button"), Return("serve_done")]
