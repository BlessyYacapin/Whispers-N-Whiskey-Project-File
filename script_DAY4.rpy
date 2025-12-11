label DAY4:
    $ renpy.save("day4_checkpoint")
    $ renpy.notify("Third Shift")

    #-------------------- DEFAULT VALUES --------------------
    default dawani_trust = 3

    stop music
    scene black with dissolve
    pause 2.0

    ############################# SCENE TRANSITION #############################
    play sound "<from 14.30 to 16.80>transition_1.mp3"
    show d4 at truecenter
    pause 3
    hide d4 with dissolve
    ############################################################################
    $ current_character = "Dawani"

    play music "audio/bar_2.mp3"
    scene bar_counter
    show bar_table onlayer foreground zorder 2

    p "{b}ACHOO!{/b}" with hpunch

    narrate "You sneezed as soon as you finished wiping the tables."

    show dieg_default onlayer foreground zorder 1 at center with easeinright

    hide dieg_default onlayer foreground
    show dieg_serious_talk onlayer foreground zorder 1
    d "You alright there, kiddo?"

    hide dieg_serious_talk onlayer foreground
    show diego_serious onlayer foreground zorder 1
    p "Yes, Senior. It's just allergies."

    hide diego_serious onlayer foreground
    show dieg_serious_talk onlayer foreground zorder 1
    d "Did you let anyone hug you last night?"

    hide dieg_serious_talk onlayer foreground
    show diego_serious onlayer foreground zorder 1
    menu:
        "Nope, why?":
            hide diego_serious onlayer foreground
            show dieg_serious_talk onlayer foreground zorder 1
            d "Mhm, it's nothing."

            hide dieg_serious_talk onlayer foreground
            show diego_serious onlayer foreground zorder 1
            narrate "The door opened as soon as those words left his lips."

            show diego_serious onlayer foreground zorder 1 at SPRITE2_pos with easeinright
            
            play sound "audio/door.mp3" noloop
            pause 1.2
            show daw_sad onlayer foreground zorder 1 at SPRITE1_pos with easeinleft

            show screen trust_display
            narrate "A beautiful, pale lady barged inside the bar."
            narrate "She was sobbing uncontrollably as her long straight hair covered almost half of his face."
            narrate "The girl lifts her head and looks at you with her teary eyes."
            narrate "Suddenly, she made her way towards you and spreads her arms, as if going in for a hug---"

            hide screen trust_display
            menu:
                "Move away":
                    jump good_dawani_r1
                "Let her hug you":
                    jump bad_dawani_r1
    
    label good_dawani_r1:
        show screen trust_display
        $ dawani_trust += 0

        narrate "Your body moved away to dodge her hug in reflex." with hpunch

        hide screen trust_display
        menu:
            "Senior Diego pulled you away from her":
                jump continue_day4

    label bad_dawani_r1:
        show screen trust_display
        $ dawani_trust -= 1

        narrate "You felt chills as you accepted her embrace and reluctantly patted her head as she cried in your arms." with hpunch
        narrate "You looked at Senior Diego in panic, asking him for help."

        hide screen trust_display
        menu:
            "Senior Diego pulled you away from her":
                jump continue_day4
        
    label continue_day4:
        show screen trust_display

        narrate "Senior Diego got in between you two and pushed you aside slightly." with hpunch

        p "What's wrong, {i}binibini{/i}?"
        p "{i}Love life, perhaps? Pft, teens.{/i}"

        hide daw_sad onlayer foreground
        show daw_talk_sad onlayer foreground zorder 1 at SPRITE1_pos
        c3 "My father..."

        hide daw_talk_sad onlayer foreground
        show daw_sad onlayer foreground zorder 1 at SPRITE1_pos
        p "{i}Oof, nevermind...{/i}"

        hide diego_serious onlayer foreground
        show dieg_serious_talk onlayer foreground zorder 1 at SPRITE2_pos
        d "Please take a seat,{w=0.5} miss...?"
        hide dieg_serious_talk onlayer foreground
        show diego_serious onlayer foreground zorder 1 at SPRITE2_pos

        hide daw_sad onlayer foreground
        show daw_talk_sad onlayer foreground zorder 1 at SPRITE1_pos
        c2d "{b}D-Dawani...{/b}"
        hide daw_talk_sad onlayer foreground
        show daw_sad onlayer foreground zorder 1 at SPRITE1_pos

        hide diego_serious onlayer foreground
        show dieg_talk_normal onlayer foreground zorder 1 at SPRITE2_pos
        d "Alright [player_name] make her something to drink"
        d "It's on the house"
        hide screen trust_display
        hide dieg_talk_normal onlayer foreground with easeoutright

        jump dawani_drink

        label dawani_drink:
            window hide
            $ result = renpy.call_screen("water_button")
            if result == "water_done":
                show glass_1 onlayer foreground zorder 2:
                    xpos 0.48 
                    ypos 0.25
                # Play sound
                play sound "<from 4.00 to 8.00>audio/fizz.mp3"

                # Pause for duration of audio
                $ renpy.pause(4.0, hard=True)  # hard=True disables skipping

                # Re-enable skipping
                $ _preferences.skip_enabled = True
                show glass_1 onlayer foreground zorder 2:
                    xpos 0.48 
                    ypos 0.25
            
            $ result = renpy.call_screen("gins_button")
            hide glass_1 onlayer foreground zorder 2
            if result == "gins_done":
                show glass_2 onlayer foreground zorder 2:
                    xpos 0.48 
                    ypos 0.25
                # Play sound
                play sound "audio/drink_1.mp3"

                # Pause for duration of audio
                $ renpy.pause(2.0, hard=True)  # hard=True disables skipping

                # Re-enable skipping
                $ _preferences.skip_enabled = True
                show glass_2 onlayer foreground zorder 2:
                    xpos 0.48 
                    ypos 0.25

            $ result = renpy.call_screen("flower_button")
            hide glass_2 onlayer foreground zorder 2
            if result == "flower_done":
                show glass_3 onlayer foreground zorder 2:
                    xpos 0.48 
                    ypos 0.25
                # Play sound
                play sound "<from 1.00 to 2.00>powder.mp3"

                # Pause for duration of audio
                $ renpy.pause(2.0, hard=True)  # hard=True disables skipping

                # Re-enable skipping
                $ _preferences.skip_enabled = True
                show glass_3 onlayer foreground zorder 2:
                    xpos 0.48 
                    ypos 0.25

            $ result = renpy.call_screen("dawani_serve_button")
            hide glass_3 onlayer foreground zorder 2
            if result == "serve_done":
                show glass_3 onlayer foreground zorder 2:
                    xpos 0.48 
                    ypos 0.25
                # Play sound
                play sound "<from 5.70 to 6.00>click.mp3" volume 1.0

                # Pause for duration of audio
                $ renpy.pause(0.1, hard=True)  # hard=True disables skipping
                jump end_dawani_drink
        
        label end_dawani_drink:
            show glass_3 onlayer foreground zorder 2:
                xpos 0.48 
                ypos 0.25
            
            show glass_3 onlayer foreground zorder 2 at drink_pos1 with ease
            show dieg_default onlayer foreground zorder 1 at SPRITE2_pos with easeinright
            show screen trust_display

            p "Take this."

            hide daw_sad onlayer foreground
            show daw_talk_sad onlayer foreground zorder 1 at SPRITE1_pos
            c2d "Thank you..."
            hide daw_talk_sad onlayer foreground
            show daw_sad onlayer foreground zorder 1 at SPRITE1_pos

            p "May we ask what happened?"

            hide daw_sad onlayer foreground
            show daw_talk_sad onlayer foreground zorder 1 at SPRITE1_pos
            c2d "My father...{w=0.5} He's sick.."
            c2d "He's always been sick. Ever since when I was a kid, he always have fever. "
            c2d "Not a single day without it. We tried asking a doctor but they couldnt tell whats going on with his body."
            c2d "We couldnt afford to stay in the hospital so now he's bedridden in our home..."
            hide daw_talk_sad onlayer foreground
            show daw_sad onlayer foreground zorder 1 at SPRITE1_pos

            hide screen trust_display
            menu:
                "What about your mother?":
                    show screen trust_display
                    hide daw_sad onlayer foreground
                    show daw_talk_sad onlayer foreground zorder 1 at SPRITE1_pos
                    c2d "I dont know where she is. I havent met her and my father refused to tell me about it."
                    hide daw_talk_sad onlayer foreground
                    show daw_sad onlayer foreground zorder 1 at SPRITE1_pos

                    hide dieg_default onlayer foreground 
                    show dieg_serious onlayer foreground zorder 1 at SPRITE2_pos
                    narrate "Senior Diego stared at her from head to toe..."
                    narrate "You followed his gaze and thats when you noticed something."
                    narrate "She was pale white, but her legs from her knees down was black with blue accents on it."

                    hide daw_sad onlayer foreground
                    show daw_annoyed onlayer foreground zorder 1 at SPRITE1_pos
                    p "Your legs..."

                    narrate "She flinched at the mention of it and tried to cover it with her skirt"

                    hide daw_annoyed onlayer foreground
                    show daw_talk_annoy onlayer foreground zorder 1 at SPRITE1_pos
                    c2d "I dont know why it's like this..."
                    hide daw_talk_annoy onlayer foreground
                    show daw_annoyed onlayer foreground zorder 1 at SPRITE1_pos

                    hide screen trust_display
                    menu:
                        "Maybe that's the reason why people are getting sick haha":
                            show screen trust_display
                            hide daw_annoyed onlayer foreground
                            show daw_default onlayer foreground zorder 1 at SPRITE1_pos
                            narrate "Her face dropped at your \"joke\", but you didnt really pay much attention to it."
                            narrate "Senior Diego was silent the whole time, observing."

                            hide screen trust_display
                            menu:
                                "Senior? Is something wrong?":
                                    jump respond_dawani

                        "It's pretty, don't worry":
                            show screen trust_display
                            p "It's pretty, dont worry."
                            hide daw_annoyed onlayer foreground
                            show daw_talk_def onlayer foreground zorder 1 at SPRITE1_pos
                            c2d "Thank you"
                            hide daw_talk_def onlayer foreground
                            show daw_default onlayer foreground zorder 1 at SPRITE1_pos

                            narrate "Senior Diego was silent the whole time, observing."

                            hide screen trust_display
                            menu:
                                "Senior? Is something wrong?":
                                    jump respond_dawani
            
        label respond_dawani:
            show screen trust_display
            hide dieg_serious onlayer foreground 
            show dieg_serious_talk onlayer foreground zorder 1 at SPRITE2_pos
            d "Can we talk for a second?"
            hide dieg_serious_talk onlayer foreground 
            show dieg_serious onlayer foreground zorder 1 at SPRITE2_pos

            hide screen trust_display
            menu:
                "Of course...?":
                    hide daw_default onlayer foreground
                    hide dieg_serious onlayer foreground
                    hide glass_3 onlayer foreground zorder 2 
                    hide bar_table onlayer foreground
                    scene black with dissolve
                    with dissolve
                    
                    pause 0.3
                    scene bar_inside with dissolve

                    show dieg_serious onlayer foreground zorder 1 at center with easeinright
                    hide dieg_serious onlayer foreground 
                    show dieg_serious_talk onlayer foreground 
                    d "Dawani... she might not be just a normal person."
                    hide dieg_serious_talk onlayer foreground 
                    show dieg_serious onlayer foreground

                    p "Huh?"

                    hide dieg_serious onlayer foreground 
                    show dieg_serious_talk onlayer foreground 
                    d "{i}Karokung{/i}. This is my first time encountering one if she actually is a {i}karokung{/i}"
                    hide dieg_serious_talk onlayer foreground 
                    show dieg_serious onlayer foreground

                    menu:
                        "What's that?":
                            hide dieg_serious onlayer foreground 
                            show dieg_serious_talk onlayer foreground
                            d "It is a river-dwelling entity associated with disease, specifically the rapid temperature shifts during a fever."
                            d "That explains her father's fever and the black-blue part of her legs."
                            hide dieg_serious_talk onlayer foreground 
                            show dieg_serious onlayer foreground

                            p "I see."

                            hide dieg_serious onlayer foreground 
                            show dieg_serious_talk onlayer foreground
                            d "Take care of her. I need to go somewhere to get something."
                            hide dieg_serious_talk onlayer foreground 
                            show dieg_serious onlayer foreground
                            hide dieg_serious onlayer foreground at center with easeoutright

                            p "{i}Good thing there were no other customers today.{/i}"
                            narrate "You made her way towards her."
                            
                            scene bg black
                            pause 0.3
                            scene bar_counter
                            show bar_table onlayer foreground zorder 2
                            show daw_default onlayer foreground zorder 1 at center
                            with dissolve

                            menu:
                                "Hey, how are you feeling?":
                                    
                                    show screen trust_display
                                    
                                    p "Hey, how are you feeling?"

                                    hide daw_default onlayer foreground
                                    show daw_talk_def onlayer foreground zorder 1
                                    c2d "Good... still worried about my father."
                                    hide daw_talk_def onlayer foreground
                                    show daw_default onlayer foreground zorder 1

                                    p "I understand.... could you tell me more about it?"

                                    hide daw_default onlayer foreground
                                    show daw_talk_annoy onlayer foreground zorder 1
                                    d "I already told you guys about it earlier."
                                    hide daw_talk_annoy onlayer foreground
                                    show daw_talk_def onlayer foreground zorder 1
                                    d "But yeah... It's just... I dont know, but I feel like I'm the reason why he's like that."
                                    hide daw_talk_def onlayer foreground
                                    show daw_default onlayer foreground zorder 1

                                    hide screen trust_display
                                    menu:
                                        "Maybe because you are":
                                            jump bad_dawani_r2
                                        "Don't blame yourself":
                                            jump good_dawani_r2
        label bad_dawani_r2:
            show screen trust_display
            $ dawani_trust -= 1

            p "Maybe because you are."
            hide daw_default onlayer foreground
            show daw_talk_annoy onlayer foreground zorder 1
            c2d "What do you mean?"
            hide daw_talk_annoy onlayer foreground
            show daw_annoyed onlayer foreground zorder 1

            hide screen trust_display
            menu:
                "{i}Tell her the truth{/i}":
                    show screen trust_display
                    p "Senior Diego told me about it. He's suspecting you might be a {i}Karokung{/i}."

                    hide daw_annoyed onlayer foreground
                    show daw_mad onlayer foreground zorder 1
                    narrate "You're getting chills as you said that."

                    p "{i}Why is it so cold so suddenly?{/i}"
                    
                    hide daw_mad onlayer foreground
                    show daw_talk_mad onlayer foreground zorder 1
                    c2d "T-That cant be... Even if I was he.. he's supposed to be dead a long time ago..."
                    hide daw_talk_mad onlayer foreground
                    show daw_mad onlayer foreground zorder 1

                    hide screen trust_display
                    menu:
                        "Tell you what, I have a theory":
                            show screen trust_display
                            $ dawani_trust -= 1
                            p "Maybe the reason why you haven't met your mother is because she was a Karokung."
                            p "Your mother and father fell in love with each other--- Boom!"
                            p "You came, half-human and haldf-karokung. Maybe that's why your fever isnt as deadly as a normal Karokung."
                            p "Especially with your father since you have his blood."
                            p "{i}Wow, I feel smart saying that{/i}"

                            stop music
                            narrate "Dawani clenched her fists..."

                            c2d "I have to go."
                            hide daw_mad onlayer foreground
                            play sound "Glitch.mp3"
                            show dawani_glitched
                            pause 1.5
                            hide dawani_glitched
                            show daw_mad onlayer foreground zorder 1        
                            p "Dawani, wait---"

                            hide daw_mad onlayer foreground with easeoutleft
                            narrate "She didnt listen."

                            hide screen trust_display    
                            menu:
                                "You went ahead to catch up.":
                                    $ dawani_trust -= 1

                                    hide bar_table onlayer foreground zorder 1
                                    scene black 
                                    with dissolve
                                    pause 1.0
                                    p "Huh... I'm still alive."
                                    #SHRUGGING NOISE
                                    ############################# SCENE TRANSITION #############################
                                    show text "{i}{size= 50}As you were about to head back to the counter, the temperature suddenly went down.{/size}{/i}" at truecenter
                                    with dissolve
                                    pause 4.0
                                    hide text with dissolve
                                    ############################################################################
                                    show text "{i}{size= 50}Your're freezing.... fever?{/size}{/i}" at truecenter
                                    with dissolve
                                    pause 2.0
                                    hide text with dissolve
                                    ############################################################################
                                    #DEAD
                                    call check_dawani_trust from _call_check_dawani_trust_2

        label good_dawani_r2:
            show screen trust_display
            $ ysabel_trust += 0
            
            p "Don't blame yourself, Dawani..."
            hide daw_mad onlayer foreground
            show daw_default onlayer foreground zorder 1
            
            pause 0.7

            hide screen trust_display with fastdissolve
            hide daw_default onlayer foreground
            hide bar_table onlayer foreground zorder 1
            scene black 
            with dissolve
            
            ############################# SCENE TRANSITION #############################
            show text "{i}{size= 50}You talked to her about it, you let her rant and shared your thoughts.{/size}{/i}" at truecenter
            with dissolve
            pause 4.0
            hide text with dissolve
            ############################################################################

            scene bar_counter
            show bar_table onlayer foreground zorder 2
            show daw_default onlayer foreground zorder 1 at SPRITE1_pos
            with dissolve
            pause 0.8  
            show dieg_default onlayer foreground zorder 1 at SPRITE2_pos with easeinright

            hide dieg_default onlayer foreground
            show dieg_talk_normal onlayer foreground zorder 1 at SPRITE2_pos
            d "Dawani."
            hide dieg_talk_normal onlayer foreground
            show dieg_default onlayer foreground zorder 1 at SPRITE2_pos

            hide daw_default onlayer foreground
            show daw_talk_def onlayer foreground zorder 1 at SPRITE1_pos
            c2d "Yes, Senior?"
            hide daw_talk_def onlayer foreground
            show daw_default onlayer foreground zorder 1 at SPRITE1_pos

            hide dieg_default onlayer foreground
            show dieg_talk_normal onlayer foreground zorder 1 at SPRITE2_pos
            d "Give this to your father. This would help him."
            hide dieg_talk_normal onlayer foreground
            show dieg_default onlayer foreground zorder 1 at SPRITE2_pos

            hide daw_default onlayer foreground
            show daw_talk_def onlayer foreground zorder 1 at SPRITE1_pos
            c2d "Really?"
            hide daw_talk_def onlayer foreground
            show daw_default onlayer foreground zorder 1 at SPRITE1_pos

            hide dieg_default onlayer foreground
            show dieg_talk_normal onlayer foreground zorder 1 at SPRITE2_pos
            d "Really."
            hide dieg_talk_normal onlayer foreground
            show dieg_default onlayer foreground zorder 1 at SPRITE2_pos

            hide daw_default onlayer foreground
            show daw_talk_happy onlayer foreground zorder 1 at SPRITE1_pos
            c2d "Thank you so much! I'll head back home now."
            hide daw_talk_happy onlayer foreground
            show daw_happy onlayer foreground zorder 1 at SPRITE1_pos

            hide dieg_default onlayer foreground
            show dieg_talk_normal onlayer foreground zorder 1 at SPRITE2_pos
            d "No problem. And Dawani? You're not different or weird--- You're special. Always remember that."
            hide dieg_talk_normal onlayer foreground
            show dieg_default onlayer foreground zorder 1 at SPRITE2_pos

            hide daw_default onlayer foreground
            show daw_talk_happy onlayer foreground zorder 1 at SPRITE1_pos
            c2d "I will... Thank you! Both of you."
            hide daw_talk_happy onlayer foreground
            show daw_happy onlayer foreground zorder 1 at SPRITE1_pos
            hide daw_happy onlayer foreground with easeoutleft

            show dieg_default onlayer foreground zorder 1 at center with ease
            show bottle onlayer foreground at bottle_pos zorder 2 
            narrate "Diego pulled out a bottle that was the same as the one he gave Dawani. He opened it and poured it onto a glass"

            hide bottle onlayer foreground
            hide dieg_default onlayer foreground
            show dieg_serious_talk onlayer foreground zorder 1
            d "Drink it. Just to be safe."
            hide dieg_serious_talk onlayer foreground
            show dieg_serious onlayer foreground zorder 1

            narrate "You nod your head and did what you were told."

            p "Why didnt you tell her the truth?"

            hide dieg_serious onlayer foreground
            show dieg_serious_talk onlayer foreground zorder 1
            d "It wasnt my job. I'm pretty sure her father will tell her the truth soon."
            hide dieg_serious_talk onlayer foreground
            show dieg_default onlayer foreground zorder 1

            hide dieg_default onlayer foreground
            show dieg_talk_normal onlayer foreground zorder 1
            d "Good job keeping her company. You're getting a raise."
            hide dieg_talk_normal onlayer foreground
            show dieg_default onlayer foreground zorder 1
            p "REALLY?!"

            hide dieg_default onlayer foreground
            hide bar_inside
            hide bar_table onlayer foreground
            scene black with dissolve
            with dissolve

            hide screen trust_display
            call screen status_menu_day4
            jump end
            
