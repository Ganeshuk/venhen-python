from typing import List

def read_file(file_path: str) -> List[str]:
    """
    Reads a text file and returns a list of strings, each representing a line in the file.

    Args:
    file_path (str): The path to the text file.

    Returns:
    List[str]: A list of strings, each representing a line in the file.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]
