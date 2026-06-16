import pygame
import random

pygame.init()

# ==========================
# WINDOW
# ==========================

WIDTH = 1000
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The Hardest Logic Puzzle Ever")

font = pygame.font.SysFont(None, 40)
title_font = pygame.font.SysFont(None, 55)

# ==========================
# IMAGES
# ==========================

unknown_img = pygame.image.load("assets/unknown.png")
azelf_img = pygame.image.load("assets/azelf.png")
mesprit_img = pygame.image.load("assets/mesprit.png")
uxie_img = pygame.image.load("assets/uxie.png")

unknown_img = pygame.transform.scale(unknown_img, (180, 180))
azelf_img = pygame.transform.scale(azelf_img, (180, 180))
mesprit_img = pygame.transform.scale(mesprit_img, (180, 180))
uxie_img = pygame.transform.scale(uxie_img, (180, 180))

# ==========================
# HELPERS
# ==========================

def get_sprite(name):

    if name == "Azelf":
        return azelf_img

    if name == "Mesprit":
        return mesprit_img

    return uxie_img

# ==========================
# RANDOM WORLD
# ==========================

gods = ["Azelf", "Mesprit", "Uxie"]
random.shuffle(gods)

positions = {
    "A": gods[0],
    "B": gods[1],
    "C": gods[2]
}

ja_means_yes = random.choice([True, False])

revealed = {
    "A": False,
    "B": False,
    "C": False
}

# ==========================
# GAME STATE
# ==========================

questions_used = 0
last_answer = "None"
game_won = False

question_options = [
    ("Is A Azelf?", lambda: positions["A"] == "Azelf"),
    ("Is A Mesprit?", lambda: positions["A"] == "Mesprit"),
    ("Is A Uxie?", lambda: positions["A"] == "Uxie"),

    ("Is B Azelf?", lambda: positions["B"] == "Azelf"),
    ("Is B Mesprit?", lambda: positions["B"] == "Mesprit"),
    ("Is B Uxie?", lambda: positions["B"] == "Uxie"),

    ("Is C Azelf?", lambda: positions["C"] == "Azelf"),
    ("Is C Mesprit?", lambda: positions["C"] == "Mesprit"),
    ("Is C Uxie?", lambda: positions["C"] == "Uxie"),
]

selected_question = 0

# ==========================
# BUTTONS
# ==========================

askA = pygame.Rect(100, 540, 150, 60)
askB = pygame.Rect(425, 540, 150, 60)
askC = pygame.Rect(750, 540, 150, 60)

revealA = pygame.Rect(100, 610, 150, 50)
revealB = pygame.Rect(425, 610, 150, 50)
revealC = pygame.Rect(750, 610, 150, 50)

# ==========================
# ANSWERING SYSTEM
# ==========================

def answer(god):

    statement = question_options[selected_question][1]()

    identity = positions[god]

    if identity == "Azelf":
        truth_value = statement

    elif identity == "Mesprit":
        truth_value = not statement

    else:
        truth_value = random.choice([True, False])

    if ja_means_yes:
        return "Ja" if truth_value else "Ka"

    return "Ka" if truth_value else "Ja"

# ==========================
# MAIN LOOP
# ==========================

running = True

