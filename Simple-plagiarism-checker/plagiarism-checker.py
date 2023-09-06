from difflib import SequenceMatcher

with open ("Text1.txt") as first_file, open ("Text2.txt") as second_file:
    file1 = first_file.read()
    file2 = second_file.read()

    similarity = SequenceMatcher(None, file1, file2).ratio()

    print(f"{round(similarity*100, 2)}% plagiarized")