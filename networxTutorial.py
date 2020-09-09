import networkx as nx
import matplotlib.pyplot as plt

gr = nx.Graph()

gr.add_node('İstanbul')
gr.add_nodes_from(['Ankara','İzmir','Edirne','Berlin','Kahire'])
gr.add_node('Kudüs', ichat = False)

gr.nodes['Ankara']['ichat'] = True
gr.nodes['İzmir']['ichat'] = True
gr.nodes['Edirne']['ichat'] = True
gr.nodes['İstanbul']['ichat'] = True
gr.nodes['Berlin']['ichat'] = False
gr.nodes['Kahire']['ichat'] = False
gr.nodes['Kudüs']['ichat'] = False

print(gr.nodes['Kudüs'])

nodeColor = ['#1f78b4' if gr.nodes[v]['ichat'] == True
             else '#33a02c' for v in gr]


gr.add_edge('İstanbul', 'Ankara')
gr.add_edges_from([('İstanbul','İzmir'),('Edirne','Ankara'),('Ankara','İzmir')])
gr.add_edges_from([('İstanbul','Kahire'),('Edirne','Berlin'),('Kahire','Kudüs')])

for v,w in gr.edges:
    if gr.nodes[v]['ichat'] == True and gr.nodes[w]['ichat'] == True:
        gr.edges[v,w]['icucus'] = True
    else:
        gr.edges[v,w]['icucus'] = False

lsticucus = [i for i in gr.edges if gr.edges[i]['icucus'] == True]
lstdisucus = [i for i in gr.edges if gr.edges[i]['icucus'] == False]

print(gr.edges)
print(gr.nodes)

print('Muğla' in gr)
print (gr.has_node('Muğla'))

print(('İstanbul','Ankara') in gr.edges)
print(gr.has_edge('İstanbul','Ankara'))

print(list(gr.neighbors('İstanbul')))

drawPos = nx.spring_layout(gr,k =0.3)
plt.figure(figsize=(7.5, 7.5))
nx.draw_networkx_nodes(gr, drawPos,label =True, node_color=nodeColor)
nx.draw_networkx_edges(gr,drawPos,edgelist=lstdisucus)
nx.draw_networkx_edges(gr,drawPos,edgelist=lsticucus, style="dashed")
nx.draw_networkx_labels(gr,drawPos)
plt.show()
