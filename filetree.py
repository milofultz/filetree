import os

def make_list(fp: str) -> list:
    # files = [item for item in os.listdir(fp)]
    contents = []
    for item in os.listdir(fp):
        contents.append(item)
    return contents

def print_items(fp: str, contents: list, indent: int, pipes: list) -> None:
    tree_base = ''
    for i in range(indent):
        tree_base += ' '
        if i%4 == 0 and i != 0:
            pipe_index = int(i/4)-1
            tree_base += pipes[pipe_index]

    files = []
    folders = []

    for item in contents:
        if os.path.isdir(os.path.join(fp, item)):
            folders.append(item)
        else:
            files.append(item)

    for folder in folders:
        d = f"{tree_base} |--- {folder}"
        if folder == folders[-1] and not files:
            pipes[-1] = ' '
            d = '\\'.join(d.rsplit('|', 1))
        print(d)
        pipes.append('|')
        print_file_tree(
                os.path.join(fp, folder),
                indent+4,
                pipes
            )
        pipes.pop()

    for file in files:
        f = f"{tree_base} |--- {file}"
        if file == files[-1]:
            pipes[-1] = ' '
            f = '\\'.join(f.rsplit('|', 1))
        print(f)

def print_file_tree(fp: str, indent: int, pipes: list) -> None:
    contents = make_list(fp)
    print_items(fp, contents, indent, pipes)


if __name__ == "__main__":
    # cwd = os.getcwd()
    cwd = '/Users/oldsilverboi/Desktop'

    print(f'.\n`-- {cwd}')
    print_file_tree(cwd, 4, ['|'])