
# Usar para baixar repositorio
# import pandas as pd

# url = "https://raw.githubusercontent.com/danielpm1982/sample-social-network-analysis/master/karate.csv"
# karate_df = pd.read_csv(url, sep=";")
# karate_df.to_csv("karate.csv", sep=";", index=False)

# Imports
from igraph import Graph, plot
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Carregando dados
karate_df = pd.read_csv("karate.csv", sep=";")
g = Graph.DataFrame(karate_df, directed=False)

# Plot básico com rótulo e tamanho proporcional à betweenness
vertex_label_list = [i for i in range(34)]
vertex_size_list = [i / 3 for i in g.betweenness()]
plot(g, bbox=(700, 1200), vertex_label=vertex_label_list, vertex_color="cyan", vertex_size=vertex_size_list)

# Estatísticas da rede
def network_statistics(network_graph, node_id_list):
    df = pd.DataFrame({"node_id": node_id_list})
    df["degree"] = network_graph.degree()
    df["cc"] = network_graph.transitivity_local_undirected()
    df["closeness"] = network_graph.closeness()
    df["betweenness"] = network_graph.betweenness()
    df["bridge"] = df["node_id"].isin(network_graph.articulation_points()).astype(int)
    return df

network_statistics_df = network_statistics(g, list(range(g.vcount())))
print(network_statistics_df.head())

# Detectando comunidades com algoritmo multilevel (Louvain)
community_multilevel = g.community_multilevel()
print(f"Modularidade: {community_multilevel.modularity}")
print(f"Número de comunidades: {len(community_multilevel)}")

# Estatísticas por comunidade
def community_statistics(community, node_id_list):
    df = pd.DataFrame({"node_id": node_id_list})
    df["degree"] = community.degree()
    df["cc"] = community.transitivity_local_undirected()
    df["closeness"] = community.closeness()
    df["betweenness"] = community.betweenness()
    df["bridge"] = df["node_id"].isin(community.articulation_points()).astype(int)
    return df

network_karate_communities_df = pd.DataFrame({
    "node_id": list(range(len(community_multilevel.membership))),
    "membership": community_multilevel.membership
})

# Estatísticas por comunidade
single_community_stats_df_list = []
for comm_id in network_karate_communities_df["membership"].unique():
    node_ids = network_karate_communities_df[network_karate_communities_df["membership"] == comm_id]["node_id"].tolist()
    subgraph = community_multilevel.subgraphs()[comm_id]
    stats_df = community_statistics(subgraph, node_ids)
    single_community_stats_df_list.append(stats_df)

# Consolidando
single_community_stats_df = pd.concat(single_community_stats_df_list)
final_df = single_community_stats_df.merge(network_karate_communities_df, on="node_id", how="left").sort_values(by="membership")
final_df = final_df.merge(network_statistics_df, on="node_id", suffixes=["_community", "_whole"])
print(final_df.head())


# Criação do grafo
g = Graph.Famous("Zachary")
vertex_label = list(range(g.vcount()))
vertex_size = [x / 3 for x in g.betweenness()]
layout = g.layout("kk")

# Detecta comunidades
communities = g.community_multilevel()
dendrogram = g.community_walktrap()

# Cria subplots lado a lado
fig, axs = plt.subplots(1, 3, figsize=(18, 6))  # 1 linha, 3 colunas

# Grafo com comunidades coloridas
plot(
    communities,
    target=axs[0],
    layout=layout,
    vertex_label=vertex_label,
    mark_groups=True,
    bbox=(300, 300),
)
axs[0].set_title("Comunidades (Louvain)")

# Dendrograma
plot(
    dendrogram,
    target=axs[1],
    bbox=(300, 300)
)
axs[1].set_title("Dendrograma (Walktrap)")

# Grafo com tamanhos proporcionais à betweenness
plot(
    g,
    target=axs[2],
    layout=layout,
    vertex_label=vertex_label,
    vertex_color="cyan",
    vertex_size=vertex_size,
    bbox=(300, 300),
)
axs[2].set_title("Centralidade (Betweenness)")

# Mostrar tudo
plt.tight_layout()
plt.show()

