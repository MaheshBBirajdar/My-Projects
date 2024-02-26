import pandas as pd
import os
import subprocess

file_path = "newxl.xls"
dependency = input("Enter Dependency Name : ")

df = pd.read_excel(file_path)
rc = df.shape[0]
for i in range(rc) :
    cl = df.iloc[i].tolist()
    
    given_exr_files_path = cl[0]
    given_scope_of_work = cl[1]
    
    saving_nk_file_path = cl[4]
    
    # mj = given_exr_files_path.split(".")
    # kj = mj[0]
    # rj = kj[0:50]
    exx = given_exr_files_path
    folder_path = exx
    files = os.listdir(folder_path)

    sorted_files = sorted(files)

    fst = sorted_files[0]
    fs = fst.split(".")
    fn = fs[0]
    fst_frame = fn[-4:]

    lst = sorted_files[-1]
    ls = lst.split(".")
    ln = ls[0]
    lst_frame = ln[-4:]

    output_file_path = ""
    list_obj1 = given_exr_files_path

    if (dependency.lower()== "cmp" or dependency.lower()=="comp"):
        a = "_cmp_OS_v000"
        output_file_path = list_obj1+a
    
    elif (dependency.lower()== "pnt" or dependency.lower()=="paint"):
        a = "_pnt_OS_v000"
        output_file_path = list_obj1+a

    print("output_file_path :" , output_file_path)
    all_exr_sorted_files = sorted(os.listdir(given_exr_files_path))
    specific_exr_file_name = all_exr_sorted_files[0]  
    extracted_exr_file_name = specific_exr_file_name.split(".")[0]
    read_section_exr_files_path = given_exr_files_path+extracted_exr_file_name[:-4]+"%04d.exr"   
    
    nk_file_path = "script_struct.nk"
    output_file_path_hd = "/oshome/mayurlagad/Desktop/Scr/outputs/HD/new_output_file_{}.mov".format(i)
    output_file_path_4k = "/oshome/mayurlagad/Desktop/Scr/outputs/4k/new_output_file_{}.mov".format(i)
    output_file_path_nk = "/oshome/mayurlagad/Desktop/mjj/WRI_103_0230_cmp_OS_v000__{}.nk".format(i)
    scope_of_work = given_scope_of_work
    new_root_name = output_file_path_nk
    new_root_first_frame = int(fst_frame) -1
    new_root_last_frame = lst_frame
    new_read_first_frame = int(new_root_first_frame) + 1
    new_read_last_frame = new_root_last_frame

    def modify_nk_file(nk_file_path, output_file_path_nk, output_file_path_hd, output_file_path_4k, new_root_name, new_root_first_frame, new_root_last_frame, new_read_first_frame, new_read_last_frame, scope_of_work, read_section_exr_files_path):
        with open(nk_file_path, 'r') as file:
            lines = file.readlines()
            
        write_index_1 = lines.index('Write {\n')
        write_end_index_1 = lines.index('}\n', write_index_1)

        # Extract the section for the first write object
        write_section_1 = lines[write_index_1:write_end_index_1 + 1]

        # Replace output file path for the first write object
        for i, line in enumerate(write_section_1):
            if line.startswith(' file '):
                write_section_1[i] = ' file {}\n'.format(output_file_path_4k)

        # Update lines with modified section for the first write object
        lines[write_index_1:write_end_index_1 + 1] = write_section_1

        # Find indices for the second write object
        write_index_2 = lines.index('Write {\n', write_end_index_1 + 1)
        write_end_index_2 = lines.index('}\n', write_index_2)

        # Extract the section for the second write object
        write_section_2 = lines[write_index_2:write_end_index_2 + 1]

        # Replace output file path for the second write object
        for i, line in enumerate(write_section_2):
            if line.startswith(' file '):
                write_section_2[i] = ' file {}\n'.format(output_file_path_hd)

        # Update lines with modified section for the second write object
        lines[write_index_2:write_end_index_2 + 1] = write_section_2
     
        
        # Flag to track if the first occurrence of f_vfx_scope_of_work has been found
        first_occurrence_found = False

        # Find and modify the line containing f_vfx_scope_of_work
        for i, line in enumerate(lines):
            if 'f_vfx_scope_of_work' in line:
                if first_occurrence_found:
                    # Replace the value in the line only if scope_of_work is provided
                    parts = line.split('"')
                    if len(parts) >= 2:
                        lines[i] = parts[0] + '"' + scope_of_work + '"' + parts[2]
                    break
                else:
                    # Set the flag to True once the first occurrence is found
                    first_occurrence_found = True

        # Find and modify Root section
        root_index = lines.index('Root {\n')
        root_end_index = lines.index('}\n', root_index)
        root_section = lines[root_index:root_end_index + 1]

        for i, line in enumerate(root_section):
            if line.startswith(' name '):
                root_section[i] = ' name "{}"\n'.format(new_root_name)
            elif line.startswith(' first_frame '):
                root_section[i] = ' first_frame {}\n'.format(new_root_first_frame)
            elif line.startswith(" frame "):
                root_section[i] = ' frame {}\n'.format(new_root_first_frame)
            elif line.startswith(' last_frame '):
                root_section[i] = ' last_frame {}\n'.format(new_root_last_frame)

        lines[root_index:root_end_index + 1] = root_section

        # Find and modify Read section
        read_index = lines.index('Read {\n')
        read_end_index = lines.index('}\n', read_index)
        read_section = lines[read_index:read_end_index + 1]

        for i, line in enumerate(read_section):
            if line.startswith(' first ') :
                read_section[i] = ' first {}\n'.format(new_read_first_frame)
            elif line.startswith(' file ') : 
                read_section[i] = ' file {}\n'.format(read_section_exr_files_path)
            elif line.startswith(' last ') :
                read_section[i] = ' last {}\n'.format(new_read_last_frame)
            elif line.startswith(' origfirst '):
                read_section[i] = ' origfirst {}\n'.format(new_read_first_frame)
            elif line.startswith(' origlast '):
                read_section[i] = ' origlast {}\n'.format(new_read_last_frame)
                
                

        lines[read_index:read_end_index + 1] = read_section

        # Write modified content to the output file
        with open(output_file_path_nk, 'w') as file:
            file.writelines(lines)
        print("File created successfully.")

        

    modify_nk_file(nk_file_path, output_file_path_nk, output_file_path_hd, output_file_path_4k, new_root_name, new_root_first_frame, new_root_last_frame, new_read_first_frame, new_read_last_frame, scope_of_work, read_section_exr_files_path)

    def render_with_nuke(nuke_path, script_path, exr_files_path):
        """
        Render .exr files to create a .mov file using Nuke software.
        
        Args:
        - nuke_path (str): Path to Nuke executable.
        - script_path (str): Path to the Nuke script file.
        - exr_files_path (str): Path to the folder containing .exr files.
        """ 
        # Construct the command to run Nuke in command line mode
        command = [nuke_path, "-x", script_path]
        
        # Set environment variable for Nuke to use the correct folder for .exr files
        os.environ["NUKE_EXR_FOLDER"] = exr_files_path
        
        # Execute the command
        try:
            subprocess.run(command, check=True)
            print("Rendering completed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error: Rendering failed with exit code {e.returncode}")

    if __name__ == "__main__":
        # Paths to Nuke executable, script file, and .exr folder
        nuke_path = "/core/Software/nuke/Nuke12.1v5/Nuke12.1"
        script_path = output_file_path_nk
        exr_files_path = given_exr_files_path
        # Call the function to render with Nuke
        # print("exr files path is : ",exr_files_path)
        render_with_nuke(nuke_path, script_path, exr_files_path)
