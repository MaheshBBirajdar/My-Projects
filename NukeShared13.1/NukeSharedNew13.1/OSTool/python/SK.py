


import nuke
import nukescripts

#Add Auto Write
def autoWrite () :
	rootName = nuke.root().knob('name').value() 
	rootName = rootName.split("/")[-1]
	rootName = rootName.rstrip('.nk')


	selNode = nuke.selectedNode()
	channels = selNode.channels()
	#path = nuke.script_directory() + ('/')
	path = nuke.script_directory()
	path = path.rstrip('Nuke')
        path = path + ('Output/')
	w = nuke.nodes.Write() 
	type = list(w['file_type'].values())
	fQuoted = ['{%s}' % c for c in type]
	nuke.delete(w)	

	panel = nuke.Panel("autoWrite ")
	panel.addFilenameSearch('Write Path', path)
	panel.addEnumerationPulldown('Frame Padding', '01 02 03 04 05 06 07 08 09')
	panel.addEnumerationPulldown('File Type', ' '.join(fQuoted))
	panel.addBooleanCheckBox('Set File name to Script name?', True)
	panel.show()

	filePath = panel.value("Write Path")
	pResult = panel.value("Frame Padding")
	fResult = panel.value("File Type")
        fResult = fResult.rstrip('			ffmpeg')
	sResult = panel.value("Set File name to Script name?")

	if    not fResult == ("mov"):

		if sResult == False:
			panel = nuke.Panel("Set File Name ")
			panel.addSingleLineInput('Set File Name', '...')   
			panel.show()
			fName = panel.value("Set File Name")  

			write = nuke.createNode('Write') 
			write.setInput(0, selNode)
			write['file_type'].setValue(fResult)
			#write["file"].setValue((filePath) + (fResult) + ("/") + (fName) + ("/") +(fName) + ('.%') + (pResult) + ('d') + ('.') + (fResult))
			write["file"].setValue((filePath) + (fResult) + ("/") + ('[file rootname [basename [value root.name]]]')+ ("/") +('[file rootname [basename [value root.name]]]')+ ('.%') + (pResult) + ('d') + ('.') + (fResult))
		elif sResult == True:
			write = nuke.createNode('Write') 
			write.setInput(0, selNode)
			write['file_type'].setValue(fResult)
			#write["file"].setValue((filePath)+ (fResult) + ("/") +(rootName) + ("/") + (rootName) + ('.%') + (pResult) + ('d') + ('.') + (fResult))
			write["file"].setValue((filePath)+ (fResult) + ("/") +('[file rootname [basename [value root.name]]]')+ ("/") + ('[file rootname [basename [value root.name]]]') + ('.%') + (pResult) + ('d') + ('.') + (fResult))
#[file rootname [basename [value root.name]]]
	else:
		if sResult == False:
				panel = nuke.Panel("Set File Name ")
				panel.addSingleLineInput('Set File Name', '...')   
				panel.show()
				fName = panel.value("Set File Name")   
			        

				write = nuke.createNode('Write') 
				write.setInput(0, selNode)
				write['file_type'].setValue(fResult)
				#write["file"].setValue((filePath)+ (fResult) + ("/") + (fName) + ('.') + (fResult))
				write["file"].setValue((filePath)+ (fResult) + ("/") + ('[file rootname [basename [value root.name]]]') + ('.') + (fResult))

		elif sResult == True:
			write = nuke.createNode('Write') 
			write.setInput(0, selNode)
			write['file_type'].setValue(fResult)
			#write["file"].setValue((filePath) + (fResult) + ("/") + (rootName) + ('.') + (fResult))
    			write["file"].setValue((filePath) + (fResult) + ("/") + ('[file rootname [basename [value root.name]]]') + ('.') + (fResult))

				
t=nuke.menu("Nodes")
u=t.addMenu("OSTools", icon="os.png")				

#toolbar = nuke.menu('Nodes')
#msmenu = toolbar.addMenu('mS_Helpers', icon='LittleHelpers.png')


ms = u.addCommand('autoWrite', 'autoWrite()', "alt+w")




		
