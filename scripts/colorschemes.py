import hou

linear = hou.rampBasis.Linear
catrom = hou.rampBasis.CatmullRom

candypeach = hou.Ramp(
    (catrom, catrom, catrom, catrom, catrom, catrom),
    (0, 0.15, 0.35, 0.65, 0.85, 1),
    ((0.409, 0.206, 0.435), (0.528, 0.355, 0.484), (0.545, 0.416, 0.426), (0.606, 0.517, 0.266), (0.72, 0.706, 0.405), (1.0, 1.0, 0.912))
)

blacktoorange = hou.Ramp(
    (linear, linear),
    (0, 1),
    ((0, 0, 0), (1, 0.325, 0.1))
)

blackbody = hou.Ramp(
    (linear, linear, linear, linear),
    (0, 0.333, 0.666, 1),
    ((0, 0, 0), (1, 0, 0), (1, 1, 0), (1, 1, 1))
)

cividis = hou.Ramp(
    (catrom, catrom, catrom, catrom, catrom),
    (0, 0.25, 0.5, 0.75, 1),
    ((0, 0.001, 0.074), (0.05, 0.072, 0.147), (0.198, 0.196, 0.187), (0.506, 0.426, 0.159), (1, 0.821, 0.061))
)

grayscale = hou.Ramp(
    (linear, linear),
    (0, 1),
    ((0, 0, 0), (1, 1, 1))
)

inferno = hou.Ramp(
    (catrom, catrom, catrom, catrom, catrom),
    (0, 0.25, 0.5, 0.75, 1),
    ((0, 0, 0), (0.092, 0, 0.154), (0.492, 0.003, 0.091), (0.949, 0.264, 0), (0.974, 0.996, 0.374))
)

infrared = hou.Ramp(
    (linear, linear, linear, linear, linear),
    (0, 0.25, 0.5, 0.75, 1),
    ((0.2, 0, 1), (0, 0.85, 1), (0, 1, 0.1), (0.95, 1, 0), (1, 0, 0))
)

magma = hou.Ramp(
    (catrom, catrom, catrom, catrom, catrom),
    (0, 0.25, 0.5, 0.75, 1),
    ((0, 0, 0), (0.078, 0, 0.199), (0.462, 0.003, 0.194), (0.968, 0.241, 0.119), (0.971, 0.981, 0.522))
)

plasma = hou.Ramp(
    (catrom, catrom, catrom, catrom, catrom),
    (0, 0.25, 0.5, 0.75, 1),
    ((0, 0, 0.241), (0.204, 0, 0.391), (0.595, 0.062, 0.19), (0.937, 0.296, 0.053), (0.869, 0.944, 0.001))
)
sand = hou.Ramp(
    (catrom, catrom, catrom),
    (0, 0.9, 1),
    ((0.4, 0.32, 0.2), (0.72, 0.706, 0.405), (1, 1, 1))
)

twilight = hou.Ramp(
    (catrom, catrom, catrom, catrom, catrom, catrom, catrom),
    (0, 0.2, 0.4, 0.5, 0.6, 0.8, 1),
    ((0.76, 0.69, 0.76), (0.16, 0.292, 0.528), (0.093, 0.001, 0.23), (0.014, 0, 0.044), (0.104, 0.001, 0.066), (0.502, 0.144, 0.099), (0.76, 0.692, 0.764))
)

twilightshifted = hou.Ramp(
    (catrom, catrom, catrom, catrom, catrom, catrom, catrom, catrom),
    (0, 0.1, 0.26, 0.42, 0.58, 0.74, 0.9, 1),
    ((0.003, 0.001, 0.044), (0.093, 0, 0.231), (0.16, 0.292, 0.528), (0.76, 0.692, 0.764), (0.759, 0.692, 0.759), (0.507, 0.144, 0.099), (0.104, 0.001, 0.066), (0.003, 0.001, 0.044))
)

twotone = hou.Ramp(
    (linear, linear, linear, linear, linear),
    (0, 0.4999, 0.5, 0.5001, 1),
    ((0, 1, 1), (0, 0, 1), (1, 0, 1), (1, 0, 0), (1, 1, 0))
)

viridis = hou.Ramp(
    (catrom, catrom, catrom, catrom, catrom),
    (0, 0.25, 0.5, 0.75, 1),
    ((0.058, 0, 0.089), (0.089, 0.083, 0.258), (0.001, 0.277, 0.265), (0.107, 0.58, 0.125), (0.985, 0.78, 0.001)), 
)

whitetored = hou.Ramp(
    (linear, linear),
    (0, 1),
    ((1, 1, 1), (1, 0, 0))
)

whitewater = hou.Ramp(
    (linear, linear, linear),
    (0, 0.5, 1),
    ((0, 0, 0.9), (0, 0.9, 0.9), (1, 1, 1))
)