import networkx as nx
import matplotlib.pyplot as plt

def bulastir(graph):
    hastalar =[]
    for i in graph.nodes():
        if graph.nodes[i]['hasta'] == True:
            hastalar.append(i)
            for j in nx.neighbors(graph, i):
                hastalar.append(j)
    for nod in graph.nodes():
        if nod in hastalar:
            graph.nodes[nod]["hasta"] = True
    return graph

grevde = nx.watts_strogatz_graph(50,4,0)
grdisari = nx.watts_strogatz_graph(50,4,1)

nx.set_node_attributes(grevde,dict((i,False) for i in grevde.nodes()),'hasta')
nx.set_node_attributes(grdisari,dict((i,False) for i in grdisari.nodes()),'hasta')

grevde.nodes()[3]['hasta'] = True
grdisari.nodes()[3]['hasta'] = True

plt.figure(figsize=(10,10))
plt.subplot(2,3,1)
plt.title("t=0 - HOME" )
nodeColor = ["red" if grevde.nodes[i]['hasta'] == True else "blue" for i in grevde.nodes() ]
drawPos = nx.circular_layout(grevde)
nx.draw_networkx_edges(grevde, drawPos)
nx.draw_networkx_nodes(grevde,node_color=nodeColor ,pos=drawPos,node_size=53)

t1gr = bulastir(grevde)
plt.subplot(2,3,2)
plt.title("t=1 -HOME")
nodeColor = ["red" if t1gr.nodes[i]['hasta'] == True else "blue" for i in t1gr.nodes() ]
drawPos = nx.circular_layout(t1gr)
nx.draw_networkx_edges(t1gr, drawPos)
nx.draw_networkx_nodes(t1gr,node_color=nodeColor ,pos=drawPos,node_size=53)

t2gr = bulastir(t1gr)
plt.subplot(2,3,3)
plt.title("t=2 - HOME")
nodeColor = ["red" if t2gr.nodes[i]['hasta'] == True else "blue" for i in t2gr.nodes() ]
drawPos = nx.circular_layout(t2gr)
nx.draw_networkx_edges(t2gr, drawPos)
nx.draw_networkx_nodes(t2gr,node_color=nodeColor ,pos=drawPos,node_size=53)


plt.subplot(2,3,4)
plt.title("t=0 - OUT")
nodeColor = ["red" if grdisari.nodes[i]['hasta'] == True else "blue" for i in grdisari.nodes() ]
drawPos = nx.circular_layout(grdisari)
nx.draw_networkx_edges(grdisari, drawPos)
nx.draw_networkx_nodes(grdisari,node_color=nodeColor ,pos=drawPos,node_size=53)

t1gr = bulastir(grdisari)
plt.subplot(2,3,5)
plt.title("t=1 - OUT")
nodeColor = ["red" if t1gr.nodes[i]['hasta'] == True else "blue" for i in t1gr.nodes() ]
drawPos = nx.circular_layout(t1gr)
nx.draw_networkx_edges(t1gr, drawPos)
nx.draw_networkx_nodes(t1gr,node_color=nodeColor ,pos=drawPos,node_size=53)

t2gr = bulastir(t1gr)
plt.subplot(2,3,6)
plt.title("t=2 - OUT")
nodeColor = ["red" if t2gr.nodes[i]['hasta'] == True else "blue" for i in t2gr.nodes() ]
drawPos = nx.circular_layout(t2gr)
nx.draw_networkx_edges(t2gr, drawPos)
nx.draw_networkx_nodes(t2gr,node_color=nodeColor ,pos=drawPos,node_size=53)



plt.show()







