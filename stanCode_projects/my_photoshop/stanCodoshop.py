"""
File: stanCodoshop.py
----------------------------------------------
SC101_Assignment3
Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.

-----------------------------------------------

TODO:
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (float): color distance between red, green, and blue pixel values

    """
    color_dist = ((red - pixel.red)**2 + (green - pixel.green)**2 + (blue - pixel.blue)**2)**0.5
    return color_dist

def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """
    total_red = 0
    total_green = 0
    total_blue = 0
    for i in range(len(pixels)):
        total_red += pixels[i].red
        total_green += pixels[i].green
        total_blue += pixels[i].blue
    avg_red = total_red // len(pixels)
    avg_green = total_green // len(pixels)
    avg_blue = total_blue // len(pixels)
    return [avg_red, avg_green, avg_blue]


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """
    ans = 0
    j = 0
    total_red = 0
    total_green = 0
    total_blue = 0
    for i in range(len(pixels)):
        total_red += pixels[i].red
        total_green += pixels[i].green
        total_blue += pixels[i].blue
    avg_red = total_red // len(pixels)
    avg_green = total_green // len(pixels)
    avg_blue = total_blue // len(pixels)

    for i in range(len(pixels)):
        color_dist = ((avg_red - pixels[i].red) ** 2 + (avg_green - pixels[i].green) ** 2 + (avg_blue - pixels[i].blue) ** 2) ** 0.5
        if i == 1:
            ans = color_dist
            j = i
        else:
            if color_dist <= ans:
                ans = color_dist
                j = i
    return pixels[j]


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """

    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    ######## YOUR CODE STARTS HERE #########
    # Write code to populate image and create the 'ghost' effect
    pixels = []
    for x in range(width):
        for y in range(height):
            for i in range(len(images)):
                pixel = images[i].get_pixel(x, y)
                pixels.append(pixel)
            best = get_best_pixel(pixels)
            blank_pixel = result.get_pixel(x, y)
            blank_pixel.red = best.red
            blank_pixel.green = best.green
            blank_pixel.blue = best.blue
            pixels = []
    ######## YOUR CODE ENDS HERE ###########
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
