import nuke
import os

def create_directory_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def get_user_root_directory(selected_format, resolution):
    user = os.getenv('USER')
    root_directory = "/FURY/SlateX/Artists/SPR/Supremes_002_002-010_MP/Comp/Output"
    user_directory = os.path.join(root_directory, selected_format, resolution, user)
    return user_directory

def get_next_version(file_path):
    base, ext = os.path.splitext(file_path)
    version = 1
    while os.path.exists(f"{base}_v{version:03d}{ext}"):
        version += 1
    return f"_v{version:03d}"

def update_write_node_output_path(write_node, read_file_path):
    base_name = os.path.basename(read_file_path)
    base, _ = os.path.splitext(base_name)

    format_options = ["exr", "dpx", "jpeg", "mov"]
    selected_format_index = nuke.choice("Choose the file format", "Select Format", format_options)

    if selected_format_index is None:
        return

    selected_format = format_options[selected_format_index]
    file_extension = f".{selected_format}"

    user_directory = ""

    if selected_format == "mov":
        resolution_options = ["4k", "HD"]
        resolution_index = nuke.choice("Choose resolution", "Select Resolution", resolution_options)
        if resolution_index is None:
            return
        resolution = resolution_options[resolution_index]
        user_directory = get_user_root_directory(selected_format, resolution)
    else:
        user_directory = get_user_root_directory(selected_format, "")

    create_directory_if_not_exists(user_directory)

    version = get_next_version(os.path.join(user_directory, f"{base}{file_extension}"))
    file_name = f"{base}{version}"
    file_path = os.path.join(user_directory, f"{file_name}{file_extension}")
    write_node['file'].setValue(file_path)

def save_composite():
    selected_node = nuke.selectedNode()

    if selected_node is None or selected_node.Class() != 'Write':
        nuke.message("Select a Write node")
        return
   
    connected_read_nodes = [node for node in selected_node.dependencies() if node.Class() == 'Read']
    if not connected_read_nodes:
        nuke.message("Connect a Read node to Write node.")
        return

    read_file_path = connected_read_nodes[0]['file'].value()
    update_write_node_output_path(selected_node, read_file_path)

    script_name = nuke.root().name()
    nuke.scriptSaveAs(script_name)
    nuke.message(f"Write Node's Filepath Updated: {selected_node['file'].value()}")

nuke.menu("Nuke").addCommand("File/Automatic Save", "save_composite()", "ctrl+w")


'''
# selected format folder is already availble inside root directory & file saved as per selected format wise in folder

import nuke
import os


def create_directory_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def get_user_root_directory(selected_format):
    user = os.getenv('USER')
    root_directory = "/FURY/SlateX/Artists/SPR/Supremes_002_002-010_MP/Comp/Output"
    user_directory = os.path.join(root_directory, selected_format, user)
    return user_directory


def get_next_version(file_path):
    base, ext = os.path.splitext(file_path)
    version = 1
    while os.path.exists(f"{base}_v{version:03d}{ext}"):
        version += 1
    return f"_v{version:03d}"


def update_write_node_output_path(write_node, read_file_path):
    base_name = os.path.basename(read_file_path)
    base, _ = os.path.splitext(base_name)

    format_options = ["exr", "dpx", "jpeg", "mov"]
    selected_format_index = nuke.choice("Choose the file format", "Select Format", format_options)

    if selected_format_index is None:
        return

    selected_format = format_options[selected_format_index]
    file_extension = f".{selected_format}"

    user_directory = get_user_root_directory(selected_format)
    create_directory_if_not_exists(user_directory)

    version = get_next_version(os.path.join(user_directory, f"{base}{file_extension}"))
    file_name = f"{base}{version}"
    file_path = os.path.join(user_directory, f"{file_name}{file_extension}")
    write_node['file'].setValue(file_path)


def save_composite():
    selected_node = nuke.selectedNode()

    if selected_node is None or selected_node.Class() != 'Write':
        nuke.message("Select a Write node")
        return

    connected_read_nodes = [node for node in selected_node.dependencies() if node.Class() == 'Read']

    if not connected_read_nodes:
        nuke.message("Connect a Read node to Write node.")
        return
    read_file_path = connected_read_nodes[0]['file'].value()
    update_write_node_output_path(selected_node, read_file_path)

    script_name = nuke.root().name()
    nuke.scriptSaveAs(script_name)
    nuke.message(f"Write Node's Filepath Updated: {selected_node['file'].value()}")

nuke.menu("Nuke").addCommand("File/Automatic Save", "save_composite()", "ctrl+w")

'''

