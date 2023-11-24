import nuke

t=nuke.menu("Nodes")
u=t.addMenu("Pixelfudger", icon="PxF_Menu.png")

t.addCommand( "Pixelfudger/PxF_Bandpass", "nuke.createNode('PxF_Bandpass')", icon="PxF_Bandpass.png" ) 
t.addCommand( "Pixelfudger/PxF_ChromaBlur", "nuke.createNode('PxF_ChromaBlur')", icon="PxF_ChromaBlur.png") 
t.addCommand( "Pixelfudger/PxF_DeepFade", "nuke.createNode('PxF_DeepFade')", icon="PxF_DeepFade.png")
t.addCommand( "Pixelfudger/PxF_DeepMask", "nuke.createNode('PxF_DeepMask')", icon="PxF_DeepMask.png")
t.addCommand( "Pixelfudger/PxF_DeepResample", "nuke.createNode('PxF_DeepResample')", icon="PxF_DeepResample.png")

t.addCommand( "Pixelfudger/PxF_DeepDefocus", "nuke.createNode('PxF_DeepDefocus')", icon="PxF_IDefocus.png")
t.addCommand( "Pixelfudger/PxF_IDefocus", "nuke.createNode('PxF_IDefocus')", icon="PxF_IDefocus.png")
t.addCommand( "Pixelfudger/PxF_ZDefocus", "nuke.createNode('PxF_ZDefocus')", icon="PxF_IDefocus.png")
t.addCommand( "Pixelfudger/PxF_Distort", "nuke.createNode('PxF_Distort')", icon="PxF_Distort.png") 
t.addCommand( "Pixelfudger/PxF_Erode", "nuke.createNode('PxF_Erode')", icon="PxF_Erode.png")
t.addCommand( "Pixelfudger/PxF_Filler", "nuke.createNode('PxF_Filler')", icon="PxF_Filler.png") 
t.addCommand( "Pixelfudger/PxF_Grain", "nuke.createNode('PxF_Grain')", icon="PxF_Grain.png") 
t.addCommand( "Pixelfudger/PxF_HueSat", "nuke.createNode('PxF_HueSat')", icon="PxF_HueSat.png")  
t.addCommand( "Pixelfudger/PxF_KillSpill", "nuke.createNode('PxF_KillSpill')", icon="PxF_KillSpill.png")

t.addCommand( "Pixelfudger/PxF_AreaLight", "nuke.createNode('PxF_AreaLight')", icon="PxF_AreaLight.png")
t.addCommand( "Pixelfudger/PxF_EnvLight", "nuke.createNode('PxF_EnvLight')", icon="PxF_EnvLight.png")
t.addCommand( "Pixelfudger/PxF_GeoLight", "nuke.createNode('PxF_GeoLight')", icon="PxF_GeoLight.png")
t.addCommand( "Pixelfudger/PxF_RingLight", "nuke.createNode('PxF_RingLight')", icon="PxF_RingLight.png")
t.addCommand( "Pixelfudger/PxF_TubeLight", "nuke.createNode('PxF_TubeLight')", icon="PxF_TubeLight.png")

t.addCommand( "Pixelfudger/PxF_Line", "nuke.createNode('PxF_Line')", icon="PxF_Line.png" ) 
t.addCommand( "Pixelfudger/PxF_MergeWrap", "nuke.createNode('PxF_MergeWrap')", icon="PxF_MergeWrap.png" ) 
t.addCommand( "Pixelfudger/PxF_Nukebench", "nuke.createNode('PxF_Nukebench')", icon="PxF_Nukebench.png")
t.addCommand( "Pixelfudger/PxF_ScreenClean", "nuke.createNode('PxF_ScreenClean')", icon="PxF_ScreenClean.png")
t.addCommand( "Pixelfudger/PxF_SmokeBox", "nuke.createNode('PxF_SmokeBox')", icon="PxF_SmokeBox.png")
t.addCommand( "Pixelfudger/PxF_Smoother", "nuke.createNode('PxF_Smoother')", icon="PxF_Smoother.png")
t.addCommand( "Pixelfudger/PxF_TimeMerge", "nuke.createNode('PxF_TimeMerge')", icon="PxF_TimeMerge.png")
t.addCommand( "Pixelfudger/PxF_VectorEdgeBlur", "nuke.createNode('PxF_VectorEdgeBlur')", icon="PxF_VectorEdgeBlur.png")

