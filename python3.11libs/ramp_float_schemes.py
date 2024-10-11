from hou import *

Constant=Ramp((rampBasis.Constant,),(0.0,),(1.0,))

Hill=Ramp((rampBasis.MonotoneCubic, rampBasis.MonotoneCubic, rampBasis.MonotoneCubic), (0.0, 0.5, 1.0), (0.0, 1.0, 0.0))

Linear=Ramp((rampBasis.Linear, rampBasis.Linear), (0.0, 1.0), (0.0, 1.0))

Round=Ramp((rampBasis.Bezier, rampBasis.Bezier, rampBasis.Bezier), (0.0, 0.8, 1.0), (0.0, 0.0, 1.0))

Sharp=Ramp((rampBasis.Bezier, rampBasis.Bezier, rampBasis.Bezier), (0.0, 0.0, 1.0), (0.0, 1.0, 1.0))

Smooth=Ramp((rampBasis.MonotoneCubic, rampBasis.MonotoneCubic), (0.0, 1.0), (0.0, 1.0))

Steps=Ramp((rampBasis.Constant, rampBasis.Constant, rampBasis.Constant, rampBasis.Constant), (0.0, 0.25, 0.5, 0.75), (0.0, 0.333, 0.667, 1.0))

Valley=Ramp((rampBasis.MonotoneCubic, rampBasis.MonotoneCubic, rampBasis.MonotoneCubic), (0.0, 0.5, 1.0), (1.0, 0.0, 1.0))




xd=Ramp((rampBasis.Bezier, rampBasis.Bezier, rampBasis.Bezier, rampBasis.Bezier, rampBasis.Bezier), (0.0, 0.29559749364852905, 0.4297693967819214, 0.6876310110092163, 0.9245283007621765), (1.0, 0.0, 0.0, 0.5666666626930237, 0.8333333134651184))
my_sharp=Ramp((rampBasis.Bezier, rampBasis.Bezier, rampBasis.Bezier), (0.0, 1.0, 1.0), (0.0, 0.0, 1.0))