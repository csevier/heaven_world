import pygame
from settings import *


class ObjectRenderer:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.render_surface = game.render_surface
        self.wall_textures = self.load_wall_textures()
        self.sky_image = self.get_texture("resources/textures/sky_2.png", (WIDTH, HALF_HEIGHT))
        self.sky_offset = 0
        self.floor = pygame.Surface((WIDTH, HEIGHT / 2))
        self.floor.fill("black")

    def draw(self):
        self.draw_background()
        self.render_game_object()
        pygame.transform.scale(self.render_surface,
                               (self.screen.get_width(),
                               self.screen.get_height()),
                               dest_surface=self.screen)

    def draw_background(self):
        self.sky_offset = (self.sky_offset + 4.5 * (self.game.player.rel / 4)) % WIDTH
        self.render_surface.blit(self.sky_image, (-self.sky_offset, 0))
        self.render_surface.blit(self.sky_image, (-self.sky_offset + WIDTH, 0))
        self.render_surface.blit(self.floor, (0, HEIGHT / 2))

    def render_game_object(self):
        list_objects = sorted(self.game.raycasting.objects_to_render, key=lambda t: t[0], reverse=True)
        for depth, image, pos in list_objects:
            self.render_surface.blit(image, pos)

    @staticmethod
    def get_texture(path, res=(TEXTURE_SIZE, TEXTURE_SIZE)):
        texture = pygame.image.load(path).convert_alpha()
        return pygame.transform.scale(texture, res)

    def load_wall_textures(self):
        return {
            1: self.get_texture('resources/textures/1.png'),
            2: self.get_texture('resources/textures/2.png'),
            3: self.get_texture('resources/textures/3.png'),
            4: self.get_texture('resources/textures/4.png'),
            5: self.get_texture('resources/textures/5.png'),
        }