label DAY2:
    $ renpy.save("day2_checkpoint")
    $ renpy.notify("First Shift")

    #-------------------- DEFAULT VALUES --------------------
    default maximo_trust = 3
    default current_character = "Maximo"  # To control which trust bar appears

    scene black with dissolve
    pause 1.3

    ############################# SCENE TRANSITION #############################
    play sound "<from 14.30 to 16.80>transition_1.mp3"
    show d2 at truecenter
    pause 3
    hide d2 with dissolve
    ############################################################################
    $ current_character = "Maximo"
    show screen trust_display
    
    play music "audio/bar_2.mp3"
    scene bar_counter
    show bar_table onlayer foreground zorder 2

    p "{i}The bar was empty like usual.{w=0.5} Are there even customers here?{/i}"
    p "{i}Its in the middle of a forest, no one's gonna see it{/i}"

    hide screen trust_display
    play sound "audio/door.mp3" noloop
    pause 2.5

    show maximo_default onlayer foreground zorder 1 at center with easeinright
    show screen trust_display

    p "{i}Just as I finished that thought, the door opened and someone entered the bar{/i}"
    p "{i}I stood up straight and greeted him with a smile,{/i}"
    p "Good evening, what can I get for you?"

    narrate "The man rolled his eyes and walked towards the counter."
    hide maximo_default onlayer foreground
    show max_talk_normal onlayer foreground zorder 1
    cus1 "Surprise me, I want something earthy but strong."

    hide max_talk_normal onlayer foreground
    show maximo_default onlayer foreground zorder 1
    narrate "He said with a huff"

    p "Gotcha,{w=0.5} and this drink is for...?"
    p "{i}He gave me an annoyed stare{/i}"

    hide maximo_default onlayer foreground
    show max_talk_normal onlayer foreground zorder 1
    cus1 "Is this a bar or a coffee shop?"

    hide max_talk_normal onlayer foreground
    show maximo_default onlayer foreground zorder 1
    p "{i}I shrugged{/i}"

    hide screen trust_display
    menu:
        "Nah, just for fun.":
            p "So... this drink is for...?"
            jump maximo_response
        
    label maximo_response:
        show screen trust_display
        narrate "He scoffed before replying"

        hide maximo_default onlayer foreground
        show max_talk_normal onlayer foreground zorder 1
        c1m "{b}Maximo.{/b}"

        hide max_talk_normal onlayer foreground
        show maximo_default onlayer foreground zorder 1
        p "Noted."

        hide screen trust_display
        show maximo_default onlayer foreground zorder 1 at SPRITE1_pos with ease
        jump maximo_drink

    label maximo_drink:
        window hide
        $ result = renpy.call_screen("beer_button")
        if result == "beer_done":
            show m_glass_1 onlayer foreground zorder 2:
                    xpos 0.37 
                    ypos 0.3
            # Play sound
            play sound "audio/drink_1.mp3"

            # Pause for duration of audio
            $ renpy.pause(2.0, hard=True)  # hard=True disables skipping

            # Re-enable skipping
            $ _preferences.skip_enabled = True
            show m_glass_1 onlayer foreground zorder 2:
                xpos 0.37 
                ypos 0.3
            
        $ result = renpy.call_screen("matcha_button")
        hide m_glass_1 onlayer foreground zorder 2
        if result == "matcha_done":
            show m_glass_2 onlayer foreground zorder 2:
                    xpos 0.37 
                    ypos 0.3
            # Play sound
            play sound "<from 1.00 to 2.00>powder.mp3"

            # Pause for duration of audio
            $ renpy.pause(2.0, hard=True)  # hard=True disables skipping

            # Re-enable skipping
            $ _preferences.skip_enabled = True
            show m_glass_2 onlayer foreground zorder 2:
                xpos 0.37 
                ypos 0.3

        $ result = renpy.call_screen("shroom_button")
        hide m_glass_2 onlayer foreground zorder 2
        if result == "shroom_done":
            show m_glass_3 onlayer foreground zorder 2:
                    xpos 0.37 
                    ypos 0.3
            # Play sound
            play sound "<from 3.40 to 4.30>drop foam.mp3"

            # Pause for duration of audio
            $ renpy.pause(2.0, hard=True)  # hard=True disables skipping

            # Re-enable skipping
            $ _preferences.skip_enabled = True
            show m_glass_3 onlayer foreground zorder 2:
                xpos 0.37 
                ypos 0.3

        $ result = renpy.call_screen("maximo_serve_button")
        hide m_glass_3 onlayer foreground zorder 2
        if result == "serve_done":
            show m_glass_3 onlayer foreground zorder 2:
                xpos 0.37 
                ypos 0.3

            # Play sound
            play sound "<from 5.70 to 6.00>click.mp3" volume 1.0

            # Pause for duration of audio
            $ renpy.pause(0.1, hard=True)  # hard=True disables skipping

            # Re-enable skipping
            $ _preferences.skip_enabled = True
            jump end_maximo_drink
        
    label end_maximo_drink:
        show m_glass_3 onlayer foreground zorder 2:
            xpos 0.37 
            ypos 0.3

        show m_glass_3 onlayer foreground zorder 2 at drink_pos with ease
        hide maximo_default onlayer foreground
        show max_talk_normal onlayer foreground
        show screen trust_display
        c1m "Ever experienced love at first sight?"
                
        hide screen trust_display
        #-------------------- ROUND 1 -------------------- 
        label maximo_round1:  
            show maximo_soft onlayer foreground 
            menu:
                "Huh?":
                    show screen trust_display

                    hide maximo_soft onlayer foreground
                    show max_talk_soft onlayer foreground zorder 1
                    c1m "Like y'know..."
                    c1m "Seeing someone for the first time and immediately knowing that they're \"the one\"."

                    hide max_talk_soft onlayer foreground
                    show maximo_soft onlayer foreground zorder 1
                    hide screen trust_display
                    menu:
                        "How is that even possible?":
                            jump bad_maximo_r1
                        "Oh... Yeah, I get what you mean. What about it?":
                            jump good_maximo_r1
                "Excuse me?":
                    show screen trust_display

                    hide maximo_soft onlayer foreground
                    show max_talk_soft onlayer foreground zorder 1
                    c1m "Like y'know..."
                    c1m "Seeing someone for the first time and immediately knowing that they're \"the one\"."

                    hide max_talk_soft onlayer foreground
                    show maximo_soft onlayer foreground zorder 1
                    hide screen trust_display
                    menu:
                        "How is that even possible?":
                            jump bad_maximo_r1
                        "Oh... Yeah, I get what you mean. What about it?":
                            jump good_maximo_r1

                    label bad_maximo_r1:
                        show screen trust_display
                        $ maximo_trust -= 1

                        narrate "You frowned at the thought."
                        p "{i}Falling in love is just as silly as seeing an unicorn running down the rainbow: {b}It's impossible.{/b}{/i}"
                        hide maximo_soft onlayer foreground
                        show maximo_default onlayer foreground zorder 1
                        p "How is that even possible? I mean..."

                        narrate "Maximo lets out a huff...{w=0.5} Like how a horse would do it."
                        hide maximo_default onlayer foreground
                        show maximo_annoyed onlayer foreground zorder 1
                        narrate "He gave you a quick glare."

                        p "{i}{cps=15}Weird...{/cps}{/i}"
                        narrate "But you just shrugged it off."

                        hide maximo_annoyed onlayer foreground
                        show max_talk_normal onlayer foreground zorder 1
                        c1m "It is possible."

                        hide max_talk_normal onlayer foreground
                        show maximo_default onlayer foreground zorder 1
                        narrate "He said with a stern voice."

                        hide screen trust_display
                        menu:
                            "How so?":
                                jump maximo_round2

                    label good_maximo_r1:
                        show screen trust_display
                        $ maximo_trust += 0

                        p "Oh...{w=0.5} Yeah, I get what you mean. What about it?"
                        
                        hide maximo_soft onlayer foreground
                        show maximo_smileblush onlayer foreground zorder 1
                        narrate "Maximo smiled at himself"

                        hide maximo_smileblush onlayer foreground
                        show max_talk_soft onlayer foreground zorder 1
                        c1m "Nothing. It's just there's this girl I---"

                        hide max_talk_soft onlayer foreground
                        show maximo_nervous onlayer foreground zorder 1
                        narrate "He paused, as if he just realized something"

                        hide maximo_nervous onlayer foreground
                        show maximo_default onlayer foreground zorder 1
                        narrate "But immediately composed himself with a soft cough"

                        
                        hide maximo_default onlayer foreground
                        show max_talk_normal onlayer foreground zorder 1
                        c1m "Nevermind"

                        hide max_talk_normal onlayer foreground
                        show maximo_default onlayer foreground zorder 1
                        hide screen trust_display
                        menu: 
                            "Nah, I'm curious now.{w=0.5} Go on, spill the tea.":
                                show screen trust_display
                                
                                hide maximo_default onlayer foreground
                                show max_talk_soft onlayer foreground zorder 1
                                c1m "It's...{w=0.5} complicated..."
                                
                                hide max_talk_soft onlayer foreground
                                show maximo_soft onlayer foreground zorder 1
                                hide screen trust_display
                                menu:
                                    "How so?":
                                        jump maximo_round2
                
        #-------------------- ROUND 2 --------------------
        label maximo_round2:
            show screen trust_display
            
            hide maximo_soft onlayer foreground
            show maximo_defopen onlayer foreground zorder 1
            narrate "Maximo sighed."

            hide maximo_defopen onlayer foreground
            show max_talk_normal onlayer foreground zorder 1
            c1m "So...{w=0.5} there's this story going around our small barrio."
            c1m "It's about a very beautiful girl and a...{w=0.5}{cps=20}{i} tikbalang.{/i}{/cps}"
            c1m "Have you ever heard of them?"

            hide max_talk_normal onlayer foreground
            show maximo_default onlayer foreground zorder 1
            hide screen trust_display
            menu: 
                "Yeah, I have.":
                    jump maximo_story_continue
                "Not really, what is it?":
                    jump maximo_story_continue

            label maximo_story_continue:
                show screen trust_display

                narrate "Maximo nodded"

                hide maximo_defopen onlayer foreground
                show max_talk_normal onlayer foreground zorder 1
                ################################ MAXIMO MAIN STORY ################################
                c1m "Tikbalang is basically  a half-human, half-horse hybrid with the head of a horse and the body of a human."
                c1m "They usually roam the human realm in their human form to find a lover."
                c1m "Some even say that if a tikbalang gets married succesfully, the sun will shine and the rain falls at the same time"

                c1m "Now, back to the story. So there's this girl I--"
                hide max_talk_normal onlayer foreground
                show maximo_softopen onlayer foreground zorder 1
                narrate "He cleared his throat"

                hide maximo_softopen onlayer foreground
                show max_talk_soft onlayer foreground zorder 1
                c1m "So there's this girl a tikbalang fell in love with." #Return to first expression
                c1m "Actually? Let me start from the beginning."
                c1m "A young tikbalang went out of his realm one day as it's his finally his time to go find a bride."
                c1m "He goes out every noon to night, hiding behind the bushes as he spectates everyone in the village near the tikbalangs' realm"
                c1m "Its been weeks and yet he couldn't find anyone that suits his taste."
                c1m "Close to giving up, the tikbalang went to the small bank just a few minutes away from the village to rehydrate himself and rest."
                c1m "As he took a few sips from the river bank's water, there he saw a beautiful lady doing her laundry at that very place."
                
                hide max_talk_soft onlayer foreground
                show max_talk_smileblush onlayer foreground zorder 1
                c1m "She looked absoloutely breathataking.{w=0.5} The way the water runs down her body---"

                hide max_talk_smileblush onlayer foreground
                show maximo_nervous onlayer foreground zorder 1
                hide screen trust_display
                menu:
                    "WOAH, let's keep it PG here, yea?":
                        jump maximo_story_continue_pt2

            label maximo_story_continue_pt2:
                show screen trust_display

                hide maximo_nervous onlayer foreground
                show max_talk_blush onlayer foreground zorder 1
                c1m "My bad. As I was saying, she looked beautiful."

                c1m "The tikbalang made sure to keep himself hidden so he can still {i}appreciate{/i} the view."
                c1m "And since then, the tikbalang kept following the said girl---{w=0.5} That later he found out she was named {i}Rosa{/i}"
                c1m "She's all every tikbalang could ever ask for---{w=0.5} Beautiful and innocent."
                c1m "The tikbalang followed her everywhere;{w=0.5}{cps=28} her house,{w=0.5} to the riverbank whenever she washes her clothes,{w=0.5} the kindergarten where she teaches,{w=0.5} even in her sleep---{/cps}"

                hide max_talk_blush onlayer foreground
                show max_talk_smileblush onlayer foreground zorder 1
                c1m "Goodness, {bt=3}she's even prettier when she sleeps.{/bt}"

                hide max_talk_smileblush onlayer foreground
                show maximo_smileblush onlayer foreground zorder 1 
                narrate "He sighs, satisfied, before continuing"

                hide maximo_smileblush onlayer foreground
                show max_talk_soft onlayer foreground zorder 1
                c1m "The tikbalang couldn't help but fall in love more with her beauty as he kept himself hidden behind the shadows."
                c1m "He knows shes \"the one\" for him."

                hide max_talk_soft onlayer foreground
                show maximo_soft onlayer foreground zorder 1
                hide screen trust_display
                menu:
                    "Is it really love...?":
                        show screen trust_display
                        hide maximo_soft onlayer foreground
                        show maximo_default onlayer foreground zorder 1
                        
                        p "That's kinda creepy and weird."
                        p "Is it really love if the tikbalang was only focusing on Rosa's physical appearance?"
                        jump maximo_story_continue_pt3
                    
            label maximo_story_continue_pt3:

                hide maximo_default onlayer foreground
                show max_talk_mad onlayer foreground zorder 1
                
                m "Excuse me?"
                
                hide max_talk_mad onlayer foreground
                show maximo_annoyed onlayer foreground zorder 1
                narrate "You shrugged"

                hide screen trust_display
                menu:
                    "You heard me.":
                        show screen trust_display
                        $ maximo_trust -= 1
                        p "Based from the story you just told me, it's clearly just pure obsession and not love."
                        jump maximo_story_continue_pt4
                    
            label maximo_story_continue_pt4:
                
                hide maximo_annoyed onlayer foreground
                show max_talk_mad onlayer foreground zorder 1

                c1m "{glitch=25.0}How can you say that?{/glitch}{w=0.5} You look young, I doubt you have fallen in love."
                hide max_talk_mad onlayer foreground
                play sound "Glitch.mp3"
                show maximo_glitched
                pause 1.5
                hide maximo_glitched
                
                show maximo_annoyed onlayer foreground zorder 1
                p "He's...{w=0.5} Glitching?{w=0.5} What is going on?"

                narrate "{cps=20}Maximo looked...{w=0.5} angry...{/cps}"

                hide screen trust_display
                menu:
                    "I stand by my point.":
                        jump bad_maximo_r2
                    "Apologize":
                        jump good_maximo_r2_0
                    
            label bad_maximo_r2:
                show screen trust_display

                hide maximo_annoyed onlayer foreground
                show max_talk_mad onlayer foreground zorder 1
                c1m "You're being ridiculous.{w=0.5} I get to decide who I want to marry"

                hide max_talk_mad onlayer foreground
                show maximo_annoyed onlayer foreground zorder 1
                p "{i}I...?{/i}"

                hide maximo_annoyed onlayer foreground
                show max_talk_mad onlayer foreground zorder 1
                c1m "She's beautiful, and that's all what matters.{w=0.5} Nothing can get in between our love."

                hide max_talk_mad onlayer foreground
                show maximo_annoyed onlayer foreground zorder 1        
                hide screen trust_display
                menu:
                    "You're missing my point---":
                        stop music
                        show screen trust_display
                        play sound "<from 2.10 to 3.50>slam.mp3" volume 5.0
                        narrate "Maximo suddenly stood up and slammed his drink on the table, causing the glass to break into pieces" with vpunch
                        
                        hide maximo_annoyed onlayer foreground
                        show max_talk_mad onlayer foreground zorder 1
                        c1m "I dont want to hear it!" 

                        hide max_talk_mad onlayer foreground
                        show maximo_annoyed onlayer foreground zorder 1
                        hide screen trust_display
                        menu:
                            "Sir---":
                                show screen trust_display
                                hide maximo_annoyed onlayer foreground
                                hide screen trust_display
                                play sound "Glitch.mp3"
                                show maximo_glitched
                                pause 0.9
                                hide maximo_glitched
                                show screen trust_display
                                show maximo_annoyed onlayer foreground zorder 1
                                p "{i}He's glitching...{w=0.5} Is he a...{w=0.5}{cps=20} Tikbalang?{/cps}{/i}"
                                p "{i}Is he the tikbalang in the story?{w=0.5} No wonder he looks so affected.{/i}"

                                hide screen trust_display
                                hide maximo_annoyed onlayer foreground with easeoutleft
                                show screen trust_display
                                narrate "Maximo immediately made his way to the door"
                                narrate "You panicked---{w=0.5} He didn't even pay for the drink yet?!"

                                hide screen trust_display
                                menu:
                                    "Follow him":
                                        show screen trust_display
                                        $ maximo_trust -= 2

                                        narrate "You abruptly left the counter to follow Maximo."

                                        p "Sir--!"
                                        hide screen trust_display
                                        hide m_glass_3 onlayer foreground
                                        hide bar_table onlayer foreground zorder 1 
                                        with fastdissolve

                                        scene black
                                        pause 1.5
                                        #JUMPSCARE SEQUENCE TO BE INSERTED IN CHECK
                                        call check_maximo_trust from _call_check_maximo_trust_1 
                                    "Apologize":
                                        jump good_maximo_r2_1
            
            label good_maximo_r2_0:
                $ maximo_trust += 0
                play music "bar_2.mp3"
                narrate "Before Maximo could reach for the door handle"

                show maximo_annoyed onlayer foreground zorder 1 with easeinleft
                p "Senior Maximo, I'd like to apologize."

                narrate "Maximo halted, but didn't turn to look at you"

                hide screen trust_display
                menu:
                    "What I was trying to say is that...":
                        show screen trust_display
                        p "What I was trying to say is that, it would be nicer if you actually get to know the person and love them for who they are."
                        p "There's so much more to love other than just physical appearance."

                        hide maximo_annoyed onlayer foreground
                        show maximo_default onlayer foreground zorder 1
                        narrate "You saw Maximo relax"
                        narrate "Maximo sighed and went back to his seat"

                        hide maximo_default onlayer foreground
                        show  max_talk_normal onlayer foreground zorder 1
                        c1m "What do you suggest I do?"

                        hide max_talk_normal onlayer foreground
                        show maximo_default onlayer foreground zorder 1
                        narrate "You smiled..."

                        hide maximo_default onlayer foreground zorder 1
                        hide m_glass_3 onlayer foreground
                        hide bar_table onlayer foreground zorder 1 
                        with fastdissolve
                        jump maximo_end_day

            label good_maximo_r2_1:
                $ maximo_trust += 0
                play music "bar_2.mp3"
                hide m_glass_3 onlayer foreground
                hide bar_table onlayer foreground zorder 1 
                with fastdissolve
                scene bar_inside with dissolve

                narrate "Before Maximo could reach for the door handle"

                show maximo_annoyed onlayer foreground zorder 1 with easeinleft
                p "Senior Maximo, I'd like to apologize."

                narrate "Maximo halted, but didn't turn to look at you"

                hide screen trust_display
                menu:
                    "What I was trying to say is that...":
                        show screen trust_display
                        p "What I was trying to say is that, it would be nicer if you actually get to know the person and love them for who they are."
                        p "There's so much more to love other than just physical appearance."

                        hide maximo_annoyed onlayer foreground
                        show maximo_default onlayer foreground zorder 1
                        narrate "You saw Maximo relax"
                        narrate "Maximo sighed and went back to his seat"

                        hide maximo_default onlayer foreground
                        show  max_talk_normal onlayer foreground zorder 1
                        c1m "What do you suggest I do?"

                        hide max_talk_normal onlayer foreground
                        show maximo_default onlayer foreground zorder 1
                        narrate "You smiled..."

                        hide maximo_default onlayer foreground zorder 1 with fastdissolve
                        jump maximo_end_day

        label maximo_end_day:
            hide screen trust_display
            scene black with fade
            pause 1.0
            ############################# SCENE TRANSITION #############################
            show text "{i}{size= 50}The night continued where you two talked about how to win Rosa's heart in a genuine way.{/size}{/i}" at truecenter
            with dissolve
            pause 4.0
            hide text with dissolve
            pause 1.0
            ############################################################################
            show text "{i}{size= 50}No more creepy stalking and all that stuff, which took Maximo awhile to fully convince him that it's for the better.{/size}{/i}" at truecenter 
            with dissolve
            pause 4.0
            hide text with dissolve
            pause 1.0
            ############################################################################
            show text "{i}{size= 50}Maximo bid his goodbye and you called it a night.{/size}{/i}" at truecenter
            with dissolve
            pause 3.0
            hide text with dissolve
            pause 1.0
            ############################################################################

            menu:
                "1st shift ends":
                    call screen status_menu_day2
                    
                    scene bar_counter with dissolve
                    show bar_table onlayer foreground zorder 2
                    show dieg_talk_normal onlayer foreground zorder 1 at center with easeinright

                    d "You handled that customer pretty well."

                    hide dieg_talk_normal onlayer foreground
                    show diego_default onlayer foreground zorder 1 at center
                    narrate "Diego said from the other side of the counter, he was spectating silently the whole time"

                    menu:
                        "{i}Laugh awkwardly{/i}":
                            p "Heh...{w=0.5} It was nerve wrecking."

                            hide diego_default onlayer foreground
                            show dieg_talk_normal onlayer foreground zorder 1 at center

                            d "You''ll get used to it."

                            hide dieg_talk_normal onlayer foreground
                            show diego_default onlayer foreground zorder 1 at center
                            menu:
                                "{i}Used to it?{/i}":
                                    p "So...{w=0.5} You're saying that..."

                                    hide diego_default onlayer foreground
                                    show dieg_talk_normal onlayer foreground zorder 1 at center
                                    d "This isn't just a normal bar, you see."
                                    d "I thought Theresa already mentioned that?"
                                    
                                    hide dieg_talk_normal onlayer foreground
                                    show diego_default onlayer foreground zorder 1 at center
                                    narrate "You shook your head"

                                    hide diego_default onlayer foreground
                                    show dieg_talk_normal onlayer foreground zorder 1
                                    d "I see.{w=0.5} Well, you better watch your words when talking to patrons."
                                    d "You don't know what they can do."

                                    hide dieg_talk_normal onlayer foreground
                                    show diego_default onlayer foreground zorder 1 at center
                                    menu:
                                        "Like?":
                                            hide diego_default onlayer foreground
                                            show dieg_talk_normal onlayer foreground zorder 1
                                            d "Dunno, they might kill you or something."
                                            
                                            hide dieg_talk_normal onlayer foreground
                                            show diego_default onlayer foreground zorder 1 at center
                                            menu:
                                                "WHAT?!":

                                                    hide diego_default onlayer foreground
                                                    show dieg_laugh_talk onlayer foreground zorder 1 at center
                                                    d "{bt=3}I'm joking...{/bt}{w=0.5} Unless?"

                                                    hide dieg_laugh_talk onlayer foreground
                                                    show dieg_close_eye onlayer foreground zorder 1 at center
                                                    menu:
                                                        "Senior Diego!":
                                                            scene black with dissolve
                                                            hide dieg_close_eye onlayer foreground zorder 1 
                                                            hide bar_table onlayer foreground zorder 1 
                                                            with fastdissolve
                                                            
                                                            jump DAY3

######## DAY 3 IN script_DAY3.rpy ########