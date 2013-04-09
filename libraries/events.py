import pygame

# Master events
MORONIAN_CUSTOM_EVENT = pygame.USEREVENT + 0

# New events
EVENT_CHANGE_LEVEL = 0

#### old style event ####
# Master events
EVENT_GAME_OVER = pygame.USEREVENT + 2
EVENT_JUMP_TO_TITLE = pygame.USEREVENT + 3

# Story line events
EVENT_STORY_SCRIPT_CAPTION = pygame.USEREVENT + 0
EVENT_STORY_SCRIPT_TYPE = pygame.USEREVENT + 4
EVENT_STORY_SCRIPT_DELAY_BEFORE_SHIP = pygame.USEREVENT + 5
EVENT_STORY_SCRIPT_DELAY_FOR_LAUGH = pygame.USEREVENT + 6
EVENT_STORY_SCRIPT_POST_LAUGH_DELAY = pygame.USEREVENT + 7
