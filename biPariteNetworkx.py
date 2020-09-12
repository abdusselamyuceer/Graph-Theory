from networkx.algorithms import bipartite
import matplotlib.pyplot as plt
import  networkx as nx

gr = nx.Graph()

gr.add_node('İstanbul')
gr.add_nodes_from(['Ankara','İzmir','Edirne','Kahire'])
gr.add_node('Kudüs', ichat = False)

gr.nodes['Ankara']['ichat'] = True
gr.nodes['İzmir']['ichat'] = True
gr.nodes['Edirne']['ichat'] = True
gr.nodes['İstanbul']['ichat'] = True
gr.nodes['Kahire']['ichat'] = False
gr.nodes['Kudüs']['ichat'] = False

for i in gr.nodes():
    gr.nodes[i]["sehir"] = True

lstfirma = ['A','B','S','D','F']
gr.add_nodes_from(lstfirma)

for j in lstfirma:
    gr.nodes[j]["sehir"]=False
    gr.nodes[j]["ichat"]=False

print(gr.nodes['Kudüs'])

nodeColor = ['#1f78b4' if gr.nodes[v]['ichat'] == True
             else '#33a02c' for v in gr]

gr.add_edge('A', 'Ankara')
gr.add_edges_from([('S','İzmir'),('S','Ankara'),('D','İzmir'),('D','İstanbul'),('D','Edirne')])
gr.add_edges_from([('F','Kahire'),('A','İzmir'),('B','Kudüs'),('A','Kahire'),('S','Kudüs')])
drawPos = nx.spring_layout(gr)
sehir, firma = bipartite.sets(gr)
print(nx.is_bipartite(gr))
nx.draw_networkx_nodes(sehir,drawPos, node_color = "blue",node_shape="h")
nx.draw_networkx_nodes(firma,drawPos, node_color = "yellow",node_shape="d")
nx.draw_networkx_edges(gr,drawPos, edge_color = "brown")
nx.draw_networkx_labels(gr,drawPos)
plt.gca().margins(0.15,0.15)
plt.show()

projGr=bipartite.projected_graph(gr,firma)

nx.draw_networkx_nodes(firma,drawPos, node_color = "blue",node_shape="h",alpha=0.5)
nx.draw_networkx_edges(projGr,drawPos, edge_color = "brown",width=3, alpha=0.2)
nx.draw_networkx_labels(projGr,drawPos)
plt.gca().margins(0.15,0.15)
plt.show()

projGr=bipartite.projected_graph(gr,sehir)

nx.draw_networkx_nodes(sehir,drawPos, node_color = "blue",node_shape="h",alpha=0.5)
nx.draw_networkx_edges(projGr,drawPos, edge_color = "brown",width=3, alpha=0.2)
nx.draw_networkx_labels(projGr,drawPos)
plt.gca().margins(0.15,0.15)
plt.show()
