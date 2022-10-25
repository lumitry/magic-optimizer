# Importing library
import subprocess
import time
from os.path import exists
'''
Automatically generate multiple optimized images for web content
'''

SUPPORTED_FILETYPES = ('avif', 'webp', 'png', 'jpeg', 'jpg', 'gif', 'bmp', 'tiff', 'exr', 'heic', 'jxl') # others are supported by imagemagick (see imagemagick.org/script/formats.php), but are unlikely to be used as they aren't popular/web-friendly
FALLBACK_FORMATS = ('webp', 'jpeg') # formats to use if user doesn't specify one, default being webp and jpeg. must be a list/tuple!!
FILEPATH = './outputs/' # defaults to outputs folder in this project's folder

def get_input():
    image_path = input("Enter the path of the image you'd like to optimize: ")
    cleaned_image_path = image_path.split("'") # removed the quotes around the image from dragging into CLI. probably better way to do this. maybe use RE?
    #TODO Use RE instead of split?
    return cleaned_image_path[1] # returns the path. will glitch out if there is a ' in the filename!!

def is_image(extension):
    '''
    Returns True if inputted path is a recognized image file
    '''
    return extension in SUPPORTED_FILETYPES # if extension is in supported filetypes, will return True. Returns False otherwise

def get_output_types():
    '''
    Returns a tuple of output types based on user input. May change to CLI launch arguments in the future.
    '''
    types = []
    while True:
        type = input("Give a file type you'd like to optimize to: ") #TODO: Add support for one-line input, i.e. type="avif, webp, jpeg, png" should get parsed
        if type == "":
            break # end loop if user doesn't specify a type
        elif type not in SUPPORTED_FILETYPES:
            print("Type not recognized! Try again!")
        else: # TODO add support for including a '.' in input, i.e. type=".avif" instead of type="avif"
            types.append(type)
            print("Type recognized:", type)
    if len(types) == 0: # return fallback formats if they didn't specify any, to prevent future code from breaking
        return FALLBACK_FORMATS
    else:
        return types

def input_path_to_name(input_path=None):
    '''
    Turns an input image's path to a cleaned-up name for the output image
    '''
    if input_path == None: # in case input path isn't specified, use get input. in this program i'll specify the path, so this is just a failsafe.
        input_path = get_input()
    #TODO: Change to Regex or something similar?
    name = ""
    for dot_char_index in range(len(input_path)-1, 0, -1): # searches from the end of the path to the beginning, stopping at the very last period in the path, ensuring that it stops on the extension
        if input_path[dot_char_index] == ".":
            break
    for slash_char_index in range(len(input_path)-1, 0, -1): # searches from the end of the path to the beginning, stopping at the very last slash in the path, ensuring that it stops on the image's folder
        if input_path[slash_char_index] in "\\/": # this should mean windows is supported, i'm not sure though
            break
    name = input_path[slash_char_index + 1:dot_char_index] # slices out the text between the last slash and the last dot in the input path
    original_extension = input_path[dot_char_index+1:]
    return name, original_extension

def get_quality_list():
    '''
    Gets list of qualities, returns a list in format ['@2x', '@1x', '@0.5x']
    '''
    quality_list = []
    if len(quality_list) == 0:
        quality_list = ['@0.5x', '@1x', '@2x']
    #TODO **allow user input**
    return quality_list

def output_paths(filename, types=None, quality_levels=None, output_path=FILEPATH):
    '''
    Returns a tuple of output paths given a filename without extension, and optionally a list of types, list of qualities, and a filepath
    '''
    paths = [] # empty list for mutability

    if types == None: # base case: if no types are specified, use get_output_types function
        types = get_output_types()
    if quality_levels == None: # another base case: if no quality levels are specified, use get_quality_list function
        quality_levels = get_quality_list()

    for type in types: # loop over each type in types
        if type[0] == ".": # if there's a dot, then the file extension doesn't need to have one
            extension = type
        else: # otherwise, put a dot before the type to make the extension
            extension = '.' + type
        for quality in quality_levels:
            path = output_path + filename + quality + extension
            paths.append(path)

    return tuple(paths) # turns list to tuple and returns

def optimize_image(image_path=None):
    '''
    Uses all other functions to optimize an image using ImageMagick.
    '''
    is_path_valid = False # assumes path isn't valid, but will still work if it isn't
    if image_path == None: # if no path is specified, get a path
            image_path = get_input()
    while is_path_valid == False: # loop until path is valid
        image_name, original_extension = input_path_to_name(image_path) # get name without extension or containing folder, and original extension
        if is_image(original_extension): # if the extension is recognized as a valid image, don't prompt for another file type
            is_path_valid = True
        else:
            print("Error! Invalid file extension recognized. Are you sure that's an image?")
            image_path = get_input()
            continue

    start = time.perf_counter() # start timer

    paths = output_paths(image_name)
    generated_count = 0 # default value for number of files generated
    for path in paths: # loop over all paths in output_paths
        if not exists(path): # if the desired file doesn't exist, add 1 to the generated files count
            generated_count += 1
        subprocess.run(["magick", image_path, path]) # runs imagemagick with image path as input and output path as output
        #TODO add CLI arguments for magick???

    end = time.perf_counter() # end timer
    elapsed_time = end - start

    return generated_count, elapsed_time

def main():
    count, elapsed_time = optimize_image()
    print("Took", round(elapsed_time, 3), "seconds to generate", count, "files!")

if __name__ == "__main__":
    main()