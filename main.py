@namespace
class SpriteKind:
    Object = SpriteKind.create()
    Starting = SpriteKind.create()
    Death = SpriteKind.create()

def on_overlap_tile(sprite22, location):
    global number_of_bricks
    tiles.set_tile_at(location, assets.tile("""
        transparency16
    """))
    Ball.set_velocity(Ball.vx, Ball.vy * SPEEDDDD)
    number_of_bricks = number_of_bricks - 1
    if number_of_bricks == 0:
        tiles.set_current_tilemap(tilemap("""
            level36
        """))
        
        def on_after():
            game.game_over(True)
            sprites.destroy_all_sprites_of_kind(SpriteKind.Object)
            sprites.destroy_all_sprites_of_kind(SpriteKind.projectile)
            sprites.destroy_all_sprites_of_kind(SpriteKind.player)
        timer.after(500, on_after)
        
    game.set_game_over_message(True, "GAME OVER! You WIN!! :3")
scene.on_overlap_tile(SpriteKind.projectile,
    assets.tile("""
        myTile
    """),
    on_overlap_tile)

def on_a_pressed():
    global SPEEDDDD, dead, Rock, House, Shroom, Ball
    SPEEDDDD = -1
    info.set_life(1)
    dead = sprites.create(img("""
            2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
                    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
                    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
                    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
                    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
                    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
                    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
                    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
                    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
                    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
                    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
                    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
                    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
                    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
                    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
                    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
        """),
        SpriteKind.Death)
    scaling.scale_to_percent(dead, 1000, ScaleDirection.UNIFORMLY, ScaleAnchor.MIDDLE)
    dead.set_position(80, 197)
    sprites.destroy_all_sprites_of_kind(SpriteKind.Starting)
    scene.set_background_image(assets.image("""
        Game_Stage
    """))
    Rock = sprites.create(assets.image("""
        rock
    """), SpriteKind.Object)
    Rock.set_stay_in_screen(True)
    Rock.set_position(154, 115)
    House = sprites.create(assets.image("""
        teeny_house
    """), SpriteKind.Object)
    scaling.scale_to_percent(House, 60, ScaleDirection.UNIFORMLY, ScaleAnchor.MIDDLE)
    House.set_stay_in_screen(True)
    House.set_position(-1, 117)
    Shroom = sprites.create(assets.image("""
        SHROOM
    """), SpriteKind.player)
    Shroom.set_stay_in_screen(True)
    Shroom.set_position(76, 106)
    controller.move_sprite(Shroom, 61, 0)
    Ball = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . 1 1 1 1 1 1 . . . . . 
                    . . . 1 1 6 6 6 6 6 6 1 1 . . . 
                    . . 1 1 6 6 6 6 6 6 6 6 1 1 . . 
                    . . 1 6 9 9 9 6 6 6 1 6 6 1 . . 
                    . 1 6 9 9 9 9 8 8 8 1 1 6 6 1 . 
                    . 1 6 9 9 9 8 8 8 8 8 5 6 6 1 . 
                    . 1 6 9 9 8 8 8 6 6 6 5 6 6 1 . 
                    . 1 8 9 9 8 8 6 6 6 6 6 5 6 1 . 
                    . 1 8 8 9 8 8 6 6 6 6 6 6 8 1 . 
                    . 1 8 8 9 9 8 6 6 6 6 6 8 8 1 . 
                    . . 1 8 8 9 8 8 6 6 6 8 8 1 . . 
                    . . 1 1 8 8 8 8 8 8 8 8 1 1 . . 
                    . . . 1 1 8 8 8 8 8 8 1 1 . . . 
                    . . . . . 1 1 1 1 1 1 . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.projectile)
    scaling.scale_to_percent(Ball, 65, ScaleDirection.UNIFORMLY, ScaleAnchor.MIDDLE)
    Ball.set_position(randint(45, 98), 37)
    Ball.set_velocity(26, 74)
    Ball.set_stay_in_screen(True)
    Ball.set_bounce_on_wall(True)
    tiles.set_current_tilemap(tilemap("""
        Bricks
    """))
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite, otherSprite):
    global SPEEDDDD
    SPEEDDDD = SPEEDDDD - 0.005
    Ball.y += -10
    Ball.set_velocity(Ball.vx, Ball.vy * SPEEDDDD)
sprites.on_overlap(SpriteKind.player, SpriteKind.projectile, on_on_overlap)

def on_on_overlap2(sprite2, otherSprite2):
    game.game_over(False)
    game.set_game_over_message(False, "LOSER!!! HAHAHA! >:)")
sprites.on_overlap(SpriteKind.projectile, SpriteKind.Death, on_on_overlap2)

Shroom: Sprite = None
House: Sprite = None
Rock: Sprite = None
dead: Sprite = None
SPEEDDDD = 0
Ball: Sprite = None
number_of_bricks = 0
number_of_bricks = 20
scene.set_background_image(assets.image("""
    Splash
"""))
game.splash("FOREST MAGIC!")
game.splash("Presented by:", "Amanda & Kylie")
A = sprites.create(assets.image("""
    A_Static
"""), SpriteKind.Starting)
scaling.scale_to_percent(A, 80, ScaleDirection.UNIFORMLY, ScaleAnchor.MIDDLE)
A.set_position(124, 71)
Press = sprites.create(assets.image("""
    Press
"""), SpriteKind.Starting)
scaling.scale_to_percent(Press, 300, ScaleDirection.UNIFORMLY, ScaleAnchor.MIDDLE)
Press.set_position(54, 88)
animation.run_image_animation(A, assets.animation("""
    A_Animated
"""), 200, True)