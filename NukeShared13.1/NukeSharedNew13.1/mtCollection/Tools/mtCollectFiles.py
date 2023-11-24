#============================================
# V1.0
# MIGUEL TORIJA
# 13/12/2002
#============================================
#
#mtCOLLECT_FILES
#
#============================================




import shutil, os, nuke, nukescripts, threading, time, datetime, psutil

def mtCollectFiles():



    #Creating Useful variables about the Project and the main Lists to store the copied Nodes 

    myProjectRoot = nuke.root().knob('name').value()
    myProject = os.path.basename(myProjectRoot)
    myRoot = os.path.dirname(myProjectRoot)
    myProjectcut = myProject[0:-3]
    copiedNodes = []
    copiedFilepaths = []
    oldData = nukescripts.get_script_data()



    # Creating The panel

    p = nuke.Panel('Collect Files')

    p.addFilenameSearch('Destination', myRoot+"/")
    p.addSingleLineInput('Folder Name', 'Collect_Files_'+myProjectcut)

    p.addSingleLineInput('Exclude Files', '')


    p.addBooleanCheckBox('Create Cache Folder', False)
    p.addSingleLineInput('Exclude Cache', '')


    p.addBooleanCheckBox('Remove solitary Reads', False)
    p.addBooleanCheckBox('Remove Not Copied Reads', False)

    # If the user click "Ok" in the panel, Let's go to work!

    if p.show() == True:

        destination = p.value('Destination')
        mainFolder = p.value('Folder Name')
 
        stringToAsk = "It could take some time, consider taking a coffee. Once it finish, you will be working on the new collected script. Are you sure to continue?"

        if nuke.ask(stringToAsk):
            nuke.scriptSave("")

            #Gathering the main results of the panel


            #Creating the main folder and New script activating the relative paths
            collected = os.makedirs(destination+mainFolder)
            os.makedirs(destination+mainFolder+"/Footage")

            nuke.scriptSaveAs(destination+mainFolder+"/collected_"+myProject)

            nuke.root().knob('project_directory').setValue("[python {nuke.script_directory()}]")




    #========================================================================
    # REMOVING SOLITARY READS
    #========================================================================
            if p.value('Remove solitary Reads') == True:

                for rem in nuke.allNodes('Read'):

                    toCheck = rem.knob('name').value()
                    nodeToCheck = nuke.toNode(toCheck)

                    a = nodeToCheck.dependent()

                    if len(a) == 0:
                        nuke.delete(nodeToCheck)

                    else:
                        pass
            else:
                pass


    #========================================================================
    # DEFINING THE LOOP TO COPY THE CACHE FILES
    #========================================================================

            def copyLoopGeo(node):


                readsToPopG = p.value('Exclude Cache')
                if readsToPopG != "":
                    readsToPopListG = readsToPopG.split(", ")
                else:
                    pass

                listToCopyG = []

                for n in nuke.allNodes(node):
                    namen = n.knob('name').value()
                    listToCopyG.append(namen)

                lenPopReadsG = len(listToCopyG)
                for m in range(0, int(lenPopReadsG)):

                    try:
                        listToCopyG.remove(readsToPopListG[m])
                    except:
                        pass

                print(listToCopyG)


                for i in nuke.allNodes(node):
                    #try:
                    Geoname = i.knob('name').value()  
                    GeoFile = i.knob('file').value()

                    if GeoFile == "":
                        continue
                    else:
                        pass

                    if os.path.isabs(GeoFile) == False:

                        GeoFile = myRoot + "/" + GeoFile
                    else:

                        pass


                    if GeoFile in copiedFilepaths:
                        continue
                    else:
                        pass

                    if Geoname in copiedNodes:
                        continue
                    else:
                        pass

                    if Geoname not in listToCopyG:
                        continue
                    else:
                        pass


                    GeoBaseName = os.path.basename(GeoFile)
                    GeoExtension = os.path.splitext(GeoBaseName)
                    
                    if listToCopyG != "":

                        os.makedirs(destination+mainFolder+"/Cache/"+str(Geoname))
                        folderToPlaceCopy = destination+mainFolder+"/Cache/"+str(Geoname)


                        shutil.copy(GeoFile, str(folderToPlaceCopy))
                        copiedNodes.append(Geoname)
                        copiedFilepaths.append(GeoFile)
                        newPath = "Cache/"+str(Geoname)+"/"+str(GeoBaseName)
                        i.knob('file').setValue(newPath)
                        continue

                    else:
                        pass
                    #except:
                        continue

            #================================================================================
            # Creating the Cache folder if required and running the function

            if p.value('Create Cache Folder') == True:
                
                os.makedirs(destination+mainFolder+"/Cache")
                copyLoopGeo('ReadGeo2')
                copyLoopGeo("Camera2")
            else:
                pass


            #================================================================================
            #================================================================================

            #TDeclaring the list of nodes we are going to copy
            
            listToCopy = []

            

            # Looping through all the nodes and appending them to the list.

            for n in nuke.allNodes('Read'):
                namen = n.knob('name').value()
                listToCopy.append(namen)

            # Looking for the nodes the user do not want to copy and removing them from the list

            readsToPop = p.value('Exclude Files')
            if readsToPop != "":
                readsToPopList = readsToPop.split(", ")
            else:
                pass

            lenPopReads = len(listToCopy)
            for m in range(0, int(lenPopReads)):

                try:
                    listToCopy.remove(readsToPopList[m])
                except:
                    pass


            # Creating the Progress Bar 

            listTimeBar = []

            for tim in nuke.allNodes('Read'):
                nameT = tim.knob('name').value()
                listTimeBar.append(nameT)
            tasks = len(listTimeBar)
            progress_BAR = nuke.ProgressTask("Copying Footage")
            bar = 0


            #================================================================================
            # With These Loop we are gonna Copy Each Target Read and create the directories
            #================================================================================

            for i in nuke.allNodes('Read'):

                try:

                    #Declaring variables for the name and filepath of the target Read
                    name = i.knob('name').value()
                    readFile = i.knob('file').value()

                    #Setting the progress of the TimeBar in each iteration of the loop
                    bar = bar + 1
                    try:                 
                        percent = int(100*(float(bar) / (tasks+1)))
                        progress_BAR.setProgress(percent)
                        progress_BAR.setMessage("Step {} of {}".format(bar, tasks))
                        time.sleep(0.1)
                        
                    except:
                        print("something happened with the progress bar")
                        pass


                    #Avoiding errors with empty and relative filepaths

                    if readFile == "":
                        continue
                    else:
                        pass

                    if os.path.isabs(readFile) == False:
                        
                        readFile = myRoot + "/" + readFile
                    else:
                        
                        pass

                    #Variables about the path and name of the Read.

                    readFilePath = os.path.dirname(readFile)
                    readBaseName = os.path.basename(readFile)
                    nameExtension = os.path.splitext(readBaseName)
                    filename = nameExtension[0]
                    fileExtension = nameExtension[1]

                    seqList = [".exr", ".dpx", ".jpg", ".png", ".tiff", ".targa", ".jpeg" ]


                    #Avoiding to copy Reads already copied.

                    if readFile in copiedFilepaths:
                        continue
                    else:
                        pass

                    if name in copiedNodes:
                        continue
                    else:
                        pass

                    if name not in listToCopy:
                        continue
                    else:
                        pass



                    ### Checking if the read have a .exr file in it by checking the padding, and, in case it have, take the first frame and last frame to create a loop  
                    ### that rename the file for each frame and copy it into a target folder. I've done that it these way to avoid copying the whole folder
                    ### Maybe there is a better way to do that. I will check for the future. But these works fine so... let's go these way!

                    if filename.find(str("%d")) != -1 or  filename.find(str("%04d")) != -1 or filename.find(str("%05d")) != -1 or filename.find(str("%06d")) != -1 or filename.find(str("####")) != -1:
                        if fileExtension in seqList:
                            print("image sequence")

                            readFirst = i['first'].value()
                            readLast = i['last'].value()

                            for e in range(readFirst, readLast+1):
                                
                                if filename.find(str("%04d")) != -1:
                                    try:
                                        readBaseNameFraming = readBaseName.replace("%04d", str(e))
                                    except:
                                        pass

                                elif filename.find(str("%d")) != -1:
                                    try:
                                        readBaseNameFraming = readBaseName.replace("%d", str(e))
                                    except:
                                        pass

                                elif filename.find(str("%05d")) != -1:
                                    try:
                                        readBaseNameFraming = readBaseName.replace("%05d", str(e))
                                    except:
                                        pass
                                elif filename.find(str("%06d")) != -1:
                                    try:
                                        readBaseNameFraming = readBaseName.replace("%06d", str(e))
                                    except:
                                        pass
                                elif filename.find(str("####")) != -1:
                                    try:
                                        readBaseNameFraming = readBaseName.replace("####", str(e))
                                    except:
                                        pass
                                else:
                                    pass

                                

                                fileToCopy = str(readFilePath) +"/"+ str(readBaseNameFraming)


                                try:
                                    if e == readFirst:
                                        
                                        if filename.find(str("%04d")) != -1:
                                            try:
                                                filenameFix = filename.replace("%04d", "")
                                            except:
                                                pass
                                        elif filename.find(str("%d")) != -1:
                                            try:
                                                filenameFix = filename.replace("%d", "")
                                            except:
                                                pass
                                        elif filename.find(str("%05d")) != -1:
                                            try:
                                                filenameFix = filename.replace("%05d", "")
                                            except:
                                                pass
                                        elif filename.find(str("%06d")) != -1:
                                            try:
                                                filenameFix = filename.replace("%06d", "")
                                            except:
                                                pass
                                        elif filename.find(str("####")) != -1:
                                            try:
                                                filenameFix = filename.replace("####", "")
                                            except:
                                                pass
                                        else:
                                            filenameFix = filename


                                        os.makedirs(destination+mainFolder+"/Footage/"+str(filenameFix))
                                        folderToPlaceCopy = destination+mainFolder+"/Footage/"+str(filenameFix)                                
                                        shutil.copy(str(fileToCopy), str(folderToPlaceCopy))


                                    elif e == readLast:
                                        shutil.copy(str(fileToCopy), str(folderToPlaceCopy))
                                        copiedNodes.append(name)
                                        copiedFilepaths.append(readFile)
                                        newPath = "Footage/"+str(filenameFix)+"/"+str(readBaseName)
                                        i.knob('file').setValue(newPath)
                                    else:
                                        shutil.copy(str(fileToCopy), str(folderToPlaceCopy))
                                    continue
                                except:
                                    print("something happened trying to copy a image sequence")
                                    continue
                    

                    # Ok, if the file is not a image sequence, just copy it. Much more easier.
                    else:
                        print("movie")
                        
                        try:
                            os.makedirs(destination+mainFolder+"/Footage/"+str(filename))
                            folderToPlaceCopy = destination+mainFolder+"/Footage/"+str(filename)
                            
                            shutil.copy(str(readFile), str(folderToPlaceCopy))
                            copiedNodes.append(name)
                            copiedFilepaths.append(readFile)
                            newPath = "Footage/"+str(filename)+"/"+str(readBaseName)
                            i.knob('file').setValue(newPath)
                        except:
                            print("something happened trying to copy a movie")
                            continue

                    if bar == tasks:
                        del(progress_BAR)
                        break
                    else:
                        pass

                except:
                    continue

            #================================================================
            # Deleting Not copied reads if required

            if p.value('Remove Not Copied Reads') == True:
                try:
                    for e in nuke.allNodes('Read'):
                        nameToRemove = e.knob('name').value()
                        removing = nuke.toNode(nameToRemove)
                        if nameToRemove not in copiedNodes:
                            nuke.delete(removing)
                        else:
                            pass
                except:
                    pass
            else:
                pass

            #================================================================
            # Creating the info .txt file!

            newData = nukescripts.get_script_data()
            totalCopied = str(len(copiedNodes))



            date = datetime.datetime.now()
            collectDate = date.strftime("%m/%d/%Y, %H:%M:%S")

            file = open(destination+mainFolder+"/collected_Info"+myProject+".txt", "w")
            file.write(collectDate + "\n\n\n" + "Total of reads copied:" + totalCopied + "\n\n\n" + "Old Script info:" + "\n\n\n" + oldData + "\n\n\n\n\n\n\n\n\n" + "New Script info:" + "\n\n\n" + newData )
            file.close()
        else:
            pass

    # We are done guys! If you have cheked the script until here... you have won a beer :)
    endM = nuke.message('Collect Files Done!')



