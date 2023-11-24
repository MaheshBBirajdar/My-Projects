import nuke

if nuke.NUKE_VERSION_MAJOR==12:
    nuke.pluginAddPath('/core/SlateX/Reference/NukeGlobal/NukeShared')

if nuke.NUKE_VERSION_STRING=="13.1v1":
    nuke.pluginAddPath("/core/SlateX/Reference/NukeGlobal/NukeSharedNew")







