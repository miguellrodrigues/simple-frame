import numpy as np

from lib.frame import Frame, FrameDrawer

f0 = Frame(0, 0, 0)
f1 = Frame(2, 2, 0)

f1.rotate_around_arbitrary_vector(1.57, [0, 1.2, 0])


def update():
  f1.translate_to(f0)

  r = np.abs(f1.rotation_to(f0))

  f1.rotate(0, -r[1]*.03, 0)


drawer = FrameDrawer([f0, f1], update)
drawer.show(True)
