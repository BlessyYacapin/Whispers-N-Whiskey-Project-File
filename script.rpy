###################### TRANSITION ######################
define fastdissolve = Dissolve(0.15)
########################################################

########################################################
transform drink_position:
    xpos 0.43
    ypos 0.25
    zoom 0.3
########################################################

##################### PRESPLASH ########################
define config.minimum_presplash_time = 3.0
########################################################

###################### SPLASH SCREEN ###################
image dev_logo = "images/CodeBERRY.png"
image title = "images/game_logo.png"

init python:
    persistent.seen_splash = False

label before_main_menu:
    if persistent.seen_splash:
        return

    scene black
    pause 1.0

    show dev_logo at truecenter with dissolve
    pause 3.0

    hide dev_logo with dissolve
    pause 1.0

    show text "{size= 42}{b}Created by BSEMC-DAT Students{/b}{size= 35}\nIszabela Caszandra Cardona\nGabrielle Revecho\nBlessy Yacapin \nat Bukidnon State University{/size}\n\n{b}Instructor:{/b} Mark Daniel G. Dacer\n\n{b}Subject:{/b} Intro to Game Design & Development\n\n{i}S.Y. 2025-2026{/size}{/i}" at truecenter with dissolve
    pause 4.0

    hide text with dissolve
    pause 1.0

    show text "{size= 42}{b}In collaboration with{/b} Data Structures & Algorithm \n{b}Instructor:{/b} Rov Japheth G. Oracion{/size}" at truecenter with dissolve
    pause 4.0

    hide text with dissolve
    pause 1.0

    show text "{b}{size= 77}WARNING{/size}{/b}\n\n{size= 45}This game is a {color=#ad0013}work of fiction{/color}\n\nIt features depictions of: \n{color=#ad0013}Alcoholic drinks and may include animated effects, flickering lights, or rapid visual transitions{/color} that could potentially trigger discomfort or photosensitive reactions in some players.\n\nIf you are sensitive to such content, please proceed with caution.{/size}" at truecenter with dissolve
    pause 10.0

    hide text with dissolve
    pause 1.5

    show title at truecenter with dissolve
    pause 3.0

    hide title with dissolve
    pause 2.0

    $ persistent.seen_splash = True
    return
########################################################


