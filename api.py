# -*- coding: utf-8 -*-

# from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, jsonify, send_from_directory
from setting import db, app
from tablemodel import *
import pymysql
import os


@app.route("/index")
def hello():
    return "hello"

@app.route('/api/query_data', methods=['POST'])
def query_data():
    # 从前端接收到POST请求传来的JSON数据
    req_data = request.get_json()

    # 从req_data中获取ana_group参数
    ana_group = req_data.get('ana_group')

    # 查询browse_deg_table表，过滤出符合条件的行
    data = test.query.filter_by(ana_group=ana_group).all()

    # 将查询结果转为JSON格式
    result = [item.to_json() for item in data]

    # 返回JSON格式的查询结果
    return jsonify(result)
 # 将查询结果转化为字典格式
# result_dict = first_row.to_json_geneinfo()
@app.route("/tabletest")
def tabletest():
    first_row = DiffexprTable.query.first()
    # 检查是否找到记录
    if first_row:
        return jsonify({"message": "找到记录"})
    else:
        return jsonify({"message": "未找到记录"})

@app.route('/api/kegg', methods=['POST'])
def kegg_gene():
    req_data = request.get_json()
    Gene_Symbol = req_data.get('Gene_Symbol')
    data = KeggGene.query.filter_by(Gene_Symbol=Gene_Symbol).all()
    result = [item.to_json_kegg() for item in data]
    response_data = {
        "code": 200,
        "msg": "请求成功",
        "data": {"result": result}
    }
    return jsonify(response_data)


@app.route('/api/gene', methods=['POST'])
def gene_info():
    req_data = request.get_json()
    Gene_Symbol = req_data.get('Gene_Symbol')
    data = GeneInfo.query.filter_by(Gene_Symbol=Gene_Symbol).all()
    result = [item.to_json_geneinfo() for item in data]
    response_data = {
        "code": 200,
        "msg": "请求成功",
        "data": {"result": result}
    }
    return jsonify(response_data)


@app.route('/api/anainfo', methods=['POST'])
def analysis_info():
    req_data = request.get_json()
    Analysis_id = req_data.get('Analysis_id')
    data = AnalysisInfo.query.filter_by(Analysis_id=Analysis_id).all()
    result = [item.to_json_analysis_info() for item in data]
    response_data = {
        "code": 200,
        "msg": "请求成功",
        "data": {"result": result}
    }
    return jsonify(response_data)

@app.route('/api/anasample', methods=['POST'])
def sample_info():
    req_data = request.get_json()
    Analysis_id = req_data.get('Analysis_id')
    data = SampleInfo.query.filter_by(Analysis_id=Analysis_id).all()
    result = [item.to_json_sample_info() for item in data]
    response_data = {
        "code": 200,
        "msg": "请求成功",
        "data": {"result": result}
    }
    return jsonify(response_data)

def kegg_filter(Analysis_id,gene_type, page=1, page_size=10):
    if gene_type == "All":
        # 当gene_type为"All"时，选择gene_type为"up"和"down"的记录
        query = KeggResult.query.filter(
            KeggResult.Analysis_id == Analysis_id,
            KeggResult.gene_type.in_(["up", "down"])
        )
    else:
        # 否则，根据提供的gene_type进行过滤
        query = KeggResult.query.filter_by(
            Analysis_id=Analysis_id,
            gene_type=gene_type
        )

    total = query.count()
    data = query.limit(page_size).offset((page - 1) * page_size).all()
    return data, total

@app.route('/api/keggresult', methods=['POST'])
def kegg_result():
    req_data = request.get_json()
    Analysis_id = req_data.get('Analysis_id')
    gene_type=req_data.get('gene_type')
    page = req_data.get('page', 1)
    page_size = req_data.get('pageSize', 10)

    result, total = kegg_filter(Analysis_id,gene_type, page, page_size)
    # 构建返回的 JSON 数据
    response_data = {
        "code": 200,
        "msg": "请求成功",
        "data": {
            "total": total,
            "info": {
                "page": page
            },
            "result": [item.to_json_kegg_result() for item in result]
        }
    }
    return jsonify(response_data)

@app.route('/api/keggbar', methods=['POST'])
def kegg_bar():
    req_data = request.get_json()
    Analysis_id = req_data.get('Analysis_id')
    data = KeggResult.query.filter_by(Analysis_id=Analysis_id).all()
    result = [item.to_json_kegg_result() for item in data]
    response_data = {
        "code": 200,
        "msg": "请求成功",
        "data": {"result": result}
    }
    return jsonify(response_data)

