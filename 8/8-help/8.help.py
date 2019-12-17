x = open("input.txt").read()
width = 25
height = 6
layers = []
for i in range(int(len(x)/(width*height))):
  layers.append(x[i*width*height:(i+1)*width*height])
#part 1
layer = [y for y in layers if y.count("0") == min([ j.count("0") for j in layers])][0]
print(layer.count("1")*layer.count("2"))
#part 2
img = ""
for c in range(width*height):
  d = 0
  while True:
    if d>=len(layers):
      img = img+"0"
    if layers[d][c]=="0"or layers[d][c]=="1":
      img= img+(layers[d][c])
      break
    d+=1
img=img.replace("0"," ")
img=img.replace("1","#")
for h in range(height):
  print(" ".join([x for x in img[h*width:(h+1)*width]]))
