height = 5

for i in range(1, height + 1):
    spaces = " " * (height - i)
    hashes = "#" * (2 * i - 1)
    print(f"{spaces}{hashes}")

trunk_spaces = " " * (height - 1)
trunk_hashes = "#"
print(f"{trunk_spaces}{trunk_hashes}")
