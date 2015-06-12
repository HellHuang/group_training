__author__ = 'fen'
#coding=utf-8
import xlrd
from igraph import *
def load_data(filename):
    bk=xlrd.open_workbook(filename)
    try:
        sh=bk.sheet_by_name("Sheet1")
    except:
        print "no "
    nrow=sh.nrows
    ncol=sh.ncols









    max_user1=0
    max_user2=0
    for i in range(1,nrow-1,1):
        max_user1=max(max_user1,sh.cell_value(i,0))
        max_user1=max(max_user1,sh.cell_value(i,1))
    max_user1=int(max(max_user1,max_user2))
    user_num=max_user1+1
    matrix=[[0 for i in range(user_num)]for j in range(user_num)]
    for row in range(1,nrow-1,1):
        user1=int(sh.cell_value(row,0))
        user2=int(sh.cell_value(row,1))
        weight=int(sh.cell_value(row,2))
        matrix[user1][user2]=weight
    return matrix,user_num

def LPA(matrix,user_num):
    g=Graph(1)
    g.add_vertices(user_num-1)
    weights=[]
    for i in range(user_num):
        for j in range(user_num):
            if matrix[i][j]>0:
                g.add_edges((i,j))
                weights.append(matrix[i][j])
    result=g.community_label_propagation(weights=weights)
    #print result
    return result

def Walktrap(matrix,user_num):
    g=Graph(1)
    g.add_vertices(user_num-1)
    weights=[]
    for i in range(user_num):
        for j in range(user_num):
            if matrix[i][j]>0:
                g.add_edges((i,j))
                weights.append(matrix[i][j])

    result=g.community_walktrap(weights=weights,steps=5)
    print "result",result
    cluster=result.as_clustering()
    #print result
    print "cluster",cluster
    return cluster



matrix,user=load_data("/home/fen/dataset/class_data.xls")
cluster1=Walktrap(matrix,user)
cluster2=LPA(matrix,user)
c=[]
print cluster2
for i in range(cluster2.__len__()):
    c.append(cluster2[i])
print c
