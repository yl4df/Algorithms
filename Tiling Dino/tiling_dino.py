# CS4102 Spring 2020 -- Homework 8
#################################
# Collaboration Policy: You are encouraged to collaborate with up to 4 other
# students, but all work submitted must be your own independently written
# solution. List the computing ids of all of your collaborators in the comment
# at the top of your java or python file. Do not seek published or online
# solutions for any assignments. If you use any published or online resources
# (which may not include solutions) when completing this assignment, be sure to
# cite them. Do not submit a solution that you are unable to explain orally to a
# member of the course staff.
#################################
# Your Computing ID: yl4df
# Collaborators: mw5ew
# Sources: Introduction to Algorithms, Cormen; Piazza Thread @644; Lecture Slides; networkx documentation
#################################
import networkx as nx
class TilingDino:
    def __init__(self):
        return

    # This is the method that should set off the computation
    # of tiling dino.  It takes as input a list lines of input
    # as strings.  You should parse that input, find a tiling,
    # and return a list of strings representing the tiling
    #
    # @return the list of strings representing the tiling
    def compute(self, lines):
        nrows = len(lines)
        ncols = len(lines[0])
        black=[]
        white=[]
        G=nx.DiGraph()
        #residual=nx.DiGraph()
        # Insert nodes to grapg and residual. Make them black/white according to their index, like chessboard.
        for i in range(0,nrows):
            for j in range(0,ncols):
                if (lines[i][j]=='#'):
                    #G.add_node((i,j))
                    #residual.add_node(((i,j)))
                    # node is white if i and j are both odd or even
                    if((i+j)%2==0):
                        white.append((i,j))
                    # node is black if exactly one of i and j is odd or even.
                    elif(not (i+j)%2==0):
                        black.append((i,j))
        # Always return impossible if #black is unequal to #white.
        if (not len(white)==len(black)):
            return ["impossible"]
        if (len(white)==0):
            return ["impossible"]

        G.add_nodes_from(white, bipartite=0)
        G.add_nodes_from(black, bipartite=1)

        # Build edge in G and residual based on whether they are adjacent.
        # In G, an edge is added between node if they are adjacent on board. Then build residual accordingly.
        for node1 in white:
            for node2 in self.adjacent(node1, G):
                G.add_edge(node1, node2, capacity=1)
                # residual.add_edge(node1, node2, weight=1)
                # residual.add_edge(node2, node1, weight=0)
        top_nodes = {n for n, d in G.nodes(data=True) if d['bipartite']==0}

        # Build max flow by adding source and sink. It looks like source -> white-> black -> sink.
        '''
        G.add_node('s')
        for wnode in white:
                G.add_edge('s', wnode, capacity=1)
                residual.add_edge('s', wnode, weight=1)
                residual.add_edge(wnode, 's', weight=0)
        G.add_node('t')
        for bnode in black:
                G.add_edge(bnode, 't', capacity=1)
                residual.add_edge('t', bnode, weight=0)
                residual.add_edge(bnode, 't', weight=1)
        '''
        # Calculate max flow. If max flow = # white nodes = # black nodes, tiling can be completed.
        # mflow = self.maxFlow(residual, 's', 't')
        flow_dict = nx.bipartite.maximum_matching(G, top_nodes=top_nodes)
        if (len(flow_dict)==2*len(white)):
            return self.getPath(flow_dict, white)
                #self.getPath(residual,'s')
        else:
            return ["impossible"]

    # Helper method to get adjacent nodes
    def adjacent(self, node, G):
        adj=[]
        if G.has_node((node[0]-1,node[1])):
            adj.append((node[0]-1,node[1]))
        if G.has_node((node[0]+1,node[1])):
            adj.append((node[0]+1,node[1]))
        if G.has_node((node[0],node[1]-1)):
            adj.append((node[0],node[1]-1))
        if G.has_node((node[0],node[1]+1)):
            adj.append((node[0],node[1]+1))
        return adj

    # Method to calculate the max flow by using Ford-Fulkerson Algorithm
    '''
    def maxFlow(self, graph, source, sink):
        mflow = 0
        # A dictionary data structure used to store parent-kid relationship between nodes.
        parent = {}
        for node in graph:
            parent[node] = ()
        # Use BFS to find augmenting path
        while self.BFS(graph, source, sink, parent):
            mflow = mflow+1
            v = sink
            while(not v == source):
                u = parent[v]
                graph[v][u]['weight'] += 1
                graph[u][v]['weight'] -= 1
                v = u
        return mflow
    '''

    # Modified BFS to find augmenting path
    '''
    def BFS(self, graph, s, t, parent):
        queue=[]
        visited =[]
        queue.append(s)
        visited.append(s)
        while queue:
            u = queue.pop(0)
            for node, atr in graph[u].items():
                if (node not in visited) and (atr['weight'] > 0) :
                    queue.append(node)
                    visited.append(node)
                    parent[node] = u
        return True if t in visited else False
    '''

    # Helper Menthod to get ideal output
    '''
    def getPath(self, graph, source):
        tiling = []
        for wnode, watr in graph[source].items():
            if watr['weight'] == 0:
                for bnode, batr in graph[wnode].items():
                    if batr['weight'] == 0:
                        tiling.append(str(bnode[1]) + ' ' + str(bnode[0]) + ' ' + str(wnode[1]) + ' ' + str(wnode[0]))
        return tiling
    '''
    # Helper Menthod to get ideal output
    def getPath(self, flow_dict, white):
         tiling = []
         for key in flow_dict:
             if key in white:
                tiling.append(str(flow_dict[key][1])+' '+str(flow_dict[key][0])+' '+str(key[1])+' '+str(key[0]))
         return tiling
