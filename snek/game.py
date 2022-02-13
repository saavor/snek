import pygame
from snek.logger import *


class game:
    def __init__(self) -> None:
        self.running = False
        self.display = None
        self.framerate = 60

    def setup(self):
        # place holder
        error("setup not defined")

    def update(self):
        # place holder
        error("Update not defined")

    def run(self):
        self.running = True

        # Run setup
        self.setup()

        while self.running:

            # Check for game close
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Run update
            self.update()

            pygame.display.update()
            pygame.time.delay(round(1000 / self.framerate))

        # Quit
        pygame.quit()
