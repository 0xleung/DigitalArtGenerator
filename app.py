from PIL import Image
import os


def _compose_image(image_files, token_id):
    composite = None
    for image_file in image_files:
        foreground = Image.open(image_file).convert("RGBA")

        if composite:
            composite = Image.alpha_composite(composite, foreground)
        else:
            composite = foreground

    output_path = "images/output/%s.png" % token_id
    composite.save(output_path)

if __name__ == '__main__':
    _compose_image(["images/bases/base-crab.png", "images/eyes/eyes-big.png", "images/mouths/mouth-happy.png"], "2")