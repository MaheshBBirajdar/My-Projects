import nuke
import os, shutil
import datetime


def SendDailies():
    #please select read node
    read_node = nuke.selectedNode()
    nodeClass = read_node.Class()
    
    if nodeClass == 'Read':
        file_knob = read_node['file']        # get file path from read node
        Original = file_knob.value()
        OriginalPath = os.path.dirname(os.path.abspath(Original))
        LastFolderName = os.path.basename(os.path.normpath(OriginalPath))
    
        path_split = os.path.normpath(OriginalPath).split(os.path.sep)
        newpath = os.path.sep.join(path_split[4:5])
            
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        Target = (r'/FURY/SlateX/Artists/Users/Dailies') +('/')+ newpath + ('/') + current_date + ('/') + (LastFolderName)
        nuke.message('Dailies Submitted Successfully')
        
        if os.path.exists(Target):
            shutil.rmtree(Target)           # replace file if exists
        
        shutil.copytree(OriginalPath, Target)  
        
    else:
        nuke.message('Before Submitting , Select Read Node')
    

