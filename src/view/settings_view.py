import pygame
from event import EventManager
from view import PygameView


class SettingsView(PygameView):
    def __init__(self, event_manager: EventManager,
                 screen: pygame.Surface) -> None:
        super(SettingsView, self).__init__(event_manager, screen)

    def render(self) -> None:
        self.screen.fill((0, 0, 0))
        somewords = self.smallfont.render(
            'Settings! (press y)', True, (0, 255, 255))
        self.screen.blit(somewords, (350, 250))
        pygame.display.flip()
