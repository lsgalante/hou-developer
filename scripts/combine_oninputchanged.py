node = kwargs['node']
group = hou.ParmTemplateGroup(())
inputs = node.inputs()
n_inputs = len(inputs)

for i in range(n_inputs):
	string_template = hou.StringParmTemplate(
		name = 'attrs' + str(i),
		label = 'Input ' + str(i) + ' Attributes',
		num_components = 1,
		default_value = (''),
		item_generator_script = "kwargs['node'].generateInputAttribMenu(" + str(i) + ", hou.attribType.Point)",
		menu_type = hou.menuType.StringToggle)
	group.append(string_template)

node.setParmTemplateGroup(group)

foreach_end1 = node.node('foreach_end1')
iterations = foreach_end1.parm('iterations')
iterations.set(n_inputs)