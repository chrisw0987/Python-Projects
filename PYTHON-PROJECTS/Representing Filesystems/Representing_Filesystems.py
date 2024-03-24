class FS_Item:
    def __init__(self, name):
        self.name = name

class Folder(FS_Item):
    def __init__(self, name):
        super().__init__(name)
        self.items = []

    def add_item(self, item):
        self.items.append(item)

class File(FS_Item):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

def load_fs(ls_output):
    with open(ls_output, 'r') as file:
        lines = file.readlines()

    root_f = Folder("Root")
    current_f = root_f

    for l in lines:
        if l.startswith('./'):
            directory_p = l.strip().strip(':')[2:]
            current_f = get_folder(root_f, directory_p)

        elif l.startswith('-'):
          
            parts = l.split()
            f_name = parts[-1]
            f_size = int(parts[4])
            current_f.add_item(File(f_name, f_size))

    return root_f


def get_folder(root_f, directory_p):
    folder = directory_p.split('/')
    current_f = root_f
    
    for f_name in folder:
        found = False

        for i in current_f.items:
            if isinstance(i, Folder) and i.name == f_name:
                current_f = i
                found = True
                break
        
        if not found:
            new_f = Folder(f_name)
            current_f.add_item(new_f)
            current_f = new_f

    return current_f


rf = load_fs("lsoutput.txt")


def print_folder(folder, indent=0):
    print("  " * indent + folder.name + "/")
    for i in folder.items:
        if isinstance(i, Folder):
            print_folder(i, indent + 1)
        else:
            print("  " * (indent + 1) + f"{i.name} ({i.size} bytes)")

print_folder(rf)