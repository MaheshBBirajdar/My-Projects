# FrameHandling Tool for Nuke

## Overview

The FrameHandling tool for Nuke provides convenient functions to manipulate frame-related operations in your Nuke scripts.

1. Enables you to set the reference frame for any selected nodes with a reference frame knob, such as Tracker, FrameHold, and VectorDistort.
2. Navigate to the reference frame of a selected node or search for a frame pattern
(the first appearance of two or more numbers together) in a StickyNote and use it to go to that frame.

## Usage

### Menu Commands

1. **Set to current frame**
   - Shortcut: `alt+shift+f`
   - Sets the reference frame for selected nodes to the current frame.

2. **Set to specific frame**
   - Shortcut: `alt+shift+g`
   - Prompts the user to input a frame and sets the reference frame for selected nodes.

3. **Go to Reference Frame**
   - Shortcut: `shift+g`
   - Navigates to the reference frame of a selected node.
   - Searches for a frame pattern (the first appearance of two or more numbers together) in a StickyNote and use it to go to that frame.
> Feel free to edit shortcuts in the menu.py.

## installation
Download the FrameHandling repository, rename the downloaded folder to ***FrameHandling*** and move it into your .nuke folder.

Add the following line to your init.py file, which is typically located in your .nuke folder:
```bash
"nuke.pluginAddPath('./FrameHandling')"
```

[Locating the default .nuke directory](https://support.foundry.com/hc/en-us/articles/207271649-Q100048-Nuke-Directory-Locations)

## Note
   - Support any node with these knobs: 'reference_frame', 'referenceFrame', 'first_frame', 'ref_frame'.
   - Support a StickyNote with a group of 2 or more numbers.
   
> Feel free to add more knobs in the **SUPPORTED_KNOBS** list

## Author
- **Author:** Luciano Cequinel
- **Contact:** lucianocequinel@gmail.com
- **Version:** 2.2.3
- **Release Date:** November 18, 2023
- **License:** MIT

## License
This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) License - see the LICENSE file for details.
