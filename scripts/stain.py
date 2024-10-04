import hou
import importlib
import stain_menu
import stain_schemes

##--initialize--##
def createdestroy_func(kwargs):
    node = kwargs['node']

    vistup = hou.viewportVisualizers.visualizers(
        hou.viewportVisualizerCategory.Node,
        node)

    ops = node.parm('vis').eval()

    for x in range(ops):
        if (x + 1) > len(vistup):
            vis = hou.viewportVisualizers.createVisualizer(
                hou.viewportVisualizers.type('vis_color'),
                hou.viewportVisualizerCategory.Node,
                node)

            vis.setIsActive(True, None)
            vis.setParm('colortype', 1)
            vis.setParm('rangespec', 1)
            vis.setParm('clamptype', 1)
            vis.setParm('colorramp', 0)

            presetParm = node.parm('preset' + str(x))
            presetStr = presetParm.evalAsString()

            rampParm = node.parm('ramp' + str(x))
            rampParm.set(getattr(stain_schemes, presetStr), None, False)
            rampRamp = rampParm.eval()

            vis.setParm('colorramp', rampRamp)

        if ops < len(vistup) and (x + 2) == len(vistup):
            vis = vistup[x + 1]
            vis.destroy()

    if ops == 0:
        vis = vistup[0]
        vis.destroy()
##--/initialize--##


##--global funcs--##
def enable_func(kwargs):
    node = kwargs['node']
    parm = kwargs['parm']
    index = kwargs['script_multiparm_index']

    vistup = hou.viewportVisualizers.visualizers(
        hou.viewportVisualizerCategory.Node,
        node)
    vis = vistup[int(index)]

    enable = parm.eval()
    if enable == 1:
        vis.setIsActive(True, None)
    if enable == 0:
        vis.setIsActive(False, None)

def attr_func(kwargs):
    node = kwargs['node']
    parm = kwargs['parm']
    index = kwargs['script_multiparm_index']

    vistup = hou.viewportVisualizers.visualizers(
        hou.viewportVisualizerCategory.Node,
        node)
    vis = vistup[int(index)]
    
    attr = parm.eval()
    vis.setParm('attrib', attr)
    vis.setLabel(attr)

def datatype_func(kwargs):
    node = kwargs['node']
    parm = kwargs['parm']
    index = kwargs['script_multiparm_index']

    vistypes = hou.viewportVisualizers.types()

    vistup = hou.viewportVisualizers.visualizers(
        hou.viewportVisualizerCategory.Node,
        node)
    vis = vistup[int(index)]

    type = parm.eval()
    
    if type == 0:
        vis.setType(vistypes[1])
    
    if type == 1:
        vis.setType(vistypes[0])
        vis.setParm('style', 4)
        coloring_func(kwargs)

def color_func(kwargs):
    node = kwargs['node']
    index = kwargs['script_multiparm_index']

    vistup = hou.viewportVisualizers.visualizers(
        hou.viewportVisualizerCategory.Node,
        node)
    vis = vistup[int(index)]
    
    colorr = node.parm('color' + index + 'r').eval()
    colorg = node.parm('color' + index + 'g').eval()
    colorb = node.parm('color' + index + 'b').eval()
    vis.setParm('markercolorr', colorr)
    vis.setParm('markercolorg', colorg)
    vis.setParm('markercolorb', colorb)
##--/global funcs--##


##--ramp funcs--##
def ramp_func(kwargs):
    node = kwargs['node']
    nesting = int(kwargs['script_multiparm_nesting'])
    index = 'undefined'

    vistup = hou.viewportVisualizers.visualizers(
        hou.viewportVisualizerCategory.Node,
        node)

    if nesting == 1:
        index = kwargs['script_multiparm_index']
    if nesting > 1:
        index = kwargs['script_multiparm_index2']

    indexInt = int(index)
    vis = vistup[indexInt]

    rampParm = node.parm('ramp' + index)
    rampData = rampParm.eval()
    vis.setParm('colorramp', rampData)

    importlib.reload(stain_menu)
    menu = stain_menu.menu
    return(menu)

def preset_func(kwargs):
    node = kwargs['node']
    index = kwargs['script_multiparm_index']

    vistup = hou.viewportVisualizers.visualizers(
        hou.viewportVisualizerCategory.Node,
        node)
    vis = vistup[int(index)]

    presetParm = node.parm('preset' + index)
    presetStr = presetParm.evalAsString()
    rampParm = node.parm('ramp' + index)
    rampData = rampParm.evalAsRamp()

    if presetStr == 'New...':
        newName = hou.ui.readInput("New Preset", ("Add", "Cancel"), hou.severityType.Message, 0, -1, None, None, 'Name...')
        
        if newName[0] == 0:
            find = str(stain_menu.menu).rfind(newName[1])

            if find == -1:
                menu = stain_menu.menu
                menu.insert(0, newName[1])
                menu.insert(0, newName[1])
                newMenu = 'menu = ' + str(menu)
                file = open('C:/Users/lucas/OneDrive/Git/morphogen/scripts/stain_menu.py', 'w')
                file.write(newMenu)
                file.close()
                importlib.reload(stain_menu)
                presetParm.set(0)

                basis = rampData.basis()
                basis = tuple('hou.' + str(x) for x in basis)
                basis = str(basis).replace("'", "")
                keys = rampData.keys()
                keys = tuple(round(x, 4) for x in keys)                
                values = rampData.values()
                values = tuple(tuple(round(x2, 4) for x2 in x) for x in values)
                newScheme = '\n' + newName[1] + '=hou.Ramp(' + str(basis) +',' + str(keys) + ',' + str(values) + ')'
                file = open(
                    'C:/Users/lucas/OneDrive/Git/morphogen/scripts/stain_schemes.py',
                    'a')
                file.write(newScheme)
                file.close()
                importlib.reload(stain_schemes)

            else:
                hou.ui.displayMessage('Already Exists')

    else:
        rampParm.set(getattr(stain_schemes, presetStr), None, False)
        ramp_func(kwargs)

