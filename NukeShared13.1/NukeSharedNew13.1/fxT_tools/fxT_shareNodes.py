
import os
import nuke
import nukescripts

try:
    if nuke.NUKE_VERSION_MAJOR < 11:
        from PySide import QtCore, QtGui as QtWidgets
    else:
        from PySide2 import QtWidgets, QtCore
except ImportError:
    from Qt import QtWidgets, QtCore


class nukeShare(nukescripts.PythonPanel):

    def __init__(self):
        nukescripts.PythonPanel.__init__(self, 'fxT_shareNodes', 'com.fxt.fxT_shareNodes')

        # create buttons
        self.shareButton = nuke.PyScript_Knob('share selected nodes', 'Share Nodes', 'fxT_shareNodes.nukeShare().share()')
        self.updateButton = nuke.PyScript_Knob('update to view all the latest shared nodes', 'Update',
                                               'fxT_shareNodes.nukeShare().update()')

        # create divider line
        self.divline01 = nuke.Text_Knob("", "", "")
        self.divline02 = nuke.Text_Knob("", "", "")
        self.divline03 = nuke.Text_Knob("", "", "")

        # create some text info for the users
        self.info = nuke.Text_Knob("", "",
                                    "SHARE NODES:\nSelect the nodes you want to share,\nthen click the Share Nodes-button.\n\n\nGET NODES:\nClick the Update-button, then pick the\nuser you want to copy nodes from\n in the dropdown menu.\n\nIMPORT:\nUse CTRL+V to paste the shared nodes\ndirectly in the nodegraph.\n")

        self.copyright = nuke.Text_Knob("", "", "<font color='#838383'>// fxT_shareNodes v1.4 &#169; Tor Andreassen</font>")

        self.lastShare = nuke.String_Knob('path', '')
        self.lastShare.setValue('click update first')
        self.lastShare.setEnabled(False)

        self.dropdown = nuke.Enumeration_Knob('Users', 'User:', [''])

        # Set the path below to the folder where shared nukeScripts will be stored for all users:
        self.tempPath = '/core/SlateX/Artists/Users/assets/nuke/public/fxT_shareNodes'

        # add buttons to pane
        self.addKnob(self.shareButton)
        self.addKnob(self.updateButton)
        self.addKnob(self.divline01)
        self.addKnob(self.info)
        self.addKnob(self.divline02)

        self.addKnob(self.dropdown)

        self.addKnob(self.lastShare)

        self.addKnob(self.divline03)
        self.addKnob(self.copyright)

    def resetSel(self):
        for each in nuke.allNodes():
            each['selected'].setValue(False)

    def share(self):
        # if there are any selected nodes, dump selected nodes into a temp path and write it to clipboard
        # for easy sharing with other team members

        # set up user folder paths
        username = os.getlogin()
        path = self.tempPath
        user_folder = os.path.join(path, username)

        # generate list to check if there are any selected nodes
        nodeCount = [i.name() for i in nuke.selectedNodes()]

        # if the user's folder does not exist, create it if there are any selected nodes
        if len(nodeCount) > 0:
            if not os.path.exists(user_folder):
                os.makedirs(user_folder)

            # generate a random filename
            random_filename = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)]) + '.nk'
            filepath = os.path.join(user_folder, random_filename)

            # save the nuke script with selected nodes
            nuke.nodeCopy(filepath)

            # print the path to the temp nuke script to the scriptEditor
            print(('tempShare: ', filepath))

            # copy the filepath to the clipboard (ctrl+v is how you import other users shared files)
            QtWidgets.QApplication.clipboard().setText(filepath)

            # confirmation pop-up box so the user sees that something was shared
            nuke.message('tempShare script saved.\n\n use ctrl+v to share or update fxT_shareNodes to see it there.\n\n')

        else:
            nuke.message('No selected nodes, select the nodes you want to share and try again!')
            return

        # this is a work in progress to not allow more than 10 files in each user's folder
        # if there are more files in the user's share folder than 10, delete these files to avoid making the folder huge
        max_Files = 10

        def sorted_ls(user_folder):
            mtime = lambda f: os.stat(os.path.join(user_folder, f)).st_mtime
            return list(sorted(os.listdir(user_folder), key=mtime))

        del_list = sorted_ls(user_folder)[0:(len(sorted_ls(user_folder)) - max_Files)]

        for dfile in del_list:
            os.remove(os.path.join(user_folder, dfile))

    def update(self):
        # find users in the share folder
        shareRoot = self.tempPath
        global user_list
        user_list = [user for user in os.listdir(shareRoot) if os.path.isdir(os.path.join(shareRoot, user))]

        # list out the latest tempShare file for all users with a tempShare folder
        all_tempShares = []
        global all_tempSharesList
        all_tempSharesList = []
        for i in user_list:
            list_of_files = glob.glob(os.path.join(shareRoot, i, '*.nk'))  # * means all if need specific format then *.extension
            latest_file = max(list_of_files, key=os.path.getctime)
            all_tempShares.append(i + ':     \n\n' + latest_file)
            all_tempSharesList.append(latest_file)

        # make global variable so it can be used outside this function
        global allPaths
        allPaths = '\n\n'.join(all_tempShares)

    # force rebuild panel so the right value shows in the text window and dropdown list
    def knobChanged(self, knob):
        if knob == self.updateButton:
            self.removeKnob(self.dropdown)
            self.dropdown.setValues(user_list)
            self.removeKnob(self.lastShare)
            self.removeKnob(self.divline03)
            self.removeKnob(self.copyright)

            self.addKnob(self.dropdown)
            self.addKnob(self.lastShare)
            self.lastShare.setValue('choose user from the dropdown to see path')
            self.addKnob(self.divline03)
            self.addKnob(self.copyright)

        if knob.name() == 'Users':
            # grab the value of the current user dropdown
            self.dropdown.setValue(int(knob.getValue()))
            num = int(knob.getValue())

            # set the correct path to the user's latest tempShare file in the textfield
            self.lastShare.setValue(str(all_tempSharesList[num]))

            # push the user's last tempShare path to the clipboard
            QtWidgets.QApplication.clipboard().setText(str(all_tempSharesList[num]))

# add to pane
def addPanel():
    return nukeShare().addToPane()

menu = nuke.menu('Pane')
menu.addCommand('fxt_shareNodes', addPanel)
nukescripts.registerPanel('com.fxt.fxT_shareNodes', addPanel)

