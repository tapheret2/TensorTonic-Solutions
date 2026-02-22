def color_to_grayscale(image):
    """
    Convert an RGB image to grayscale using luminance weights.
    """
    # Write code here
    result=image
    for i in range(len(image)):
        for j in range(len(image[i])):
            result[i][j]=image[i][j][0]*0.299+image[i][j][1]*0.587+image[i][j][2]*0.114
    return result