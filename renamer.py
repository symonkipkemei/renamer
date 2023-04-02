import pathlib


# path to my desktop
start_path = "/mnt/d/New folder"
start_path_obj = pathlib.Path(start_path)



# create new folder
new_path = pathlib.Path(f"{start_path}/Gachietha-chronicles")
new_path.mkdir(exist_ok=True )


def check_move_files(path,new_path) -> None:
    """check if file is  png it then moves to a separate folder

    Args:
        path (Path): path of the current folder/file/directory

    """

    if path.suffix == ".rvt" or path.suffix == ".txt" or path.suffix == ".png":
       #renaming by reverising their file names
       path_name = path.name
       new_name = path_name[::-1] + path.suffix
        # create a new path for the level_1 
       new_filepath = new_path.joinpath(new_name)
    
       #move files
       path.replace(new_filepath)




# create an object that points to where the level_1 are 


# starting level
for level_1 in start_path_obj.iterdir():
    if level_1.is_file():
        check_move_files(level_1,new_path)

    # level 1
    else:
        level_1_path = start_path_obj.joinpath(level_1)
        for level_2 in level_1_path.iterdir():
            if level_2.is_file():
                check_move_files(level_2,new_path)
            #level 2
            else:
                level_2_path = level_1_path.joinpath(level_2)
                for level_3 in level_2_path.iterdir():
                    if level_2.is_file():
                        check_move_files(level_3,new_path)

                
        
        



        

print("completed succesfully")