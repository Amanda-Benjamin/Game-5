namespace SpriteKind {
    export const Object = SpriteKind.create()
    export const Starting = SpriteKind.create()
    export const Death = SpriteKind.create()
}

scene.onOverlapTile(SpriteKind.Projectile, assets.tile`
        myTile
    `, function on_overlap_tile(sprite22: Sprite, location: tiles.Location) {
    
    tiles.setTileAt(location, assets.tile`
        transparency16
    `)
    Ball.setVelocity(Ball.vx, Ball.vy * SPEEDDDD)
    number_of_bricks = number_of_bricks - 1
    if (number_of_bricks == 0) {
        tiles.setCurrentTilemap(tilemap`
            level36
        `)
        timer.after(500, function on_after() {
            game.gameOver(true)
            sprites.destroyAllSpritesOfKind(SpriteKind.Object)
            sprites.destroyAllSpritesOfKind(SpriteKind.Projectile)
            sprites.destroyAllSpritesOfKind(SpriteKind.Player)
        })
    }
    
    game.setGameOverMessage(true, "GAME OVER! You WIN!! :3")
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function on_a_pressed() {
    
    SPEEDDDD = -1
    info.setLife(1)
    dead = sprites.create(img`
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
        `, SpriteKind.Death)
    scaling.scaleToPercent(dead, 1000, ScaleDirection.Uniformly, ScaleAnchor.Middle)
    dead.setPosition(80, 197)
    sprites.destroyAllSpritesOfKind(SpriteKind.Starting)
    scene.setBackgroundImage(assets.image`
        Game_Stage
    `)
    Rock = sprites.create(assets.image`
        rock
    `, SpriteKind.Object)
    Rock.setStayInScreen(true)
    Rock.setPosition(154, 115)
    House = sprites.create(assets.image`
        teeny_house
    `, SpriteKind.Object)
    scaling.scaleToPercent(House, 60, ScaleDirection.Uniformly, ScaleAnchor.Middle)
    House.setStayInScreen(true)
    House.setPosition(-1, 117)
    Shroom = sprites.create(assets.image`
        SHROOM
    `, SpriteKind.Player)
    Shroom.setStayInScreen(true)
    Shroom.setPosition(76, 106)
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
    Ball.setPosition(randint(45, 98), 37)
    Ball.setVelocity(26, 74)
    Ball.setStayInScreen(true)
    Ball.setBounceOnWall(true)
    tiles.setCurrentTilemap(tilemap`
        Bricks
    `)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Projectile, function on_on_overlap(sprite: Sprite, otherSprite: Sprite) {
    
    SPEEDDDD = SPEEDDDD - 0.005
    Ball.y += -10
    Ball.setVelocity(Ball.vx, Ball.vy * SPEEDDDD)
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Death, function on_on_overlap2(sprite2: Sprite, otherSprite2: Sprite) {
    game.gameOver(false)
    game.setGameOverMessage(false, "LOSER!!! HAHAHA! >:)")
})
let Shroom : Sprite = null
let House : Sprite = null
let Rock : Sprite = null
let dead : Sprite = null
let SPEEDDDD = 0
let Ball : Sprite = null
let number_of_bricks = 0
number_of_bricks = 20
scene.setBackgroundImage(assets.image`
    Splash
`)
game.splash("FOREST MAGIC!")
game.splash("Presented by:", "Amanda & Kylie")
let A = sprites.create(assets.image`
    A_Static
`, SpriteKind.Starting)
scaling.scaleToPercent(A, 80, ScaleDirection.Uniformly, ScaleAnchor.Middle)
A.setPosition(124, 71)
let Press = sprites.create(assets.image`
    Press
`, SpriteKind.Starting)
scaling.scaleToPercent(Press, 300, ScaleDirection.Uniformly, ScaleAnchor.Middle)
Press.setPosition(54, 88)
animation.runImageAnimation(A, assets.animation`
    A_Animated
`, 200, true)
