﻿# The script of the game goes in this file.

# The game starts here.

label start():

    #============= Major choices==================
    $ Mode = "null"
    $ Choice_ch1 = "null"
    $ Choice_ch3 = "null"
    #=============Minor choices===================
    $ food_eaten = 0
    $ alphabet_selected = "null"
    $ banana_selected = False
    $ carrot_selected = False
    $ potato_selected = False


    jump diffSelect


    return
