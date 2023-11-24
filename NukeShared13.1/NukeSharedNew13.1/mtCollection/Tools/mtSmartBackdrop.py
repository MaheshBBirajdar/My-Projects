import nukescripts
import nuke

def quickBackdrop(): 

	qBD = nuke.Panel('quickBackdrop')

	qBD.addEnumerationPulldown('Presets', 'NONE Key Despill Matte Grade CleanUp Transforms BG FG AOVs')
	qBD.addSingleLineInput('Extra Label', '')


	def autoNodeIsInside (node, backdropNode): 
		"""Returns true if node geometry is inside backdropNode otherwise returns false""" 
		topLeftNode = [node.xpos(), node.ypos()] 
		topLeftBackDrop = [backdropNode.xpos(), backdropNode.ypos()] 
		bottomRightNode = [node.xpos() + node.screenWidth(), node.ypos() + node.screenHeight()] 
		bottomRightBackdrop = [backdropNode.xpos() + backdropNode.screenWidth(), backdropNode.ypos() + backdropNode.screenHeight()] 

		topLeft = ( topLeftNode[0] >= topLeftBackDrop[0] ) and ( topLeftNode[1] >= topLeftBackDrop[1] ) 
		bottomRight = ( bottomRightNode[0] <= bottomRightBackdrop[0] ) and ( bottomRightNode[1] <= bottomRightBackdrop[1] ) 

		return topLeft and bottomRight 

	def autoQuickBackdrop(): 

		selNodes = nuke.selectedNodes() 
		if not selNodes: 
			return nuke.nodes.BackdropNode() 

		# Calculate bounds for the backdrop node. 
		bdX = min([node.xpos() for node in selNodes]) 
		bdY = min([node.ypos() for node in selNodes]) 
		bdW = max([node.xpos() + node.screenWidth() for node in selNodes]) - bdX 
		bdH = max([node.ypos() + node.screenHeight() for node in selNodes]) - bdY 

		zOrder = 0 
		selectedBackdropNodes = nuke.selectedNodes( "BackdropNode" ) 
		#if there are backdropNodes selected put the new one immediately behind the farthest one 
		if len( selectedBackdropNodes ) : 
			zOrder = min( [node.knob( "z_order" ).value() for node in selectedBackdropNodes] ) - 1 
		else : 
			#otherwise (no backdrop in selection) find the nearest backdrop if exists and set the new one in front of it 
			nonSelectedBackdropNodes = nuke.allNodes("BackdropNode") 
			for nonBackdrop in selNodes: 
				for backdrop in nonSelectedBackdropNodes: 
					if autoNodeIsInside( nonBackdrop, backdrop ): 
						zOrder = max( zOrder, backdrop.knob( "z_order" ).value() + 1 ) 

		# Expand the bounds to leave a little border. Elements are offsets for left, top, right and bottom edges respectively 
		left, top, right, bottom = (-15, -100, 15, 15) 
		bdX += left 
		bdY += top 
		bdW += (right - left) 
		bdH += (bottom - top)

		cKey = 0.35*255,0.75*255,0.35*255

		cDespill = 0.55*255,0.6*255,0.55*255

		#cRoto = 0.3*255,0.5*255,0.3*255

		cMatte = 0.25*255,0.25*255,0.5*255

		cGrade = 0.5*255,0.5*255,0.75*255

		cCleanUp = 0.6*255,0.4*255,0.85*255

		cFG = 0.60*255,0.30*255,0.30*255

		cBG = 0.5*255,0.3*255,0.3*255

		cAOVs = 0.38*255,0.635*255,0.749*255

		cTransforms = 0.656*255,0.395*255,0.79*255

		cNONE = 0.50*255,0.50*255,0.50*255


		myDic = {"Key" : cKey, "Matte" : cMatte, "Grade" : cGrade, "CleanUp" : cCleanUp, "FG" : cFG, "BG" : cBG, "Despill" : cDespill, "NONE" : cNONE, "AOVs" : cAOVs, "Transforms" : cTransforms}

		valuePreset = qBD.value('Presets')
		valueExtraLabel = qBD.value('Extra Label')


		colorBD = myDic[valuePreset]

		iKey = "Keyer.png"

		#iRoto = "Roto.png"

		iMatte = "MergeMatte.png"

		iDespill = "HueCorrect.png"

		iGrade = "ColorCorrect.png"

		iCleanUp = "RotoPaint.png"

		iFG = "Merge.png"

		iBG = "Read.png"

		iTransforms = "CornerPin.png"

		iAOVs = "Shader.png"

		iNONE = ''

		myDic2 = {"Key" : iKey, "Matte" : iMatte, "Grade" : iGrade, "CleanUp" : iCleanUp, "FG" : iFG, "BG" : iBG, "Despill" : iDespill, "NONE" : iNONE, "AOVs" : iAOVs, "Transforms" : iTransforms}

		imageBD = myDic2[valuePreset]


		n = nuke.nodes.BackdropNode(xpos = bdX, bdwidth = bdW, ypos = bdY, bdheight = bdH, tile_color = int('%02x%02x%02x%02x' % (colorBD[0], colorBD[1], colorBD[2],1),16), note_font_size=42, z_order = zOrder ) 

		if valuePreset != "NONE":
			n['label'].setValue('<img src="'+imageBD+'">'+' '+valuePreset+' '+valueExtraLabel)
			try:
				n['note_font'].setValue("Verdana")
			except:
				pass
		else:
			n['label'].setValue(valueExtraLabel)

		n['selected'].setValue(False) 
		for node in selNodes: 
			node['selected'].setValue(True)

		return n


	#-------------------------------------------------
	if qBD.show() == True:
		autoQuickBackdrop()
	else:
		pass


