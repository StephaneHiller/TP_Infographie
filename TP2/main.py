import cng
import bresenham

if __name__ == '__main__':
    cng.init_window('Bresenham',
                        800,
                        800)

    #bresenham.default(100, 100)

    #bresenham.advanced(150, 100, 500, 500)

    #bresenham.two_octant(50, 350)

    # /!\ ordinate (400, 400) /!\
    bresenham.generic(-100, 100, -200, -200)

    cng.main_loop()
