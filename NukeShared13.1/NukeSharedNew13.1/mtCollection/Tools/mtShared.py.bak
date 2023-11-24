#============================================
# V1.1
# MIGUEL TORIJA
# 02/02/2002
#============================================
# mtShared
#============================================

import nuke, os, nukescripts

myProjectRoot = nuke.root().knob('name').value()



myProject = os.path.basename(myProjectRoot)
myRoot = os.path.dirname(myProjectRoot)
myProjectcut = myProject[0:-3]




def shareNodes(defaultFolder):
	checkList = []

	try:
	    for i in nuke.selectedNodes():
			checkList.append(i)
			
	except:
		nuke.message('You have to select some nodes')

	if len(checkList) == 0:
		nuke.message('You have to select some nodes')

	elif len(checkList) > 0:
		f = nuke.Panel("Share Nodes")
		f.addFilenameSearch('file path', defaultFolder)
		f.addSingleLineInput('name', myProjectcut + '_shared')



		if f.show() == True:

			pathValue = f.value("file path")
			nameValue = f.value("name")
			pathToPlace = pathValue + "/"+nameValue + ".nk"
			nuke.nodeCopy(pathToPlace)

		else:
			
			pass
	else:
		pass




def getNodes(defaultFolder):

	f = nuke.Panel("Folder To Search")
	
	f.addBooleanCheckBox('Do not use Default Folder',  False)
	f.addFilenameSearch('Alternative File Path', defaultFolder)


	panel1 = f.show()

	if panel1 == True:

		if f.value('Do not use Default Folder') == False:
			dirFilesList = os.listdir(defaultFolder)

			dirFilesString = ' '.join(dirFilesList)

			g = nuke.Panel("Get Nodes")
			g.addEnumerationPulldown('Shared Nodes', dirFilesString)
			
			if g.show() == True:

				x = g.value('Shared Nodes')
				s = defaultFolder + "/" + x
				nuke.nodePaste(s) 

		elif f.value('Do not use Default Folder') == True:
			
			try:

				try:
					pathW = f.value('Alternative File Path')

					if pathW.find(str(".nk")) != -1:
						alternativeFolder = os.path.dirname(pathW)

					else:
						alternativeFolder = f.value('Alternative File Path')

				except:
					nuke.message('You must select a Folder, not a file')
					
				dirFilesList = os.listdir(alternativeFolder)

				dirFilesString = ' '.join(dirFilesList)

				g = nuke.Panel("Get Nodes")
				g.addEnumerationPulldown('Shared Nodes', dirFilesString)
				
				if g.show() == True:

					x = g.value('Shared Nodes')
					s = alternativeFolder + "/" + x
					nuke.nodePaste(s) 

			except:

				nuke.message('You must select a Folder, not a file')

	if panel1 == False:
		pass




