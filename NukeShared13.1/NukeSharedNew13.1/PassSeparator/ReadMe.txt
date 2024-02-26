Author:	Silvio André dos Santos
Profile: Nuke Compositor and Nuke Script Developer (starting at Mar-2014)
ToolName: Pass Separator
Description: This tool separates your image ReadNode Passes in a automated way. 
		You can choose to create only a Shuffle Node or a complete series of nodes including Crop, DiskCache and LayerContactSheet. 
		It also provides you an easy to follow screen instructions to rename your extracted passes or remove any pass from the final output.
		At the end, the tool automatically saves your work.

If you are interested in using it, please follow these 6 easy steps:

1. Locate your .nuke directory
	a. Open up Nuke
	b. Open the Script Editor Pane
	c. Type in
		nuke.pluginPath()
	d. Execute by pressing Ctrl+Enter
	e. The first result should be your .nuke directory

2. Open your .nuke directory in your operating system

3. Copy the file Pass_Sep.png to this .nuke directory

4. Adjust the menu.py file under .nuke directory 
	a. If the menu.py file doesn't exist:
		a.1 Simply copy the menu.py to the .nuke directory (captalization matters, so make sure the file name is in lowercase)
		a.2 Go directly to step 4.c 
	b. If you already have a menu.py file in your .nuke directory:
		b.0 First of all, make a backup copy of your menu.py file before any editing
		b.1. Open this menu.py file in your prefered text editor (notepad or Notepad++, do not use a Rich Text Word Processor cause it can generate invalid characters in your file)
		b.2. Copy the contents from my provided menu.py to your menu.py, please make sure that you do not override any old content to cause any unwanted errors

		Obs.: Be careful to not indent this code, copy it as-is, since Python is sensitive to indentation

		b3. Save the menu.py file

		c. Close Nuke (exit it completely)
	
		d. Open up Nuke again. If nuke doesn't start, please restore your original menu.py file (saved on step b.0.) and send me an e-mail asking for help

5. To use the tool:
	a. Open up Nuke
	b. Click the Channel Icon on the nodes toolbar and verify that the Pass Separator is at the bottom of the list
	c. Test it by creating a Read Node pointing to your image file containing several channel passes, select the read node and click Ctrl+Shift+a
	d. If everything is fine you will see a panel with two sections containing two buttons each one:
		d.1 The first section will not ask you any layer name and will do everything automatically
			- Shuffle Only Button: the code will generate a shuffle node for each pass
			- Complete Button: he code will generate a shuffle node for each pass, including a curvetool/crop node and a diskcache, additionally a LayerContactSheet is also generated
		d.2 The second section will do exactly the same thing as the first one, but it will give you a chance to rename or delete any layer from the final output

	e. Obs.: For the Complete button, if you do not like any created node like the LayerContactSheet or the DiskCache you can simply delete them as you would normally work in nuke
	f. Feel Free to provide your comments and feedback

6. Thank you and enjoy...

Silvio

