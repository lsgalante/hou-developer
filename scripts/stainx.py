import importlib
import stain_menu
import stain_schemes

def add(kwargs):
    node = kwargs['node']
        
    group = node.parmTemplateGroup()
    entries = group.entries()
        
    id = 1
    for parm_template in entries:
        if parm_template.type() == hou.parmTemplateType.Folder:
            id += 1
    
    enable_template = hou.ToggleParmTemplate(
    	'enable' + str(id),
    	label = 'Enable',
    	default_value = False,
    	disable_when = None,
    	is_hidden = False,
    	is_label_hidden = False,
    	join_with_next = False,
    	help = None,
    	script_callback = None,
    	default_expression_language = hou.scriptLanguage.Python)

    name_template = hou.StringParmTemplate(
    	name = 'name' + str(id),
    	label = 'Name',
    	num_components = 1,
    	default_value = (),
    	naming_scheme = hou.parmNamingScheme.Base1,
    	string_type = hou.stringParmType.Regular,
    	file_type = hou.fileType.Any,
    	menu_items = (),
    	menu_labels = (),
    	icon_names = ())
    	# item_generator_script = ())
    	# item_generator_script_language = None)
    	# menu_type = hou.menuType.StringReplace,
    	# disable_when = None,
    	# is_hidden = False,
    	# is_label_hidden = False,
    	# join_with_next = False,
    	# help = None,
    	# script_callback = None)

    del_template = hou.ButtonParmTemplate(
        name = 'del' + str(id),
        label = 'Delete',
        disable_when = None,
        is_hidden = False,
        is_label_hidden = False,
        join_with_next = False,
        help = None,
        script_callback = 'hou.phm().delete(kwargs)',
        script_callback_language = hou.scriptLanguage.Python)
            
    folder_template = hou.FolderParmTemplate(
        name = 'vis',
        label = 'Vis ' + str(id),
        parm_templates = ([
        	enable_template,
        	name_template,
        	del_template]),
        folder_type = hou.folderType.Tabs)
    
    group.append(folder_template)
    node.setParmTemplateGroup(group)
    
def delete(kwargs):
    node = kwargs['node']
    button_name = kwargs['parm_name']
    button_parm = node.parm(button_name)
    folder_index = button_parm.containingFolderIndices()
    folder_index = (folder_index[0] + 1,)

    group = node.parmTemplateGroup()

    group.remove(button_name)
    group.remove(folder_index)
    
    entries = group.entries()
    node.setParmTemplateGroup(group)

    folder_id = 0
    for parm_template in entries:
        if parm_template.type() == hou.parmTemplateType.Folder:
            folder_id += 1

            new_template = parm_template.clone()

            contents = parm_template.parmTemplates()
            for parm_template2 in contents:
                if parm_template2.label() == "Delete":
                    parm_template2.setName('del' + str(folder_id))
            
            new_template.setParmTemplates(contents)
            new_template.setLabel("Vis " + str(folder_id))

            group.replace(parm_template, new_template)

    node.setParmTemplateGroup(group)

def preset_menu(kwargs):
	importlib.reload(stain_menu)
	menu = stain_menu.menu
	return(menu)

def preset(kwargs):
	node = kwargs['node']
	name = kwargs['parm_name']
	presetParm = kwargs['parm']

	vis_id = name.replace('preset', '')
	
	presetVal = presetParm.evalAsString()
	
	print(presetVal)

	rampParm = node.parm('ramp' + vis_id)
	rampParm.set(getattr(stain_schemes, presetVal), None, False)