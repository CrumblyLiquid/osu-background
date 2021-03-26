import os
from PIL import Image

img_path = input("Please enter the full image path you want to select: ")
osu_path = input("Please enter the full osu path: ") + "\\Data\\bg"

print(f"Loading image form {img_path}")
img = Image.open(img_path)

print("Replacing backgrounds")
for file in os.listdir(osu_path):
    if file.endswith(".jpg") or file.endswith(".png"):
        filepath = os.path.join(osu_path, file)
        os.remove(filepath)
        img.save(filepath)
        print(f"Replaced {file}")
print("Replaced all your backgrounds! Set your \"Options -> Main menu -> Seasonal backgrounds\" to \"Allways\"")