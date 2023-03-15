nested = [['python', 1], ['django', 2], ['git', 3]]
for lst in nested:
    print(f"List = {lst}")
    for item in lst:
        print(f"Item -> {item}")
