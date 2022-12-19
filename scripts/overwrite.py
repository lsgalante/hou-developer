import hou

linear = hou.rampBasis.Linear
catrom = hou.rampBasis.CatmullRom
candypeach = hou.Ramp(
    (catrom, catrom),
    (0, 1),
    ((0, 0, 0), (0, 0, 0))
) 
x