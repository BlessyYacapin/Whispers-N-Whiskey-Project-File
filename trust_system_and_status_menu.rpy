 #-------------------- SCREENS --------------------
screen trust_display():
    hbox:
        xalign 0.85
        yalign 0.7
        spacing 10

        if current_character == "Maximo":
            $ trust_val = maximo_trust
        elif current_character == "Ysabel":
            $ trust_val = ysabel_trust
        else:
            $ trust_val = dawani_trust
        

        for i in range(3):
            if i < trust_val:
                add "heart_full" zoom 0.56
            else:
                add "heart_empty" zoom 0.56

screen status_menu_day2():
    tag menu
    modal True
    frame:
        xalign 0.5
        yalign 0.5
        padding (40, 40)
        vbox:
            spacing 15
            hbox:
                xalign 0.5
                yalign 0.7
                spacing 5

                if current_character == "Maximo":
                    $ trust_val = maximo_trust

                for i in range(3):
                    if i < trust_val:
                        add "heart_full" zoom 0.56
                    else:
                        add "heart_empty" zoom 0.56
            text "Trust Status Summary" size 40
            text "Maximo Trust: [maximo_trust]/3"
            textbutton "Return" action [Hide("status_menu_day2"), Return()]

    
screen status_menu_day3():
    tag menu
    modal True
    frame:
        xalign 0.5
        yalign 0.5
        padding (40, 40)
        vbox:
            spacing 15
            hbox:
                xalign 0.5
                yalign 0.7
                spacing 5

                if current_character == "Maximo":
                    $ trust_val = maximo_trust
                else:
                    $ trust_val = ysabel_trust
                
                for i in range(3):
                    if i < trust_val:
                        add "heart_full" zoom 0.56
                    else:
                        add "heart_empty" zoom 0.56
            text "Trust Status Summary" size 40
            text "Maximo Trust: [maximo_trust]/3"
            text "Ysabel Trust: [ysabel_trust]/3"
            textbutton "Return" action [Hide("status_menu_day3"), Return()]

screen status_menu_day4():
    tag menu
    modal True
    frame:
        xalign 0.5
        yalign 0.5
        padding (40, 40)
        vbox:
            spacing 15
            hbox:
                xalign 0.5
                yalign 0.7
                spacing 5

                if current_character == "Maximo":
                    $ trust_val = maximo_trust
                elif current_character == "Ysabel":
                    $ trust_val = ysabel_trust
                else:
                    $ trust_val = dawani_trust
                
                for i in range(3):
                    if i < trust_val:
                        add "heart_full" zoom 0.56
                    else:
                        add "heart_empty" zoom 0.56
            text "Trust Status Summary" size 40
            text "Maximo Trust: [maximo_trust]/3"
            text "Ysabel Trust: [ysabel_trust]/3"
            text "Dawani Trust: [dawani_trust]/3"
            textbutton "Return" action [Hide("status_menu_day4"), Return()]