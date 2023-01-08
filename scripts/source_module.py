import hou
import importlib
import stain_menu
import stain_schemes

def add_vis(kwargs):
	node = kwargs['node']

	group = node.parmTemplateGroup()
	entries = group.entries()

	vis_count = 0
	for parm_template in entries:
		if parm_template.type() == hou.parmTemplateType.Folder:
			vis_count += 1

	new_id = str(vis_count + 1)

	enable_template = hou.ToggleParmTemplate(
		'enable_vis' + new_id,
		label = "Enable Visualizer",
		default_value = True,
		script_callback = 'hou.phm().enable(kwargs)',
		script_callback_language = hou.scriptLanguage.Python)

	attr_template = hou.StringParmTemplate(
		name = 'attr' + new_id,
		label = "Attribute",
		num_components = 1,
		menu_items = ('mag', 'mag2', 'mag3', 'dir', 'dir2', 'dir3'),
		menu_labels = ("mag", "mag2", "mag3", "dir", "dir2", "dir3"),
		menu_type = hou.menuType.StringReplace,
		script_callback = 'hou.phm().attr(kwargs)',
		script_callback_language = hou.scriptLanguage.Python)

	type_template = hou.MenuParmTemplate(
		name = 'type' + new_id,
		label = "Type",
		menu_items = ('color', 'marker'),
		menu_labels = ("Color", "Marker"),
		script_callback = 'hou.phm().type(kwargs)',
		script_callback_language = hou.scriptLanguage.Python)

	coloring_template = hou.MenuParmTemplate(
		name = 'coloring' + new_id,
		label = "Coloring",
		menu_items = ('fixed', 'val', 'dir', 'other'),
		menu_labels = ("Fixed Color", "Vector Values", "Vector Directions", "Other Attribute"),
		script_callback = 'hou.phm().coloring(kwargs)',
		script_callback_language = hou.scriptLanguage.Python)

	coloring_template.setConditional(
		hou.parmCondType.HideWhen,
		'{ type' + new_id + ' != marker }')

	sep_template1 = hou.SeparatorParmTemplate(
		name = 'sep1_' + new_id)

	preset_template = hou.MenuParmTemplate(
		name = 'preset' + new_id,
		label = "Preset",
		menu_items = (),
		menu_labels = (),
		item_generator_script = 'hou.phm().preset_menu(kwargs)',
		script_callback = 'hou.phm().preset(kwargs)',
		script_callback_language = hou.scriptLanguage.Python,
		join_with_next = True)

	preset_template.setConditional(
		hou.parmCondType.HideWhen,
		'{ type' + new_id + ' == marker coloring' + new_id + ' == fixed }')

	overwrite_template = hou.ButtonParmTemplate(
		name = 'overwrite' + new_id,
		label = "Overwrite",
		script_callback = 'hou.phm().overwrite(kwargs)',
		script_callback_language = hou.scriptLanguage.Python,
		join_with_next = True)

	overwrite_template.setConditional(
		hou.parmCondType.HideWhen,
		'{ type' + new_id + ' == marker coloring' + new_id + ' == fixed }')

	del_preset_template = hou.ButtonParmTemplate(
		name = 'del_preset' + new_id,
		label = "Delete Preset",
		script_callback = 'hou.phm().del_preset(kwargs)',
		script_callback_language = hou.scriptLanguage.Python)

	del_preset_template.setConditional(
		hou.parmCondType.HideWhen,
		'{ type' + new_id + ' == marker coloring' + new_id + ' == fixed }')

	interpol_template = hou.MenuParmTemplate(
		name = 'interpol' + new_id,
		label = "Interpolation",
		menu_items = ('Constant', 'Linear', 'CatmullRom', 'MonotoneCubic', 'Bezier', 'BSpline', 'Hermite'),
		menu_labels = ("Constant", "Linear", "Catmull-Rom", "Monotone-Cubic", "Bezier", "B-Spline", "Hermite"),
		script_callback = 'hou.phm().interpol(kwargs)',
		script_callback_language = hou.scriptLanguage.Python)

	interpol_template.setConditional(
		hou.parmCondType.HideWhen,
		'{ type' + new_id + ' == marker coloring' + new_id + ' == fixed }')

	ramp_template = hou.RampParmTemplate(
		name = 'ramp' + new_id,
		label = "Color Ramp",
		ramp_parm_type = hou.rampParmType.Color,
		show_controls = False,
		script_callback = 'hou.phm().ramp(kwargs)',
		script_callback_language = hou.scriptLanguage.Python)

	ramp_template.setConditional(
		hou.parmCondType.HideWhen,
		'{ type' + new_id + ' == marker coloring' + new_id + ' == fixed }')

	color_template = hou.FloatParmTemplate(
		name = 'color' + new_id,
		label = "Color",
		num_components = 3,
		naming_scheme = hou.parmNamingScheme.RGBA,
		look = hou.parmLook.ColorSquare,
		script_callback = 'hou.phm().ramp(kwargs)',
		script_callback_language = hou.scriptLanguage.Python)

	color_template.setConditional(
		hou.parmCondType.HideWhen,
		'{ type' + new_id + ' != marker } { coloring' + new_id + '!= fixed }')

	length_template = hou.FloatParmTemplate(
		name = 'length' + new_id,
		label = "Length Scale",
		num_components = 1,
		max = 1.0,
		script_callback = 'hou.phm().length(kwargs)',
		script_callback_language = hou.scriptLanguage.Python)

	length_template.setConditional(
		hou.parmCondType.HideWhen,
		'{ type' + new_id + ' != marker }')

	sep_template2 = hou.SeparatorParmTemplate(
		name = 'sep2_' + new_id)

	del_vis_template = hou.ButtonParmTemplate(
		name = 'del_vis' + new_id,
		label = "Delete Visualizer",
		script_callback = 'hou.phm().del_vis(kwargs)',
		script_callback_language = hou.scriptLanguage.Python)

	folder_template = hou.FolderParmTemplate(
		name = 'folder' + new_id,
		label = "Vis " + new_id,
		parm_templates = ([
			enable_template,
			attr_template,
			type_template,
			coloring_template,
			sep_template1,
			preset_template,
			overwrite_template,
			del_preset_template,
			interpol_template,
			ramp_template,
			color_template,
			length_template,
			sep_template2,
			del_vis_template]),
		folder_type = hou.folderType.Tabs)

	group.append(folder_template)
	node.setParmTemplateGroup(group)

	##

	attr_parm = node.parm('attr' + new_id)
	attr_parm.set('vis' + new_id)

	preset_parm = node.parm('preset' + new_id)
	preset_val = preset_parm.evalAsString()

	ramp_parm = node.parm('ramp' + new_id)
	ramp_val = getattr(stain_schemes, preset_val)
	ramp_parm.set(ramp_val)

	##

	vis = hou.viewportVisualizers.createVisualizer(
		hou.viewportVisualizers.type('vis_color'),
		hou.viewportVisualizerCategory.Node,
		hou.node('./vis'))
	vis.setParm('colortype', 1)
	vis.setParm('rangespec', 1)
	vis.setParm('clamptype', 1)
	vis.setParm('colorramp', ramp_val)
	vis.setName('vis' + new_id)
	vis.setLabel('vis' + new_id)
	vis.setParm('attrib', 'vis' + new_id)
	vis.setIsActive(True)

