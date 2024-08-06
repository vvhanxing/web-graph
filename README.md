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





# import




```

from neo4j import GraphDatabase
 
# 连接Neo4j数据库
driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "password"))
 
# 创建一个会话
with driver.session() as session:
    # 准备CSV文件中的数据
    csv_data = """
    Node1,Node2
    Label1,Label2
    Data1,Data2
    """
 
    # 执行LOAD CSV命令
    session.run("""
        LOAD CSV WITH HEADERS FROM {csv} AS row
        CREATE (n:Label {key: row.Node1, value: row.Node2})
    """, csv=csv_data)
 
# 关闭驱动
driver.close()



```
```html


<html>
<head>
    <meta charset="utf-8">
    <title>Force</title>
    <style>
 
        .nodetext {
            font-size: 12px ;
            font-family: SimSun;//字体
            fill:#000000;
        }
        .linetext {
            /*font-family: SimSun;*/
            fill:#1f77b4;
            fill-opacity:0.0;
        .circleImg {
            stroke: #ff7f0e;
            stroke-width: 1.5px;
    </style></head>
<body>
<script src="http://d3js.org/d3.v3.min.js" charset="utf-8"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/d3/3.5.5/d3.min.js"></script>
<script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
<script>
    var width = 900;
    var height = 800;
    var img_w = 77;
    var img_h = 80;
    var radius = 30;    //圆形半径
    var svg = d3.select("body")
        .append("svg")
        .attr("width",width)
        .attr("height",height);
    var edges = [];
    d3.json("my.json",function(error,root){
        if( error ){
            return console.log(error);
        console.log(root);
//默认按索引链接结点,我强制改成通过id链接它们。
        root.edges.forEach(function (e) {
                var sourceNode = root.nodes.filter(function (n) {
                        return n.id === e.source;
                    })[0],
                    targetNode = root.nodes.filter(function (n) {
                        return n.id === e.target;
                    })[0];
                edges.push({
                 source: sourceNode,
                 target: targetNode,
                 relation: e.type
                })
        });
console.log(edges)
        //D3力导向布局
        var force = d3.layout.force()
            .nodes(root.nodes)
            .links(edges)
            .size([width,height])
            .linkDistance(200)
            .charge(-1500)
            .start();
        var defs = svg.append("defs");
        var arrowMarker = defs.append("marker")
            .attr("id","arrow")
            .attr("markerUnits","strokeWidth")//图最前端大小
            .attr("markerWidth","15")//标识长宽
            .attr("markerHeight","15")
            .attr("viewBox","0 0 12 12")//坐标系区域
            .attr("refX","17")
            .attr("refY","6")
            .attr("orient","auto");//方向
        var arrow_path = "M2,2 L10,6 L2,10 L6,6 L2,2";
        arrowMarker.append("path")
            .attr("d",arrow_path)
            .attr("fill","#ccc");
        //边
        var edges_line =svg.selectAll("line")
            .data(edges)
            .enter()
            .append("line")
            .attr("class","line")
            .style("stroke","#ddd")
            .style("linewidth",2)
            .attr("marker-end","url(#arrow)")
            .style("stroke-width",3);
        //边上的文字（人物之间的关系）
        var edges_text = svg.selectAll(".linetext")
            .append("text")
            .attr("class","linetext")
            .text(function(d){
                return d.relation;
            })
            .style("fill-opacity",1.0);//不透明度
        // 圆形图片节点（人物头像）
        var nodes_img = svg.selectAll("image")
            .data(root.nodes)
            .append("circle")
            .attr("class", "circleImg")
            .attr("r", radius)
            .attr("fill", function(d, i){
                //创建圆形图片
                var defs = svg.append("defs").attr("id", "imgdefs")
                var catpattern = defs.append("pattern")
                    .attr("id", "catpattern" + i)
                    .attr("height", 1)
                    .attr("width", 1)
                catpattern.append("image")
                    .attr("x", - (img_w / 2 - radius))
                    .attr("y", - (img_h / 2 - radius))
                    .attr("width", img_w)
                    .attr("height", img_h)
                    .attr("xlink:href", d.labels)
                return "url(#catpattern" + i + ")";
            // .on("mouseover",function(d,i){
            //     //显示连接线上的文字
            //     edges_text.style("fill-opacity",function(edge){
            //         if( parseInt(edge.source) === d || parseInt(edge.target) === d ){
            //             return 1.0;
            //         }
            //     });
            // })
            // .on("mouseout",function(d,i){
            //     //隐去连接线上的文字
            //         if( edge.source === d || edge.target === d ){
            //             return 0.0;
            .call(force.drag);
        var text_dx = -20;
        var text_dy = 20;
        var nodes_text = svg.selectAll(".nodetext")
            .style("stroke","#ff7f0e")
            .attr("class","nodetext")
            .attr("dx",text_dx)
            .attr("dy",text_dy)
                var uservalue = d.properties.username;
                var personvalue = d.properties.person;
                var phonevalue = d.properties.phone;
                if ( uservalue == undefined ){
                    uservalue = "";
                }
                if(personvalue == undefined){
                    personvalue = "";
                if (phonevalue == undefined){
                    phonevalue = "";
                return uservalue + phonevalue + personvalue;
            });
        force.on("tick", function(){
            //限制结点的边界
            root.nodes.forEach(function(d,i){
                d.x = d.x - img_w/2 < 0     ? img_w/2 : d.x ;
                d.x = d.x + img_w/2 > width ? width - img_w/2 : d.x ;
                d.y = d.y - img_h/2 < 0      ? img_h/2 : d.y ;
                d.y = d.y + img_h/2 + text_dy > height ? height - img_h/2 - text_dy : d.y ;
            //更新连接线的位置
            edges_line.attr("x1",function(d){ return d.source.x; });
            edges_line.attr("y1",function(d){ return d.source.y; });
            edges_line.attr("x2",function(d){ return d.target.x; });
            edges_line.attr("y2",function(d){ return d.target.y; });
            //更新连接线上文字的位置
            edges_text.attr("x",function(d){ return (d.source.x + d.target.x) / 2 ; });
            edges_text.attr("y",function(d){ return (d.source.y + d.target.y) / 2 ; });
            //更新结点图片和文字
            nodes_img.attr("cx",function(d){ return d.x });
            nodes_img.attr("cy",function(d){ return d.y });
            nodes_text.attr("x",function(d){ return d.x });
            nodes_text.attr("y",function(d){ return d.y + img_w/2; });
    });
</script>
</body>
</html>


```


