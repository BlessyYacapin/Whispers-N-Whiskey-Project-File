label DAY3:
    $ renpy.save("day3_checkpoint")
    $ renpy.notify("Second Shift")

    #-------------------- DEFAULT VALUES --------------------
    default ysabel_trust = 3

    stop music
    scene black with dissolve
    pause 2.0
    
    ############################# SCENE TRANSITION #############################
    play sound "<from 14.30 to 16.80>transition_1.mp3"
    show d3 at truecenter
    pause 3
    hide d3 with dissolve
    ############################################################################
    $ current_character = "Ysabel"

    play music "audio/bar_1.mp3"
    scene bar_counter
    show bar_table onlayer foreground zorder 2
    show diego_default onlayer foreground zorder 1 at center with easeinright

    narrate "Senior Diego was wiping the shot glasses while you helped him arrange it in the cabinet while waiting for customers to arrive."
    narrate "You were chatting with him about a certain customer's weird order you did last night, when all of a sudden, the bottle of an oil looking thing started bubbling."
    narrate "You raised a brow"

    p "What's that?"

    hide diego_default onlayer foreground
    show dieg_serious_talk onlayer foreground zorder 1
    show lana onlayer foreground at bottle_pos zorder 2 
    d "{i}Lana{/i}, it's an \"anti-aswang\" oil that bubbles when the creature is nearby."
    hide lana onlayer foreground
    
    hide dieg_serious_talk onlayer foreground
    show diego_serious onlayer foreground zorder 1
    p "{b}ASWANG?!{/b}" with hpunch

    hide diego_serious onlayer foreground
    show dieg_serious_talk onlayer foreground zorder 1
    d "Mhm, which reminds me that there's a sudden attack of {i}Tiktik{/i} the other night at the barrio near us."

    hide dieg_serious_talk onlayer foreground
    show diego_serious onlayer foreground zorder 1
    p "Tiktik?"

    hide diego_serious onlayer foreground
    show dieg_serious_talk onlayer foreground zorder 1
    d "It's a creature under the aswang category."
    d "They usually go for unborn children as their food."

    hide dieg_serious_talk onlayer foreground
    show diego_serious onlayer foreground zorder 1
    narrate "You grimaced at the thought"
    hide diego_serious onlayer foreground zorder 1 with easeoutleft
    p "Jeez..."

    play sound "audio/door.mp3" noloop
    pause 2.5

    narrate "The door opened, revealing a beautiful woman with long brown wavy hair."
    show ysabel_default onlayer foreground zorder 1 at center with easeinright
    show screen trust_display

    hide ysabel_default onlayer foreground
    show ysa_talk_def onlayer foreground zorder 1
    c2 "Good evening..."
    
    hide ysa_talk_def onlayer foreground
    show ysabel_default onlayer foreground zorder 1
    hide screen trust_display
    menu:
        "You smiled":
            jump continue_day3
        "You nod yor head as a greeting":
            jump continue_day3
        
    label continue_day3:
        show screen trust_display
        p "What can I get for you today, {i}binibini{/i}?"

        hide ysabel_default onlayer foreground
        show ysa_talk_def onlayer foreground zorder 1
        c2 "I'm no longer a {i}binibini{/i}, I'm married---{w=0.5} Well, was."
        c2 "{i}E-ehem{/i} Something sweet but strong, please."

        hide ysa_talk_def onlayer foreground
        show ysabel_default onlayer foreground zorder 1
        p "Of course, this drink is for?"

        narrate "You chuckled in your head, thinking how hilarious it is to keep this question going everytime someone orders..."
        narrate "It seems like the lady didn't mind."

        hide ysabel_default onlayer foreground
        show ysa_talk_def onlayer foreground zorder 1
        y "{b}Ysabel.{/b}"

        hide ysa_talk_def onlayer foreground
        show ysabel_default onlayer foreground zorder 1
        hide screen trust_display
        show ysabel_default onlayer foreground zorder 1 at SPRITE1_pos with ease
        jump ysabel_drink

        label ysabel_drink:
            window hide
            $ result = renpy.call_screen("wine_button")
            if result == "wine_done":
                show y_glass_1 onlayer foreground zorder 2:
                    xpos 0.43 
                    ypos 0.35
                # Play sound
                play sound "audio/drink_1.mp3"

                # Pause for duration of audio
                $ renpy.pause(2.0, hard=True)  # hard=True disables skipping

                # Re-enable skipping
                $ _preferences.skip_enabled = True
                show y_glass_1 onlayer foreground zorder 2:
                    xpos 0.43 
                    ypos 0.35
            
            $ result = renpy.call_screen("pomegranate_button")
            hide y_glass_1 onlayer foreground zorder 2
            if result == "pomegranate_done":
                show y_glass_2 onlayer foreground zorder 2:
                    xpos 0.43 
                    ypos 0.35
                # Play sound
                play sound "<from 1.00 to 2.00>powder.mp3"

                # Pause for duration of audio
                $ renpy.pause(2.0, hard=True)  # hard=True disables skipping

                # Re-enable skipping
                $ _preferences.skip_enabled = True
                show y_glass_2 onlayer foreground zorder 2:
                    xpos 0.43 
                    ypos 0.35

            $ result = renpy.call_screen("gum_button")
            hide y_glass_2 onlayer foreground zorder 2
            if result == "gum_done":
                show y_glass_3 onlayer foreground zorder 2:
                    xpos 0.43 
                    ypos 0.35
                # Play sound
                play sound "<from 1.00 to 2.00>powder.mp3"

                # Pause for duration of audio
                $ renpy.pause(2.0, hard=True)  # hard=True disables skipping

                # Re-enable skipping
                $ _preferences.skip_enabled = True
                show y_glass_3 onlayer foreground zorder 2:
                    xpos 0.43 
                    ypos 0.35

            $ result = renpy.call_screen("ysabel_serve_button")
            hide y_glass_3 onlayer foreground zorder 2
            if result == "ysabel_serve_done":
                show y_glass_3 onlayer foreground zorder 2:
                    xpos 0.43 
                    ypos 0.35
                # Play sound
                play sound "<from 5.70 to 6.00>click.mp3" volume 1.0

                # Pause for duration of audio
                $ renpy.pause(0.1, hard=True)  # hard=True disables skipping

                # Re-enable skipping
                $ _preferences.skip_enabled = True
                jump end_ysabel_drink
        
        label end_ysabel_drink:
            show y_glass_3 onlayer foreground zorder 2:
                xpos 0.43 
                ypos 0.35

            show y_glass_3 onlayer foreground zorder 2 at drink_pos with ease
            show ysabel_default onlayer foreground zorder 1 at center with easeinright
            show screen trust_display
            p "Here you go, Señora"
            
            hide ysabel_default onlayer foreground
            show ysa_talk_def onlayer foreground zorder 1
            y "Sour strips candy? I haven't had this in so long."

            hide ysa_talk_def onlayer foreground
            show ysabel_default onlayer foreground zorder 1
            p "Mhm, are you a fan of it?"
            
            hide ysabel_default onlayer foreground
            show ysa_talk_def onlayer foreground zorder 1
            y "My son does."

            hide ysa_talk_def onlayer foreground
            show ysabel_default onlayer foreground zorder 1
            hide screen trust_display
            menu:
                "Aww, that's nice.":
                    show screen trust_display
                    p "How old is he if you dont mind?"
                    y "..."

                    hide ysabel_default onlayer foreground
                    show ysa_talk_sad onlayer foreground zorder 1
                    y "... He's supposed to turn 5 years old this December."

                    hide ysa_talk_sad onlayer foreground
                    show ysabel_sad onlayer foreground zorder 1
                    p "{i}Supposed to?{/i}"

                    hide screen trust_display
                    menu:
                        "{i}You raised a brow{/i}":
                            show screen trust_display
                            p "Huh? what do you mean?"
                            p "{i}Is it what I think it is?{/i}"

                            narrate "Her aura changed as soon as those words left your mouth"

                            hide ysabel_sad onlayer foreground
                            show ysa_talk_sad onlayer foreground zorder 1
                            y "My son passed away 5 years ago."

                            hide ysa_talk_sad onlayer foreground
                            show ysabel_sad onlayer foreground zorder 1
                            hide screen trust_display
                            menu:
                                "Oh... I'm sorry to hear that.":
                                    jump ysabel_response1

                        "Oh... I'm sorry to hear that.":
                            jump ysabel_response1
                
            label ysabel_response1:
                show screen trust_display
                p "I'm sorry to hear that..."

                hide ysabel_sad onlayer foreground
                show ysa_talk_sad onlayer foreground zorder 1
                y "It's nothing. No use missing an unborn child that I lost almost 5 years ago."
                
                hide ysa_talk_sad onlayer foreground
                show ysabel_sad onlayer foreground zorder 1
                narrate "You shook your head as it reminded you of the {i}Tiktik{/i} incident Senior Diego mentioned earlier."

                p "I'm still sorry for your loss, it must've been hard."
                p "The mothers' who were victims of {i}Tiktik{/i} at the next barrio could probably relate with you, Señora."

                hide ysabel_sad onlayer foreground
                show ysabel_annoyed onlayer foreground zorder 1
                narrate "Ysabel froze at the mention of that, her facial expression shifted from the calm one to something else..."

                hide ysabel_annoyed onlayer foreground
                show ysa_talk_annoy onlayer foreground zorder 1
                y "It's different."
                y "I dont share the same pain as them. They probably deserved it."

                hide ysa_talk_annoy onlayer foreground
                show ysabel_annoyed onlayer foreground zorder 1
                narrate "Ysabel continued with a scoff,  taking another sip of her drink"

                hide screen trust_display
                menu:
                    "That's a mean thing to say":
                        jump bad_ysabel_r1
                    "May I ask why?":
                        jump good_ysabel_r1
                
            label bad_ysabel_r1:
                show screen trust_display
                $ ysabel_trust -= 1

                p "That's a mean thing to say..."
                p "Yeah, maybe you dont share the same pain as them but that doesnt mean they deserved losing their child."

                hide ysabel_annoyed onlayer foreground
                show ysa_talk_mad onlayer foreground zorder 1
                y "You dont know what they did that's why you're saying that."

                hide ysa_talk_mad onlayer foreground
                show ysa_mad onlayer foreground zorder 1
                narrate "Ysabel said as he gripped the glass tighter"

                p "What do you mean?"
                hide ysa_mad onlayer foreground
                show ysa_talk_annoy onlayer foreground zorder 1
                y "It's a long story."

                hide ysa_talk_annoy onlayer foreground
                show ysa_annoyed onlayer foreground zorder 1
                hide screen trust_display
                menu:
                    "I'm willing to listen...":
                        jump continue_day3_1
                        
            label good_ysabel_r1:
                show screen trust_display
                $ ysabel_trust += 0

                p "May I ask why?"
                hide ysabel_annoyed onlayer foreground
                show ysa_talk_annoy onlayer foreground zorder 1
                y "It's a long story."

                hide ysa_talk_annoy onlayer foreground
                show ysa_annoyed onlayer foreground zorder 1
                hide screen trust_display
                menu:
                    "I'm willing to listen...":
                        jump continue_day3_1
                
        label continue_day3_1:
            show screen trust_display
            hide ysabel_annoyed onlayer foreground
            show ysa_talk_def onlayer foreground zorder 1
            y "I understand the Tiktik why she did it. I believe I have a valid reason to do so."

            hide ysa_talk_def onlayer foreground
            show ysa_default onlayer foreground zorder 1
            p "{i}I? She has a valid reason?{/i}"

            hide screen trust_display
            menu:
                "Like what?":
                    show screen trust_display
                    hide ysa_default onlayer foreground
                    show ysa_talk_def onlayer foreground zorder 1
                    y "I don't know. Maybe... revenge?"

                    stop music
                    hide ysa_talk_def onlayer foreground
                    show ysa_default onlayer foreground zorder 1    
                    narrate "It gave you chills as soon as she said that."

                    p "Revenge?"

                    narrate "Ysabel leaned back on her chair and swirled the drink on the hands as she talked"
                    
                    play music "bar_1.mp3"
                    hide ysa_default onlayer foreground
                    show ysa_talk_def onlayer foreground zorder 1
                    y "The {i}victims{/i} of the Tiktik you mentioned we're all well known gossipers, {i}mga Marites{/i}."

                    hide ysa_talk_def onlayer foreground
                    show ysa_talk_annoy onlayer foreground zorder 1
                    y "All they do is talk bad about everyone. And I was a victim-- I lost my child because of those kind people"
                    y "They deserved it. If I can't live with my child in peace then so can they. It's only fair after what they did to me... To my family."

                    hide ysa_talk_annoy onlayer foreground
                    show ysa_annoyed onlayer foreground zorder 1
                    hide screen trust_display
                    menu:
                        "May I ask what happened?":
                            show screen trust_display
                            hide ysa_annoyed onlayer foreground
                            show ysa_talk_annoy onlayer foreground zorder 1
                            y "They spread rumors about me being a Tiktik."
                            y "Causing everyone else in my old barrio to attack my home..."

                            hide ysa_talk_annoy onlayer foreground
                            show ysa_talk_sad onlayer foreground zorder 1
                            y "They took everything from me."
                            y "My home, my husband, my baby..."
                            
                            hide ysa_talk_sad onlayer foreground
                            show ysa_sad onlayer foreground zorder 1
                            hide screen trust_display
                            menu:
                                "That's still a bit messed up":
                                    jump bad_ysabel_r2
                                "I understand where you're coming from.":
                                    jump good_ysabel_r2_0
                
            label bad_ysabel_r2:
                show screen trust_display
                $ ysabel_trust -= 1

                p "That's still a bit messed up."
                hide ysa_sad onlayer foreground
                show ysa_annoyed onlayer foreground zorder 1
                p "What you feel is valid but you shouldn't wish bad upon others."

                hide ysa_annoyed onlayer foreground
                show ysa_talk_annoy onlayer foreground zorder 1
                y "I do whatever I want."
                hide ysa_talk_annoy onlayer foreground
                show ysa_talk_mad onlayer foreground zorder 1
                y "And if that means feasting on their unborn children after they killed mine, then I will keep doing it with pleasure!" with hpunch
                hide ysa_talk_mad onlayer foreground
                show ysa_mad onlayer foreground zorder 1
                narrate "That gave you chills."

                p "Does that mean..."
                narrate "You shook your head at the thought, focusing on the matter at hand."

                hide screen trust_display
                menu:
                    "You're not getting my point---":
                        stop music
                        show screen trust_display
                        hide ysa_mad onlayer foreground
                        show ysa_talk_red onlayer foreground zorder 1
                        y "And you dont get mine!" with vpunch

                        hide ysa_talk_red onlayer foreground
                        play sound "Glitch.mp3"
                        show ysabel_glitched
                        pause 1.5
                        hide ysabel_glitched
                        show ysa_red onlayer foreground zorder 1
                        narrate "She said in a loud voice as she slammed the glass on the table, shattering it into pieces. Ysabel was breathing heavily as she glared at you with her..."
                        narrate "Red eyes?"

                        hide screen trust_display
                        menu:
                            "Hold her shoulder":
                                show screen trust_display
                                $ ysabel_trust -= 2
                                scene black
                                hide screen trust_display
                                hide y_glass_3 onlayer foreground zorder 2
                                hide ysa_red onlayer foreground zorder 1
                                hide bar_table onlayer foreground zorder 1 
                                with fastdissolve

                                ############################# SCENE TRANSITION #############################
                                show text "{i}{size= 50}As soon as your hand came in contact with her shoulder, Ysabel gripped your hand tightly enough to feel her nails dig onto your skin.{/size}{/i}" at truecenter
                                with dissolve
                                pause 4.0
                                hide text with dissolve
                                ############################################################################
                                call check_ysabel_trust from _call_check_ysabel_trust_2

                            "I understand where you're coming from":
                                jump good_ysabel_r2_1
                                
                        
            label good_ysabel_r2_0:
                show screen trust_display
                $ ysabel_trust += 0

                p "I understand where you're coming from. I really do."
                p "I lost someone dear to me as well, So I get what you're feeling."
                hide ysa_sad onlayer foreground
                show ysa_default onlayer foreground zorder 1

                hide screen trust_display
                scene black with dissolve
                hide y_glass_3 onlayer foreground zorder 2
                hide ysa_default onlayer foreground zorder 2
                hide bar_table onlayer foreground zorder 1 
                with fastdissolve
                
                pause 1.0
                ############################# SCENE TRANSITION #############################
                show text "{i}{size= 50}You explained that dragging all other \"marites\" and their innocent babies to her anger is wrong.{/size}{/i}" at truecenter
                with dissolve
                pause 4.0
                hide text with dissolve
                pause 1.0
                ############################################################################
                show text "{i}{size= 50}Took her awhile to be fully convinced but she accepted your advice and promised not to attack anymore before she left.{/size}{/i}" at truecenter 
                with dissolve
                pause 4.0
                hide text with dissolve
                pause 1.0
                ############################################################################

                menu:
                    "2nd shift ends":
                        call screen status_menu_day3
                    
                        scene bar_counter with dissolve
                        show bar_table onlayer foreground zorder 2
                        show dieg_default onlayer foreground zorder 1 at center with easeinright

                        hide dieg_default onlayer foreground
                        show dieg_laugh_talk onlayer foreground zorder 1
                        d "You almost died back there."

                        hide dieg_laugh_talk onlayer foreground
                        show dieg_default onlayer foreground zorder 1
                        p "That's not something to laugh about, Senior!" with hpunch

                        hide dieg_default onlayer foreground
                        show dieg_talk_normal onlayer foreground zorder 1
                        d "But in all seriousness, Good job today."
                        d "I'm surprised you're still alive."
                        d "Most baristas I recruited barely survives the first day. The longest one to survive was your mother."

                        hide dieg_talk_normal onlayer foreground
                        show dieg_default onlayer foreground zorder 1
                        p "I miss her dearly..."

                        hide dieg_default onlayer foreground
                        show dieg_talk_normal onlayer foreground zorder 1
                        d "I'm sure she's proud of you."
                        d "Go rest, I'll handle everything from here"

                        hide dieg_talk_normal onlayer foreground
                        show dieg_default onlayer foreground zorder 1
                        p "Thanks, Senior Diego."

                        scene black with dissolve
                        hide dieg_default onlayer foreground zorder 1 with fastdissolve
                        hide bar_table onlayer foreground zorder 1 with fastdissolve

                        jump DAY4
    
            label good_ysabel_r2_1:
                show screen trust_display
                $ ysabel_trust += 0

                play music "bar_1.mp3"
                p "I understand where you're coming from. I really do."
                p "I lost someone dear to me as well, So I get what you're feeling."
                hide ysa_red onlayer foreground
                show ysa_default onlayer foreground zorder 1

                hide screen trust_display
                scene black with dissolve
                hide y_glass_3 onlayer foreground zorder 2
                hide ysa_default onlayer foreground zorder 2
                hide bar_table onlayer foreground zorder 1 
                with fastdissolve
                
                pause 1.0
                ############################# SCENE TRANSITION #############################
                show text "{i}{size= 50}You explained that dragging all other \"marites\" and their innocent babies to her anger is wrong.{/size}{/i}" at truecenter
                with dissolve
                pause 4.0
                hide text with dissolve
                pause 1.0
                ############################################################################
                show text "{i}{size= 50}Took her awhile to be fully convinced but she accepted your advice and promised not to attack anymore before she left.{/size}{/i}" at truecenter 
                with dissolve
                pause 4.0
                hide text with dissolve
                pause 1.0
                ############################################################################

                menu:
                    "2nd shift ends":
                        scene bar_counter with dissolve
                        show bar_table onlayer foreground zorder 2
                        show dieg_default onlayer foreground zorder 1 at center with easeinright

                        hide dieg_default onlayer foreground
                        show dieg_laugh_talk onlayer foreground zorder 1
                        d "You almost died back there."

                        hide dieg_laugh_talk onlayer foreground
                        show dieg_default onlayer foreground zorder 1
                        p "That's not something to laugh about, Senior!" with hpunch

                        hide dieg_default onlayer foreground
                        show dieg_talk_normal onlayer foreground zorder 1
                        d "But in all seriousness, Good job today."
                        d "I'm surprised you're still alive."
                        d "Most baristas I recruited barely survives the first day. The longest one to survive was your mother."

                        hide dieg_talk_normal onlayer foreground
                        show dieg_default onlayer foreground zorder 1
                        p "I miss her dearly..."

                        hide dieg_default onlayer foreground
                        show dieg_talk_normal onlayer foreground zorder 1
                        d "I'm sure she's proud of you."
                        d "Go rest, I'll handle everything from here"

                        hide dieg_talk_normal onlayer foreground
                        show dieg_default onlayer foreground zorder 1
                        p "Thanks, Senior Diego."

                        scene black
                        hide dieg_default onlayer foreground zorder 1
                        hide bar_table onlayer foreground zorder 1 
                        with dissolve

                        jump DAY4            
######## DAY 4 IN script_DAY4.rpy ########