# pi-pins
An ASCII art diagram drawing aid for raspberry pi projects

A dufus script that draws a few diagrams that look liek the header of a Raspberry Pi, but in different orientations.
You can use this code to draw diagrams for microcontrollers or any dual-inline chip also if desired.


## Upright

                          .___.
                  +3V3--1-|O O|-2--+5V   
          (SDA) GPIO2---3-|O O|-4--+5V   
         (SCL1) GPIO3---5-|O O|-6--GND   
         (GLCK) GPIO4---7-|O O|-8--GPIO14 (TXD0)
                   GND--9-|O O|-10-GPIO15 (RXD0)
    (GPIO_GEN0) GPIO17-11-|O O|-12-GPIO18 (GPIO_GEN1)
    (GPIO_GEN2) GPIO27-13-|O O|-14-GND   
    (GPIO_GEN3) GPIO22-15-|O O|-16-GPIO23 (GPIO_GEN4)
                  +3V3-17-|O O|-18-GPIO24 (GPIO_GEN5)
     (SPI_MOSI) GPIO10-19-|O O|-20-GND   
     (SPI_MISO) GPIO9--21-|O O|-22-GPIO25 (GPIO_GEN6)
     (SPI_SCLK) GPIO11-23-|O O|-24-GPIO8  (SPI_C0_N)
                   GND-25-|O O|-26-GPIO7  (SPI_C1_N)
       (EEPROM) ID_SD--27-|O O|-28-ID_SC  (Reserved)
                GPIO5--29-|O O|-30-GND   
                GPIO6--31-|O O|-32-GPIO12
                GPIO13-33-|O O|-34-GND   
                GPIO19-35-|O O|-36-GPIO16
                GPIO26-37-|O O|-38-GPIO20
                   GND-39-|O O|-40-GPIO21
                          '---'
## Downwards
                          .___.
                GPIO21-40-|O O|-39-GND   
                GPIO20-38-|O O|-37-GPIO26
                GPIO16-36-|O O|-35-GPIO19
                   GND-34-|O O|-33-GPIO13
                GPIO12-32-|O O|-31-GPIO6 
                   GND-30-|O O|-29-GPIO5 
     (Reserved) ID_SC--28-|O O|-27-ID_SD  (EEPROM)
     (SPI_C1_N) GPIO7--26-|O O|-25-GND   
     (SPI_C0_N) GPIO8--24-|O O|-23-GPIO11 (SPI_SCLK)
    (GPIO_GEN6) GPIO25-22-|O O|-21-GPIO9  (SPI_MISO)
                   GND-20-|O O|-19-GPIO10 (SPI_MOSI)
    (GPIO_GEN5) GPIO24-18-|O O|-17-+3V3  
    (GPIO_GEN4) GPIO23-16-|O O|-15-GPIO22 (GPIO_GEN3)
                   GND-14-|O O|-13-GPIO27 (GPIO_GEN2)
    (GPIO_GEN1) GPIO18-12-|O O|-11-GPIO17 (GPIO_GEN0)
         (RXD0) GPIO15-10-|O O|-9--GND   
         (TXD0) GPIO14--8-|O O|-7--GPIO4  (GLCK)
                   GND--6-|O O|-5--GPIO3  (SCL1)
                   +5V--4-|O O|-3--GPIO2  (SDA)
                   +5V--2-|O O|-1--+3V3  
                          '---'
