from pathlib import Path

path = Path("emails")
# Making a directory
# path.mkdir()
# Removing a directory
# path.rmdir()


# If we want to know all the files with .py in current directory
# here path() with no argument indicates current path
path = Path()
for file in path.glob('*.py'):
    print(file)
