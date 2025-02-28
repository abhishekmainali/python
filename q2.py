import os

def read_file_content(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def write_to_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def find_longest_word(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        words = file.read().split()
    return max(words, key=len) if words else None

def check_file_empty(file_path):
    return os.stat(file_path).st_size == 0  

def reverse_file_content(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()[::-1]  

    new_file_path = os.path.join(os.path.dirname(file_path), "reversed.txt")
    with open(new_file_path, 'w', encoding='utf-8') as new_file:
        new_file.write(content)

def convert_to_uppercase(words):
    return list(map(lambda word: word.upper(), words))

def filter_even_length_words(words):
    return list(filter(lambda word: len(word) % 2 == 0, words))

def process_file_with_lambda(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    processed_lines = [" ".join(map(lambda word: word.upper(), line.split())) for line in lines]

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write("\n".join(processed_lines))

if __name__ == "__main__":
    file_path = r"D:\coding\python\week 4"

    print("File Content:")
    print(read_file_content(file_path))

    
    write_to_file(file_path, "Hello World! Python is fun.")

    print("Longest Word:", find_longest_word(file_path))

    print("Is File Empty:", check_file_empty(file_path))

    reverse_file_content(file_path)
    print("Reversed file content saved.")

    words_list = ["hello", "world", "python", "lambda"]
    print("Uppercase Words:", convert_to_uppercase(words_list))

    print("Even-Length Words:", filter_even_length_words(words_list))

    process_file_with_lambda(file_path)
    print("File content converted to uppercase.")