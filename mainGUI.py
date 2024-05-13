import pygame
import json

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Login System")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Fonts
font = pygame.font.Font(None, 32)

# Load JSON data
def load_data():
    with open('usernames.json', 'r') as usernames_file:
        username_data = json.load(usernames_file)
    with open('passwords.json', 'r') as passwords_file:
        password_data = json.load(passwords_file)
    return username_data, password_data

# Register new user
def register(username, password):
    username_data, password_data = load_data()
    username_data['id'].append(username)
    password_data['password'].append(password)
    with open('usernames.json', 'w') as usernames_file:
        json.dump(username_data, usernames_file)
    with open('passwords.json', 'w') as passwords_file:
        json.dump(password_data, passwords_file)
    print("User {} registered successfully.".format(username))

# Login user
def login(username, password):
    username_data, password_data = load_data()
    if username in username_data['id']:
        index = username_data['id'].index(username)
        if password == password_data['password'][index]:
            print("Welcome, {}!".format(username))
            return True
    print("Incorrect username or password.")
    return False

# Text input field
class TextInput:
    def __init__(self, rect, text=''):
        self.rect = pygame.Rect(rect)
        self.text = text
        self.color = GRAY
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False
            self.color = GREEN if self.active else GRAY
        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_RETURN:
                self.active = False
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode

    def draw(self, surface):
        text_surface = font.render(self.text, True, BLACK)
        width = max(200, text_surface.get_width() + 10)
        self.rect.w = width
        pygame.draw.rect(surface, self.color, self.rect, 0)
        surface.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))

# Button
class Button:
    def __init__(self, rect, text, color, action):
        self.rect = pygame.Rect(rect)
        self.text = text
        self.color = color
        self.action = action

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.action()

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, 0)
        text_surface = font.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

# Initialize text input fields and buttons
username_input = TextInput((100, 50, 200, 40))
password_input = TextInput((100, 120, 200, 40))
login_button = Button((100, 200, 90, 40), "Login", GRAY, lambda: login(username_input.text, password_input.text))
register_button = Button((210, 200, 90, 40), "Register", GRAY, lambda: register(username_input.text, password_input.text))
inputs = [username_input, password_input]
buttons = [login_button, register_button]

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        for input in inputs:
            input.handle_event(event)
        for button in buttons:
            button.handle_event(event)

    for input in inputs:
        input.draw(screen)
    for button in buttons:
        button.draw(screen)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
