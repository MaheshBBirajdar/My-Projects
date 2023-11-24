# --------------------------------------------------------------
#  KeyMix_Template.py
#  Version: 1.0.0
#  Author: Miguel Torija
#
#  Last Modified by: Miguel Torija
#  Last Updated: 11/05/2020
# --------------------------------------------------------------

# --------------------------------------------------------------
#  USAGE:
#
#  Creates different KeyMix templates to help to make Clean Ups
# --------------------------------------------------------------


import nuke



def simple_KeymixTemplate(wGrade, Condition, Label, OpenColor, Color):

  
    try:
        Dummy = nuke.selectedNode()

    except:
        Dummy = nuke.createNode('Dot', inpanel = False)


    Dummy_xPos = Dummy['xpos'].value()
    Dummy_yPos = Dummy['ypos'].value()
    #---------------------------------------------
            
    #Create 1st DOT     
    myDot1 = nuke.createNode("Dot", inpanel = False)

    #Set Input and Position of myDot1
    myDot1.setInput(0, Dummy)

    myDot1['ypos'].setValue(Dummy_yPos +100)
    myDot1['xpos'].setValue(Dummy_xPos +34)

    myDot1_xpos = myDot1['xpos'].value()
    myDot1_ypos = myDot1['ypos'].value()

    #---------------------------------------------

    #Create 2nd DOT       
    myDot2 = nuke.createNode("Dot", inpanel = False)

    #Set Input and Position of myDot2
    myDot2.setInput(0, myDot1)

    myDot2['ypos'].setValue(myDot1_ypos +0)
    myDot2['xpos'].setValue(myDot1_xpos +200)

    #---------------------------------------------

    def wanted_Grade(wGrade):
        if wGrade == True:
            #Create Grade  
            nuke.createNode('Grade', inpanel = False)
            myGrade = nuke.selectedNode()
            
            #Set Input and Position of myGrade
            myGrade.setInput(0, myDot2)

            myGrade['ypos'].setValue(myDot1_ypos +80)
            myGrade['xpos'].setValue(myDot1_xpos +167)
        
        else:
            pass

    wanted_Grade(wGrade)

    myGrade = nuke.selectedNode()


    #---------------------------------------------

    #Create Transform  
    nuke.createNode("Transform", inpanel = False)
    myTransform = nuke.selectedNode()

    #Set Input and Position of myTransform
    try:
        myTransform.setInput(0, myGrade)
    except:
    	myTransform.setInput(0, myDot2)


    myTransform['ypos'].setValue(myDot1_ypos +150)
    myTransform['xpos'].setValue(myDot1_xpos +167)


    myTransform['label'].setValue('translate: [value translate] \n scale: [value scale] \n rotate: [value rotate]')

    #---------------------------------------------



    #Create 3th DOT       
    myDot3 = nuke.createNode("Dot", inpanel = False)

    #Set Input and Position of myDot3

    myDot3.setInput(0, myTransform)

    myDot3['ypos'].setValue(myDot1_ypos +259)
    myDot3['xpos'].setValue(myDot1_xpos +200)

    #---------------------------------------------

    #Create Roto 
    myRoto = nuke.createNode("Roto", inpanel = True)
    

    #Set Input and Position of myRoto
    myRoto.setInput(0, None)

    myRoto['ypos'].setValue(myDot1_ypos +150)
    myRoto['xpos'].setValue(myDot1_xpos -167)

    #---------------------------------------------

    #Create 4th DOT       
    myDot4 = nuke.createNode("Dot", inpanel = False)

    #Set Input and Position of myDot4
    myDot4.setInput(0, myRoto)

    myDot4['ypos'].setValue(myDot1_ypos +259)
    myDot4['xpos'].setValue(myDot1_xpos -134)

    #---------------------------------------------

    #Create KEYMIX         
    nuke.createNode("Keymix", inpanel = False)
    myKeymix = nuke.selectedNode()

    #Set Input and Position of myKeyMix     
    myKeymix.setInput(0, myDot1)
    myKeymix.setInput(1, myDot3)
    myKeymix.setInput(2, myDot4)

    myKeymix['ypos'].setValue(myDot1_ypos +245)
    myKeymix['xpos'].setValue(myDot1_xpos -34)

    myKeymix['bbox'].setValue('B')
    myKeymix['label'].setValue('BBox:[value bbox]')


    def simple_Backdrop(Condition, Label, OpenColor, Color):

        if Condition == True:
        
            nuke.createNode('BackdropNode', inpanel = False)

            b = nuke.selectedNode()
            b['bdwidth'].setValue(float(578))
            b['bdheight'].setValue(float(385))


            b['label'].setValue(Label)
            b['note_font_size'].setValue(50)



        
            b['xpos'].setValue(Dummy_xPos - 215)
            b['ypos'].setValue(Dummy_yPos + 60)
 


            if OpenColor == True:
                b['tile_color'].setValue(Color)
            else:
                pass                   

        else:
            pass

    simple_Backdrop(Condition, Label, OpenColor, Color)

    #---------------------------------------------

    #Create 5th DOT       
    myDot5 = nuke.createNode("Dot", inpanel = False)

    #Set Input and Position of myDot4
    myDot5.setInput(0, myKeymix)

    myDot5['ypos'].setValue(myDot1_ypos +300)
    myDot5['xpos'].setValue(myDot1_xpos +0)



