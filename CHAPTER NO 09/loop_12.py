list_of_tuples = [(1, 'python'), (2, 'django'), (3, 'git')]
for number, lang in list_of_tuples:
    if lang == 'django':
        print("Django Found")
        break
    print(f"{number} - {lang}")