def enable(kwargs):
	node = kwargs['node']
	parm = kwargs['parm']
	val = parm.eval()

	vis_id = get_vis_id(kwargs, 'enable_vis')
	vis = get_vis(vis_id)

	if val == 1:
		vis.setIsActive(True)
	if val == 0:
		vis.setIsActive(False)

def attr(kwargs):
	node = kwargs['node']
	parm = kwargs['parm']
	val = parm.evalAsString()

	vis_id = get_vis_id(kwargs, 'attr')
	vis = get_vis(vis_id)

	vis.setParm('attrib', val)
	vis.setLabel(val)

	##

	folder = 'x'
	folder_name = 'x'

	group = node.parmTemplateGroup()

	if vis_id == '1':
		folder_name = 'folder1'
		

	else:
		folder_name = 'folder1_' + str(int(vis_id) - 1)

	folder = group.find(folder_name)
	folder.setLabel(val)

	group.replace(folder_name, folder)
	node.setParmTemplateGroup(group)

def type(kwargs):
	node = kwargs['node']
	parm = kwargs['parm']
	val = parm.eval()

	vis_id = get_vis_id(kwargs, 'type')
	vis = get_vis(vis_id)

	vistypes = hou.viewportVisualizers.types()

	if val == 0:
		vis.setType(vistypes[1])
	if val == 1:
		vis.setType(vistypes[0])
		vis.setParm('style', 4)

		coloring_parm = node.parm('coloring' + vis_id)
		coloring_val = coloring_parm.eval()

		vis.setParm('vectorcoloring', coloring_val)

		if coloring_val == 0:
			colorr = node.parm('color' + vis_id + 'r').eval()
			colorg = node.parm('color' + vis_id + 'g').eval()
			colorb = node.parm('color' + vis_id + 'b').eval()
			vis.setParm('markercolorr', colorr)
			vis.setParm('markercolorg', colorg)
			vis.setParm('markercolorb', colorb)
		if coloring_val != 0:
			vis.setParm('ramptype', 6)
			vis.setParm('rangespec', 0)
		if coloring_val == 3:
			colorattr = node.parm('colorattr' + index).eval()
			vis.setParm('colorattrib', colorattr)

