# Grafo Genérico – Estrutura de Dados

## 📌 Nome do Projeto
Implementação de Grafo Genérico (não-direcionado)

## 🧩 Descrição do Problema / Solução
Este projeto implementa uma estrutura básica de **grafos não-direcionados** utilizando lista de adjacência.  
O objetivo é demonstrar operações fundamentais de manipulação de grafos, incluindo:

- criação de vértices  
- remoção de vértices  
- criação de arestas  
- remoção de arestas  
- exibição do grafo  

A solução cumpre todos os requisitos mínimos da atividade de Estrutura de Dados.

---

## 🧪 Funcionalidades Implementadas
### ✔ Requisitos mínimos:
- Representação do grafo por lista de adjacência  
- Adicionar vértice  
- Adicionar aresta  
- Remover vértice  
- Remover aresta  
- Exibir o grafo (textual + lista de adjacência)

### ❌ Funcionalidades avançadas:
- Não se aplica para este projeto

---

## 🛠️ Linguagem e Versão
- Python **3.11+**
- Nenhuma biblioteca externa necessária

---

## ▶️ Instruções de Execução
Dentro da pasta do projeto execute:

```bash
python src/main.py
```
## 📥 Exemplo de Entrada (dentro do código)
- g.add_vertex('A')
- g.add_vertex('B')
- g.add_vertex('C')
- g.add_edge('A', 'B')
- g.add_edge('A', 'C')
- g.add_edge('B', 'C')

## 📤 Exemplo de Saída
# Lista de adjacência (raw):
- {'A': ['B', 'C'], 'B': ['A', 'C'], 'C': ['A', 'B']}

# Lista de adjacência (formatada):
- A -> B, C
- B -> A, C
- C -> A, B

# Impressão demonstrativa:
- A -> ['B', 'C']
- B -> ['A', 'C']
- C -> ['A', 'B']

## Link do Vídeo
(https://youtu.be/XZB94kWNOTc?si=MICkh11C2QctF8Ys)

## 👤 Autor
Marcello Sampaio
