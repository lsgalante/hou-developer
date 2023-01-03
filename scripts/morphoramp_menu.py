import default_ramp_schemes

node = kwargs['node']
rampParm = node.parm('ramp')
ramp = rampParm.evalAsRamp()
basis = ramp.basis()
keys = ramp.keys()
values = ramp.values()

key = str(basis) + ', ' + str(keys) + ', ' + str(values)

houdini_preset = ['Custom', 'Custom']

if key == default_ramp_schemes.Black_to_Orange:
	houdini_preset = ['Black_to_Orange', 'Black to Orange']

if key == default_ramp_schemes.Blackbody:
	houdini_preset = ['Blackbody', 'Blackbody']

if key == default_ramp_schemes.Cividis:
	houdini_preset = ['Cividis', 'Cividis']

if key == default_ramp_schemes.Grayscale:
	houdini_preset = ['Grayscale', 'Grayscale']

if key == default_ramp_schemes.Inferno:
	houdini_preset = ['Inferno', 'Inferno']

if key == default_ramp_schemes.Infra_Red:
	houdini_preset = ['Infra_Red', 'Infra-Red']

if key == default_ramp_schemes.Magma:
	houdini_preset = ['Magma', 'Magma']

if key == default_ramp_schemes.Plasma:
	houdini_preset = ['Plasma', 'Plasma']

if key == default_ramp_schemes.Sand:
	houdini_preset = ['Sand', 'Sand']

if key == default_ramp_schemes.Twilight:
	houdini_preset = ['Twilight', 'Twilight']

if key == default_ramp_schemes.Twilight_Shifted:
	houdini_preset = ['Twilight_Shifted', 'Twilight Shifted']

if key == default_ramp_schemes.Two_Tone:
	houdini_preset = ['Two_Tone', 'Two-Tone']

if key == default_ramp_schemes.Viridis:
	houdini_preset = ['Viridis', 'Viridis']

if key == default_ramp_schemes.White_to_Red:
	houdini_preset = ['White_to_Red', 'White to Red']

if key == default_ramp_schemes.Whitewater:
	houdini_preset = ['Whitewater', 'Whitewater']

menu = houdini_preset + ['_separator_', '_separator_', 'new', 'New Preset']

return menu