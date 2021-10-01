import time
 
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
 
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
 
import subprocess
 
RST = None
 
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)
 
# Initialize library.
disp.begin()
 
# Clear display.
disp.clear()
disp.display()
 
while True:
    x = 0
    y = -2
    # Create blank image for drawing.
    # Make sure to create image with mode '1' for 1-bit color.
    width = disp.width
    height = disp.height
    image = Image.new('1', (width, height))
    # Get drawing object to draw on image.
    draw = ImageDraw.Draw(image)
    # Draw a black filled box to clear the image.
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    
    font = ImageFont.truetype('123.ttf', 13)
    
    for Test in range(1,50):
        # Draw a black filled box to clear the image.
        draw.rectangle((0,0,width,height), outline=0, fill=0)
 
        # Shell scripts for system monitoring from here : https://unix.stackexchange.com/questions/119126/command-to-display-memory-usage-disk-usage-and-cpu-load
        cmd = "hostname -I | cut -d\' \' -f1"
        IP = subprocess.check_output(cmd, shell = True )
        cmd = "top -bn1 | grep load | awk '{printf \"CPU Load: %.2f\", $(NF-2)}'"
        CPU = subprocess.check_output(cmd, shell = True )
        cmd = "free -m | awk 'NR==2{printf \"Mem: %s/%sMB %.2f%%\", $3,$2,$3*100/$2 }'"
        MemUsage = subprocess.check_output(cmd, shell = True )
        cmd = "df -h | awk '$NF==\"/\"{printf \"Disk: %d/%dGB %s\", $3,$2,$5}'"
        Disk = subprocess.check_output(cmd, shell = True )
 
        # Write two lines of text.
        draw.text((x+32, y),    "Liuzewen pi",  font=font, fill=255)
        draw.text((x, y+11),    "Test: ",  font=font, fill=255)
        draw.text((x, y+22),    "IP: " + str(IP),  font=font, fill=255)
        draw.text((x, y+32),    str(CPU), font=font, fill=255)
        draw.text((x, y+42),    str(MemUsage),  font=font, fill=255)
        draw.text((x, y+52),    str(Disk),  font=font, fill=255)
 
        # Display image.
        disp.image(image)
        disp.display()
        time.sleep(.1)
        
    for begin in range(1,10):
        draw.rectangle((0,0,width,height), outline=0, fill=0)
        font = ImageFont.truetype('cubic.ttf', 20)
        draw.text((x+32, y+24), "Begin", font=font, fill=255)
        font = ImageFont.truetype('LED Dot-Matrix.ttf', 14)
        draw.text((x+115, y), str(10+1-begin) , font=font, fill=255)
        # Display image.
        disp.image(image)
        disp.display()
        time.sleep(1)
    
    for I_image in range(1,6540):#6540
        image = Image.open('badapple/'+str(I_image)+'.jpg').convert('1')
        disp.image(image)
        disp.display()   
    
 
 