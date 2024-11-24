from PIL import Image
from os.path import join

path_base_bajos = join("..", "imgs", "CSE_tramos_bajos", "mapas_calor")
path_base_altos = join("..", "imgs", "CSE_tramos_altos", "mapas_calor")

paths_bajos = []
paths_altos = []
for i in range(16, 22):
    paths_bajos.append(join(path_base_bajos, f"20{i}06.png"))
    paths_bajos.append(join(path_base_bajos, f"20{i}12.png"))
    paths_altos.append(join(path_base_altos, f"20{i}06.png"))
    paths_altos.append(join(path_base_altos, f"20{i}12.png"))

frames_bajos = [Image.open(path) for path in paths_bajos]
frames_altos = [Image.open(path) for path in paths_altos]

path_gif_bajos = join("..", "imgs", "CSE_tramos_bajos", "cambio_mapas.gif")
path_gif_altos = join("..", "imgs", "CSE_tramos_altos", "cambio_mapas.gif")

frames_bajos[0].save(
    path_gif_bajos,
    save_all = True,
    append_images = frames_bajos[1:],
    duration = 1000,
    loop = 0
)

frames_altos[0].save(
    path_gif_altos,
    save_all = True,
    append_images = frames_altos[1:],
    duration = 1000,
    loop = 0
)