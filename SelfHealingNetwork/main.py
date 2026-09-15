import networkx as nx
import matplotlib.pyplot as plt

# ==========================================
# SELF-HEALING NETWORK SIMULATOR
# ==========================================

# Create the network
G = nx.Graph()

# Add devices
nodes = ["PC", "R1", "R2", "R3", "R4", "Server"]
G.add_nodes_from(nodes)

# Add network connections
edges = [
    ("PC", "R1"),
    ("PC", "R3"),
    ("R1", "R2"),
    ("R3", "R4"),
    ("R2", "Server"),
    ("R4", "Server"),
    ("R1", "R3"),
    ("R2", "R4")
]

G.add_edges_from(edges)

# Fixed positions for devices
pos = {
    "PC": (0, 1),
    "R1": (1, 2),
    "R3": (1, 0),
    "R2": (3, 2),
    "R4": (3, 0),
    "Server": (4, 1)
}

# ==========================================
# NORMAL NETWORK
# ==========================================

normal_path = nx.shortest_path(
    G,
    source="PC",
    target="Server"
)

print("\n========================================")
print(" SELF-HEALING NETWORK SIMULATOR")
print("========================================")

print("\nNORMAL NETWORK STATUS: ONLINE")
print("Normal Route:")
print(" → ".join(normal_path))

# ==========================================
# SIMULATE ROUTER FAILURE
# ==========================================

failed_router = "R2"

print("\n----------------------------------------")
print(f"ROUTER FAILURE DETECTED: {failed_router}")
print("----------------------------------------")

# Remove failed router
G.remove_node(failed_router)

# ==========================================
# AUTOMATIC ROUTE RECOVERY
# ==========================================

try:
    new_path = nx.shortest_path(
        G,
        source="PC",
        target="Server"
    )

    print("\nSEARCHING FOR ALTERNATIVE ROUTE...")
    print("NEW ROUTE FOUND:")
    print(" → ".join(new_path))

    print("\nCONNECTION RESTORED SUCCESSFULLY!")

except nx.NetworkXNoPath:

    new_path = []

    print("\nNO ALTERNATIVE ROUTE AVAILABLE")
    print("CONNECTION FAILED")

# ==========================================
# VISUAL NETWORK DISPLAY
# ==========================================

plt.figure(figsize=(10, 6))

# Active nodes
active_nodes = list(G.nodes())

# Draw normal active network
nx.draw_networkx_edges(
    G,
    pos,
    edge_color="gray",
    width=2
)

# Draw active nodes
nx.draw_networkx_nodes(
    G,
    pos,
    nodelist=active_nodes,
    node_size=2500,
    node_color="lightblue"
)

# Draw failed router separately
nx.draw_networkx_nodes(
    nx.Graph(),
    pos,
    nodelist=[failed_router],
    node_size=2500,
    node_color="red"
)

# Draw labels
nx.draw_networkx_labels(
    G,
    pos,
    font_size=11,
    font_weight="bold"
)

# Label for failed router
plt.text(
    pos[failed_router][0],
    pos[failed_router][1],
    failed_router + "\nFAILED",
    horizontalalignment="center",
    verticalalignment="center",
    fontweight="bold"
)

# Highlight recovered route
if new_path:
    path_edges = list(zip(new_path, new_path[1:]))

    nx.draw_networkx_edges(
        G,
        pos,
        edgelist=path_edges,
        edge_color="green",
        width=5
    )

plt.title(
    "Self-Healing Network - Router R2 Failed | Alternative Route Activated",
    fontsize=13,
    fontweight="bold"
)

plt.axis("off")
plt.show()