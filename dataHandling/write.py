from typing import List

def write_file(file_path: str, lines: List[str]) -> None:
    """
    Writes a list of strings to a text file, each string on a new line.

    Args:
    file_path (str): The path to the text file.
    lines (List[str]): A list of strings to write to the file.

    Returns:
    None
    """
    with open(file_path, 'w', encoding='utf-8') as file:
        for line in lines:
            file.write(line + '\n')
