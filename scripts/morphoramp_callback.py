node = kwargs['node']

menuParm = node.parm('presets')
menuStr = menuParm.evalAsString()

if menuStr == 'new':
	input = hou.ui.readInput("New Preset", ("Add", "Cancel"), hou.severityType.Message, 0, -1, None, None, 'Name')
        

rampParm = node.parm('ramp')
ramp = rampParm.evalAsRamp()
basis = ramp.basis()
keys = ramp.keys()
values = ramp.values()