import networkx as nx
import matplotlib.pyplot as plt

gr = nx.Graph()


gr.add_nodes_from(['İstanbul','Ankara','İzmir','Edirne','Kudüs','Berlin','Kahire'])

gr.nodes['Ankara']['ichat'] = True
gr.nodes['İzmir']['ichat'] = True
gr.nodes['Edirne']['ichat'] = True
gr.nodes['İstanbul']['ichat'] = True
gr.nodes['Berlin']['ichat'] = False
gr.nodes['Kahire']['ichat'] = False
gr.nodes['Kudüs']['ichat'] = False

nodeColor = ['#1f78b4' if gr.nodes[v]['ichat'] == True
             else '#33a02c' for v in gr]


gr.add_edge('İstanbul', 'Ankara')
gr.add_edges_from([('İstanbul','İzmir'),('Edirne','Ankara'),('Ankara','İzmir')])
gr.add_edges_from([('İstanbul','Kahire'),('Edirne','Berlin'),('Kahire','Kudüs')])

gr.edges['İstanbul','İzmir']['dakika'] = 60
gr.edges['İstanbul','Ankara']['dakika'] = 30
gr.edges['Edirne','Ankara']['dakika'] = 40
gr.edges['Ankara','İzmir']['dakika'] = 20
gr.edges['İstanbul','Kahire']['dakika'] = 160
gr.edges['Edirne','Berlin']['dakika'] = 260
gr.edges['Kahire','Kudüs']['dakika'] = 60

weigthEdge = [gr.edges[v,w]['dakika'] /10 for v,w in gr.edges]

drawPos = nx.spring_layout(gr, weight="weigth", k = 0.3)
print(weigthEdge)
nx.draw_networkx(gr, pos=drawPos, width=10, edge_color=weigthEdge, edge_cmap = plt.cm.Reds,edge_vmin = 0, edge_vmax = 6)
plt.show()
