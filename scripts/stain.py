import hou

from colorschemes import *

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
    index = int(kwargs["script_multiparm_index"])

    vistup = hou.viewportVisualizers.visualizers(
        hou.viewportVisualizerCategory.Node,
        node
    )

    vis = vistup[index]
    enable = parm.eval()

    if enable == 1:
        vis.setIsActive(True, None)
    if enable == 0:
        vis.setIsActive(False, None)

def attr_func(kwargs):
    node = kwargs["node"]
    parm = kwargs["parm"]
    index = int(kwargs["script_multiparm_index"])

    vistup = hou.viewportVisualizers.visualizers(
        hou.viewportVisualizerCategory.Node,
        node
    )

    vis = vistup[index]
    attr = parm.eval()
    vis.setParm("attrib", attr)
    vis.setLabel(attr)

def datatype_func(kwargs):
    node = kwargs["node"]
    parm = kwargs["parm"]
    index = int(kwargs["script_multiparm_index"])

    vistypes = hou.viewportVisualizers.types()

    vistup = hou.viewportVisualizers.visualizers(
        hou.viewportVisualizerCategory.Node,
        node
    )

    vis = vistup[index]
    type = parm.eval()

    if type == 0:
        vis.setType(vistypes[1])
        color_func(kwargs)

    if type == 1:
        vis.setType(vistypes[0])
        vis.setParm("style", 4)
        coloring_func(kwargs)

def colorramp_func(kwargs):
    node = kwargs["node"]

    preset = node.parm("preset" + str(x)).eval()

def ramppreset_func(kwargs):

    node = kwargs["node"]

    vistup = hou.viewportVisualizers.visualizers(
        hou.viewportVisualizerCategory.Node,
        node
    )

    nvis = len(vistup)

    for x in range(nvis):
        vis = vistup[x]

        presetval = node.parm("preset" + str(x)).eval()

        rampparm = node.parm("ramp" + str(x))

        if presetval == 0:
            rampparm.set(candypeach, None, False)

        if presetval == 1:
            rampparm.set(blacktoorange, None, False)

        if presetval == 2:
            rampparm.set(blackbody, None, False)

        if presetval == 3:
            rampparm.set(cividis, None, False)

        if presetval == 4:
            rampparm.set(grayscale, None, False)

        if presetval == 5:
            rampparm.set(inferno, None, False)

        if presetval == 6:
            rampparm.set(infrared, None, False)

        if presetval == 7:
            rampparm.set(magma, None, False)

        if presetval == 8:
            rampparm.set(plasma, None, False)

        if presetval == 9:
            rampparm.set(sand, None, False)

        if presetval == 10:
            rampparm.set(twilight, None, False)

        if presetval == 11:
            rampparm.set(twilightshifted, None, False)

        if presetval == 12:
            rampparm.set(twotone, None, False)

        if presetval == 13:
            rampparm.set(viridis, None, False)

        if presetval == 14:
            rampparm.set(whitetored, None, False)

        if presetval == 15:
            rampparm.set(whitewater, None, False)

        ramp = rampparm.eval()

        vis.setParm("colorramp", ramp)

def rampedit(kwargs):

    node = kwargs["node"]

    vistup = hou.viewportVisualizers.visualizers(
        hou.viewportVisualizerCategory.Node,
        node
    )

    nvis = len(vistup)

    for x in range(nvis):

        vis = vistup[x]

        ramp = node.parm("ramp" + str(x)).eval()

        vis.setParm("colorramp", ramp)

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

def colorattr(kwargs):
    node = kwargs["node"]
    vistup = hou.viewportVisualizers.visualizers(
        hou.viewportVisualizerCategory.Node,
        node
    )

    nvis = len(vistup)

    for x in range(nvis):

        vis = vistup[x]
       
        colorattr = node.parm("colorattr" + str(x)).eval()

        vis.setParm("colorattrib", colorattr)
####------------------------------global funcs------------------------------####

####------------------------------float funcs------------------------------####
def rampattr_func(kwargs):
    node = kwargs["node"]
    parm = kwargs["node"]
    index = int(kwargs["script_multiparm_index"])

    vistup = hou.viewportVisualizers.visualizers(
        hou.viewportVisualizerCategory.Node,
        node
    )

    vis = vistup[index]
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

def lengthscale_func(kwargs):
    node = kwargs["node"]
    parm = kwargs["parm"]
    index = int(kwargs["script_multiparm_index"])
    vistup = hou.viewportVisualizers.visualizers(
        hou.viewportVisualizerCategory.Node,
        node
    )
    vis = vistup[index]
    lengthscale = parm.eval()
    vis.setParm("lengthscale", lengthscale)
####------------------------------vec funcs------------------------------####

