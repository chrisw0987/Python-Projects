The Linux shell command: ls -lR > lsoutput.txt
prints the recursively explored contents of the filesystem starting at the current directory (using a
long listing format) to the standard output. The output is redirected to a file called lsoutput.txt in
the current directory.

System management requires operating on filesystem data from within our programs and scripts.
Properly representing the entities in the file system within our programs is a good application of
object orientation.

Please create three classes: (a) FS_Item, (b) Folder, (c) File

a. FS_Item class: This class will be the parent class for the other two. Every FS_Item has a
single instance variable called name. The value of name is a string. The value of this instance
variables should be set by the __init__() method of the FS_Item class.

b. Folder class: This class will be a subclass of the FS_Item class. Folders represent
directories. In addition to the name attribute that is inherited from FS_Item, every instance of
the Folder class contains an additional instance variable called items, which should be
initialized as an empty list.

Define a method within the Folder class called add_item(), which takes an instance of
FS_Item (either a Folder or a File) as argument passed to a parameter called item. The
argument is appended to the current Folder objects self.items list. This method does not
return anything.

c. File class: This class will be a subclass of the FS_Item class. Files represent documents
stored in the file system. In addition to the name attribute that is inherited from FS_Item, every
instance of the File class contains an additional instance variable called size. The value of
this instance variable should be set by the __init__() method for the File class and
represent the size of the file in bytes.

d. Function Description: Write a function called load_fs(), which has a single parameter
called ls_output. The argument passed to ls_output is the name of a file which contains
the output of the system command ls -lR.

The function should read this file and use it to construct an internal representation of the part of
the file system recorded in the file named by ls_output. For each directory, create a Folder
object with the same name. Add each directory and document contained in that directory as a
Folder or File element of its items list. For each File element make sure to set its name
and filesize when adding it to the items list of the Folder that contains it.

When done the function should return a reference to the top-level Folder item (the one
corresponding to the top-level directory in ls_output.