def coloring(kwargs):
	node = kwargs['node']
	parm = kwargs['parm']
	val = parm.eval()

	vis_id = get_vis_id(kwargs, 'coloring')
	vis = get_vis(vis_id)

	vis.setParm('vectorcoloring', val)

	if coloring == 0:
		color(kwargs)
	if coloring != 0:
		vis.setParm('ramptype', 6)
		vis.setParm('rangespec', 0)
	if coloring == 3:
		colorattr(kwargs)

def preset(kwargs):
	node = kwargs['node']
	vis_node = hou.node('./vis')
	name = kwargs['parm_name']
	vis_id = name.replace('preset', '')

	preset_parm = kwargs['parm']
	preset_val = preset_parm.evalAsString()

	ramp_parm = node.parm('ramp' + vis_id)

	if preset_val == 'New...':
		new_preset(preset_parm, ramp_parm)

	else:
		ramp_val = getattr(stain_schemes, preset_val)
		ramp_parm.set(ramp_val)

		##

		vistup = hou.viewportVisualizers.visualizers(
			hou.viewportVisualizerCategory.Node,
			vis_node)

		attr_parm = node.parm('attr' + vis_id)
		attr_val = attr_parm.evalAsString()

		vis = 0
		for x in vistup:
			if x.name() == attr_val:
				vis = x

		vis.setParm('colorramp', ramp_val)

def preset_menu(kwargs):
	importlib.reload(stain_menu)
	menu = stain_menu.menu
	return(menu)

def new_preset(preset_parm, ramp_parm):
	new_name = hou.ui.readInput(
		"New Preset",
		buttons = ("Add", "Cancel"))

	if new_name[0] == 0:
		menu = stain_menu.menu
		menu.insert(0, new_name[1])
		menu.insert(0, new_name[1])

		menu_file = open('C:/Users/lucas/OneDrive/Git/morphogen/scripts/stain_menu.py', 'w')
		menu_file.write('menu=' + str(menu))
		menu_file.close()

		importlib.reload(stain_menu)
		preset_parm.set(0)

		##

		ramp_val = ramp_parm.evalAsRamp()

		new_scheme = create_scheme(new_name[1], ramp_val)

		scheme_file = open('C:/Users/lucas/OneDrive/Git/morphogen/scripts/stain_schemes.py', 'a')
		scheme_file.write(new_scheme)
		scheme_file.close()

		importlib.reload(stain_schemes)

