# web-graph

networkx
```

import networkx as nx
from networkx.readwrite import json_graph
import matplotlib.pyplot as plt
import pandas as pd
import os
import json 

print(os.listdir())


pd_data_dir = pd.read_csv("entity_0530.csv",sep=",")
#pd_trans = pd.read_csv("relation1.csv",sep=";")
entity_id_name,entity_name,entity_type_name =pd_data_dir.columns
print("bond_type,head,tail",entity_id_name,entity_name,entity_type_name)
print("head:\n",pd_data_dir.head())
print("shape:\n",pd_data_dir.shape)





entity_dir = {}


for i in  range(pd_data_dir.shape[0]):
    entity_id        = pd_data_dir.loc[i,entity_id_name]
    entity          = pd_data_dir.loc[i,entity_name]
    entity_type      = pd_data_dir.loc[i,entity_type_name]
    print("-->",entity_id_name,entity_name,entity_type_name)

    entity_dir[entity_id] = [entity,entity_type]


















pd_data = pd.read_csv("relation_0530.csv",sep=",")
#pd_trans = pd.read_csv("relation1.csv",sep=";")
bond_type_name,head_name,tail_name =pd_data.columns
print("bond_type,head,tail",bond_type_name,head_name,tail_name)
print("head:\n",pd_data.head())
print("shape:\n",pd_data.shape)


H = nx.DiGraph()
# H = nx.Graph()


for i in  range(pd_data.shape[0]):
    bond_type = pd_data.loc[i,bond_type_name]
    head      = pd_data.loc[i,head_name]
    tail      = pd_data.loc[i,tail_name]

    print("-->",bond_type,head,tail)
    H.add_node(entity_dir[head][0],desc = entity_dir[head][0])
    H.nodes[entity_dir[head][0]] ['group'] =   entity_dir[head][1]

    H.add_node(entity_dir[tail][0],desc = entity_dir[tail][0])
    H.nodes[entity_dir[tail][0]] ['group'] =   entity_dir[tail][1]

    H.add_edge(entity_dir[head][0],entity_dir[tail][0],name=bond_type)


    # if i>1000:
    #     break

# G = nx.Graph()
# G.add_edge(0,1,weight=0.5)
# print(H)

# pos = nx.spring_layout(H)
# nx.draw(H,pos)

# node_labels = nx.get_node_attributes(H, 'desc')
# nx.draw_networkx_labels(H, pos, labels=node_labels)


# edge_labels = nx.get_edge_attributes(H, 'name')
# nx.draw_networkx_edge_labels(H, pos, edge_labels=edge_labels)

# plt.show()


graph_json = json_graph.node_link_data(H)



json_str = json.dumps(graph_json)
with open('./static/datasets/test_data.json', 'w') as json_file:
    json_file.write(json_str)

print("finish")





# relation_type:TYPE
# Drug_Disease
# Class_Disease
# Anatomy_Disease
# ADE_Drug
# Symptom_Disease
# Test_Disease
# TestItems_Disease
# Pathogenesis_Disease
# Treatment_Disease
# Method_Drug
# Frequency_Drug
# Operation_Disease
# Amount_Drug
# Reason_Disease
# Duration_Drug


entity_type_group_dir = {

"Class":0,
"Drug":1,
"TestItems":2,
"TestValue":3,
"Pathogenesis":4,
"Anatomy":5,
"Reason":6,
"ADE":7,
"Frequency":8,
"Level":9,
"Duration":10,
"Method":11,
"Test":12,
"Symptom":13,
"Treatment":14,
"Amount":15,
"Operation":16,



}

```
