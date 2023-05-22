import Augmentor

#duplicates data to 50000 samples + original sample size to increase dataset size
p = Augmentor.Pipeline(r"C:\\Users\\ardaa\\OneDrive\\Desktop\\archive\\BrainT-Dataset")
p.zoom(probability=0.4, min_factor=0.8, max_factor=1.5)
p.flip_top_bottom(probability=0.4)
p.flip_left_right(probability=0.4)
p.random_brightness(probability=0.5, min_factor=0.3, max_factor=1.2)
p.random_distortion(probability=0.1, grid_width=4, grid_height=4, magnitude=8)
p.invert(probability=0.5)
p.rotate90(probability=0.33)
p.rotate180(probability=0.33)
p.rotate270(probability=0.33)
p.sample(18000)