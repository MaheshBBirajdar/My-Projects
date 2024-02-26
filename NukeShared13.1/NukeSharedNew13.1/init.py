# NukeShared - Max van Leeuwen - maxvanleeuwen.com/nukeshared
# This will only redirect Nuke to the 'Required'-path, which is where NukeShared lives.


import nuke
import autosave

nuke.pluginAddPath('/core/SlateX/Reference/NukeGlobal/NukeSharedNew/NukeSurvivalToolkit')
nuke.pluginAddPath('/core/SlateX/Reference/NukeGlobal/NukeSharedNew/WrapItUp')
nuke.pluginAddPath('/core/SlateX/Reference/NukeGlobal/NukeSharedNew/pixelfudger')
nuke.pluginAddPath('/core/SlateX/Reference/NukeGlobal/NukeSharedNew/Cryptomatte/nuke')
nuke.pluginAddPath('/core/SlateX/Reference/NukeGlobal/NukeSharedNew/HeatWave 3.0')
nuke.pluginAddPath('/core/SlateX/Reference/NukeGlobal/NukeSharedNew/mtCollection')
nuke.pluginAddPath('/core/SlateX/Reference/NukeGlobal/NukeSharedNew/fxT_tools')
nuke.pluginAddPath('/core/SlateX/Reference/NukeGlobal/NukeSharedNew/PassSeparator')
nuke.pluginAddPath('/core/SlateX/Reference/NukeGlobal/NukeSharedNew/Shortcuts/py')
nuke.pluginAddPath('/core/SlateX/Reference/NukeGlobal/NukeSharedNew/AutoProjectSettings')
nuke.pluginAddPath('/core/SlateX/Reference/NukeGlobal/NukeSharedNew/AutoFlare2.2')
#nuke.pluginAddPath('/core/SlateX/Reference/NukeGlobal/NukeSharedNew/Baselight')
nuke.pluginAddPath('/core/SlateX/Reference/NukeGlobal/NukeSharedNew/Baselight_for_Nuke14-5.3.17521')

#nuke.knobDefault ('filter','Lanczos6')
nuke.knobDefault ('filter','cubic')

