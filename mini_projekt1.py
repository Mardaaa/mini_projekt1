import pygame
import math
from datetime import datetime

pygame.init()
x_center = 600
y_center = 600
screen = pygame.display.set_mode((x_center, y_center)) # Set resolution for image

center = (300, 300) # Set the coordinates for the center of the clock
minut_viser = 180 # Length of minute hand
time_viser = 130 # Length of hour hand
sekund_viser = 180 # Length of second hand

font = pygame.font.SysFont(None,46) # Text font

pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((255,255,200))

    # Draw outline of the clock
    pygame.draw.circle(screen, (0,0,0), center, 210, width=4)

    # Draw the insides of the clock (white circle)
    pygame.draw.circle(screen, (255,255,255), center, 206)

    length = 200

    #Add black dots and 12 black lines
    for angle in range(0,360,30): # 360 / 12 = 30 degrees pr. dot
        end_x = center[0] + length * math.cos(math.radians(angle))
        end_y = center[1] + length * math.sin(math.radians(angle))
        end_point = (end_x, end_y)
        pygame.draw.line(screen, (0,0,0), center, end_point, 4) # Add 12 black lines (optional remove)
        pygame.draw.circle(screen, (0,0,0), (end_x, end_y), 6) # 12 larger circles (optional)

    #Add 60 smaller black dots
    for angle in range(0,360,6): # 360 / 60 = 6 dots pr degree
        end_x = center[0] + length * math.cos(math.radians(angle))
        end_y = center[1] + length * math.sin(math.radians(angle))
        end_point = (end_x, end_y)
        pygame.draw.circle(screen, (0,0,0), (end_x, end_y), 2)

    # Add white circle with a smaller radius to hide part of the long black lines
    pygame.draw.circle(screen,(255,255,255), center, 180) 
    
    # Add hours/numbers on clock
    text_length = 160 # Distance from center
    for i in range(1,13):
        text = font.render(str(i), True, (0,220,0))
        
        #Calculate text position
        text_x = center[0] + text_length * math.cos(math.radians(i*30-90)) - (
            text.get_width() // 2) #i * 30 because they need to be 30 degrees spread apart
        text_y = center[1] + text_length * math.sin(math.radians(i*30-90)) - (
            text.get_width() // 2)
        text_pos = (text_x, text_y)
        screen.blit(text,text_pos)


    second = datetime.now().second
    minute = datetime.now().minute
    hour = datetime.now().hour%12 # 12 hours instead of 24 hours

    # Second hand angle:
    sekund_vinkel = second * 6 # 360 / 60 = 6 degrees pr sek
    # Calculate end_pos
    end_x = center[0] + sekund_viser * math.cos(math.radians
                                                     (sekund_vinkel-90))
    end_y = center[1] + sekund_viser * math.sin(math.radians
                                                     (sekund_vinkel-90))
    end_pos = (end_x, end_y)
    # Draw second hand
    pygame.draw.line(screen,(255,0,0), center, end_pos, 2)

    
    # Minute hand angle:
    minut_vinkel = minute * 6 # 6 degrees pr min. (since 360 / 60 = 6)
    # Calculate end_pos
    end_x = center[0] + minut_viser * math.cos(math.radians
                                                    (minut_vinkel-90))
    end_y = center[1] + minut_viser * math.sin(math.radians
                                                    (minut_vinkel-90))
    end_pos = (end_x, end_y)
    # Draw minute hand
    pygame.draw.line(screen, (0,0,0), center, end_pos, 2)


    # Hour hand angle:
    time_vinkel = (hour + minute/60) * 30 # (Hour + minute/60) * 30 degrees so it doesn't 'jump' 30 degrees but instead goes smoothly
    # Calculate end_pos
    end_x = center[0] + time_viser * math.cos(math.radians
                                                    (time_vinkel-90))
    end_y = center[1] + time_viser * math.sin(math.radians
                                                    (time_vinkel-90))
    end_pos = (end_x, end_y)
    # Draw hour hand
    pygame.draw.line(screen, (0,0,0), center, end_pos, 5)


    # Update the display
    pygame.display.flip()
