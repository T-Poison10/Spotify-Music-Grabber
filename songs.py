"""This script defines the `Songs` class, which is used to read song names from a text file."""

class Songs:
    def __init__(self, path) -> None:
        self.path = path

    def readNames(self):
        names = []
        with open(self.path, "r") as file:
            for line in file:
                names.append(line)
        return names


if __name__ == "__main__":
    song = Songs("Data/Music.txt")
    names = song.readNames()
    for name in names:
        print(name)
