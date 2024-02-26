
fltoolbar = nuke.toolbar("Nodes").addMenu('FilmLight', icon='nuke.png')
fltoolbar.addCommand("Baselight", "nuke.createNode('Baselight')", icon="nuke.png")
fltoolbar.addSeparator()
fltoolbarsetups = fltoolbar.addMenu("Setups")
bldir = os.path.dirname(os.path.abspath(__file__))
if nuke.env["WIN32"]:
    bldir = bldir.replace('\\', '/')
blworkflows = {
    'SetUp1_FilmStyle_ACES_Linear_EXR.nk': 'ACES EXR Workflow',
    'SetUp2_FilmStyle_CameraRGB_Linear_EXR.nk': 'Camera EXR Workflow',
    'SetUp3_FilmStyle_CameraRGB_Log_DPX.nk': 'Camera DPX Workflow',
    'SetUp4_TeleCineStyle_CameraRGB_Log_DPX.nk': 'Telecine DPX Workflow'
}
def addBaselightSetups(item):
    for key in sorted(blworkflows):
        item.addCommand(blworkflows[key], 'loadBaselightSetup(\"setups/' + blworkflows[key] + '\",\"' + key + '\")')
addBaselightSetups(fltoolbarsetups)
def loadBaselightSetup(name, scriptname):
    nuke.loadToolset(bldir + '/setups/' + scriptname)
    n = nuke.selectedNodes('Read')
    for r in n:
        f = r['file'].value()
        r['file'].setValue(bldir + '/setups/footage/' + os.path.basename(f))
flmenubar = nuke.menu("Nuke")
flmenu = flmenubar.addMenu("FilmLight")
flmenu.addCommand("Baselight", "nuke.createNode('Baselight')", icon="nuke.png")
flmenu.addSeparator()
flmenusetups = flmenu.addMenu("Setups")
addBaselightSetups(flmenusetups)

