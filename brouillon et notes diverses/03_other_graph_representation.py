import networkx as nx
import plotly.graph_objects as go


def construct_overlap_network(Patterns):
    G = nx.DiGraph()
    G.add_nodes_from(Patterns)

    for i, Pattern in enumerate(Patterns):
        for j, Pattern_prime in enumerate(Patterns):
            if i == j:
                continue
            if Suffix(Pattern) == Prefix(Pattern_prime):
                G.add_edge(Pattern, Pattern_prime)

    return G


def plot_graph(G):
    pos = nx.spring_layout(G)  # positions for all nodes
    edges = G.edges()
    edge_x = []
    edge_y = []

    for edge in edges:
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.append(x0)
        edge_x.append(x1)
        edge_x.append(None)  # to break line between edges
        edge_y.append(y0)
        edge_y.append(y1)
        edge_y.append(None)

    node_x = []
    node_y = []
    for node in G.nodes():
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)

    # Create the figure
    fig = go.Figure()

    # Add edges to the figure
    fig.add_trace(
        go.Scatter(
            x=edge_x,
            y=edge_y,
            line=dict(width=0.5, color="#888"),
            hoverinfo="none",
            mode="lines",
        )
    )

    # Add nodes to the figure
    fig.add_trace(
        go.Scatter(
            x=node_x,
            y=node_y,
            mode="markers+text",
            marker=dict(
                showscale=True, colorscale="YlGnBu", size=10, color=[], line_width=2
            ),
            text=list(G.nodes()),
            textposition="top center",
        )
    )

    fig.update_layout(
        title="Overlap Graph",
        titlefont_size=16,
        showlegend=False,
        hovermode="closest",
        margin=dict(b=0, l=0, r=0, t=40),
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
    )

    fig.show()


# Create and plot the graph
G = construct_overlap_network(testseq)
plot_graph(G)