##############################################################################################################################

'''
# selected format folder is already availble inside root directory , but file not saved as per selected format wise in folder

import nuke
import os

def create_directory_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def get_user_root_directory():
    user = os.getenv('USER')
    root_directory = "/FURY/SlateX/Artists/SPR/Supremes_002_002-010_MP/Comp/Output/exr"
    user_directory = os.path.join(root_directory, user)
    return user_directory


def get_next_version(file_path):
    base, ext = os.path.splitext(file_path)
    version = 1
    while os.path.exists(f"{base}_v{version:03d}{ext}"):
        version += 1
    return f"_v{version:03d}"


def update_write_node_output_path(write_node, read_file_path):
    base_name = os.path.basename(read_file_path)
    base, _ = os.path.splitext(base_name)

    user_directory = get_user_root_directory()
    create_directory_if_not_exists(user_directory)

    format_options = ["exr", "mov", "dpx", "jpeg"]
    selected_format_index = nuke.choice("Choose the file format", "Select Format", format_options)

    if selected_format_index is None:
        return

    selected_format = format_options[selected_format_index]
    file_extension = f".{selected_format}"

    version = get_next_version(os.path.join(user_directory, f"{base}{file_extension}"))
    file_name = f"{base}{version}"
    file_path = os.path.join(user_directory, f"{file_name}{file_extension}")
    write_node['file'].setValue(file_path)


def save_composite():
    selected_node = nuke.selectedNode()

    if selected_node is None or selected_node.Class() != 'Write':
        nuke.message("Select a Write node before running this script.")
        return

    connected_read_nodes = [node for node in selected_node.dependencies() if node.Class() == 'Read']

    if not connected_read_nodes:
        nuke.message("Connect a Read node to the selected Write node.")
        return

    read_file_path = connected_read_nodes[0]['file'].value()
    update_write_node_output_path(selected_node, read_file_path)

    script_name = nuke.root().name()
    nuke.scriptSaveAs(script_name)
    nuke.message(f"Write Node's Filepath Updated: {selected_node['file'].value()}")
'''

###################################################################################################################################

'''
# selected format folder is not exist inside root directory

import nuke
import os

def create_directory_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def get_user_root_directory(selected_format):
    user = os.getenv('USER')
    dir1 = '/FURY/SlateX/Artists/SPR/Supremes_002_002-010_MP/Comp/Output'
    root_directory = os.path.join(dir1, selected_format)
    user_directory = os.path.join(root_directory, user)
    
    create_directory_if_not_exists(root_directory)
    return user_directory


def get_next_version(file_path):
    base, ext = os.path.splitext(file_path)
    version = 1
    while os.path.exists(f"{base}_v{version:03d}{ext}"):
        version += 1
    return f"_v{version:03d}"


def update_write_node_output_path(write_node, read_file_path):
    base_name = os.path.basename(read_file_path)
    base, _ = os.path.splitext(base_name)

    format_options = ["exr", "mov", "dpx", "jpeg"]
    selected_format_index = nuke.choice("Choose the file format", "Select Format", format_options)

    if selected_format_index is None:
        return

    selected_format = format_options[selected_format_index]
    file_extension = f".{selected_format}"

    user_directory = get_user_root_directory(selected_format)
    create_directory_if_not_exists(user_directory)

    version = get_next_version(os.path.join(user_directory, f"{base}{file_extension}"))
    file_name = f"{base}{version}"
    file_path = os.path.join(user_directory, f"{file_name}{file_extension}")
    write_node['file'].setValue(file_path)

def save_composite():
    selected_node = nuke.selectedNode()

    if selected_node is None or selected_node.Class() != 'Write':
        nuke.message("Select a Write node before running this script.")
        return

    connected_read_nodes = [node for node in selected_node.dependencies() if node.Class() == 'Read']

    if not connected_read_nodes:
        nuke.message("Connect a Read node to the selected Write node.")
        return

    read_file_path = connected_read_nodes[0]['file'].value()
    update_write_node_output_path(selected_node, read_file_path)

    script_name = nuke.root().name()
    nuke.scriptSaveAs(script_name)
    nuke.message(f"Write Node's Filepath Updated: {selected_node['file'].value()}")
'''



#####################################################################################################################################



