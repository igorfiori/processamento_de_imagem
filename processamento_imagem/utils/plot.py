import matplotlib.pyplot as plt

def plot_image(image):
    plt.figure(figsize=(12, 4))
    plt.imshow(image, cmap='gray')
    plt.axis('off')
    plt.show()

def plot_result(*args):
    num_images = len(args)
    fig, axis = plt.subplots(1, num_images, figsize=(12, 4))
    names_lst = ['image{}'.format(i) for i in range(1, num_images)]
    names_lst.append('result')
    for ax, img, name in zip(axis, args, names_lst):
        ax.imshow(image, cmap='gray')
        ax.axis('off')
    fig.tight_layout()
    plt.show()

def plot_histogram(image):
    fig, axis = plt.subplots(nrows=1, ncols=2, figsize=(12, 4), sharex=True, sharey=True)
    colors = ['red', 'green', 'blue']
    for index, (ax, color) in enumerate(zip(axis, color_lst)):
        ax.set_title('{} histogram'.format(color))
        ax.hist(image[:, :, index].ravel(), bins=256, color=color, alpha=0.8)
    fig.tight_layout()
    plt.show()