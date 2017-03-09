# -*- coding: utf-8 -*-

# PsychoPy 2 - Posner Cueing Task Example w/ Frame Timer
# Dr K McCarty
# Northumbria University
# February 2017

#Import the necessary modules from the Python storage bank

#Create a dictionary called info with the following keys and values:
        # participant   -   '' (an empty string)
        # dateStr       -   data.getDateStr()



###############----------------My Filename when saved----------------------###############

# Below, create a variable called filename that should start with "data/" and adds participant 
# code an underscore (_) and the date - use string addition for this 



###############----------------Windows, Stimuli and Conditions File Stuff------------------------###############

# Create the following below
        # a window, call the variable win. set the resolution to 1024x768, fullscr = False
        # a fixation cross or circle, call this fixation, size 5, line and fill color white
        # a response clock, call this respClock
        # a probe, use an image stim, size 80, mask = gauss, make this whatever color you want
        # a cue, make this a shape stim. we will talk about vertices in developing the shape 



###############-------------Trial/Experiment Handler---------------------------###############

# Create the following below:
        # conditions, using the data.importConditions function import your condition .XLS file

        # trials, initiate a trialHandler and pass the trialList argument to your conditions variable,
        #         set nReps to 5

        # posnerExp, an experiment handler, pass the extraInfo your dictionary from earlier
        #            and dataFileName to filename (your filename string)

        # finally, run the function expHander.addLoop(<your trial handler>)



#add trialHandler


#add trials to the experiment handler to store data



###############----------------Trials-----------------------###############

# Instructions

# Start a For Loop to loop through your trial handler using the iterater name thisTrial


    # Set two variables resp and rt to None (dont forget the capital)

    # Set the orientation of the probe and cue, set these to whats currently in the trial handler (your iterator)


    ## Next, we want to display our fixation cross
    ## We should use a frame timer, assume your monitor is 60Hz and display for 500ms


    ## After fixation, we want to display our cue, again use the frame timer, 200ms this time


    ## Now for the critical bit, we want to display our probe

     # first use a function that calls a selected function when the frame flip - get it to reset the clock

     # Now we need to clear the events buffer of any rogue key presses call event.clearEvents()

    # Now for the probe loop, this time we want to display the probe for 200ms but also monitor key presses
      # so, start your frame loop as usual
      # next, add in a function that checks the keyboard for presses and adds them to a list called resp (getKeys)
      # follwing this, we should check if a key was pressed, and if it was, store the resulting reaction to rt and 
      # break the loop


    # We want the screen to go to black once a key is pressed so we should flip the buffer but not give any draw commands


    # We should wait if participants have yet to make a response
    # Lets use logic to achieve this: if there isnt a response
      # Use the if to call a function that waits for a press
      # then collect the first response and assign it to resp 
      # then stop the rt timer and assign the result to rt


    # To make our lives easier, we should work out if the participant was correct 
     # using what we know about the trial we should assign a variable corr with either 1 for correct or 0 for no


    # We should really log some data in a file, lets use the trial handler to do this

    # Tell the experiment handler that this trial is now over and to begin the next trial






###############-----------------Ends-----------------------###############

# Homework Challenges, 
# (better) Prizes will be provided on completion and certificates put on your student file

# It's a bit odd actually having a blank screen while you wait, it looks like a crash!
# stop this blanking from happening  

# I dont trust the psychopy data logger, write your own file of just the variables you want

# Make the timing settings for the presentation of the stimuli flexible on load using a GUI
# Dont forget to make sure its wholley divisible by the refresh rate
# Bonus: is there a way we can dynamically check what the refresh rate of the monitor is?

# When people have responded, show them their rt

# Create a new block that replicates the Friesen and Kingstone experiment you made in opensesame
# Now randomise the order of blocks on presentation (repeated measures)
