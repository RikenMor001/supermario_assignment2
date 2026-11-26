import pygame as pg
from source.main import main
from demo_simulation import generate_demo_image

if __name__ == '__main__':
    consent = input("Generate a synthetic demo image? (y/n): ")

    if consent.lower() == "y":
        generate_demo_image()

    main()
    pg.quit()