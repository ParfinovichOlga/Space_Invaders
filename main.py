from turtle import Screen
from player import Player
from invader import Invader
from bunker import Bunker
from scoreboard import Scoreboard
from secret_ship import SecretShip

STARTING_POSITION = (0, -250)
ship_shape = ((2, -4), (-1, -4), (-1, -1), (-3, 0), (-1, 1), (-1, 4), (2, 4))
START_POINTS = [(-220, -200), (-100, -200), (20, -200), (140, -200)]


screen = Screen()
screen.setup(width=800, height=600)


def start_game():
    screen.bgcolor("black")
    screen.title("Space_Invaders")
    screen.register_shape('ship', ship_shape)
    screen.register_shape('invader.gif')
    screen.register_shape('inv.gif')
    screen.register_shape('inv1.gif')
    screen.register_shape('secret.gif')
    screen.listen()
    screen.tracer(0)

    player = Player(STARTING_POSITION, 'ship')
    invaders = Invader(['inv1.gif', 'invader.gif', 'invader.gif', 'inv.gif', 'inv.gif'])
    bunker = Bunker(START_POINTS)
    secret = SecretShip('secret.gif')
    scoreboard = Scoreboard()
    scoreboard.update_score()

    screen.update()
    screen.onkey(player.go_left, 'Left')
    screen.onkey(player.go_right, 'Right')
    screen.onkey(player.fire, 'space')
    screen.onkey(restart, 'Up')

    continue_game = True
    while continue_game:
        screen.update()
        if len(invaders.group) < 1:
            invaders.create_group(['inv1.gif', 'invader.gif', 'invader.gif', 'inv.gif', 'inv.gif'])
            invaders.fire()
        invaders.move()
        secret.move()

    # Check distance between invaders' bullet and bunker, invaders & player
        for bullet in invaders.bullets:
            bullet.attact()
            for brick in bunker.reserve:
                if brick.distance(bullet) < 10:
                    bunker.element_destroyed(brick)
                    bullet.spent(bullet)
            if bullet.distance(player) < 20:
                bullet.spent(bullet)
                scoreboard.killed()
                scoreboard.update_score()
                if scoreboard.turn < 1:
                    scoreboard.end_game()
                    continue_game = False

            if bullet.ycor() < -310:
                invaders.bullets.remove(bullet)
                for active in invaders.bullets:
                    bullet.spent(active)
                invaders.fire()

    # Check distance between player's bullet and bunker
        if player.bullet is not None:
            for brick in bunker.reserve:
                if player.bullet.distance(brick) < 20:
                    bunker.element_destroyed(brick)
                    player.bullet.spent(player.bullet)
                    player.bullet = None
                    break

    # Check distance between player's bullet and invaders
        if player.bullet is not None:
            player.bullet.fire()
            for i in range(len(invaders.group)):
                if player.bullet.distance(invaders.group[i]) < 30:
                    invaders.killed(invaders.group[i])
                    player.bullet.spent(player.bullet)
                    invaders.increase_speed()
                    player.bullet = None
                    scoreboard.point()
                    scoreboard.update_score()
                    break

    # Check distance between player's bullet and secret ship
        if player.bullet is not None:
            if player.bullet.distance(secret) < 30:
                player.bullet.spent(player.bullet)
                secret.killed()
                scoreboard.high_point()
                scoreboard.update_score()

    # Check the invaders reach the bottom of the screen
        if len(invaders.group) > 0:
            for invader in invaders.group:
                if invader.ycor() < -220:
                    scoreboard.end_game()
                    continue_game = False
                    break


def restart():
    screen.clear()
    start_game()


start_game()

screen.mainloop()