def overwrite_func(kwargs):
    node = kwargs['node']
    index = kwargs['script_multiparm_index']

    vistup = hou.viewportVisualizers.visualizers(
        hou.viewportVisualizerCategory.Node,
        node)
    vis = vistup[int(index)]

    presetParm = node.parm('preset' + index)
    presetStr = presetParm.evalAsString()

    oldRamp = getattr(stain_schemes, presetStr)
    basis = oldRamp.basis()
    basis = tuple('hou.' + str(x) for x in basis)
    basis = str(basis).replace("'", "")
    keys = oldRamp.keys()
    keys = tuple(round(x, 4) for x in keys)                
    values = oldRamp.values()
    values = tuple(tuple(round(x2, 4) for x2 in x) for x in values)
    oldScheme = presetStr + '=hou.Ramp(' + str(basis) +',' + str(keys) + ',' + str(values) + ')'

    rampParm = node.parm('ramp' + index)
    newRamp = rampParm.evalAsRamp()
    basis = newRamp.basis()
    basis = tuple('hou.' + str(x) for x in basis)
    basis = str(basis).replace("'", "")
    keys = newRamp.keys()
    keys = tuple(round(x, 4) for x in keys)                
    values = newRamp.values()
    values = tuple(tuple(round(x2, 4) for x2 in x) for x in values)
    newScheme = presetStr + '=hou.Ramp(' + str(basis) +',' + str(keys) + ',' + str(values) + ')'

    file = open('C:/Users/lucas/OneDrive/Git/morphogen/scripts/stain_schemes.py', 'r')
    fileStr = file.read()
    file.close()

    newStr = fileStr.replace(oldScheme, newScheme)

    file = open('C:/Users/lucas/OneDrive/Git/morphogen/scripts/stain_schemes.py', 'w')
    file.write(newStr)
    file.close()
    importlib.reload(stain_schemes)

def delete_func(kwargs):
    node = kwargs['node']
    index = kwargs['script_multiparm_index']

    vistup = hou.viewportVisualizers.visualizers(
        hou.viewportVisualizerCategory.Node,
        node)
    vis = vistup[int(index)]

    presetParm = node.parm('preset' + index)
    presetStr = presetParm.evalAsString()
    presetInt = presetParm.evalAsInt()
    menu = stain_menu.menu
    menu.remove(presetStr)
    menu.remove(presetStr)
    newMenu = 'menu=' + str(menu)
    file = open(
        'C:/Users/lucas/OneDrive/Git/morphogen/scripts/stain_menu.py',
        'w')
    file.write(newMenu)
    file.close()
    importlib.reload(stain_menu)
    presetParm.set(0)

    rampRamp = getattr(stain_schemes, presetStr)
    basis = rampRamp.basis()
    basis = tuple('hou.' + str(x) for x in basis)
    basis = str(basis).replace("'", "")
    keys = rampRamp.keys()
    keys = tuple(round(x, 4) for x in keys)                
    values = rampRamp.values()
    values = tuple(tuple(round(x2, 4) for x2 in x) for x in values)

    scheme = presetStr + '=hou.Ramp(' + str(basis) + ',' + str(keys) + ',' + str(values) + ')'

    file = open(
        'C:/Users/lucas/OneDrive/Git/morphogen/scripts/stain_schemes.py',
        'r')
    fileStr = file.read()
    file.close()

    newStr = fileStr.replace(scheme, '')

    file = open(
        'C:/Users/lucas/OneDrive/Git/morphogen/scripts/stain_schemes.py',
        'w')
    file.write(newStr)
    file.close()

    preset_func(kwargs)

##--/ramp funcs--##


##--float funcs--##
def rampattr_func(kwargs):
    node = kwargs['node']
    parm = kwargs['node']
    index = kwargs['script_multiparm_index']
    vistup = hou.viewportVisualizers.visualizers(
        hou.viewportVisualizerCategory.Node,
        node)
    vis = vistup[int(index)]
    rampattr = parm.eval()
    vis.setParm('attrib', rampattr)
##--/float funcs--##


##--vec funcs--##
def coloring_func(kwargs):
    node = kwargs['node']
    parm = kwargs['parm']
    index = kwargs['script_multiparm_index']
    vistup = hou.viewportVisualizers.visualizers(
        hou.viewportVisualizerCategory.Node,
        node)
    vis = vistup[int(index)]
    coloring = node.parm('coloring' + index).eval()
    vis.setParm('vectorcoloring', coloring)
    if coloring == 0:
        color_func(kwargs)
    if coloring != 0:
        vis.setParm('ramptype', 6)
        vis.setParm('rangespec', 0 )
    if coloring == 3:
        colorattr_func(kwargs)

def lengthscale_func(kwargs):
    node = kwargs['node']
    parm = kwargs['parm']
    index = kwargs['script_multiparm_index']
    vistup = hou.viewportVisualizers.visualizers(
        hou.viewportVisualizerCategory.Node,
        node)
    vis = vistup[int(index)]
    lengthscale = parm.eval()
    vis.setParm('lengthscale', lengthscale)

def colorattr_func(kwargs):
    node = kwargs['node']
    index = kwargs['script_multiparm_index']
    vistup = hou.viewportVisualizers.visualizers(
        hou.viewportVisualizerCategory.Node,
        node)
    vis = vistup[int(index)]
    colorattr = node.parm('colorattr' + index).eval()
    vis.setParm('colorattrib', colorattr)
##--/vec funcs--##

