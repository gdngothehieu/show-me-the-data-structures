
import os

#Directory Listing
    # ./testdir
    # ./testdir/subdir1
    # ./testdir/subdir1/a.c
    # ./testdir/subdir1/a.h
    # ./testdir/subdir2
    # ./testdir/subdir2/.gitkeep
    # ./testdir/subdir3
    # ./testdir/subdir3/subsubdir1
    # ./testdir/subdir3/subsubdir1/b.c
    # ./testdir/subdir3/subsubdir1/b.h
    # ./testdir/subdir4
    # ./testdir/subdir4/.gitkeep
    # ./testdir/subdir5
    # ./testdir/subdir5/a.c
    # ./testdir/subdir5/a.h
    # ./testdir/t1.c
    # ./testdir/t1.h

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """

    

        # Iterate through entire directory
            #If isfile - file ends with suffix - append to filesList else do nothing
            #else- Join paths and call function recursively. 

    filesList = []

    try:
         content = os.listdir(path)
    except FileNotFoundError:
        return "Directory does not exist"

    

    for item in content:
        if os.path.isfile("{}/{}".format(path,item)):
            
            try:
                if "{}/{}".format(path,item).endswith(suffix):
                    file_path = ("{}/{}".format(path,item))
                    filesList.append(file_path)
            except TypeError:
                return "Suffix must be of type str."

            
        else:
            new_path = "{}/{}".format(path,item)

            sub_compound = find_files(suffix,new_path)

            for file in sub_compound:
                filesList.append(file)
    


    return filesList

## Test Cases

print(find_files('.h','./testdir')) #Returns ['./testdir/subdir3/subsubdir1/b.h', './testdir/subdir5/a.h', './testdir/t1.h', './testdir/subdir1/a.h']
print(find_files('.h','./testdir/subdir3/subsubdir1')) #Returns ['./testdir/subdir3/subsubdir1/b.h']
print(find_files('.gitkeep','./testdir')) #Returns ['./testdir/subdir4/.gitkeep', './testdir/subdir2/.gitkeep']

## Edge Cases
print(find_files('.h','./testdirsdfs')) #Returns directory does not exist.
print(find_files('.py','./testdir')) #Returns []
print(find_files(-1,'./testdir')) #Returns TypeError: ends with first arg must be str or a tuple of str, not int


