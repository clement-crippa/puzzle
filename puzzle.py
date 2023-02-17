import sys
import pygame
import random
from bouton import Bouton

pygame.init()

# Taille de la fenêtre
taille_fenetre = (800, 700)
fenetre = pygame.display.set_mode(taille_fenetre)
pygame.display.set_caption('Slide Puzzle')
# Bouton partie en 3x3
image_3x3 = pygame.image.load("img/3x3.png")
bouton_jouer_3x3 = Bouton(100, 175, image_3x3, 1)
# Bouton partie en 4x4
image_4x4 = pygame.image.load("img/4x4.png")
bouton_jouer_4x4 = Bouton(310, 175, image_4x4, 1)
# Bouton partie en 5x5
image_5x5 = pygame.image.load("img/5x5.png")
bouton_jouer_5x5 = Bouton(520, 175, image_5x5, 1)
# Bouton scores
image_scores = pygame.image.load("img/scores.png")
bouton_scores = Bouton(310, 375, image_scores, 1)


# Affichage du menu principal
def menu():
    while True:
        fenetre.fill((255, 255, 255))
        # Affichage des boutons
        bouton_jouer_3x3.afficher_bouton(fenetre)
        bouton_jouer_4x4.afficher_bouton(fenetre)
        bouton_jouer_5x5.afficher_bouton(fenetre)
        bouton_scores.afficher_bouton(fenetre)
        for clique in pygame.event.get():
            # Permet de fermer le programme
            if clique.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Lance une partie de puzzle sur un plateau 3x3
            elif bouton_jouer_3x3.clique:
                jouer_3x3()
            # Lance une partie de puzzle sur un plateau 4x4
            elif bouton_jouer_4x4.clique:
                jouer_4x4()
            # Lance une partie de puzzle sur un plateau 5x5
            elif bouton_jouer_5x5.clique:
                jouer_5x5()
            # Affiche le meilleur score
            elif bouton_scores.clique:
                scores()
        # Affiche le menu principal
        pygame.display.update()


