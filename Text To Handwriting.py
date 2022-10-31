from PIL import Image
from sys import argv

fileName = "sample.txt" 
try:
    txt=open(argv[1], "r")

except IndexError:
    print("No file entered. Using default file...")
    txt=open(fileName, "r")
    
except FileNotFoundError:
    print("Could not find file. Using default file...")
    txt=open(fileName, "r")   

BG=Image.open("myfont/bg.png") 
sheet_width=BG.width
gap, ht = 500, 500
for i in txt.read().replace("\n",""):
        cases = Image.open("myfont/{}.png".format(str(ord(i))))
        BG.paste(cases, (gap, ht))
        size = cases.width
        height=cases.height
        print("Running...........")
        gap+=size

        if sheet_width < gap or len(i)*115 >(sheet_width-gap):
            gap,ht=0,ht+140

print(gap)
print(sheet_width)
BG.show()
