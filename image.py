from PIL import Image

image=Image.open("bar_1.png")
image.show()
print(image.format)
print(image.mode)
print(image.size)
print(image.palette)
#changing  immage type
image=Image.open("bar_1.png")
image.save("bar_1.jpg")
#resizing images

image=Image.open("hist_1.png")
image.size
image2=image.resize((400,400))
image2.show()
image2.size
image2.save("image-400.jpg")
image=Image.open("hist_1.png")
image.size
image.thumbnail((400,100))
image.show()
image.size

#cropping image
image=Image.open("bar_1.png")
image.show()
image.size
box=(0,150,200,200)
Cropped_image=image.crop(box)
Cropped_image.show()
Cropped_image.save("Cropped_image.png")
#pasting an images
image=Image.open("bar_1.png")
image.show()
hist=Image.open("hist_1.png")
hist.show()
image.paste(hist,box=(2,2))
image.show()
#rotating images
image=Image.open("bar_1.png")
image.show()
rot_90=image.rotate(90)
rot_90.show()
rot_90=image.rotate(90,expand=True)
rot_90.show()
#flipping images
image=Image.open("bar_1.png")
image.show()
left_right=image.transpose(Image.FLIP_LEFT_RIGHT)
left_right.show()
top_bottom=image.transpose(Image.FLIP_TOP_BOTTOM)
top_bottom.show()