import pygame

#pygame setup
map_size = 800
pygame.init()
screen = pygame.display.set_mode((map_size, map_size))
clock = pygame.time.Clock()
speed = 15


#this will be the map for which cells are either dead or alive
cells = [[False]*(map_size//10) for _ in range(map_size//10)]
run = True
started = False


def is_valid_pos(i, j, n, m):
    if i < 0 or j < 0 or i >= n or j >= m:
        return 0
    return 1

# Function that returns all adjacent elements
def get_adjacent_living(arr, i, j):

    n = len(arr)
    m = len(arr[0])
    ans = []
    if is_valid_pos(i - 1, j - 1, n, m):
        ans.append(arr[i - 1][j - 1])
    if is_valid_pos(i - 1, j, n, m):
        ans.append(arr[i - 1][j])
    if is_valid_pos(i - 1, j + 1, n, m):
        ans.append(arr[i - 1][j + 1])
    if is_valid_pos(i, j - 1, n, m):
        ans.append(arr[i][j - 1])
    if is_valid_pos(i, j + 1, n, m):
        ans.append(arr[i][j + 1])
    if is_valid_pos(i + 1, j - 1, n, m):
        ans.append(arr[i + 1][j - 1])
    if is_valid_pos(i + 1, j, n, m):
        ans.append(arr[i + 1][j])
    if is_valid_pos(i + 1, j + 1, n, m):
        ans.append(arr[i + 1][j + 1])

    return ans.count(True)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            #allows the player to turn cells on or off by clicking
            mouse_position = pygame.mouse.get_pos()
            cells[mouse_position[0]//10][mouse_position[1]//10] = not cells[mouse_position[0]//10][mouse_position[1]//10]
        if event.type == pygame.KEYDOWN:
            started = not started
    #wipe away anything from last frame
    screen.fill("black")

    #determines which cells live and which cells die
    if started:
        switch_list = []
        for i in range(len(cells)):
            for j in range(len(cells[i])):
                living_neighbours = get_adjacent_living(cells, i, j)
                if cells[i][j]:
                    if living_neighbours<2 or living_neighbours>3:
                        switch_list.append((i, j))
                else:
                    if living_neighbours == 3:
                        switch_list.append((i, j))
    
        #kills living cells and brings dead cells to life that need to be
        for i in switch_list:
            cells[i[0]][i[1]] = not cells[i[0]][i[1]]


    #render the cells onto the screen
    for i in range(len(cells)):
        for j in range(len(cells[i])):
            if cells[i][j]:
                pygame.draw.rect(screen, "white", (i*10, j*10, 10, 10))
    
    #puts things on the screen
    pygame.display.flip()
    clock.tick(speed)