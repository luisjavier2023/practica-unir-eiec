"""
License: Apache
Organization: UNIR
"""

import os
import sys

DEFAULT_FILENAME = "words.txt"
DEFAULT_DUPLICATES = False
DEFAULT_ASC_DESC = True # Usar True para ascendente y False para descendente


def sort_list(items, ascending=True):
    if not isinstance(items, list):
        raise RuntimeError(f"Can't order {type(items)}")

    return sorted(items, reverse=(not ascending))

def descending_sort_list(items, ascending=False):
    if not isinstance(items, list):
        raise RuntimeError(f"can't order {type(items)}")

    return sorted(items, reverse=(not ascending))

def remove_duplicates_from_list(items):
    return list(set(items))

if __name__ == "__main__":
    filename = DEFAULT_FILENAME
    remove_duplicates = DEFAULT_DUPLICATES
    asc_desc_value = DEFAULT_ASC_DESC
    add_to_list = ""

    if len(sys.argv) >= 4:
        filename = sys.argv[1]
        remove_duplicates = sys.argv[2].lower() == "yes"
        asc_desc_value = sys.argv[3].lower() == "yes"
    else:
        print("The file must be indicated as the first argument")
        print("The second argument indicates whether you want to eliminate duplicates")
        print("The third argument indicates whether the order is ascending or descending.")
        print("The fourth argument indicates whether the order is ascending or descending.")
        sys.exit(1)

    print(f"The words from the file will be read {filename}")
    file_path = os.path.join(".", filename)
    if os.path.isfile(file_path):
        word_list = []
        with open(file_path, "r") as file:
            for line in file:
                word_list.append(line.strip())
    else:
        print(f"The file {filename} does not exist")
        word_list = ["ravenclaw", "gryffindor", "slytherin", "hufflepuff"]

    if len(sys.argv) == 5:
        word_list.append(sys.argv[4])

    if remove_duplicates:
        word_list = remove_duplicates_from_list(word_list)

    if asc_desc_value:
        print(sort_list(word_list))
    else:
        print(descending_sort_list(word_list))
