import pygame


def tup_list_to_dict(tup_list):
    result_dict = {}
    for k, v in tup_list:
        result_dict[k] = v
    return result_dict


def is_under_func(pos, points):
    y_val = points.get(pos[0])
    if y_val is None:
        return True
    if pos[1] < y_val:
        return True
    return False


def draw_circle_alpha(surface, color, center, radius):
    target_rect = pygame.Rect(center, (0, 0)).inflate((radius * 2, radius * 2))
    shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
    pygame.draw.circle(shape_surf, color, (radius, radius), radius)
    surface.blit(shape_surf, target_rect)
