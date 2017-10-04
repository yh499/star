# #part1
 apple = [4, 6, 1, 3, 5, 7, 25]
 def draw_stars(lis):
     for i in apple: 
         print '*' * i

 draw_stars(apple)

#part2
y = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
def findpart():
    for i in y: 
        if isinstance(i, int):
            print '*' * i
        else:
            print i[0].lower()* len(i)
findpart()



