label JuansEatingHabit:
    stop music

    scene black with dissolve
    show text("{size=60}Juan's eating habit{/size}") with dissolve
    with Pause(2)
    hide text with dissolve

    play music "assets/BGM/HelloHowAreYou.mp3"

    scene daytimeBedroom with dissolve
    show Joseph laugh
    Joseph_center "Ok little Juan here I go!"
    Joseph_center "A,B,C,D,E,F - "
    show mode confirm with dissolve
    call screen ABCD with dissolve
    hide mode confirm with dissolve

    if alphabet_selected == "G":
        Joseph_center "Great!"
        Joseph_center "I think you're ready for school now. Don't you think so too, little Juan? Huh? Huh?"
        Juan_center "Hehe"
        Joseph_center "Haha just kidding"
        Joseph_center "But you're really good!"
    else:
        show Joseph neutral
        Joseph_center "Haha nice try."
        Joseph_center "But i can see you're trying your best"
        none "Juan chuckles."
        Joseph_center "Okay let's do it again.."
        Juan_center "Yeah!"

    none "(While Joseph and Juan were spending time together learning the Alphabet.)"
    none "(Mary comes in from the kitchen and called Joseph and Juan)"

    show Mary neutralright with easeinright
    show Joseph panLeft
    Mary_right "Dad, Juan, come on it's lunch time!"
    Joseph_left "Great job, little Juan!"
    Juan_center "Yay!"
    Joseph_left "Ok Juan we should do more later, ok big champ?"
    Joseph_left "But first we should have lunch. Get a little food in Juan's little tummy."
    show Mary surprised
    Mary_right "Remember Juan you should never skip any meals throughout the day. Food gives you energy."
    show Joseph talking with dissolve
    Joseph_left "Yes Juan, Skipping meals is bad for you."
    show Joseph neutral with dissolve
    Mary_right "Especially for your young body, you're quite vulnerable to any micro-nutrient deficiencies."
    Juan_center "Yes mom!."
    show Mary smile
    Mary_right "Anyways let's go eat now."

    scene black with dissolve
    none "(And so, the family went to the dining table and get lunch together.)"
    scene kitchen with dissolve

    show Joseph neutralright with dissolve
    show Mary neutralLeft with dissolve
    Mary_left "Ok before we eat, let's give our thanks prayer to Papa Jesus."
    Juan_center "Okay!"
    Joseph_right "Okay!"
    none "(The family closed their eyes and pray as they give thanks for their wonderful food.)"
    Mary_left "Amen."
    Joseph_right "Amen."
    Juan_center "Amen."
    show Mary smile
    Mary_left "Let's eat!"
    Juan_center "Yay!"
    scene table with dissolve
    Mary_center "Here's for you Juan."

    Mary_center "Carrots, Mashed Potato and Banana"
    Joseph_center "Wow! this taste really good!"

    show mode confirm with dissolve
    call screen FoodPlate with dissolve
    hide mode confirm with dissolve
    scene kitchen with dissolve
    show Mary neutralLeft with dissolve
    show Joseph neutralright with dissolve

    if food_eaten < 3:
        $ Choice_ch3 = "picky"
        $ renpy.notify("Picky kid perk unlocked!")
        none "(Juan ate some of the food and leave everything on the plate.)"
        Juan_center "Yummy!"
        show Mary smile
        Mary_left "Glad you liked it!"
        show Mary surprised
        Mary_left "But your plate seems like it's not done yet Juan."
        show Joseph laugh
        Joseph_right "It's really delicious Ma!"
        Juan_center "I don't like those food Mom."
        show Mary smile
        Mary_left "Oh well, hahaha."

    else:
        $ Choice_ch3 = "healthy"
        $ renpy.notify("Healthy kid perk unlocked!")
        none "(Juan ate everything and left nothing on his plate.)"
        Juan_center "Yummy!"
        show Mary smile
        Mary_left "Glad you liked it!"
        show Joseph laugh
        Joseph_right "It's really delicious Ma!"
        Juan_center "Delicious!"

    scene black with dissolve
    none "(After lunch Joseph and Juan went back to play)"
    scene daytimeBedroom with dissolve
    show Joseph laugh with dissolve
    none "Joseph laughs"
    Juan_center "Hahaha dad that's really cool!"
    show Joseph neutral
    Joseph_center "Anyway we should do this again next time."
    Juan_center "Yay!"
    none "(And so little Juan is really happy after playing with Joseph)"
    scene black with dissolve

    jump JuansLittleSister

#====================custom screens for choices=====================

    screen ABCD():
     modal True

     $ A = Text("A",size=200, bold=True, color="#FF5631")
     $ G = Text("G",size=200, bold=True, color="#5DFF31")
     $ P = Text("P",size=200, bold=True, color="#E631FF")
     text("A B C D E F -?") size 60 xpos 0.4 ypos 30

     hbox xalign 0.5 yalign 0 spacing 200:
        textbutton (A) ypos 300 action [SetVariable("alphabet_selected", "A"),Return()]
        textbutton (G) ypos 300 action [SetVariable("alphabet_selected", "G"),Return()]
        textbutton (P) ypos 300 action [SetVariable("alphabet_selected", "P"),Return()]



    screen FoodPlate():
        modal True
        $ Done= Text("Done",size=100, bold=True)
        $ AllDone= Text("Done",size=100, bold=True, color="#FFEC31")
        $ potato = Image("assets/Sprites/Items/mashedpotato.png")
        $ banana = Image("assets/Sprites/Items/bananas.png")
        $ carrot = Image("assets/Sprites/Items/carrots.png")
        $ eaten = "not yet"

        hbox xalign 0.5:
            text(Text("Juan is hungry, Juan should eat his food.",size=50))
        hbox xpos 650 ypos 250:
            if carrot_selected == False:
                imagebutton idle Transform(carrot, zoom=0.6) action [SetVariable("carrot_selected", True),SetVariable("food_eaten", food_eaten + 1)]
        hbox xalign 0.5 ypos 450:
            if potato_selected == False:
                imagebutton idle Transform(potato, zoom=0.6) action [SetVariable("potato_selected", True),SetVariable("food_eaten", food_eaten + 1)]
        hbox xpos 1000 ypos 250:
            if banana_selected == False:
                imagebutton idle Transform(banana, zoom=0.6) action [SetVariable("banana_selected", True),SetVariable("food_eaten", food_eaten + 1)]

        hbox:
            if food_eaten >= 3:
                textbutton (AllDone) xpos 1500 action Return()
            elif food_eaten >=1:
                textbutton (Done) xpos 1500 action Return()


    return
