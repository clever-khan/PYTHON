my_dict = {
    1 : 'python',
    2 : 'django',
    3 : 'git',
}
list_of_tuples = [(num, lang) for num in my_dict for lang in my_dict.values() if my_dict[num] == lang]
print(list_of_tuples)
