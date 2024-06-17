@namespace
class SpriteKind:
    Object = SpriteKind.create()
    Starting = SpriteKind.create()

def on_a_pressed():
    global Rock, House, Shroom, Ball
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
    info.set_score(0)
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
    Ball.set_position(randint(0, 160), 10)
    Ball.set_velocity(26, 74)
    Ball.set_stay_in_screen(True)
    Ball.set_bounce_on_wall(True)
    while False:
        
        def on_after():
            pass
        timer.after(500, on_after)
        
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite, otherSprite):
    Ball.set_velocity(Ball.vx, Ball.vy * -1)
sprites.on_overlap(SpriteKind.player, SpriteKind.projectile, on_on_overlap)

Ball: Sprite = None
Shroom: Sprite = None
House: Sprite = None
Rock: Sprite = None
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