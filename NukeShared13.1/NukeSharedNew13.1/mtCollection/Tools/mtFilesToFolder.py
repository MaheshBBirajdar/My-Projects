#============================================
# V1.0
# MIGUEL TORIJA
# 30/11/2002
#============================================
#
#mtFiles_To_Folder
#
#============================================

import shutil, os, nuke, nukescripts, threading, time, datetime

def FilesToFolder():

    myProjectRoot = nuke.root().knob('name').value()

    myProject = os.path.basename(myProjectRoot)
    myRoot = os.path.dirname(myProjectRoot)
    myProjectcut = myProject[0:-3]

    listToCopyInFolder = []
    listToCopyInFolder2 = []
    listToCopyInFolderG = []
    listToCopyInFolderG2 = []

    for i in nuke.selectedNodes('Read'):
        readsCopy = i.knob('name').value()
        listToCopyInFolder.append(readsCopy)

    for n in nuke.allNodes('Read'):
        readsCopy2 = n.knob('name').value()
        listToCopyInFolder2.append(readsCopy2)

    for i in nuke.selectedNodes('ReadGeo2'):
        readsCopyG = i.knob('name').value()
        listToCopyInFolderG.append(readsCopyG) 

    for i in nuke.allNodes('ReadGeo2'):
        readsCopyG2 = i.knob('name').value()
        listToCopyInFolderG2.append(readsCopyG2)    


    str1 = ", "

    readsString = str1.join(listToCopyInFolder)
    readsStringCheck = str1.join(listToCopyInFolder2)
    readsStringG = str1.join(listToCopyInFolderG)
    readsStringG2 = str1.join(listToCopyInFolderG2)


    if len(listToCopyInFolderG) > 0:
        ReadsToCopy_INPUT = readsString+ ", " + readsStringG
    else:
        ReadsToCopy_INPUT = readsString

    p = nuke.Panel('Copy Files To Folder')

    p.addFilenameSearch('Destination', myRoot+"/")

    p.addSingleLineInput('Reads To Copy', ReadsToCopy_INPUT)
    p.addNotepad('All Reads', readsStringCheck)
    p.addSingleLineInput('All Read Geos', readsStringG2)

    if p.show() == True:

        destination = p.value('Destination')
        copiedNodes = []
        copiedFilepaths = []


        ReadsToCopy = p.value('Reads To Copy')
        ReadsToCopylist = ReadsToCopy.split(", ")


        lenReadsCopyList = len(ReadsToCopylist)


        for i in ReadsToCopylist:

            if lenReadsCopyList == 0:
                break
            else:
                pass

            name = i
            targetN = nuke.toNode(i)
            readFile = targetN.knob('file').value()

            readFilePath = os.path.dirname(readFile)
            readBaseName = os.path.basename(readFile)
            nameExtension = os.path.splitext(readBaseName)
            filename = nameExtension[0]
            fileExtension = nameExtension[1]


            if readFile == "":
                continue
            else:
                pass

            if os.path.isabs(readFile) == False:
                
                readFile = myRoot + "/" + readFile
            else:
                
                pass

            seqList = [".exr", ".dpx", ".jpg", ".png", ".tiff", ".targa", ".jpeg" ]

            if readFile in copiedFilepaths:
                continue
            else:
                pass

            if name in copiedNodes:
                continue
            else:
                pass

            if name not in ReadsToCopylist:
                continue
            else:
                pass


            if targetN.Class() == 'Read':


                if filename.find(str("%d")) != -1 or  filename.find(str("%04d")) != -1 or filename.find(str("%05d")) != -1 or filename.find(str("%06d")) != -1 or filename.find(str("####")) != -1:
                    if fileExtension in seqList:
                        print("image sequence")

                        readFirst = targetN['first'].value()
                        readLast = targetN['last'].value()

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

                            #print readBaseNameFraming

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


                                    os.makedirs(destination+str(filenameFix))
                                    folderToPlaceCopy = destination+str(filenameFix)                                
                                    shutil.copy(str(fileToCopy), str(folderToPlaceCopy))


                                elif e == readLast:
                                    shutil.copy(str(fileToCopy), str(folderToPlaceCopy))
                                    copiedNodes.append(name)
                                    copiedFilepaths.append(readFile)

                                else:
                                    shutil.copy(str(fileToCopy), str(folderToPlaceCopy))
                                continue
                            except:
                                print("something happened trying to copy a image sequence")
                                continue
                else:
                    print("movie")
                    
                    try:
                        os.makedirs(destination+str(filename))
                        folderToPlaceCopy = destination+str(filename)
                        
                        shutil.copy(str(readFile), str(folderToPlaceCopy))
                        copiedNodes.append(name)
                        copiedFilepaths.append(readFile)

                    except:
                        print("something happened trying to copy a movie")
                        continue

            elif targetN.Class() == 'ReadGeo2':
                try:
                    os.makedirs(destination+str(filename))
                    folderToPlaceCopy = destination+str(filename)
                    
                    shutil.copy(str(readFile), str(folderToPlaceCopy))
                    copiedNodes.append(name)
                    copiedFilepaths.append(readFile)

                except:
                    continue

            else:
                pass



	j = nuke.message('All Files copied!')

