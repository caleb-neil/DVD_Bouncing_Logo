import sys, pygame, random
pygame.init()

size = width, height = 800, 450
speed = [1.0, 1.0]
black = 0, 0, 0

coordinates = x, y = 0, 0
top = 1

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
dt = 0
dvd_list = ['blue_dvd.png','green_dvd.png','indigo_dvd.png','orange_dvd.png','red_dvd.png','violet_dvd.png','yellow_dvd.png']

dvd = pygame.image.load(f"images/{random.choice(dvd_list)}")
dvdrect = dvd.get_rect()
counter = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    dvdrect = dvdrect.move(speed)

    if dvdrect.left < 0 or dvdrect.right > width:
        speed[0] = -speed[0]
        dvd = pygame.image.load(f"images/{random.choice(dvd_list)}")

    if dvdrect.top < 0 or dvdrect.bottom > height:
        speed[1] = -speed[1]
        dvd = pygame.image.load(f"images/{random.choice(dvd_list)}")

    if (dvdrect.top < 0 or dvdrect.bottom > height) and (dvdrect.left < 0 or dvdrect.right > width):
        counter += 1

    pygame.display.set_caption(f"Counter: {counter}, X: {x} Y: {y} Speed_X: {speed[0]} Speed_Y: {speed[1]} DVDRect: {dvdrect}")

    screen.fill(black)
    screen.blit(dvd, dvdrect)
    pygame.display.flip()

    dt = clock.tick(120) / 1000