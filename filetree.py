import os

def make_list(fp: str) -> list:
    # files = [item for item in os.listdir(fp)]
    contents = []
    for item in os.listdir(fp):
        contents.append(item)
    return contents

def print_items(fp: str, contents: list, indent: int) -> None:
    files = []

    for item in contents:
        if os.path.isdir(os.path.join(fp, item)):
            print(f"{indent*' '}{item}")
            print_file_tree(
                os.path.join(fp, item),
                indent+2
            )
        else:
            files.append(item)

    for file in files: print(f"{indent*' '}{file}")

def print_file_tree(fp: str, indent: int = 0) -> None:
    contents = make_list(fp)
    print_items(fp, contents, indent)


if __name__ == "__main__":
    cwd = os.getcwd()

    print_file_tree(cwd)
