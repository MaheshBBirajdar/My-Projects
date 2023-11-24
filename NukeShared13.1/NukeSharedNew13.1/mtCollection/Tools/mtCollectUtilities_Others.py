#============================================
# V1.0
# MIGUEL TORIJA
# 30/11/2002
#============================================
#
#mtCollectUtilities_Others
#
#============================================



import nuke, os, sys

def mtReduceProject():


    myList = []
    for rem in nuke.allNodes('Read'):

        toCheck = rem.knob('name').value()
        nodeToCheck = nuke.toNode(toCheck)

        a = nodeToCheck.dependent()

        if len(a) == 0:
            myList.append(toCheck)

        else:
            pass


    allReadL = []
    for n in nuke.allNodes('Read'):
        ojo = n.knob('name').value()
        allReadL.append(ojo) 
    
    str1 = ", "

    toCheckString = str1.join(myList)
    readsStringCheck = str1.join(allReadL)


    p = nuke.Panel('Reduce Project')
    p.addSingleLineInput('Reads To Delete', toCheckString)
    p.addNotepad('Solitary Reads', toCheckString)
    p.addNotepad('All Reads', readsStringCheck)
    
    if p.show() == True:
        if nuke.ask("Are you sure to continue?"):
            stringToDelete = p.value('Reads To Delete')
            try:
                ReadsToDelete = stringToDelete.split(", ")
                for i in ReadsToDelete:
                    nodeToDelete = nuke.toNode(i)
                    nuke.delete(nodeToDelete)
            except:
                pass




def mtBringRendersandFolders():

    try:
        targetNode = nuke.selectedNode()
        targetNodeClass = nuke.selectedNode().Class()

        TargetWriteFile = targetNode['file'].value()

        firstFrame = nuke.root()['first_frame'].value()
        lastFrame = nuke.root()['last_frame'].value()
        RootColor = nuke.root()['workingSpaceLUT'].value()

        if targetNodeClass == "Write":

            TargetWriteType = targetNode['file_type'].value()
            TargetWriteColor = targetNode['colorspace'].value()

            nuke.createNode('Read')
            myRead = nuke.selectedNode()
            myRead['file'].setValue(TargetWriteFile)
            myRead['file_type'].setValue(TargetWriteType)
            myRead['colorspace'].setValue(RootColor)
            myRead['first'].setValue(int(firstFrame))
            myRead['last'].setValue(int(lastFrame))
            myRead['on_error'].setValue(1)
        
        elif targetNodeClass == "WriteGeo":

            nuke.createNode('ReadGeo')
            myReadGeo = nuke.selectedNode()
            myReadGeo['file'].setValue(TargetWriteFile)

        elif targetNodeClass == 'Read' or targetNodeClass == 'ReadGeo2':
            myPath = os.path.abspath(targetNode['file'].value())
            myPathString = os.path.dirname(myPath)
            myPathStringNormalize = myPathString.replace('/', '\\')
            os.system('explorer %s' % myPathStringNormalize)


        else:
            pass


    except:
        #nuke.message('something bad happened :(')
        pass