def overwrite(kwargs):
	node = kwargs['node']
	vis_node = hou.node('./vis')
	name = kwargs['parm_name']
	vis_id = name.replace('overwrite', '')

	preset_parm = node.parm('preset' + vis_id)
	preset_val = preset_parm.evalAsString()

	current_ramp = getattr(stain_schemes, preset_val)
	current_scheme = create_scheme(preset_val, current_ramp)

	ramp_parm = node.parm('ramp' + vis_id)
	ramp_val = ramp_parm.evalAsRamp()
	new_scheme = create_scheme(preset_val, ramp_val)

	file = 'C:/Users/lucas/OneDrive/Git/morphogen/scripts/stain_schemes.py'

	schemes = open(file, 'r').read()
	new_schemes = schemes.replace(current_scheme, new_scheme)

	write = open(file, 'w')
	write.write(new_schemes)
	write.close()

	importlib.reload(stain_schemes)

def del_preset(kwargs):
	node = kwargs['node']
	vis_node = hou.node('./vis')
	name = kwargs['parm_name']
	vis_id = name.replace('del_preset', '')

	preset_parm = node.parm('preset' + vis_id)
	preset_val = preset_parm.evalAsString()

	menu = stain_menu.menu
	menu.remove(preset_val)
	menu.remove(preset_val)

	menu_file = open('C:/Users/lucas/OneDrive/Git/morphogen/scripts/stain_menu.py', 'w')
	menu_file.write('menu=' + str(menu))
	preset_parm.set(0)
	menu_file.close()

	ramp = getattr(stain_schemes, preset_val)
	current_scheme = create_scheme(preset_val, ramp)

	scheme_file = 'C:/Users/lucas/OneDrive/Git/morphogen/scripts/stain_schemes.py'

	schemes = open(scheme_file, 'r').read()
	new_schemes = schemes.replace(current_scheme, '')

	write = open(scheme_file, 'w')
	write.write(new_schemes)
	write.close()

	importlib.reload(stain_menu)
	importlib.reload(stain_schemes)

def interpol(kwargs):
	node = kwargs['node']

	parm_name = kwargs['parm_name']
	vis_id = parm_name.replace('interpol', '')

	parm = kwargs['parm']
	val = parm.evalAsString()

	ramp_parm = node.parm('ramp' + vis_id)
	ramp_val = ramp_parm.evalAsRamp()

	basis = ramp_val.basis()
	keys = ramp_val.keys()
	values = ramp_val.values()

	new_basis = []

	for x in basis:
		if val == 'Constant':
			new_basis.append(hou.rampBasis.Constant)
		if val == 'Linear':
			new_basis.append(hou.rampBasis.Linear)
		if val == 'CatmullRom':
			new_basis.append(hou.rampBasis.CatmullRom)
		if val == 'MonotoneCubic':
			new_basis.append(hou.rampBasis.MonotoneCubic)
		if val == 'Bezier':
			new_basis.append(hou.rampBasis.Bezier)
		if val == 'BSpline':
			new_basis.append(hou.rampBasis.BSpline)
		if val == 'Hermite':
			new_basis.append(hou.rampBasis.Hermite)

	new_ramp = hou.Ramp(
		new_basis,
		keys,
		values)

	ramp_parm.set(new_ramp)

	vis = get_vis(vis_id)
	vis.setParm('colorramp', new_ramp)

def ramp(kwargs):
	node = kwargs['node']
	parm = kwargs['parm']
	val = parm.evalAsRamp()

	vis_id = get_vis_id(kwargs, 'ramp')
	vis = get_vis(vis_id)

	vis.setParm('colorramp', val)

	##

	preset_parm = node.parm('preset' + vis_id)
	preset_parm.set('_separator_')

