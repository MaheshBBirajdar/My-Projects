#----------------------------------------
# mtCollection menu.py
# Version: 1.0.0
# Last updated: 02-02-2021
#----------------------------------------

import nuke, nukescripts


nuke.pluginAddPath('./icons')
nuke.pluginAddPath('./Gizmos')
nuke.pluginAddPath('./Tools')

from mtCollectFiles import *
from mtCollectUtilities_Others import *
import KeyMix_Template
import mtSmartBackdrop



ec = nuke.menu('Nodes').addMenu('mtCollection', icon="mtCollection_icon.png")

ec.addCommand('Gizmos/Edges/mtEdgeFromAlpha', 'nuke.createNode("mtEdgeFromAlpha")', icon="EdgeFromAlpha_icon.png")
ec.addCommand('Gizmos/Edges/mtEdgeGrade', 'nuke.createNode("mtEdgeGrade")', icon="EdgeGrade_icon.png")
ec.addCommand('Gizmos/Edges/mtEdgeMix', 'nuke.createNode("mtEdgeMix")', icon="EdgeMix_icon.png")
ec.addCommand('Gizmos/TechFix/mtHelpNode', 'nuke.createNode("mtHelpNode")', icon="HelpNode_icon.png")
ec.addCommand('Gizmos/GradeTransform/mtLayerGrade', 'nuke.createNode("mtLayerGrade")', icon="LayerGrade_icon.png")
ec.addCommand('Gizmos/TechFix/mtLines', 'nuke.createNode("mtLines")', icon="Lines_icon.png")
ec.addCommand('Gizmos/GradeTransform/mtOffsetCopies', 'nuke.createNode("mtOffsetCopies")', icon="OffsetCopies_icon.png")
ec.addCommand('Gizmos/TechFix/mtPixelFixer', 'nuke.createNode("mtPixelFixer")', icon="PixelFixer_icon.png")
ec.addCommand('Gizmos/TechFix/mtTechCheck', 'nuke.createNode("mtTechCheck")', icon="TechCheck_icon.png")
ec.addCommand('Tools/KeyMixTemplates/mtKeyMixSimple',          'KeyMix_Template.dummy()', 'ctrl+alt+k', shortcutContext=2)
ec.addCommand('Tools/KeyMixTemplates/mtKeyMixFrameHolded',     'KeyMix_Template.dummy_2()', 'ctrl+shift+k', shortcutContext=2)
ec.addCommand('Tools/KeyMixTemplates/mtKeyMixTemplate',        'KeyMix_Template.keyMix_Template()', 'ctrl+alt+shift+k', shortcutContext=2)
ec.addCommand('Tools/SmartBackdrop',                           'mtSmartBackdrop.quickBackdrop()', 'ctrl+shift+b', shortcutContext=2)
ec.addCommand('Tools/mtCollectFiles',                          'mtCollectFiles()', 'ctrl+shift+F2', shortcutContext=2)
ec.addCommand('Tools/mtCollect Utilities/Reduce Project' , 'mtReduceProject()', "ctrl+shift+alt+f", shortcutContext=2)
ec.addCommand('Tools/mtCollect Utilities/Bring Render-Folder' , 'mtBringRendersandFolders()', "e", shortcutContext=2)

