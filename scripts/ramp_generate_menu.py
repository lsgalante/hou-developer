node = kwargs['node']
geometry = node.geometry()
pts = geometry.pointAttribs()
dets = geometry.globalAttribs()

index_parm = node.parm('index')
index_parm.set(len(pts))

menu = []
for pt in pts:
	menu.append(pt.name())
	menu.append(pt.name())
menu.append('_separator_')
menu.append('_separator_')
for det in dets:
	menu.append(det.name())
	menu.append(det.name())
return(menu)