################### GAME STARTS HERE ###################
label start:
    play music "audio/hospital_1.mp3" 
    ###################### OPENING #####################
    "{i}Beep... beep...{/i}" # Insert audio
    
    scene hospital 
    play sound "audio/Cough.mp3" volume 0.75
    "Ma..."

    m "Nak...{w=0.5}you already know I dont have much time."

    "Ma, don't say that! I will find a job, buy you medicines that you need." 
    "Just don't leave me... {w=0.5}{cps=30}not yet...{/cps}"

    m "{i}*chuckles*{/i}"
    show cut1 with dissolve
    m "Promise me one thing, nak"

    "Stop... {w=0.5}You're acting like you're gonna leave me. I don't like it--"

    hide cut1
    show cut2 
    with dissolve
    m "Promise me you'll take care of yourself even when I'm gone." 
    m "Help people and continue being kind to everyone"

    "Ma---"

    m "Promise me."
    
    hide cut2
    # Choice pt.1
    menu:
        "... I promise":
            jump choice1_yes
        "Okay...":
            jump choice1_yes

    label choice1_yes:
        $ menu_flag = True
        show cut2
        m "That's good to hear"
        jump choice1_done

    label choice1_done:
        # ... The game continues here.
    
    hide cut2
    show cut3
    with dissolve

    "What's this?"

    m "Go to that address around that specific time. I'm sure he'll help you out."

    hide cut3  with dissolve
    "He?{w=0.5} Who's {i}he?{w=0.5}{/i}"

    m "{b}Senior Diego{/b}. He'll help you find a job..."
    
    stop music
    play sound "<from 0.00 to 8.50>audio/hospital_2.mp3" noloop

    "Ma, I don't understand---"


    "Ma? {w=1.0}{sc=3}Ma!{w=1.0}{/sc} {sc=2}Nurse! Help!{/sc}" with hpunch

    scene black 
    with dissolve
    pause 8.0
    stop sound
    ################## SCENE TRANSITION ##################
    show text "{i}{size=50}On the way to the bar{/size}{/i}" at truecenter
    pause 3
    hide text
    with dissolve
    ######################################################
    
    play music "audio/Night Street.mp3"
    play sound "<from 0.00 to 2.00>Leaves Crunching.mp3" noloop

    "Is this really the right way? {w=0.5}The rela refused to go further than this."
    "My last 150 pesos..."
    "{cps=10}...{w=1.0}{/cps}all gone."
    play sound "<from 0.00 to 1.00>sigh.mp3" noloop
    "{cps=10}...{/cps}"
    "It's been days since mama died... {w=0.5}I miss her already.."

    play sound "<from 2.00 to 4.00>Leaves Crunching.mp3" noloop
    narrate "You continued walking"

    play music "audio/bar_1.mp3" fadeout 1.0 fadein 0.5 volume 0.025
    "Music?"
    "Where is it coming from?"

    # Choice pt.2
    menu:
        "Find where it is coming from":
            jump find_music
        "Ignore and leave":
            jump ignore_music

    # Choice pt.2.1
    label find_music:
        stop music
        play music "audio/forest.mp3"
        $ renpy.music.set_volume(0.2, channel="music")
        narrate "You see a sign that says: {b}'This way to Sesión del Barrio'{/b}"

        scene forest_1 with dissolve
        show hand
        "Guess I'm going the right way... {w=0.5}But why is it coming from the middle of the forest?"
        hide hand with fastdissolve

        play sound "<from 4.00 to 6.00>Leaves Crunching.mp3" fadeout 1.0 noloop
        narrate "You walked deeper into the forest"
        "What did my Ma say about going to these kind of places again? I'm pretty sure you need to say something--- ah, right."
        "Tabi tabi po..."
        play music "audio/bar_1.mp3" fadein 1.0 volume 0.1
        narrate "{cps=20}The wind stops. {w=0.5}The music can be heard clearly again{/cps}"

        scene forest_door with dissolve
        "A door...?"

        # Choice pt.3
        menu:
            "Open the door":
                jump open_door

        label open_door:
            scene black
            play sound "audio/door.mp3"
            $ renpy.music.set_volume(1.0, delay=1.0, channel="music")
            "{i}I could feel the cold air greeting my body despite of the jacket im wearing.{/i}"
            "{i}I try to adjust my sight because of the light--- {w=0.5}I couldnt help but feel chills running though my spine as I look around.{/i}"
            "{i}The atmosphere was eerie but comforting in ways I could not explain{/i}"

            ############################# SCENE TRANSITION #############################
            window hide
            show text "{i}{b}{size=50}Sesión del Barrio\nNovember 1, 20XX :: 12MN{/size}{/b}{/i}" at truecenter
            pause 3
            hide text
            with dissolve
            ############################################################################
            
            scene bar_inside

            "Is this place a...{w=0.5} bar?"

            show dieg_shadow at center with easeinright

            unknown "Who goes there?"

            "{i}I froze, composing myself before I turned around to see who's voice was it from {/i}"

            "Good evening... {w=0.5}I was told to come here..."
            show hand with fastdissolve
            "{i}I said as I showed him the piece of paper my Mama gave along with the pendant{/i}"
            hide hand with fastdissolve
            "{i}He inspects the paper and the pendant carefully, my brows furrowed in confusion.{/i}"

            unknown "Very well.{w=0.5} May I ask for you name?"

            $ player_name = renpy.input("Enter name: ", length = 25)
            $ player_name = player_name.strip()
            if player_name == "":
                $ player_name = "Alex"
            
            ################ PLAYER ################
            define p = Character ("[player_name]", color="#ffffff")
            ########################################

            p "My name is [player_name] Gonzales..."

            unknown "{i}He raised his brow{/i}"
            unknown "Gonzales?{w=0.5} By any chance, are you related to Theresa Gonzales?"

            p "{i}I nodded my head{/i}"
            p "She's my mother, the one who told me to go here..."
            p "She told me this place can help me get a job..."

            unknown "I see... "

            hide dieg_shadow
            show dieg_talk_normal at center with fastdissolve

            d "Well then, I am Diego Concepcion, the owner of {i}Sesión del Barrio{/i}."
            d "They call me Senior Diego."
            d "Your mother,{w=0.5} Theresa Gonzales,{w=0.5} used to work here for me as a bartender"

            hide dieg_talk_normal
            show dieg_default at center

            p "{i}Senior Diego handed me back the paper and pendant{/i}"

            hide dieg_default
            show dieg_talk_normal at center
            d "Keep that pendant with you at all times, it'll keep you safe for a while."
            d "Make sure to not let it break"

            hide dieg_talk_normal
            show dieg_default at center

            p "{i}I reluctantly nod my head in response{/i}"

            hide dieg_default
            show dieg_talk_normal at center

            d "Follow me, I'll show you your room upstairs."
            d  "For now, rest. Your training starts tomorrow."

            hide dieg_talk_normal
            show dieg_default at center

            jump DAY_1

    # Choice pt.2.2
    label ignore_music:
        stop music
        "Y'know what? I'll just go. It's too scary out here."

        play sound "<from 2.00 to 4.00>Leaves Crunching.mp3" noloop

        "Right, can't go back."
        "I dont know where the way back is, it's too dark."

        "Guess I dont have any other choice."

        jump find_music 


