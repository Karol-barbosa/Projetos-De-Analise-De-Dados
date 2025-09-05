import medical_data_visualizer

# Gera e salva o catplot
fig1 = medical_data_visualizer.draw_cat_plot()
fig1.savefig('catplot.png')

# Gera e salva o heatmap
fig2 = medical_data_visualizer.draw_heat_map()
fig2.savefig('heatmap.png')