def color(kwargs):
	node = kwargs['node']
	vis_node = hou.node('./vis')

	parm_name = kwargs['parm_name']
	vis_id = parm_name.replace('color', '')

	colorr = node.parm('color' + vis_id + 'r').eval()
	colorg = node.parm('color' + vis_id + 'g').eval()
	colorb = node.parm('color' + vis_id + 'b').eval()

	vis = get_vis(vis_id)

	vis.setParm('markercolorr', colorr)
	vis.setParm('markercolorg', colorg)
	vis.setParm('markercolorb', colorb)

def colorattr(kwargs):
	node = kwargs['node']
	vis_node = hou.node('./vis')

	parm_name = kwargs['parm_name']
	parm_val = parm_name.eval()
	vis_id = parm_name.replace('colorattr', '')

	vis = get_vis(vis_id)

	vis.setParm('colorattrib', parm_val)

def length(kwargs):
	parm = kwargs['parm']
	val = length_parm.eval()

	vis_id = get_vis_id(kwargs, 'length')
	vis = get_vis(vis_id)

	vis.setParm('lengthscale', val)

def del_vis(kwargs):
    node = kwargs['node']

    vis_id = get_vis_id(kwargs, 'del_vis')
    vis = get_vis(vis_id)
    
    parm = kwargs['parm']
    index = parm.containingFolderIndices()
    index = (index[0] + 1,)

    group = node.parmTemplateGroup()
    group.remove(index)

    entries = group.entries()
    folder_id = 0
    
    for entry in entries:
        if entry.type() == hou.parmTemplateType.Folder:
            folder_id += 1

            new_entry = entry.clone()
            new_entry.setLabel("Vis " + str(folder_id))

            contents = new_entry.parmTemplates()
            for template in contents:
            	if template.label() == "Enable Visualizer":
            		template.setName('enable_vis' + str(folder_id))
            	if template.label() == "Attribute":
            		template.setName('attr' + str(folder_id))
            	if template.label() == "Type":
            		template.setName('type' + str(folder_id))
            	if template.label() == "Coloring":
            		template.setName('coloring' + str(folder_id))
            	if 'sep1_' in template.name():
            		template.setName('sep1_' + str(folder_id))
            	if template.label() == "Preset":
            		template.setName('preset' + str(folder_id))
            	if template.label() == "Overwrite":
            		template.setName('overwrite' + str(folder_id))
            	if template.label() == "Delete Preset":
            		template.setName('del_preset' + str(folder_id))
            	if template.label() == "Interpolation":
            		template.setName('interpol' + str(folder_id))
            	if template.label() == "Color Ramp":
            		template.setName('ramp' + str(folder_id))
            	if template.label() == "Color":
            		template.setName('color' + str(folder_id))
            	if template.label() == "Length Scale":
            		template.setName('length' + str(folder_id))
            	if 'sep2_' in template.name():
            		template.setName('sep2_' + str(folder_id))
            	if template.label() == "Delete Visualizer":
            		template.setName('del_vis' + str(folder_id))

            new_entry.setParmTemplates(contents)

            group.replace(entry, new_entry)

    node.setParmTemplateGroup(group)

def create_scheme(preset_val, ramp_val):
	basis = ramp_val.basis()
	basis = tuple('hou.' + str(x) for x in basis)
	basis = str(basis).replace("'", "")

	keys = ramp_val.keys()
	keys = tuple(round(x, 4) for x in keys)

	values = ramp_val.values()
	values = tuple(tuple(round(x2, 4) for x2 in x) for x in values)

	scheme = '\n' + preset_val + '=' + 'hou.Ramp(' + str(basis) + ',' + str(keys) + ',' + str(values) + ')\n'

	return(scheme)

def get_vis_id(kwargs, replace):
	name = kwargs['parm_name']
	vis_id = name.replace(replace, '')
	return(vis_id)

def get_vis(vis_id):
	vistup = hou.viewportVisualizers.visualizers(
		hou.viewportVisualizerCategory.Node,
		hou.node('./vis'))
	vis = vistup[int(vis_id) - 1]
	return(vis) 