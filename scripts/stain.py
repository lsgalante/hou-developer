import hou

from colorschemes import *
# from overwrite import *

def createdestroy_func(kwargs):
    node = kwargs["node"]
    vistup = hou.viewportVisualizers.visualizers(
        hou.viewportVisualizerCategory.Node,
        node
    )
    ops = node.parm("vis").eval()
    for x in range(ops):
        if (x + 1) > len(vistup):        
            vis = hou.viewportVisualizers.createVisualizer(
                hou.viewportVisualizers.type("vis_color"),
                hou.viewportVisualizerCategory.Node,
                node
            )
            vis.setIsActive(True, None)
            vis.setParm("colortype", 1)
            vis.setParm("rangespec", 1)
            vis.setParm("clamptype", 1)
            vis.setParm("colorramp", candypeach)
            ramp = node.parm("ramp" + str(x))
            ramp.set(candypeach, None, False)
        if ops < len(vistup) and (x + 2) == len(vistup):
            vis = vistup[x + 1]
            vis.destroy()
    if ops == 0:
        vis = vistup[0]
        vis.destroy()

####------------------------------global funcs------------------------------####
def enable_func(kwargs):
    node = kwargs["node"]
    parm = kwargs["parm"]
    index = kwargs["script_multiparm_index"]
    vistup = hou.viewportVisualizers.visualizers(
        hou.viewportVisualizerCategory.Node,
        node
    )
    vis = vistup[int(index)]
    enable = parm.eval()
    if enable == 1:
        vis.setIsActive(True, None)
    if enable == 0:
        vis.setIsActive(False, None)

def attr_func(kwargs):
    node = kwargs["node"]
    parm = kwargs["parm"]
    index = kwargs["script_multiparm_index"]
    vistup = hou.viewportVisualizers.visualizers(
        hou.viewportVisualizerCategory.Node,
        node
    )
    vis = vistup[int(index)]
    attr = parm.eval()
    vis.setParm("attrib", attr)
    vis.setLabel(attr)

def datatype_func(kwargs):
    node = kwargs["node"]
    parm = kwargs["parm"]
    index = kwargs["script_multiparm_index"]
    vistypes = hou.viewportVisualizers.types()
    vistup = hou.viewportVisualizers.visualizers(
        hou.viewportVisualizerCategory.Node,
        node
    )
    vis = vistup[int(index)]
    type = parm.eval()
    if type == 0:
        vis.setType(vistypes[1])
    if type == 1:
        vis.setType(vistypes[0])
        vis.setParm("style", 4)
        coloring_func(kwargs)

def preset_func(kwargs):
    node = kwargs["node"]
    index = kwargs["script_multiparm_index"]
    vistup = hou.viewportVisualizers.visualizers(
        hou.viewportVisualizerCategory.Node,
        node
    )
    vis = vistup[int(index)]
    preset = node.parm("preset" + index).eval()
    ramp = node.parm("ramp" + index)
    if preset == 0:
        ramp.set(candypeach, None, False)
    if preset == 1:
        ramp.set(blacktoorange, None, False)
    if preset == 2:
        ramp.set(blackbody, None, False)
    if preset == 3:
        ramp.set(cividis, None, False)
    if preset == 4:
        ramp.set(grayscale, None, False)
    if preset == 5:
        ramp.set(inferno, None, False)
    if preset == 6:
        ramp.set(infrared, None, False)
    if preset == 7:
        ramp.set(magma, None, False)
    if preset == 8:
        ramp.set(plasma, None, False)
    if preset == 9:
        ramp.set(sand, None, False)
    if preset == 10:
        ramp.set(twilight, None, False)
    if preset == 11:
        ramp.set(twilightshifted, None, False)
    if preset == 12:
        ramp.set(twotone, None, False)
    if preset == 13:
        ramp.set(viridis, None, False)
    if preset == 14:
        ramp.set(whitetored, None, False)
    if preset == 15:
        ramp.set(whitewater, None, False)
    ramp = ramp.eval()
    vis.setParm("colorramp", ramp)