#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------


def framehold_KeymixTemplate(wGrade, Condition, Label, OpenColor, Color):

    try:
        Dummy = nuke.selectedNode()

    except:
        Dummy = nuke.createNode('Dot', inpanel = False)


    Dummy_xPos = Dummy['xpos'].value()
    Dummy_yPos = Dummy['ypos'].value()

    #---------------------------------------------
            
    #Create 1st DOT     
    myDot1 = nuke.createNode("Dot", inpanel = False)

    #Set Input and Position of myDot1
    myDot1.setInput(0, Dummy)

    myDot1['ypos'].setValue(Dummy_yPos +100)
    myDot1['xpos'].setValue(Dummy_xPos +34)

    myDot1_xpos = myDot1['xpos'].value()
    myDot1_ypos = myDot1['ypos'].value()

    #---------------------------------------------

    #Create 2nd DOT       
    myDot2 = nuke.createNode("Dot", inpanel = False)

    #Set Input and Position of myDot2
    myDot2.setInput(0, myDot1)

    myDot2['ypos'].setValue(myDot1_ypos +0)
    myDot2['xpos'].setValue(myDot1_xpos +200)

    myDot2['label'].setValue('Remember to Denoise')

    #---------------------------------------------

    #Create FrameHold  
    nuke.createNode("FrameHold", inpanel = False)
    myFramehold = nuke.selectedNode()

    #Set Input and Position of myTransform
    myFramehold.setInput(0, myDot2)

    myFramehold['ypos'].setValue(myDot1_ypos +40)
    myFramehold['xpos'].setValue(myDot1_xpos +167)

    myFramehold['first_frame'].setValue(nuke.frame())

    #---------------------------------------------


    #Create Tracker
    nuke.createNode('Tracker4', inpanel = False)
    myTracker = nuke.selectedNode()

    myTracker.setInput(0, None)

    myTracker['ypos'].setValue(myDot1_ypos+170)
    myTracker['xpos'].setValue(myDot1_xpos+400)

    myTracker['reference_frame'].setValue(nuke.frame())
    

    #---------------------------------------------

    myBackdrop = nuke.createNode('BackdropNode', inpanel = False)

    myBackdrop['bdwidth'].setValue(float(347))
    myBackdrop['bdheight'].setValue(float(127))

    myBackdrop['ypos'].setValue(myDot1_ypos+130)
    myBackdrop['xpos'].setValue(myDot1_xpos+140)

    myBackdrop['z_order'].setValue(1)

    #---------------------------------------------

    def wanted_Grade(wGrade):
        if wGrade == True:
            #Create Grade  
            nuke.createNode('Grade', inpanel = False)
            myGrade = nuke.selectedNode()

            #Set Input and Position of myGrade
            myGrade.setInput(0, myFramehold)

            myGrade['ypos'].setValue(myDot1_ypos +90)
            myGrade['xpos'].setValue(myDot1_xpos +167)
        
        else:
            pass

    wanted_Grade(wGrade)

    myGrade = nuke.selectedNode()

    #---------------------------------------------

    #Create Transform  
    nuke.createNode("Transform", inpanel = False)
    myTransform = nuke.selectedNode()

    #Set Input and Position of myTransform
    try:
        myTransform.setInput(0, myGrade)

    except:
        myTransform.setInput(0, myFramehold)

    myTransform['ypos'].setValue(myDot1_ypos +295)
    myTransform['xpos'].setValue(myDot1_xpos +167)


    myTransform['label'].setValue('translate: [value translate] \n scale: [value scale] \n rotate: [value rotate]')



    #---------------------------------------------

    #Create 3th DOT       
    myDot3 = nuke.createNode("Dot", inpanel = False)

    #Set Input and Position of myDot3
    myDot3.setInput(0, myTransform)

    myDot3['ypos'].setValue(myDot1_ypos +359)
    myDot3['xpos'].setValue(myDot1_xpos +200)

    myDot3['label'].setValue('Remember to Grain')

    #---------------------------------------------

    #Create Roto 
    myRoto = nuke.createNode("Roto", inpanel = True)
    

    #Set Input and Position of myRoto
    myRoto.setInput(0, None)

    myRoto['ypos'].setValue(myDot1_ypos +230)
    myRoto['xpos'].setValue(myDot1_xpos -167)

    #---------------------------------------------

    #Create 4th DOT       
    myDot4 = nuke.createNode("Dot", inpanel = False)

    #Set Input and Position of myDot4
    myDot4.setInput(0, myRoto)

    myDot4['ypos'].setValue(myDot1_ypos +359)
    myDot4['xpos'].setValue(myDot1_xpos -134)

    #---------------------------------------------

    #Create KEYMIX         
    nuke.createNode("Keymix", inpanel = False)
    myKeymix = nuke.selectedNode()

    #Set Input and Position of myKeyMix     
    myKeymix.setInput(0, myDot1)
    myKeymix.setInput(1, myDot3)
    myKeymix.setInput(2, myDot4)

    myKeymix['ypos'].setValue(myDot1_ypos +345)
    myKeymix['xpos'].setValue(myDot1_xpos -34)
    
    myKeymix['bbox'].setValue('B')
    myKeymix['label'].setValue('BBox:[value bbox]')


    #---------------------------------------------


    def framehold_Backdrop(Condition, Label, OpenColor, Color):

        if Condition == True:
        
            nuke.createNode('BackdropNode', inpanel = False)

            b = nuke.selectedNode()
            b['bdwidth'].setValue(float(798))
            b['bdheight'].setValue(float(524))


            b['label'].setValue(Label)
            b['note_font_size'].setValue(50)



        
            b['xpos'].setValue(Dummy_xPos - 215)
            b['ypos'].setValue(Dummy_yPos + 60)
 


            if OpenColor == True:
                b['tile_color'].setValue(Color)
            else:
                pass                   

        else:
            pass

    framehold_Backdrop(Condition, Label, OpenColor, Color)


    #---------------------------------------------

    #Create 5th DOT       
    myDot5 = nuke.createNode("Dot", inpanel = False)

    #Set Input and Position of myDot4
    myDot5.setInput(0, myKeymix)

    myDot5['ypos'].setValue(myDot1_ypos +440)
    myDot5['xpos'].setValue(myDot1_xpos +0)




