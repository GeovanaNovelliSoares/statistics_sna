# 🥋 Statistics SNA - Zachary's Karate Club

Este projeto realiza uma análise de redes sociais (SNA - Social Network Analysis) sobre o grafo clássico do **Zachary's Karate Club**, utilizando Python e a biblioteca `igraph`.

Através de algoritmos de detecção de comunidades, medidas de centralidade e visualizações gráficas, o projeto explora como os membros do clube se conectam e se dividem em subgrupos.

---

## 📁 Sobre o dataset

- O grafo representa conexões entre 34 membros de um clube universitário de karatê.
- Originalmente estudado por Wayne W. Zachary (1977), e amplamente utilizado em pesquisas de SNA.

---

## 📌 O que este projeto faz

✔ Cria e visualiza o grafo da rede do clube  
✔ Calcula métricas estruturais: grau, centralidade, clustering, etc  
✔ Detecta comunidades com diferentes algoritmos:  
   - Louvain  
   - Walktrap  
   - Fast Greedy  
   - Edge Betweenness  
✔ Compara modularidade e estrutura das comunidades  
✔ Gera gráficos com base nos resultados

---

## 📊 Tecnologias e bibliotecas utilizadas

- Python 3.12+
- [igraph](https://igraph.org/python/)
- matplotlib
- pandas
- numpy
- pycairo

---


```bash
git clone https://github.com/GeovanaNovelliSoares/statistics_sna.git
cd statistics_sna