```html

<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Document</title>

        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@baklavajs/themes@2.0.2-beta.3/dist/syrup-dark.css" />
        <style>
            html,
            body {
                margin: 0;
            }

            #editor {
                width: 100vw;
                height: 100vh;
            }
        </style>
    </head>
    <body>
        <div id="editor"></div>

        <script src="./static/cdn.jsdelivr.net_npm_baklavajs@2.0.2-beta.3_dist_bundle.js"></script>
        <script>
            const viewModel = BaklavaJS.createBaklava(document.getElementById("editor"));
            const PromptNode = BaklavaJS.Core.defineNode({
                type: "PlanerNode",
                inputs: {
                    input1: () => new BaklavaJS.RendererVue.TextInputInterface("Hello", "world"),
                    input2: () => new BaklavaJS.RendererVue.TextInputInterface("Hello", "world"),
                    operation: () => new BaklavaJS.RendererVue.SliderInterface("Name", 0.5, 0, 1),
                },
                outputs: {
                    ouput1: () => new BaklavaJS.RendererVue.TextInputInterface("Hello", "world"),
                },
            });

            const SkillNode = BaklavaJS.Core.defineNode({
                type: "SkillNode",
                inputs: {
                    input1: () => new BaklavaJS.RendererVue.TextInputInterface("Hello", "world"),
                },
                outputs: {
                    ouput1: () => new BaklavaJS.RendererVue.TextInputInterface("Hello", "world"),
                },
            });

            const MathNode = BaklavaJS.Core.defineNode({
                type: "MathNode",
                inputs: {
                    number1: () => new BaklavaJS.RendererVue.NumberInterface("Number", 1),
                    number2: () => new BaklavaJS.RendererVue.NumberInterface("Number", 10),
                    operation: () => new BaklavaJS.RendererVue.SelectInterface("Operation", "Add", ["Add", "Subtract"]).setPort(false),
                    },
                outputs: {
                    output: () => new BaklavaJS.RendererVue.NumberInterface("Output", 0),
                    },
                calculate({ number1, number2, operation }) {
                    let output = number;
                    if (operation === "Add") {
                        output = number1 + number2;
                    } else if (operation === "Subtract") {
                        output = number1 - number2;
                    } else {
                        throw new Error("Unknown operation: " + operation);
                    }
                    console.log(output);
                    return { output };
                },
            });

            const Display = BaklavaJS.Core.defineNode({
                type: "Display",
                inputs: {
                    Value: () => new BaklavaJS.RendererVue.NumberInterface("Number", 0),
                    },
                    
                calculate(Value) {
                   
                    console.log(Value);
                }
            });
            
            

            viewModel.editor.registerNodeType(PromptNode);
            viewModel.editor.registerNodeType(SkillNode);
            viewModel.editor.registerNodeType(MathNode);
            viewModel.editor.registerNodeType(Display);
        </script>
    </body>
</html>

```

