from PIL import Image, ImageDraw 

def main():
    picture_name = "sectors.png" # make sure this is valid.
    stadion = Image.open(picture_name)

    title_text = "cim mezo teszt"

    editable_image = ImageDraw.Draw(stadion)

    rgb_config = (0, 0, 0) # color setting
    x, y = 15, 15
    editable_image.text((x, y), title_text, rgb_config)

    stadion.save("result.png") # file extension should be the same



if __name__ == '__main__':
    main()