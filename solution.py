cpol_Radar = pyart.io.read('data/Gunn_pt_20060120005000ppi.nc')
cpol_map = pyart.graph.RadarMapDisplayCartopy(cpol_Radar)
fig, ax = plt.subplots(1, 2, figsize=(8, 6))
cpol_map.plot_ppi_map('reflectivity', sweep=1, vmin=0., vmax=60., 
                      ax=ax[0], resolution='10m', cmap=pyart.graph.cm.NWSRef)
fig, ax = plt.subplots(1, 2, figsize=(8, 6))
cpol_map.plot_ppi_map('corrected_velocity', sweep=1, vmin=-20, vmax=20.,
                      ax=ax[1], resolution='10m', cmap=pyart.graph.cm.NWSVel)