####################### DAY 1 ########################
    label DAY_1:
        scene black with dissolve
        pause 2.0
        ############################# SCENE TRANSITION #############################
        stop music
        play sound "<from 14.30 to 16.80>transition_1.mp3"
        show d1 at truecenter
        pause 3
        hide d1 with dissolve
        ############################################################################
        play music "audio/bar_1.mp3"
        scene bar_counter
        show bar_table onlayer foreground zorder 2
        show dieg_talk_normal onlayer foreground zorder 1 at center with easeinright
        
        d "Had a good sleep?"
        
        hide dieg_talk_normal onlayer foreground 
        show dieg_default onlayer foreground zorder 1 at center
        menu:
            "Yes!":
                jump day1_tutorial

        ######### DAY 1 TUTORIAL START #########
        label day1_tutorial:
            hide dieg_default onlayer foreground 
            show dieg_talk_normal onlayer foreground zorder 1 at center 

            d "Good, good"
            d "Well then, let us begin your training"
            jump tutorial
            
        label tutorial:
            $ cup_stage_tut = 0
            d "First, let's start simple"
            d "Click the gin bottle on the counter"

            hide dieg_talk_normal onlayer foreground
            show dieg_default onlayer foreground zorder 1 at center

            show dieg_default onlayer foreground zorder 1 at SPRITE1_pos with ease

            window hide
            $ result = renpy.call_screen("gin_button")
            if result == "gin_done":
                show cup_1 onlayer foreground zorder 2:
                    xpos 0.45 
                    ypos 0.34 
                    zoom 1.1

                # Play sound
                play sound "audio/drink_1.mp3"

                # Pause for duration of audio
                $ renpy.pause(2.0, hard=True)  # hard=True disables skipping

                # Re-enable skipping
                $ _preferences.skip_enabled = True
                show cup_1 onlayer foreground zorder 2:
                    xpos 0.45 
                    ypos 0.34 
                    zoom 1.1
                window show

                hide dieg_default onlayer foreground
                show dieg_talk_normal onlayer foreground zorder 1 at SPRITE1_pos
                d "Good. You poured the gin nicely"
                
            d "Next, let's add some sweetness. Click the honey."

            hide dieg_talk_normal onlayer foreground
            show dieg_default onlayer foreground zorder 1 at SPRITE1_pos

            window hide
            $ result = renpy.call_screen("honey_button")
            hide cup_1 onlayer foreground zorder 2
            if result == "honey_done":
                show cup_2 onlayer foreground zorder 2:
                    xpos 0.45 
                    ypos 0.34 
                    zoom 1.1

                # Play sound
                play sound "<from 5.00 to 6.00>Thick Liquid.mp3"

                # Pause for duration of audio
                $ renpy.pause(1.0, hard=True)  # hard=True disables skipping

                # Re-enable skipping
                $ _preferences.skip_enabled = True
                show cup_2 onlayer foreground zorder 2:
                    xpos 0.45 
                    ypos 0.34 
                    zoom 1.1
                window show

                hide dieg_default onlayer foreground
                show dieg_talk_normal onlayer foreground zorder 1 at SPRITE1_pos

                d "Perfect. Now the mixture looks smoother."

            d "Now, for a little bit of tang, add the lime."

            hide dieg_talk_normal onlayer foreground
            show dieg_default onlayer foreground zorder 1 at SPRITE1_pos

            window hide
            $ result = renpy.call_screen("lime_button")
            hide cup_2 onlayer foreground zorder 2
            if result == "lime_done":
                show cup_3 onlayer foreground zorder 2:
                    xpos 0.45 
                    ypos 0.34 
                    zoom 1.1

                # Play sound
                play sound "<from 1.50 to 2.00>spray.mp3"

                # Pause for duration of audio
                $ renpy.pause(0.2, hard=True)  # hard=True disables skipping

                # Re-enable skipping
                $ _preferences.skip_enabled = True

                show cup_3 onlayer foreground zorder 2:
                    xpos 0.45 
                    ypos 0.34 
                    zoom 1.1
                window show

                hide dieg_default onlayer foreground
                show dieg_talk_normal onlayer foreground zorder 1 at SPRITE1_pos

                d "Nicely done! Almost there."

            d "Finally, click the serve button to finish your first drink."

            hide dieg_talk_normal onlayer foreground
            show dieg_default onlayer foreground zorder 1 at SPRITE1_pos

            window hide
            $ result = renpy.call_screen("serve_button")
            hide cup_3 onlayer foreground zorder 2
            if result == "serve_done":
                show cup_3 onlayer foreground zorder 2:
                    xpos 0.45 
                    ypos 0.34 
                    zoom 1.1

                # Play sound
                play sound "<from 5.70 to 6.00>click.mp3" volume 1.0

                # Pause for duration of audio
                $ renpy.pause(0.1, hard=True)  # hard=True disables skipping

                # Re-enable skipping
                $ _preferences.skip_enabled = True
                jump end_tutorial
        
        label end_tutorial:
            show cup_3 onlayer foreground zorder 2:
                xpos 0.45 
                ypos 0.34 
                zoom 1.1

            hide dieg_default onlayer foreground
            show dieg_talk_normal onlayer foreground zorder 1 at SPRITE1_pos

            d "Great! You have made a drink"
            d "Easy, right? Do you think you can do it?"

            hide cup_3 onlayer foreground zorder 2 with fastdissolve

            hide dieg_talk_normal onlayer foreground
            show dieg_default onlayer foreground zorder 1 at SPRITE1_pos
            show dieg_default onlayer foreground zorder 1 at center with ease
            
            menu:
                "Yeah, I think I got it.":
                    scene black with dissolve
                    hide bar_table onlayer foreground zorder 1
                    hide dieg_default onlayer foreground 
                    with fastdissolve
                    stop music
                    jump DAY2
                "Uhm... Can you please explain it again?":
                    narrate "He sighed"

                    hide dieg_default onlayer foreground
                    show dieg_serious_talk onlayer foreground zorder 1 at center 
                    d "I'm too old for this. But since you asked nicely..."
                    hide dieg_serious_talk onlayer foreground
                    show dieg_default onlayer foreground zorder 1 at center 
                    jump tutorial