#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------




def keyMix_Template():
   

    try:
        Dummy_1 = nuke.selectedNode()

        Dummy_xPos_1 = Dummy_1['xpos'].value()
        Dummy_yPos_1 = Dummy_1['ypos'].value()



    except:
        nuke.createNode('Dot', inpanel = False)
        Dummy_2 = nuke.selectedNode()

        Dummy_xPos_2 = Dummy_2['xpos'].value()
        Dummy_yPos_2 = Dummy_2['ypos'].value() 


    p = nuke.Panel('mt Keymix Template')

    p.addBooleanCheckBox("FrameHold", "FrameHolded")

    p.addBooleanCheckBox("Include Grade", True)

    p.addBooleanCheckBox("Include BackDrop", True)

    p.addBooleanCheckBox("Change Backdrop color at exit", False)

    p.addSingleLineInput("Backdrop Text", "")

    p.addSingleLineInput("Iterations number", "1")


    if not p.show():
        return


    myCheckBox = p.value('FrameHold')

    myIterations = p.value('Iterations number')

    wantedGrade = p.value('Include Grade')

    myBackdrop = p.value('Include BackDrop')

    BackLabel = p.value('Backdrop Text')

    OpenColor = p.value("Change Backdrop color at exit")

    if OpenColor == True:
        B_Color = nuke.getColor()
    else:
        B_Color = int('%02x%02x%02x%02x' % (0.5*255,0.5*255,0.5*255,1),16)

    try:
        int(myIterations)
    except:
        nuke.message('Iterations number can not be letters or float numbers')
        return        




    for loops in range(0, int(myIterations)):

        if myCheckBox == False and wantedGrade == True:
            if myBackdrop == True:
            
                simple_KeymixTemplate(True, True, BackLabel, OpenColor, B_Color)
     
                

            else:
                simple_KeymixTemplate(True, False, BackLabel, OpenColor, B_Color)

        elif myCheckBox == False and wantedGrade == False:
                
            if myBackdrop == True:
                
                simple_KeymixTemplate(False, True, BackLabel, OpenColor, B_Color)
                                

            else:
                simple_KeymixTemplate(False, False, BackLabel, OpenColor, B_Color)


        elif myCheckBox == True and wantedGrade == True:
            if myBackdrop == True:
            
                framehold_KeymixTemplate(True, True, BackLabel, OpenColor, B_Color)
     
                

            else:
                framehold_KeymixTemplate(True, False, BackLabel, OpenColor, B_Color)


        elif myCheckBox == True and wantedGrade == False:
            if myBackdrop == True:
                framehold_KeymixTemplate(False, True, BackLabel, OpenColor, B_Color)
     
                

            else:
                framehold_KeymixTemplate(False, False, BackLabel, OpenColor, B_Color)
     
        else:
            pass


    

#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------


def dummy():
    a = None
    c = 0
    simple_KeymixTemplate(True, False, a, False, c)

def dummy_2():
    a = None
    c = 0
    framehold_KeymixTemplate(True, False, a, False, c) 