def ramp_func(kwargs):
    node = kwargs["node"]
    nesting = int(kwargs["script_multiparm_nesting"])
    vistup = hou.viewportVisualizers.visualizers(
        hou.viewportVisualizerCategory.Node,
        node
    )
    index = "undefined"
    if nesting == 1:
        index = kwargs["script_multiparm_index"]
    if nesting > 1:
        index = kwargs["script_multiparm_index2"]
    indexint = int(index)
    vis = vistup[indexint]
    ramp = node.parm("ramp" + index).eval()
    vis.setParm("colorramp", ramp)

def overwrite_func(kwargs):
    node = kwargs["node"]
    index = kwargs["script_multiparm_index"]
    ramp = node.parm("ramp" + index).eval()
    preset = str(node.parm("preset" + index).evalAsString())
    scheme = "candypeach = hou.Ramp(" + str(ramp.basis()) + ", " + str(ramp.keys()) + ", " + str(ramp.values()) + ") \n"
    # with open("C:/Users/lucas/OneDrive/Git/morphogen/scripts/overwrite.py", "a") as append:
    #     append.write(scheme)
    test = hou.ui.readInput("Overwrite Preset?", ("Yes", "Cancel"), hou.severityType.Message, 0, -1, None, None, preset)

def color_func(kwargs):
    node = kwargs["node"]
    vistup = hou.viewportVisualizers.visualizers(
        hou.viewportVisualizerCategory.Node,
        node
    )
    index = kwargs["script_multiparm_index"]
    colorr = node.parm("color" + index + "r").eval()
    colorg = node.parm("color" + index + "g").eval()
    colorb = node.parm("color" + index + "b").eval()
    vis = vistup[int(index)]
    vis.setParm("markercolorr", colorr)
    vis.setParm("markercolorg", colorg)
    vis.setParm("markercolorb", colorb)
####------------------------------global funcs------------------------------####


####------------------------------float funcs------------------------------####
def rampattr_func(kwargs):
    node = kwargs["node"]
    parm = kwargs["node"]
    index = kwargs["script_multiparm_index"]
    vistup = hou.viewportVisualizers.visualizers(
        hou.viewportVisualizerCategory.Node,
        node
    )
    vis = vistup[int(index)]
    rampattr = parm.eval()
    vis.setParm("attrib", rampattr)
####------------------------------float funcs------------------------------####


####------------------------------vec funcs------------------------------####
def coloring_func(kwargs):
    node = kwargs["node"]
    parm = kwargs["parm"]
    index = kwargs["script_multiparm_index"]
    vistup = hou.viewportVisualizers.visualizers(
        hou.viewportVisualizerCategory.Node,
        node
    )
    vis = vistup[int(index)]
    coloring = node.parm("coloring" + index).eval()
    vis.setParm("vectorcoloring", coloring)
    if coloring == 0:
        color_func(kwargs)
    if coloring != 0:
        vis.setParm("ramptype", 6)
        vis.setParm("rangespec", 0 )
    if coloring == 3:
        colorattr_func(kwargs)

def lengthscale_func(kwargs):
    node = kwargs["node"]
    parm = kwargs["parm"]
    index = kwargs["script_multiparm_index"]
    vistup = hou.viewportVisualizers.visualizers(
        hou.viewportVisualizerCategory.Node,
        node
    )
    vis = vistup[int(index)]
    lengthscale = parm.eval()
    vis.setParm("lengthscale", lengthscale)

def colorattr_func(kwargs):
    node = kwargs["node"]
    index = kwargs["script_multiparm_index"]
    vistup = hou.viewportVisualizers.visualizers(
        hou.viewportVisualizerCategory.Node,
        node
    )
    vis = vistup[int(index)]
    colorattr = node.parm("colorattr" + index).eval()
    vis.setParm("colorattrib", colorattr)
####------------------------------vec funcs------------------------------####

