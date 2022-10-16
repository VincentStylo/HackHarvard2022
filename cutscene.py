import moviepy.editor
from pygame.sprite import Sprite
import pygame
from re import S
import os
os.environ["IMAGEIO_FFMPEG_EXE"] = "/usr/bin/ffmpeg"


class Intro(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        video = moviepy.editor.VideoFileClip("movies/IntroCutscene.mp4")
        video.preview()
