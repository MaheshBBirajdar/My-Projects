
"""
FrameHandling Tool for Nuke
This tool provides functions to manipulate frame-related operations in Nuke.

Usage:
    - Run the `change_reference_frame` function to set the reference frame for selected nodes.
    - Run the `go_to_reference_frame` function to navigate to the reference frame of a selected node.

Note:
    - Supported knobs for reference frame manipulation:
        'reference_frame', 'referenceFrame', 'first_frame', 'ref_frame'.

menu.py Script:
    - This script sets up menu commands for easy access to the FrameHandling tool in the Nodes menu.
"""

__title__ = 'FrameHandling'
__author__ = 'Luciano Cequinel'
__contact__ = 'lucianocequinel@gmail.com'
__version__ = '2.2.3'
__release_date__ = 'November, 18 2023'
__license__ = 'MIT'

import nuke
import re

SUPPORTED_KNOBS = ['reference_frame', 'referenceFrame', 'first_frame', 'ref_frame']


def change_reference_frame(from_user=False):
    """
        Set the reference frame for selected nodes.
        Parameters:
            - from_user (bool): If True, prompts the user to input a frame. Defaults to False.
    """

    nodes = get_selection(True)
    if nodes:
        frame_value = get_frame(from_user)
        if frame_value:
            for node in nodes:
                for reference_knob in node.knobs():
                    if reference_knob in SUPPORTED_KNOBS:
                        node[reference_knob].setValue(frame_value)
                        print('\t :> {}.{} got the value: {}'.format(node.name(), reference_knob, frame_value))

    else:
        create_sticky_reference(nuke.frame())


def go_to_reference_frame():
    """
        Navigate to the reference frame of a selected node.
    """
    node = get_selection(False)

    if node:
        if node.Class() in 'StickyNote':
            label = node['label'].value()

            # search for the first group of numbers and use it as frame
            find_frame = re.findall("([0-9]{2,})", label)
            if find_frame:
                frame_value = find_frame[0]
                nuke.frame(int(frame_value))
            else:
                nuke.message('No reference frame in this StickyNote')

        else:
            for knob in node.knobs():
                if knob in SUPPORTED_KNOBS:
                    nuke.frame(node[knob].value())


def create_sticky_reference(frame_value):
    """
        When nothing is selected, it creates a StickyNote with the current frame as the label
    """

    sticky_reference = nuke.createNode('StickyNote', inpanel=False)
    sticky_reference['label'].setValue('{}'.format(frame_value))
    sticky_reference['note_font'].setValue('Verdana Bold')
    sticky_reference['note_font_size'].setValue(50)


def get_frame(from_user):
    """
        Get the frame value either from user input or the current frame.
        Parameters:
            - from_user (bool): If True, prompts the user to input a frame. Defaults to False.
    """

    if from_user:
        user_frame = nuke.getInput('set frame to', '{}'.format(str(nuke.frame())))
        if user_frame:
            try:
                frame_value = int(user_frame)
                return frame_value
            except ValueError as error:
                nuke.message('You must write an integer value! (e.g., 1055)\n{}'.format(error))
                return None

    else:
        return nuke.frame()


def get_selection(multiple_nodes=True):
    """
        Get the selected nodes in the Nuke script.
        Parameters:
            - multiple_nodes (bool): If True, returns a list of selected nodes;
                                     returns a single selected node otherwise.
    """

    nodes = nuke.selectedNodes()

    if multiple_nodes:
        return nodes

    else:
        if len(nodes) == 1:
            return nuke.selectedNode()

        else :
            if len(nodes) > 1:
                nuke.message('Select only one node')
            else:
                nuke.message('Select something!')

            return None
