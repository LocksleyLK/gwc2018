from PIL import Image
import filters

def main():
    im = filters.load_img("HarpyEagleDrawing")
    filters.show_img(im)
    #im = filters.obamicon(im)
    #filters.show_img(im)
    #im = filters.sepia(im)
    #filters.show_img(im)

    #filters.save_img(im, "HarpyEagleFiltered")


if __name__ == "__main__":
  main()
