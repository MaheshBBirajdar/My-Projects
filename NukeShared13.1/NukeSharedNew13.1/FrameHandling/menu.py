import nuke
import FrameHandling

SHORTCUT_SET_FRAME = 'alt+shift+f'
ICON_SET_FRAME = 'FrameHandling_setFrame.png'

SHORTCUT_USER_FRAME = 'alt+shift+g'
ICON_USER_FRAME = 'FrameHandling_userFrame.png'

SHORTCUT_GO_TO_FRAME = 'shift+g'
ICON_GO_TO_FRAME = 'FrameHandling_goToFrame.png'

# Add to Nodes menu
toolbar = nuke.menu('Nodes')
cqnTools = toolbar.addMenu('CQN Tools', icon='CQN_icon.png')

cqnTools.addCommand('Set to current frame',
                    'FrameHandling.change_reference_frame()',
                    SHORTCUT_SET_FRAME,
                    icon=ICON_SET_FRAME)

cqnTools.addCommand('Set to specific a frame',
                    'FrameHandling.change_reference_frame(True)',
                    SHORTCUT_USER_FRAME,
                    icon=ICON_USER_FRAME)

cqnTools.addCommand('Go to Frame',
                    'FrameHandling.go_to_reference_frame()',
                    SHORTCUT_GO_TO_FRAME,
                    icon=ICON_GO_TO_FRAME)