## Horizontal

               (   ( (   (                  
               G   G G   G ( ( (            
               P   P P   P S S R            
               I   I I   I P P e            
               O   O O   O I I s            
           ( ( '   ' '   ' ' ' e            
           T R G   G G   G C C r            
           X X E   E E   E 0 1 v            
           D D N   N N   N ' ' e            
           0 0 1   4 5   6 N N d            
           ) ) )   ) )   ) ) ) )            
    
           G G G   G G   G G G I   G   G G G
           P P P   P P   P P P D   P   P P P
           I I I   I I   I I I '   I   I I I
     + + G O O O G O O G O O O S G O G O O O
     5 5 N 1 1 1 N 2 2 N 2 8 7 C N 1 N 1 2 2
     V V D 4 5 8 D 3 4 D 5 | | | D 2 D 6 0 1
     | | | | | | | | | | | | | | | | | | | |
     | | | | 1 1 1 1 1 2 2 2 2 2 3 3 3 3 3 4
     2 4 6 8 0 2 4 6 8 0 2 4 6 8 0 2 4 6 8 0
     M M M M M M M M M M M M M M M M M M M M
    +---------------------------------------+
    |O O O O O O O O O O O O O O O O O O O O|
    |                                       |
    |O O O O O O O O O O O O O O O O O O O O|
    +---------------------------------------+
     M M M M M M M M M M M M M M M M M M M M
     1 3 5 7 9 1 1 1 1 1 2 2 2 2 2 3 3 3 3 3
     | | | | | 1 3 5 7 9 1 3 5 7 9 1 3 5 7 9
     | | | | | | | | | | | | | | | | | | | |
     + G G G G G G G + G G G G I G G G G G G
     3 P P P N P P P 3 P P P N D P P P P P N
     V I I I D I I I V I I I D ' I I I I I D
     3 O O O   O O O 3 O O O   S O O O O O  
       2 3 4   1 2 2   1 9 1   D 5 6 1 1 2  
               7 7 2   0   1         3 9 6  
    
       ( ( (   ( ( (   ( ( (   (
       S S G   G G G   S S S   E
       D C L   P P P   P P P   E
       A L C   I I I   I I I   P
       ) 1 K   O O O   ' ' '   R
         ) )   ' ' '   M M S   O
               G G G   O I C   M
               E E E   S S L   )
               N N N   I O K
               0 2 3   ) ) )
               ) ) )

## Horizontal flip
                             ( ( (          
                     ( ( (   G G G          
                     S S S   P P P          
                 (   P P P   I I I          
                 E   I I I   O O O          
                 E   ' ' '   ' ' '   ( (    
                 P   S M M   G G G   G S (  
                 R   C I O   E E E   L C S  
                 O   L S S   N N N   C L D  
                 M   K O I   3 2 0   K 1 A  
                 )   ) ) )   ) ) )   ) ) )  
    
       G G G G G I   G G G   G G G   G G G  
       P P P P P D   P P P   P P P   P P P  
       I I I I I '   I I I + I I I   I I I +
     G O O O O O S G O O O 3 O O O G O O O 3
     N 2 1 1 6 5 D N 1 9 1 V 2 2 1 N 4 3 2 V
     D 6 9 3 | | | D 1 | 0 3 2 7 7 D | | | 3
     | | | | | | | | | | | | | | | | | | | |
     3 3 3 3 3 2 2 2 2 2 1 1 1 1 1 | | | | |
     9 7 5 3 1 9 7 5 3 1 9 7 5 3 1 9 7 5 3 1
     M M M M M M M M M M M M M M M M M M M M
    +----------------------------------------+
    |O O O O O O O O O O O O O O O O O O O O |
    |                                        |
    |O O O O O O O O O O O O O O O O O O O O |
    +----------------------------------------+
     M M M M M M M M M M M M M M M M M M M M
     4 3 3 3 3 3 2 2 2 2 2 1 1 1 1 1 8 6 4 2
     0 8 6 4 2 0 8 6 4 2 0 8 6 4 2 0 | | | |
     | | | | | | | | | | | | | | | | | | | |
     G G G G G G I G G G G G G G G G G G + +
     P P P N P N D P P P N P P N P P P N 5 5
     I I I D I D ' I I I D I I D I I I D V V
     O O O   O   S O O O   O O   O O O      
     2 2 1   1   C 7 8 2   2 2   1 1 1      
     1 0 6   2         5   4 3   8 5 4      
    
                 ( ( ( (   ( (   ( ( (
                 R S S G   G G   G R T
                 e P P P   P P   P X X
                 s I I I   I I   I D D
                 e ' ' O   O O   O 0 0
                 r C C '   ' '   ' ) )
                 v 1 0 G   G G   G
                 e ' ' E   E E   E
                 d N N N   N N   N
                 ) ) ) 6   5 4   1
                       )   ) )   )


You get the idea. It also supports drawing a notch in the header/chip near pin 1. Needs some work, but does this job well enough already. And in terms of priority, this can be finished after the main project im busy with is done.
    