def browse_filter(pain, tissue, organism,detail, page=1, page_size=20):
    # 基于 pain 参数的值调整查询
    if pain in ['Chronic', 'Acute']:
        # 不包括 Detail 参数
        query = BrowseTable.query.filter_by(Pain_type=pain, Tissue=tissue, Organism=organism)
    else:
        # 包括 Detail 参数
        query = BrowseTable.query.filter_by(Pain_type=pain, Tissue=tissue, Organism=organism, Detail=detail)
    total = query.count()
    data = query.limit(page_size).offset((page - 1) * page_size).all()
    return data, total

@app.route('/api/browse', methods=['POST'])
def browse_data():
    req_data = request.get_json()

    # 获取请求参数
    pain = req_data.get('pain')
    tissue = req_data.get('tissue')
    organism = req_data.get('organism')
    detail = req_data.get('detail')
    page = req_data.get('page', 1)
    page_size = req_data.get('pageSize', 20)

    # 执行查询
    result, total = browse_filter(pain, tissue, organism,detail, page, page_size)

    # 构建返回的 JSON 数据
    response_data = {
        "code": 200,
        "msg": "请求成功",
        "data": {
            "total": total,
            "info": {
                "page": page
            },
            "result": [item.to_json_browse() for item in result]
        }
    }
    return jsonify(response_data)
def Diffexpr_filter( gene,page=1, page_size=20):
        # 执行数据库查询的逻辑，这里简化为一个假设的查询
        query = DiffexprTable.query.filter_by(Gene_Symbol=gene)
        total = query.count()
        data = query.limit(page_size).offset((page - 1) * page_size).all()
        return data, total

@app.route('/api/diffexpr', methods=['POST'])
def gene_expr():
        req_data = request.get_json()

        # 获取请求参数
        gene=req_data.get("Gene_Symbol")
        page = req_data.get('page', 1)
        page_size = req_data.get('pageSize', 20)

        # 执行查询
        result, total = Diffexpr_filter( gene , page, page_size)

        # 构建返回的 JSON 数据
        response_data = {
            "code": 200,
            "msg": "请求成功",
            "data": {
                "total": total,
                "info": {
                    "page": page
                },
                "result": [item.diffexpr_to_json() for item in result]
            }
        }
        return jsonify(response_data)

@app.route('/api/heatmap', methods=['POST'])
def get_heatmap():
    req_data = request.get_json()
    analysis_id = req_data.get('Analysis_id')

    # heatmap_table_path = '/backup/tpea/heatmap_table/'

    # heatmap_table_path = 'D:\\PythonProject\\pythonProject\\test2\\backup\\tpea\\heatmap_table'

    heatmap_table_path = 'C:\\Users\\admin\\Desktop\\tpea\\TPEA_tables\\heatmap_table'
    file_path = os.path.join(heatmap_table_path, '{}.heatmap.txt'.format(analysis_id))

    if not os.path.exists(file_path):
        response_data = {
            "code": 404,
            "msg": "未找到对应的表格",
            "data": {"result": []},
            "Analysis_id":analysis_id,
            "file_path":file_path
        }
        return jsonify(response_data)

    result = []

    with open(file_path, 'r') as file:
        header = file.readline().strip().split('\t')
        for line in file:
            values = line.strip().split('\t')
            gene_data = {"Gene_Symbol": values[0]}
            for i in range(1, len(header)):
                try:
                    # 保留五位小数
                    gene_data[header[i]] = round(float(values[i]), 4)
                except ValueError:
                    # 如果不是浮点数，保留原始值
                    gene_data[header[i]] = values[i]
            result.append(gene_data)

    response_data = {
        "code": 200,
        "msg": "请求成功",
        "data": {"result": result}
    }

    return jsonify(response_data)

@app.route('/download/Analysis_keggresults.txt')
def download_Analysis_keggresults():
    directory = 'C:\\Users\\admin\\Desktop\\tpea\\TPEA_tables\\download'  # 文件所在目录
    filename = "Analysis_keggresults.zip"  # 文件名
    return send_from_directory(directory, filename, as_attachment=True)

@app.route('/download/Browse_table.txt')
def download_Browse_table():
    directory = 'C:\\Users\\admin\\Desktop\\tpea\\TPEA_tables\\download'  # 文件所在目录
    filename = "Browse_table.zip"  # 文件名
    return send_from_directory(directory, filename, as_attachment=True)

@app.route('/download/Sample_information.txt')
def download_Sample_information():
    directory = 'C:\\Users\\admin\\Desktop\\tpea\\TPEA_tables\\download'  # 文件所在目录
    filename = "Sample_information.zip"  # 文件名
    return send_from_directory(directory, filename, as_attachment=True)




#要在这里run，不能在setting
if __name__ == '__main__':
    app.run(debug=True)