"""from pathlib import Path

with open('test.txt') as test_file:
    print(test_file.read())

with open('test.txt') as test_file:
    print(test_file.readlines())

with open('new.txt', 'w') as new_file:
    new_file.write("First comment\n")

with open('new.txt') as new_file:
    print(new_file.read())

with open('nex.txt', 'a') as new_file:
    new_file.write("Second line \n")

with open('nex.txt') as new_file:
    print(new_file.read())

if Path('nex.txt').exists():
    Path('nex.txt').unlink() 

print(Path('nex.txt').exists())

test_file_two = open('test_two.txt', 'a')
test_file_two.write("First comment \n")
test_file_two.write("Second comment \n")
test_file_two.close()

with open('test_two.txt') as test_file_two:
    lines = test_file_two.readlines()
    for line in lines:
        print(line)

my_file = Path('test.txt')
if my_file.exists():
    my_file.unlink()

    """


from pathlib import Path

files_dir = Path("files")
files_dir.mkdir(exist_ok=True)

first_file = files_dir / "first.txt"
second_file = files_dir / "second.txt"

with open(first_file, "w") as f:
    f.write("First line \nSecond line \nThird line \n")

with open(second_file, "w") as f:
    lines = [
        "First line in second file",
        "Second line in second file",
        "Third line in second file",
    ]

    for line in lines:
        f.write(line + "\n")

with open(first_file) as f:
    print(f.read())

with open(second_file) as f:
    for line in f:
        print(line.strip())

"""     while True:
        line = f.readline()
        if not line:
            break
        print(line.strip()) """


first_file.unlink()
second_file.unlink()
files_dir.rmdir()