while running:

    screen.fill((25, 25, 40))

    # ======================
    # TITLE
    # ======================

    title = title_font.render(
        "The Hardest Logic Puzzle Ever",
        True,
        (255, 255, 255)
    )

    screen.blit(title, (180, 40))

    # ======================
    # GODS
    # ======================

    x_positions = [100, 400, 700]

    for i, label in enumerate(["A", "B", "C"]):

        if revealed[label]:
            sprite = get_sprite(positions[label])
        else:
            sprite = unknown_img

        screen.blit(
            sprite,
            (x_positions[i], 180)
        )

        label_text = font.render(
            label,
            True,
            (255, 255, 0)
        )

        screen.blit(
            label_text,
            (x_positions[i] + 80, 145)
        )

        if revealed[label]:
            text = positions[label]
        else:
            text = "????"

        txt = font.render(
            text,
            True,
            (255, 255, 255)
        )

        screen.blit(
            txt,
            (x_positions[i] + 20, 380)
        )

    # ======================
    # BUTTONS
    # ======================

    pygame.draw.rect(screen, (70, 130, 220), askA)
    pygame.draw.rect(screen, (70, 130, 220), askB)
    pygame.draw.rect(screen, (70, 130, 220), askC)

    screen.blit(
        font.render("Ask A", True, (255,255,255)),
        (130, 555)
    )

    screen.blit(
        font.render("Ask B", True, (255,255,255)),
        (455, 555)
    )

    screen.blit(
        font.render("Ask C", True, (255,255,255)),
        (780, 555)
    )
    pygame.draw.rect(screen, (180, 100, 80), revealA)
    pygame.draw.rect(screen, (180, 100, 80), revealB)
    pygame.draw.rect(screen, (180, 100, 80), revealC)

    screen.blit(
    font.render("Reveal A", True, (255,255,255)),
    (115,620)
    )

    screen.blit(
    font.render("Reveal B", True, (255,255,255)),
    (440,620)
    )

    screen.blit(
    font.render("Reveal C", True, (255,255,255)),
    (765,620)
    )

    # ======================
    # INFO
    # ======================
    current_question = font.render(
        question_options[selected_question][0],
        True,
        (255,255,255)
    )

    screen.blit(current_question, (330, 480))

    help_text = font.render(
        
        "<-  -> Change Question",
        True, 
        (200, 200, 200)
    )
    screen.blit(help_text, (300, 520))
    

    answer_text = font.render(
        f"Last Answer: {last_answer}",
        True,
        (255,255,255)
    )

    screen.blit(answer_text, (40, 640))

    question_text = font.render(
        f"Questions Used: {questions_used}",
        True,
        (255,255,255)
    )

    screen.blit(question_text, (600, 640))

    if all(revealed.values()):
        game_won = True

    if game_won:

        overlay = pygame.Surface((WIDTH, HEIGHT))
        overlay.set_alpha(220)
        overlay.fill((0, 0, 0))

        screen.blit(overlay, (0, 0))

        win_text = title_font.render(
            "PUZZLE SOLVED!",
            True,
            (0, 255, 0)
        )

        screen.blit(win_text, (300, 180))

        result = font.render(
            f"A={positions['A']}  B={positions['B']}  C={positions['C']}",
            True,
            (255,255,255)
        )

        screen.blit(result, (180, 280))

        score = max(0, 1000 - questions_used * 100)

        score_text = font.render(
        f"Score: {score}",
        True,
        (255,255,0)
        )

        screen.blit(score_text, (420, 350))

        q_text = font.render(
            f"Questions Used: {questions_used}",
            True,
            (255,255,255)
        )

        screen.blit(q_text, (350, 400))

    pygame.display.flip()

    # ======================
    # EVENTS
    # ======================

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                selected_question -= 1

                if selected_question < 0:
                    selected_question = len(question_options) - 1
            if event.key == pygame.K_RIGHT:
                selected_question += 1

                if selected_question >= len(question_options):
                    selected_question = 0



            

        if event.type == pygame.MOUSEBUTTONDOWN:
            if revealA.collidepoint(event.pos):
                revealed["A"] = True

            if revealB.collidepoint(event.pos):
                revealed["B"] = True

            if revealC.collidepoint(event.pos):
                revealed["C"] = True

            if askA.collidepoint(event.pos):
                last_answer = answer("A")
                questions_used += 1

            if askB.collidepoint(event.pos):
                last_answer = answer("B")
                questions_used += 1

            if askC.collidepoint(event.pos):
                last_answer = answer("C")
                questions_used += 1

pygame.quit()