######## DAY 2 IN script_DAY2.rpy ########
######## DAY 3 IN script_DAY3.rpy ########
######## DAY 4 IN script_DAY4.rpy ########

    # This ends the game.
    label end:
        stop music
        ############################# SCENE TRANSITION #############################
        pause 1.0
        show text "{i}{size= 80}TO BE CONTINUED...{/size}{/i}" at truecenter
        with dissolve
        pause 4.0
        hide text with dissolve
        pause 1.0
        ############################################################################
        jump credits

    #################################### CREDITS ###################################    
    label credits:
        $ credits_speed = 25 #scrolling speed in seconds
        play music "audio/Main Menu Music.mp3"
        scene black
        $ quick_menu = False

        show title at truecenter with dissolve
        pause 3.0
        hide title with dissolve

        image cred = Text(credits_s, text_align=0.5)
        image thanks = Text("{size=80}Thank you for Playing!", text_align=0.5)
        
        #show scrolling credits
        show cred at Move((0.5, 5.2), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")

        # Pause until credits finish scrolling
        $renpy.pause(credits_speed, hard=True) 

        pause 1.0
        show dev_logo at truecenter with dissolve
        with Pause(3)
        hide dev_logo with dissolve
        with Pause(1)

        show thanks:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        with Pause(3)
        hide thanks with dissolve
        with Pause(3)
        
        return

init python:
    credits = (
        ('Characters', 'Diego'), 
        ('Characters', 'Maximo'), 
        ('Characters', 'Ysabel'),
        ('Characters', 'Dawani'),  
        ('Executive Producer', 'Mark Daniel G. Dacer, MSIT'), 
        ('Game Director', 'Iszabela Caszandra N. Cardona'), 
        ('Story Writer', 'Iszabela Caszandra N. Cardona'), 
        ('Sound Designer', 'Gabrielle Revecho'), 
        ('Programmer', 'Blessy J. Yacapin'), 
        ('Artists', 'Iszabela Caszandra N. Cardona'), 
        ('Artists', 'Gabrielle Revecho'), 
        ('Artists', 'Blessy J. Yacapin'),
        ('UI', 'Customized in Canva'),
        ('Music', 'Made in Audacity'), 
        ('Music', 'Toyy Lao'),
        ('SFX', 'Creator Assets'),
        ('SFX', 'SoundDesignForYou'),
        ('SFX', 'Royalty Free SFX'),
        ('', 'Made by Bukidnon State University BSEMC-DAT Students\nIntro to Game Design & Development\n{size=25}S.Y. 2025-2026{/size}')
    )
    credits_s = "{font=fonts/Belgan Aesthetic.ttf}{size=120}CREDITS\n{/size}{/font}"
    c1 = ''
    for c in credits:
        if not c1==c[0]:
            credits_s += "\n\n\n{font=fonts/Belgan Aesthetic.ttf}{size=83}{color=#FFFFFF}" + c[0] + "\n"
        credits_s += "{font=fonts/Poppins-Regular.ttf}{size=34}{color=#FFFFFF}" + c[1] + "\n"
        c1=c[0]
    credits_s += "\n{font=fonts/Belgan Aesthetic.ttf}{size=83}{color=#ad0013}Engine\n{size=40}" "{font=fonts/Poppins-Regular.ttf}{size=34}{color=#FFFFFF}" + renpy.version()
        

    