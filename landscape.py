import pygame
import math 

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width = 800
screen_height = 600

# Create window
screen = pygame.display.set_mode((screen_width, screen_height))

# Set caption
pygame.display.set_caption("Landscape")

# Set colours
sky_colour = (135, 206, 235) # sky blue
sun_outer_colour = (255,223,34)# Sun yellow 
sun_inner_colour = (255, 255, 0)# yellow 
moon_outer_colour = (192, 192, 192)# silver
moon_inner_colour = (169, 169, 169)# dark grey
moon_spots_colour = (128, 128, 128)# grey
grass_day_colour = (0,154,23) # grass green
grass_night_colour = (3, 75, 3) # deep green
fence_day_colour = (255,255,255) # white
fence_night_colour = (211,211,211) # grey
house_day_colour = (255, 128, 0) # orange
house_night_colour = (204,85,0) # dark orange
door_day_colour = (165,42,42) # brown
door_night_colour = (165,42,42) # brown
doorknob_colour = (255, 215, 0) # golden
cloud_colour = (240, 240, 240) # grey94

# Set variables 
current_time = 6.00 # start at morning
sun_x = 0
sun_y = screen_height // 6
moon_x = screen_width
moon_y = screen_height // 6
house_x = screen_width // 2
house_y = screen_height // 2
cloud_1 = screen_width // 0.1
cloud_2 = screen_width // 10
cloud_3 = screen_width // 3.5
cloud_4 = screen_width // 2
cloud_y = screen_height // 11
cloud_width = 100
cloud_height = 50

# Cloud function - Partialy SiggyWithACiggy from discord (Line 52) and Mr. Gallo
def cloud(cloud_num, cloud_y):
  pygame.draw.circle(screen, cloud_colour, (cloud_num, cloud_y), 30)
  pygame.draw.circle(screen, cloud_colour, (cloud_num + 17, cloud_y - 22), 30)
  pygame.draw.circle(screen, cloud_colour, (cloud_num + 33, cloud_y - 5), 30)

# Load font - Pygame Docs
font = pygame.font.SysFont(None, 48)

# Set clock
clock = pygame.time.Clock()

# Run game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit
            
    # Set sky colour
    if current_time >= 6 and current_time <= 18:
        screen.fill(sky_colour)
    else:
        screen.fill((0, 0, 0)) # black for night sky

    # Draw sun or moon
    if current_time >= 6 and current_time <= 18:
        # Day/Sun
        sun_x = int(((current_time - 6) / 12) * screen_width)
        pygame.draw.circle(screen, sun_outer_colour, (sun_x, sun_y), 50)
        pygame.draw.circle(screen, sun_inner_colour, (sun_x, sun_y), 40)
    else:
        # Night/Moon
        moon_x = int(((current_time - 18) / 6) * screen_width)
        pygame.draw.circle(screen, moon_outer_colour, (moon_x, moon_y), 50)
        pygame.draw.circle(screen, moon_inner_colour, (moon_x, moon_y), 40)
        pygame.draw.circle(screen, moon_spots_colour, (moon_x + 10, moon_y - 13), 10) 
        pygame.draw.circle(screen, moon_spots_colour, (moon_x - 15, moon_y), 10)
        pygame.draw.circle(screen, moon_spots_colour, (moon_x + 10, moon_y + 15), 10)

    # Draw grass
    if current_time >= 6 and current_time <= 18:
      pygame.draw.rect(screen, grass_day_colour, (0, screen_height // 2, screen_width, screen_height // 2))
    else:
      pygame.draw.rect(screen, grass_night_colour, (0, screen_height // 2, screen_width, screen_height // 2))

    # Draw fence 
    if current_time >= 6 and current_time <= 18:
      for i in range(0, screen_width, 40): 
        pygame.draw.rect(screen, fence_day_colour, (i, screen_height // 3 + 40, 20, 60))
        pygame.draw.rect(screen, fence_day_colour, (i, screen_height // 3 + 60 , 40, 20))
    else:
      for i in range(0, screen_width, 40):
        pygame.draw.rect(screen, fence_night_colour, (i, screen_height // 3 + 40, 20, 60))
        pygame.draw.rect(screen, fence_night_colour, (i, screen_height // 3 + 60 , 40, 20))
      
    # Draw house
    if current_time >= 6 and current_time <= 18:
        pygame.draw.rect(screen, house_day_colour, (house_x - 100, house_y - 50, 200, 100))
    else:
         pygame.draw.rect(screen, house_night_colour, (house_x - 100, house_y - 50, 200, 100))
      
    # Draw door
    if current_time >= 6 and current_time <= 18:
        pygame.draw.rect(screen, door_day_colour, (house_x - 20, house_y - 30, 50, 80))
    else:
        pygame.draw.rect(screen, door_night_colour, (house_x - 20, house_y - 30, 50, 80))
    
    #Draw doorknob 
    pygame.draw.circle(screen, doorknob_colour, (house_x - 11, house_y + 10), 5)    
  
    # Draw roof
    if current_time >= 6 and current_time <= 18:
        pygame.draw.polygon(screen, (255, 0, 0), [(house_x - 150, house_y - 50), (house_x + 150, house_y - 50), (house_x, house_y - 150)])
    else:
        pygame.draw.polygon(screen, (139, 0, 0), [(house_x - 150, house_y - 50), (house_x + 150, house_y - 50), (house_x, house_y - 150)])

    # Move cloud
    cloud_1 += 0.5 
    if cloud_1 > screen_width:
        cloud_1 = -cloud_width
      
    cloud_2 += 0.6
    if cloud_2 > screen_width:
        cloud_2 = -cloud_width
    
    cloud_3 += 0.6
    if cloud_3 > screen_width:
        cloud_3 = -cloud_width
    
    cloud_4 += 0.6
    if cloud_4 > screen_width:
        cloud_4 = -cloud_width
      
    # Draw cloud
    cloud(cloud_1, cloud_y)
    cloud(cloud_2, cloud_y)
    cloud(cloud_3, cloud_y)
    cloud(cloud_4, cloud_y)

    # Update time
    current_time += 0.01
    if current_time >= 24.5:
      current_time = 6
      print("The next day")

    # Draw time
    time_text = font.render(str(math.floor(current_time)) + ":00", True, (255, 255, 255))
    screen.blit(time_text, (10, 10))
    
    # Update screen
    pygame.display.update()
    clock.tick(20)

# Quit Pygame
pygame.quit()
exit()

#Pygame docs link for Load font section
#https://www.pygame.org/docs/ref/font.html#:~:text=You%20can%20load%20fonts%20from,look%20up%20the%20system%20fonts.
