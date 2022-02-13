from snek import *  # src bc thats where the library is
import sys


class game1(game):
    def setup(self):
        self.display = create_window(640, 480)

    def update(self):
        background(self, 255, 255, 0)
        rect(self, 100, 100, 200, 200, (0, 0, 255))


def main():
    gaming = game1()
    gaming.run()


if __name__ == "__main__":
    sys.exit(main())
