import pygame
import sys
from snek import logger

# Initialize pygame
pygame.init()

# Post init info logs
logger.info(f"SDL Version {pygame.get_sdl_version()}")
logger.info(f"pygame Version {pygame.version.ver}")
logger.info(f"Python Version: {sys.version}")

from snek.game import *
from snek.window import *

from snek.graphics.background import background
from snek.graphics.primitives import *
