import pygame
import random

# On intialise PyGame
pygame.init()

# On va créer d'abord plusieurs variables qui vont nous servir à créer le jeu

# On définit la taille de la fenêtre du jeu (on met des valeurs fixes pour l'instant)
WINDOW_WIDTH = 800 # en pixels
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) # on crée la fenêtre
pygame.display.set_caption("Space Invaders") # on donne un titre à la fenêtre

# On crée la variable pour afficher le fond de la fenêtre
background = pygame.image.load("/home/antoine/Bureau/Atelier Jeux Vidéos/Pygame/test_space_invaders/background.png")

# On crée la variable pour afficher le vaisseau du joueur
player_image = pygame.image.load("/home/antoine/Bureau/Atelier Jeux Vidéos/Pygame/test_space_invaders/player.gif")
# on place le vaisseau au milieu de la fenêtre
player_x = WINDOW_WIDTH / 2 - player_image.get_width() / 2 # on divise par 2 la taille de l'écran et la largeur du sprite pour centrer le joueur
player_y = WINDOW_HEIGHT - player_image.get_height() - 10
player_speed = 5 # vitesse de déplacement du joueur (en pixels par frame)

# On crée la variable pour afficher les vaisseaux ennemis sur 4 ou 5 lignes
enemy_image = pygame.image.load("/home/antoine/Bureau/Atelier Jeux Vidéos/Pygame/test_space_invaders/enemy_test.gif")
enemy_speed = 2 # vitesse de déplacement des ennemis
enemies = [] # on crée une liste vide pour stocker les ennemis
for i in range(5): # on crée une boucle pour créer les ennemis
    enemy_x = 100 + i * 150 # on place les ennemis à 100 pixels du bord de l'écran et on les espace de 150 pixels (le premier 150 * 0, le deuxième 150 * 1, le troisième 150 * 2, etc.)
    enemy_y = 100 # on place les ennemis à 100 pixels du haut de l'écran
    enemies.append([enemy_x, enemy_y]) # on ajoute les coordonnées des ennemis à la liste enemies

for i in range(5):
    enemy_x = 100 + i * 150
    enemy_y = 150
    enemies.append([enemy_x, enemy_y])

for i in range(5):
    enemy_x = 100 + i * 150
    enemy_y = 200
    enemies.append([enemy_x, enemy_y])

for i in range(5):
    enemy_x = 100 + i * 150
    enemy_y = 250  
    enemies.append([enemy_x, enemy_y])



# On crée la variable pour afficher les tirs du joueur
bullet_image = pygame.image.load("/home/antoine/Bureau/Atelier Jeux Vidéos/Pygame/test_space_invaders/bullet.png")
bullet_speed = 10 # vitesse de déplacement des tirs du joueur
bullets = [] # on crée une liste vide pour stocker les tirs du joueur
bullet_cooldown = 0 # on crée une variable pour gérer le cooldown des tirs du joueur (temps entre chaque tir)

# On crée la variable pour afficher les tirs des ennemis
enemy_bullet_image = pygame.image.load("/home/antoine/Bureau/Atelier Jeux Vidéos/Pygame/test_space_invaders/bullet.png")
enemy_bullet_speed = 5 # vitesse de déplacement des tirs des ennemis
enemy_bullets = [] # on crée une liste vide pour stocker les tirs des ennemis
enemy_bullet_cooldown = 0 # on crée une variable pour gérer le cooldown des tirs des ennemis (temps entre chaque tir)

# On crée la variable pour gérer le temps
clock = pygame.time.Clock()

