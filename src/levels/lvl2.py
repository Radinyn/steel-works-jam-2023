from pygame import Vector2
from components.text_box import TextBox
from game import Game
from components.sprite import Sprite
from components.trigger import Trigger
from core.math import BBox
from objective import Objective


class SecondLevel:
    def open(self, game: Game, prev_level_id: str) -> None:
        self.game = game

        self.game.map.load_from_file("res/next-test-level-map.png")

        self.game.enemy_manager.add_enemy("warrior", Vector2(4, 9))
        self.game.enemy_manager.add_enemy("sorcerer", Vector2(4, 2))
        self.game.enemy_manager.add_enemy("sorcerer", Vector2(5, 9))
        self.game.enemy_manager.add_enemy("warrior", Vector2(8, 8))
        self.game.enemy_manager.add_enemy("sorcerer", Vector2(8, 6))
        self.game.enemy_manager.add_enemy("warrior", Vector2(16, 10))
        self.game.enemy_manager.add_enemy("warrior", Vector2(22, 2))


        # self.game.enemy_manager.add_enemy("boss", Vector2(5, 9))
        # exit : Vector2(24, 2)
        self.game.player.position = Vector2(2, 11)
        self.game.camera.position = (
            self.game.player.position * self.game.map.get_tile_size()
        )

        self.level_art = Sprite(path="res/next-test-level-art.png", scale=4)

        self.objective = Objective(
            {},
            kill_all=True
        )

        self.trigger = Trigger(
            player=self.game.player,
            bbox=BBox(x=24, y=2, w=0.1, h=2),
            on_enter=lambda: self.game.set_level(level_id="lvl3"),
        )

    def update(self):
        if self.objective.satisfied(self.game.player, self.game.enemy_manager._enemies):
            self.trigger.update(window=self.game.window)

    def draw_bg(self):
        self.level_art.draw(camera=self.game.camera)
