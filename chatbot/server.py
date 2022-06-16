from flask import Flask,render_template
from flask import jsonify
from flask import request
from py2neo import *
import json 

# neo4j.bat console


# neo4j install service


# neo4j start


# neo4j-admin start

app = Flask(__name__)

r = "none"

graph = Graph('http://localhost:7500/')
# res = graph.run("MATCH p=()-[r:ADE_Drug]->() RETURN p LIMIT 25")
# r = "{Fake:"+   str(res.data()[1]) +"}"
# r = """{"Fake":["结果是1","结果是2","结果是3","结果是4"] }"""
# print("#########################3",r)
def getNeo(query):
    print("@ ",query)
      


    query_ent = query.split('的')

    #graph = Graph('http://localhost:7500/')

    query_ent_name = query_ent[0]
    res = ""
    if "方法" in query_ent[1]:
        res = graph.run("MATCH (t:Treatment)-[r:Treatment_Disease]->(d:Disease{entity:'" + str(query_ent_name) + "'}) RETURN t.entity")
        res_list = []
        for r in res:
            res_list.append(str(r))

        reply = '治疗{a}的方法有{b}种，包括{c}'.format(a=query_ent_name, b=str(len(res_list)),
                                            c=str([x for x in res_list]).replace("\"", '').replace('[', '').replace(']','')
                                                .replace("Record t.entity=","")
                                                .replace("<","")
                                                .replace(">",""))
        print(reply)
        return reply

    elif "药" in query_ent[1]:
        res = graph.run("MATCH (t:Drug)-[r:Drug_Disease]->(d:Disease{entity:'" + str(query_ent_name) + "'}) RETURN t.entity")
        res_list = []
        for r in res:
            res_list.append(str(r))

        reply = '治疗{a}的药物有{b}种，包括{c}'.format(a=query_ent_name, b=str(len(res_list)),
                                            c=str([x for x in res_list]).replace("\"", '').replace('[', '').replace(']',   '')
                                                .replace("Record t.entity=","")
                                                .replace("<","")
                                                .replace(">",""))
        print(reply)
        return reply

    elif "手术" in query_ent[1]:
        res = graph.run("MATCH (t:Operation)-[r:Operation_Disease]->(d:Disease{entity:'" + str(query_ent_name) + "'}) RETURN t.entity")
        res_list = []
        for r in res:
            res_list.append(str(r))

        reply = '{a}的手术方案有{b}种，包括{c}'.format(a=query_ent_name, b=str(len(res_list)),
                                            c=str([x for x in res_list]).replace("\"", '').replace('[', '').replace(']',   '')
                                                .replace("Record t.entity=","")
                                                .replace("<","")
                                                .replace(">",""))
        print(reply)
        return reply
#Pathogenesis_Disease

    elif "症状" in query_ent[1]:
        res = graph.run("MATCH (t:Pathogenesis)-[r:Pathogenesis_Disease]->(d:Disease{entity:'" + str(query_ent_name) + "'}) RETURN t.entity")
        res_list = []
        for r in res:
            res_list.append(str(r))

        reply = '{a}的症状有{b}种，包括{c}'.format(a=query_ent_name, b=str(len(res_list)),
                                            c=str([x for x in res_list]).replace("\"", '').replace('[', '').replace(']',   '')
                                                .replace("Record t.entity=","")
                                                .replace("<","")
                                                .replace(">",""))
        print(reply)
        return reply

    elif "原因" in query_ent[1]:
        res = graph.run("MATCH (t:Reason)-[r:Reason_Disease]->(d:Disease{entity:'" + str(query_ent_name) + "'}) RETURN t.entity")
        res_list = []
        for r in res:
            res_list.append(str(r))

        reply = '{a}的原因有{b}种，包括{c}'.format(a=query_ent_name, b=str(len(res_list)),
                                            c=str([x for x in res_list]).replace("\"", '').replace('[', '').replace(']',   '')
                                                .replace("Record t.entity=","")
                                                .replace("<","")
                                                .replace(">",""))
        print(reply)
        return reply

    


@app.route('/', methods=['GET', 'POST'])
def home():

    return render_template('index.html')



@app.route('/neo', methods=['GET', 'POST'])

def neo_test():


    print("--",request.get_json())
    j = request.get_json()
    print(j["inputTxt"][0])

    t = getNeo(j["inputTxt"][0])

    r = """{" """+ str(t) +""" "  }"""
    return r








    # with open("index.html","r") as  txt:
    #     html_txt = ""
    #     html = list(txt.readlines())
    #     html_txt = "".join(html )
    
    #return html_txt
    # return jsonify(res[0]), 200






if __name__ == '__main__':
    app.run(host='192.168.31.67',debug=True,port=5000)
   
#debug=False,host='192.168.1.111',port=5000 192.168.9.106
    #ipconfig 192.168.1.111
