namespace SpriteKind {
    export const Object = SpriteKind.create()
    export const Starting = SpriteKind.create()
}
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    sprites.destroyAllSpritesOfKind(SpriteKind.Starting)
    scene.setBackgroundImage(assets.image`Game_Stage`)
    Rock = sprites.create(assets.image`rock`, SpriteKind.Object)
    Rock.setStayInScreen(true)
    Rock.setPosition(154, 115)
    House = sprites.create(assets.image`teeny_house`, SpriteKind.Object)
    scaling.scaleToPercent(House, 60, ScaleDirection.Uniformly, ScaleAnchor.Middle)
    House.setStayInScreen(true)
    House.setPosition(-1, 117)
    Shroom = sprites.create(assets.image`SHROOM`, SpriteKind.Player)
    Shroom.setStayInScreen(true)
    Shroom.setPosition(76, 106)
    info.setScore(0)
    controller.moveSprite(Shroom, 61, 0)
    Ball = sprites.create(img`
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
        `, SpriteKind.Projectile)
    scaling.scaleToPercent(Ball, 65, ScaleDirection.Uniformly, ScaleAnchor.Middle)
    Ball.setPosition(randint(0, 160), 10)
    Ball.setVelocity(26, 74)
    Ball.setStayInScreen(true)
    Ball.setBounceOnWall(true)
    while (false) {
        tiles.setCurrentTilemap(tilemap`level12`)
        timer.after(500, function () {
        	
        })
    }
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Projectile, function (sprite, otherSprite) {
    Ball.setVelocity(Ball.vx, Ball.vy * -1)
})
let Ball: Sprite = null
let Shroom: Sprite = null
let House: Sprite = null
let Rock: Sprite = null
scene.setBackgroundImage(assets.image`Splash`)
game.splash("FOREST MAGIC!")
game.splash("Presented by:", "Amanda & Kylie")
let A = sprites.create(assets.image`A_Static`, SpriteKind.Starting)
scaling.scaleToPercent(A, 80, ScaleDirection.Uniformly, ScaleAnchor.Middle)
A.setPosition(124, 71)
let Press = sprites.create(assets.image`Press`, SpriteKind.Starting)
scaling.scaleToPercent(Press, 300, ScaleDirection.Uniformly, ScaleAnchor.Middle)
Press.setPosition(54, 88)
animation.runImageAnimation(
A,
assets.animation`A_Animated`,
200,
true
)