def jouer_3x3():
    # Configuration du puzzle
    noir = (0, 0, 0)
    blanc = (255, 255, 255)
    puzzle = [1, 2, 3, 4, 5, 6, 7, 8, None]
    scores = 1000
    # Mélanger automatiquement les pièces
    random.shuffle(puzzle)
    # Taille des pièces de puzzle selon la taille de la fenêtre
    taille_case = (taille_fenetre[0] // 3, taille_fenetre[1] // 3)
    while True:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                case_vide = None
                for i, case in enumerate(puzzle):
                    if case is None:
                        case_vide = i
                        break
                # Mélanger les pièces en appuyant sur R pendant une partie
                if event.key == pygame.K_r:
                    random.shuffle(puzzle)
                    # Reset score
                    scores = 1000
                # Quitter la partie en appuyant sur Escape/Echap
                elif event.key == pygame.K_ESCAPE:
                    menu()
                    break
                # Impossibilité d'aller plus de 2 fois dans la même direction
                if event.key == pygame.K_UP:
                    if case_vide < 6:
                        puzzle[case_vide] = puzzle[case_vide + 3]
                        puzzle[case_vide + 3] = None
                        scores -= 5
                if event.key == pygame.K_DOWN:
                    if case_vide > 2:
                        puzzle[case_vide] = puzzle[case_vide - 3]
                        puzzle[case_vide - 3] = None
                        scores -= 5
                if event.key == pygame.K_LEFT:
                    if case_vide % 3 != 2:
                        puzzle[case_vide] = puzzle[case_vide + 1]
                        puzzle[case_vide + 1] = None
                        scores -= 5
                if event.key == pygame.K_RIGHT:
                    if case_vide % 3 != 0:
                        puzzle[case_vide] = puzzle[case_vide - 1]
                        puzzle[case_vide - 1] = None
                        scores -= 5
        fenetre.fill(noir)
        for i, case in enumerate(puzzle):
            if case is not None:
                nombres = case
                # Taille des bordures
                x = (i % 3) * taille_case[0]
                y = (i // 3) * taille_case[1]
                pygame.draw.rect(fenetre, blanc, (x, y, taille_case[0], taille_case[1]), 1)
                # Taille des nombres dans les cases et positions
                texte_police = pygame.font.Font(None, 100)
                texte = texte_police.render(str(nombres), True, blanc)
                texte_nombres = texte.get_rect(center=(x + taille_case[0] // 2, y + taille_case[1] // 2))
                fenetre.blit(texte, texte_nombres)
                # Si le puzzle est terminé correctement
                if puzzle == [1, 2, 3, 4, 5, 6, 7, 8, None]:
                    fenetre.fill(noir)
                    texte_police = pygame.font.Font(None, 72)
                    texte = texte_police.render("Victoire! Votre score est de: " + str(scores), True, (0, 255, 0))
                    fenetre.blit(texte, (20, 300))
                    with open('scores.txt', 'r') as z:
                        historique_score = int(z.read())
                        # Enregistre le score s'il est plus grand que celui du fichier txt
                        if historique_score < int(scores):
                            with open('scores.txt', 'w') as z:
                                z.write(str(scores))
                    pygame.display.update()
                    pygame.time.wait(5000)
                    menu()
                    break


def jouer_4x4():
    # Configuration du puzzle
    noir = (0, 0, 0)
    blanc = (255, 255, 255)
    puzzle = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None]
    scores = 1000
    # Mélanger automatiquement les pièces
    random.shuffle(puzzle)
    # Taille des pièces de puzzle selon la taille de la fenêtre
    taille_case = (taille_fenetre[0] // 4, taille_fenetre[1] // 4)
    while True:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                case_vide = None
                for i, case in enumerate(puzzle):
                    if case is None:
                        case_vide = i
                        break
                # Mélanger les pièces en appuyant sur R pendant une partie
                if event.key == pygame.K_r:
                    random.shuffle(puzzle)
                    # Reset score
                    scores = 1000
                # Quitter la partie en appuyant sur Escape/Echap
                elif event.key == pygame.K_ESCAPE:
                    menu()
                    break
                # Impossibilité d'aller plus de 3 fois dans la même direction
                if event.key == pygame.K_UP:
                    if case_vide < 12:
                        puzzle[case_vide] = puzzle[case_vide + 4]
                        puzzle[case_vide + 4] = None
                        scores -= 3
                if event.key == pygame.K_DOWN:
                    if case_vide > 3:
                        puzzle[case_vide] = puzzle[case_vide - 4]
                        puzzle[case_vide - 4] = None
                        scores -= 3
                if event.key == pygame.K_LEFT:
                    if case_vide % 4 != 3:
                        puzzle[case_vide] = puzzle[case_vide + 1]
                        puzzle[case_vide + 1] = None
                        scores -= 3
                if event.key == pygame.K_RIGHT:
                    if case_vide % 4 != 0:
                        puzzle[case_vide] = puzzle[case_vide - 1]
                        puzzle[case_vide - 1] = None
                        scores -= 3
        fenetre.fill(noir)
        for i, case in enumerate(puzzle):
            if case is not None:
                nombres = case
                # Taille des bordures
                x = (i % 4) * taille_case[0]
                y = (i // 4) * taille_case[1]
                pygame.draw.rect(fenetre, blanc, (x, y, taille_case[0], taille_case[1]), 1)
                # Taille des nombres dans les cases et positions
                texte_police= pygame.font.Font(None, 100)
                texte = texte_police.render(str(nombres), True, blanc)
                texte_nombres = texte.get_rect(center=(x + taille_case[0] // 2, y + taille_case[1] // 2))
                fenetre.blit(texte, texte_nombres)
                # Si le puzzle est terminé correctement
                if puzzle == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None]:
                    fenetre.fill(noir)
                    texte_police = pygame.font.Font(None, 72)
                    texte = texte_police.render("Victoire! Votre score est de: " + str(scores), True, (0, 255, 0))
                    fenetre.blit(texte, (20, 300))
                    with open('scores.txt', 'r') as z:
                        historique_score = int(z.read())
                        # Enregistre le score s'il est plus grand que celui du fichier txt
                        if historique_score < int(scores):
                            with open('scores.txt', 'w') as z:
                                z.write(str(scores))
                    pygame.display.update()
                    pygame.time.wait(5000)
                    menu()
                    break


def jouer_5x5():
    # Configuration du puzzle
    noir = (0, 0, 0)
    blanc = (255, 255, 255)
    puzzle = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, None]
    scores = 1000
    # Mélanger automatiquement les pièces
    random.shuffle(puzzle)
    # Taille des pièces de puzzle selon la taille de la fenêtre
    taille_case = (taille_fenetre[0] // 5, taille_fenetre[1] // 5)
    while True:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                case_vide = None
                for i, case in enumerate(puzzle):
                    if case is None:
                        case_vide = i
                        break
                # Mélanger les pièces en appuyant sur R pendant une partie
                if event.key == pygame.K_r:
                    random.shuffle(puzzle)
                    # Reset score
                    scores = 1000
                # Quitter la partie en appuyant sur Escape/Echap
                elif event.key == pygame.K_ESCAPE:
                    menu()
                    break
                # Impossibilité d'aller plus de 4 fois dans la même direction
                if event.key == pygame.K_UP:
                    if case_vide < 20:
                        puzzle[case_vide] = puzzle[case_vide + 5]
                        puzzle[case_vide + 5] = None
                        scores -= 1
                if event.key == pygame.K_DOWN:
                    if case_vide > 4:
                        puzzle[case_vide] = puzzle[case_vide - 5]
                        puzzle[case_vide - 5] = None
                        scores -= 1
                if event.key == pygame.K_LEFT:
                    if case_vide % 5 != 4:
                        puzzle[case_vide] = puzzle[case_vide + 1]
                        puzzle[case_vide + 1] = None
                        scores -= 1
                if event.key == pygame.K_RIGHT:
                    if case_vide % 5 != 0:
                        puzzle[case_vide] = puzzle[case_vide - 1]
                        puzzle[case_vide - 1] = None
                        scores -= 1
        fenetre.fill(noir)
        for i, case in enumerate(puzzle):
            if case is not None:
                nombres = case
                # Taille des bordures
                x = (i % 5) * taille_case[0]
                y = (i // 5) * taille_case[1]
                pygame.draw.rect(fenetre, blanc, (x, y, taille_case[0], taille_case[1]), 1)
                # Taille des nombres dans les cases et positions
                texte_police = pygame.font.Font(None, 100)
                texte = texte_police.render(str(nombres), True, blanc)
                texte_nombres = texte.get_rect(center=(x + taille_case[0] // 2, y + taille_case[1] // 2))
                fenetre.blit(texte, texte_nombres)
                # Si le puzzle est terminé correctement
                if puzzle == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, None]:
                    fenetre.fill(noir)
                    texte_police = pygame.font.Font(None, 72)
                    texte = texte_police.render("Victoire! Votre score est de: " + str(scores), True, (0, 255, 0))
                    fenetre.blit(texte, (20, 300))
                    with open('scores.txt', 'r') as z:
                        historique_score = int(z.read())
                        # Enregistre le score s'il est plus grand que celui du fichier txt
                        if historique_score < int(scores):
                            with open('scores.txt', 'w') as z:
                                z.write(str(scores))
                    pygame.display.update()
                    pygame.time.wait(5000)
                    menu()
                    break


def scores():
    while True:
        # Affiche le meilleur score
        meilleur_score = open("scores.txt", "r").read()
        fenetre.fill((255, 255, 255))
        texte_police = pygame.font.Font(None, 70)
        texte = texte_police.render("Meilleur score: " + str(meilleur_score), True, (0, 0, 0))
        fenetre.blit(texte, (150, 10))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Echap/Escape pour quitter et retourner au menu
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    menu()
                    break


menu()
