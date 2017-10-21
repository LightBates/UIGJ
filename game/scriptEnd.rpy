label EndScene:
    if ($ math.fabs(empathy) > math.fabs(pacifism)):
        if $ empathy > 0:
            jump Empathy
        else:
            jump Apathy
    elif ($ math.fabs(empathy) < math.fabs(pacifism)):
        if $ pacifism > 0:
            jump Pacifism
        else:
            jump Violence
    else: 
        if $ renpy.random.randint(0,1) < 1:
            if $ empathy >= 0:
                jump Empathy
            else:
                jump Apathy
        else:
            if $ pacifism >= 0:
                jump Pacifism
            else:
                jump Violence
    
    
          
    
label Apathy:
    "Nothing matters. There is no horror, no specter they can bring before you that will bring fear or hesitation into your heart."
    "Nothing in this forest has fazed you, and nothing ever will."
    "Even if you are to wander here forever. Even if Glen is to waste away beside you, their hand slipping from yours one last time."
    "Their weight will fall to the ground and off of your shoulders, forever."
    return

label Empathy:
    

label Violence:
    
    
label Pacifism: