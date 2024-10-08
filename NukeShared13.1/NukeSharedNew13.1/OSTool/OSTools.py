import nuke

t=nuke.menu("Nodes")
u=t.addMenu("OSTools", icon="os.png")

t.addCommand( "OSTools/AdditiveKeyer2", "nuke.createNode('AdditiveKeyer2')")
t.addCommand( "OSTools/AP_Fractal_blur", "nuke.createNode('AP_Fractal_blur')")
t.addCommand( "OSTools/aPMatte", "nuke.createNode('aPMatte')")
t.addCommand( "OSTools/autoContactSheet", "nuke.createNode('autoContactSheet')")
t.addCommand( "OSTools/beauty", "nuke.createNode('beauty')")
t.addCommand( "OSTools/cfCatsEyeDefocus", "nuke.createNode('cfCatsEyeDefocus')")
t.addCommand( "OSTools/ChannelKeyer", "nuke.createNode('ChannelKeyer')")
t.addCommand( "OSTools/Chromatik", "nuke.createNode('Chromatik')")
t.addCommand( "OSTools/Cloud_Maker_v1", "nuke.createNode('Cloud_Maker_v1')") 
t.addCommand( "OSTools/ColorDilatePF", "nuke.createNode('ColorDilatePF')")
t.addCommand( "OSTools/colorPickerID", "nuke.createNode('colorPickerID')")
t.addCommand( "OSTools/ColorSmear", "nuke.createNode('ColorSmear')")
t.addCommand( "OSTools/CS_HeatDistortion", "nuke.createNode('CS_HeatDistortion')")
t.addCommand( "OSTools/CSR_Laser_Generator", "nuke.createNode('CSR_Laser_Generator')")
t.addCommand( "OSTools/DasGrain", "nuke.createNode('DasGrain')")
t.addCommand( "OSTools/DeFlicker", "nuke.createNode('DeFlicker')")
t.addCommand( "OSTools/DegrainHelper", "nuke.createNode('DegrainHelper')")
t.addCommand( "OSTools/DespillMadness", "nuke.createNode('DespillMadness')")
t.addCommand( "OSTools/dirBlurIntuitive", "nuke.createNode('dirBlurIntuitive')")
t.addCommand( "OSTools/Edge", "nuke.createNode('Edge')")
t.addCommand( "OSTools/Edge_Expand", "nuke.createNode('Edge_Expand')")
t.addCommand( "OSTools/EdgeExtend2", "nuke.createNode('EdgeExtend2')")
t.addCommand( "OSTools/EdgeFromAlpha", "nuke.createNode('EdgeFromAlpha')")
t.addCommand( "OSTools/Erode_Fine", "nuke.createNode('Erode_Fine')")
t.addCommand( "OSTools/ExpressionWaveGenerator", "nuke.createNode('ExpressionWaveGenerator')")
t.addCommand( "OSTools/FlareFactory", "nuke.createNode('FlareFactory')")
t.addCommand( "OSTools/FlareFactory_Plus", "nuke.createNode('FlareFactory_Plus')")
t.addCommand( "OSTools/FloodBucket", "nuke.createNode('FloodBucket')")
t.addCommand( "OSTools/fxT_chromaKeyer", "nuke.createNode('fxT_chromaKeyer')")
t.addCommand( "OSTools/Get_Edge", "nuke.createNode('Get_Edge')")
t.addCommand( "OSTools/Glow_Exponential", "nuke.createNode('Glow_Exponential')")
t.addCommand( "OSTools/GodRaysProjector", "nuke.createNode('GodRaysProjector')")
t.addCommand( "OSTools/GradePlus", "nuke.createNode('GradePlus')")
t.addCommand( "OSTools/IBKCleanPlate", "nuke.createNode('IBKCleanPlate')")
t.addCommand( "OSTools/iBlur", "nuke.createNode('iBlur')")
t.addCommand( "OSTools/ImagePlane", "nuke.createNode('ImagePlane')")
t.addCommand( "OSTools/iTransform", "nuke.createNode('iTransform')")
t.addCommand( "OSTools/K_LensEngine", "nuke.createNode('K_LensEngine')")
#t.addCommand( "OSTools/KillOutline", "nuke.createNode('KillOutline')")
t.addCommand( "OSTools/KillSpill", "nuke.createNode('KillSpill')")
t.addCommand( "OSTools/KillSpillPlus", "nuke.createNode('KillSpillPlus')")
t.addCommand( "OSTools/L_AlphaClean_v03", "nuke.createNode('L_AlphaClean_v03')")
t.addCommand( "OSTools/MECfiller", "nuke.createNode('MECfiller')")
t.addCommand( "OSTools/MonochromePlus", "nuke.createNode('MonochromePlus')")
t.addCommand( "OSTools/MotionBlur_Paint", "nuke.createNode('MotionBlur_Paint')")
t.addCommand( "OSTools/Noise_3D", "nuke.createNode('Noise_3D')")
t.addCommand( "OSTools/Offset", "nuke.createNode('Offset')")
t.addCommand( "OSTools/OpticalZDefocus", "nuke.createNode('OpticalZDefocus')")
t.addCommand( "OSTools/patchUp", "nuke.createNode('patchUp')")
t.addCommand( "OSTools/PositionToNormal", "nuke.createNode('PositionToNormal')")
t.addCommand( "OSTools/PxF_Filler", "nuke.createNode('PxF_Filler')")
t.addCommand( "OSTools/PxF_Kill_spill", "nuke.createNode('PxF_Kill_spill')")
t.addCommand( "OSTools/QC_Grain", "nuke.createNode('QC_Grain')")
t.addCommand( "OSTools/QcTechnical", "nuke.createNode('QcTechnical')")
t.addCommand( "OSTools/Relight_Simple", "nuke.createNode('Relight_Simple')")
t.addCommand( "OSTools/ReProject_3D", "nuke.createNode('ReProject_3D')")
t.addCommand( "OSTools/rs_GuidedBlur_v1_3", "nuke.createNode('rs_GuidedBlur_v1_3')")
t.addCommand( "OSTools/screenCorrect", "nuke.createNode('screenCorrect')")
t.addCommand( "OSTools/Spill_Correct", "nuke.createNode('Spill_Correct')")
t.addCommand( "OSTools/SpillReplace2", "nuke.createNode('SpillReplace2')")
t.addCommand( "OSTools/SplineBlur", "nuke.createNode('SplineBlur')")
t.addCommand( "OSTools/T_Embers", "nuke.createNode('T_Embers')")
t.addCommand( "OSTools/T_HeatDistortion", "nuke.createNode('T_HeatDistortion')")
t.addCommand( "OSTools/TrueExponentialBlur", "nuke.createNode('TrueExponentialBlur')")
t.addCommand( "OSTools/UnsharpMask", "nuke.createNode('UnsharpMask')")
t.addCommand( "OSTools/V_Slate", "nuke.createNode('V_Slate')")
t.addCommand( "OSTools/X_Tesla", "nuke.createNode('X_Tesla')")
t.addCommand( "OSTools/x_VectorBlur", "nuke.createNode('x_VectorBlur')")
t.addCommand( "OSTools/LumaKeyer", "nuke.createNode('LumaKeyer')")
t.addCommand( "OSTools/LumiMatch_ByBrunoEdelman", "nuke.createNode('LumiMatch_ByBrunoEdelman')")
t.addCommand( "OSTools/ColorDifferenceKey", "nuke.createNode('ColorDifferenceKey')")
t.addCommand( "OSTools/BM_LumaKeyer", "nuke.createNode('BM_LumaKeyer')")
t.addCommand( "OSTools/RoughenEdges", "nuke.createNode('RoughenEdges')")
t.addCommand( "OSTools/snowy", "nuke.createNode('snowy')")
t.addCommand( "OSTools/edgeNoise", "nuke.createNode('edgeNoise')")
t.addCommand( "OSTools/Projectionset", "nuke.createNode('Projectionset')")
t.addCommand( "OSTools/D_QCTool_v02", "nuke.createNode('D_QCTool_v02')")
t.addCommand( "OSTools/L_Grain_v05", "nuke.createNode('L_Grain_v05')")
t.addCommand( "OSTools/DespillMadness_v3", "nuke.createNode('DespillMadness_v3')")
t.addCommand( "OSTools/Day2Night", "nuke.createNode('Day2Night')")
t.addCommand( "OSTools/manual_MBlur", "nuke.createNode('manual_MBlur')")
t.addCommand( "OSTools/Normalised_Grain", "nuke.createNode('Normalised_Grain')")
t.addCommand( "OSTools/ExpandRGB", "nuke.createNode('ExpandRGB')")
t.addCommand( "OSTools/GradMagic", "nuke.createNode('GradMagic')")
t.addCommand( "OSTools/BlitzDefocus-6.4.nk", "nuke.createNode('BlitzDefocus-6.4.nk')")
t.addCommand( "OSTools/BlitzDefocus-6.4-advanced.nk", "nuke.createNode('BlitzDefocus-6.4-advanced.nk')")
t.addCommand( "OSTools/GradMagic", "nuke.createNode('empty_UV')")
t.addCommand( "OSTools/GradMagic", "nuke.createNode('Morph_Dissolve')")
t.addCommand( "OSTools/lp_hairkey", "nuke.createNode('lp_hairkey')")
t.addCommand( "OSTools/HairKey", "nuke.createNode('HairKey')")
t.addCommand( "OSTools/PolarCoords.nk", "nuke.createNode('PolarCoords.nk')")
t.addCommand( "OSTools/Vignette", "nuke.createNode('Vignette')")
#t.addCommand( "OSTools/FireflyKiller", "nuke.createNode('FireflyKiller')")
t.addCommand( "OSTools/K_Defocus", "nuke.createNode('K_Defocus')")
t.addCommand( "OSTools/Extruder", "nuke.createNode('Extruder')")
t.addCommand( "OSTools/rs_GuidedBlur_v1_31", "nuke.createNode('rs_GuidedBlur_v1_31')")
t.addCommand( "OSTools/aeTransform", "nuke.createNode('aeTransform')")
t.addCommand( "OSTools/ScreenXchange", "nuke.createNode('ScreenXchange')")
t.addCommand( "OSTools/VectorExtendEdge", "nuke.createNode('VectorExtendEdge')")
t.addCommand( "OSTools/FineEdgeDetect", "nuke.createNode('FineEdgeDetect')")
