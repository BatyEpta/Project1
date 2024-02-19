import pygame, sys, threading

pygame.init()
screen = pygame.display.set_mode((1000, 300))
pygame.display.set_caption("Loading")

clock1 = pygame.time.Clock()

w = 10000000

l_bg = pygame.image.load("lbg1.png")
l_bg_rect = l_bg.get_rect(center=(500, 150))

l_bar = pygame.image.load("lb1.png")
l_bar_rect = l_bg.get_rect(midleft=(142, 150))
is_fin = False
l_pr = 0
l_wth = 8


def doWork():
    global is_fin, l_pr
    for i in range(w):
        math_eq = 523687 / 789456 * 89456
        l_pr = i
    is_fin = True

threading.Thread(target=doWork).start()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((25, 25, 50))

    l_wth = l_pr / w * 720
    l_bar = pygame.transform.scale(l_bar, (int(l_wth), 150))
    l_bar_rect = l_bar.get_rect(midleft=(142, 150))

    screen.blit(l_bg, l_bg_rect)
    screen.blit(l_bar, l_bar_rect)

    pygame.display.update()
    clock1.tick(60)