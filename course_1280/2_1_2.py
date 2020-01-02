from skimage.io import imread, imsave
img = imread('img.png');
img[int(img.shape[0]/2), int(img.shape[1]/2)]=[102, 204, 102]
imsave('out_img.png',img)