# On crée la boucle principale du jeu
running = True
while running:
    # Si on reçoit un évènement égal à pygame.QUIT, on arrête la boucle principale
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Conntrôles du joueur
    keys = pygame.key.get_pressed() # on récupère les touches appuyées
    if keys[pygame.K_LEFT] and player_x > 0: # si la touche gauche est appuyée et que le joueur n'est pas au bord de l'écran
        player_x -= player_speed # on déplace le joueur vers la gauche du nombre de pixels definis par player_speed
    if keys[pygame.K_RIGHT] and player_x < WINDOW_WIDTH - player_image.get_width():
        player_x += player_speed

    # On bouge les ennemis de gauche à droite et on les fait descendre quand ils touchent le bord de l'écran en inversant le sens de déplacement
    for enemy in enemies: # on parcourt la liste des ennemis
        enemy[0] += enemy_speed # on déplace l'ennemi de enemy_speed pixels vers la droite
        if enemy[0] > WINDOW_WIDTH - enemy_image.get_width() or enemy[0] < 0: # si l'ennemi touche le bord de l'écran (enemy[0] correspond à la position en x de l'ennemi)
            enemy_speed *= -1 # on inverse le sens de déplacement
            for enemy in enemies: # on parcourt la liste des ennemis
                enemy[1] += 10 # on fait descendre les ennemis de 10 pixels (enemy[1] correspond à la position en y de l'ennemi)

    # Le joueur tire
    if keys[pygame.K_SPACE] and bullet_cooldown == 0: # si la touche espace est appuyée et que le cooldown est à 0
        bullet_x = player_x + player_image.get_width() / 2 - bullet_image.get_width() / 2 # on place le tir du joueur au milieu du vaisseau
        bullet_y = player_y - bullet_image.get_height() # on place le tir du joueur au dessus du vaisseau
        bullets.append([bullet_x, bullet_y]) # on ajoute les coordonnées du tir à la liste bullets
        bullet_cooldown = 10 # on met le cooldown à 10

    # Les ennemis tirent
    if enemy_bullet_cooldown == 0: # si le cooldown est à 0
        enemy = random.choice(enemies) # on choisit un ennemi au hasard (on importe la bibliothèque random)
        enemy_bullet_x = enemy[0] + enemy_image.get_width() / 2 - enemy_bullet_image.get_width() / 2 # on place le tir de l'ennemi au milieu du vaisseau
        enemy_bullet_y = enemy[1] + enemy_image.get_height() # on place le tir de l'ennemi en dessous du vaisseau
        enemy_bullets.append([enemy_bullet_x, enemy_bullet_y]) # on ajoute les coordonnées du tir à la liste enemy_bullets
        enemy_bullet_cooldown = 30 # on met le cooldown à 30

    # On fait 'bouger' les tirs du joueur
    for bullet in bullets: # on parcourt la liste des tirs du joueur
        bullet[1] -= bullet_speed # on déplace le tir du joueur de bullet_speed pixels vers le haut (bullet[1] correspond à la position en y du tir)

    # On fait 'bouger' les tirs des ennemis
    for enemy_bullet in enemy_bullets: # on parcourt la liste des tirs des ennemis
        enemy_bullet[1] += enemy_bullet_speed # on déplace le tir de l'ennemi de enemy_bullet_speed pixels vers le bas (enemy_bullet[1] correspond à la position en y du tir)

    # On vérifie si les tirs du joueur ont touché un ennemi
    for bullet in bullets: # on parcourt la liste des tirs du joueur
        for enemy in enemies: # on parcourt la liste des ennemis
            if bullet[1] < enemy[1] + enemy_image.get_height() and \
               bullet[1] + bullet_image.get_height() > enemy[1] and \
               bullet[0] < enemy[0] + enemy_image.get_width() and \
               bullet[0] + bullet_image.get_width() > enemy[0]: # si le tir du joueur touche un ennemi (on vérifie si les rectangles des sprites se touchent)
                bullets.remove(bullet) # on supprime le tir du joueur
                enemies.remove(enemy) # on supprime l'ennemi

    # On vérifie si les tirs des ennemis ont touché le joueur
    for enemy_bullet in enemy_bullets:
        if enemy_bullet[1] < player_y + player_image.get_height() and \
           enemy_bullet[1] + enemy_bullet_image.get_height() > player_y and \
           enemy_bullet[0] < player_x + player_image.get_width() and \
           enemy_bullet[0] + enemy_bullet_image.get_width() > player_x: # si le tir de l'ennemi touche le joueur
            enemy_bullets.remove(enemy_bullet) # on supprime le tir de l'ennemi
            running = False # on arrête la boucle principale (le jeu s'arrête)
   

    # On affiche l'image de background grâce à la fonction blit qui permet d'afficher une image à l'écran
    window.blit(background, (0, 0)) # on place l'image de background en haut à gauche de la fenêtre (x = 0, y = 0 correspondant au coin supérieur gauche de la fenêtre)

    # On affiche l'image du joueur
    window.blit(player_image, (player_x, player_y)) # on place le joueur aux coordonnées player_x et player_y en positionnant son image à cet endroit

    # On affiche les ennemis
    for enemy in enemies:
        window.blit(enemy_image, (enemy[0], enemy[1]))

    #   On affiche les tirs du joueur
    for bullet in bullets:
        window.blit(bullet_image, (bullet[0], bullet[1]))

    # On affiche les tirs des ennemis
    for enemy_bullet in enemy_bullets:
        window.blit(enemy_bullet_image, (enemy_bullet[0], enemy_bullet[1]))

    # On met à jour l'affichage (à chaque frame, on efface l'écran et on réaffiche les images)
    pygame.display.update()

    # O définit le nombre de frames par seconde
    clock.tick(60) # on veut que le jeu tourne à 60 FPS (au maximum on aura 60 frames par seconde)

    # On met à jour le cooldown des tirs
    if bullet_cooldown > 0:
        bullet_cooldown -= 1
    if enemy_bullet_cooldown > 0:
        enemy_bullet_cooldown -= 1

# On quitte PyGame (quand on sort de la boucle principale)
pygame.quit()
