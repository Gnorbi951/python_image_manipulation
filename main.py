from PIL import Image, ImageDraw, ImageFont, ImageOps

def draw_text(image, angle, xy, text, fill, *args, **kwargs):
    """ Draw text at an angle into an image, takes the same arguments
        as Image.text() except for:

    :param image: Image to write text into
    :param angle: Angle to write text at
    """
    # get the size of our image
    width, height = image.size
    max_dim = max(width, height)

    # build a transparency mask large enough to hold the text
    mask_size = (max_dim * 2, max_dim * 2)
    mask = Image.new('L', mask_size, 0)

    # add text to mask
    draw = ImageDraw.Draw(mask)
    draw.text((max_dim, max_dim), text, 255, *args, **kwargs)

    if angle % 90 == 0:
        # rotate by multiple of 90 deg is easier
        rotated_mask = mask.rotate(angle)
    else:
        # rotate an an enlarged mask to minimize jaggies
        bigger_mask = mask.resize((max_dim*8, max_dim*8),
                                  resample=Image.BICUBIC)
        rotated_mask = bigger_mask.rotate(angle).resize(
            mask_size, resample=Image.LANCZOS)

    # crop the mask to match image
    mask_xy = (max_dim - xy[0], max_dim - xy[1])
    b_box = mask_xy + (mask_xy[0] + width, mask_xy[1] + height)
    mask = rotated_mask.crop(b_box)

    # paste the appropriate color, with the text transparency mask
    color_image = Image.new('RGBA', image.size, fill)
    image.paste(color_image, mask)

def main():
    picture_name = "sectors.png" # make sure this is valid image.
    stadion = Image.open(picture_name)

    # draw the text
    font_size = 35
    x_y_coords = (200, 180)
    rgb_color = (0, 0, 0)
    text1 = "test_text1"
    angle1 = 0

    text2 = "test_text2"
    angle2 = 90


    font = ImageFont.truetype('./ArialUnicodeMS.ttf', font_size)
    draw_text(stadion, angle1, x_y_coords, text1, rgb_color, font=font)
    draw_text(stadion, angle2, x_y_coords, text2, rgb_color, font=font)

    stadion.show()
    # stadion.save('edited_sectors.png')  # save file with this line 

if __name__ == '__main__':
    main()