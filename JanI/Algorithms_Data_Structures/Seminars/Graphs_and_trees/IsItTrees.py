#!/usr/bin/python3
import sys
from pytokr import pytokr


def visit_checker(node, parent, visited, par_list, in_list):
    visited[node]=True
    par_list[node]=parent

    for neighbor in in_list[node]:
        if visited[neighbor]==False: #if neighbir hasnt been visited
            if visit_checker(neighbor, node, visited, par_list, in_list): #go in the node, treat it as parent of the nodes inside
                return True
        
        elif neighbor!=parent: #and if neighbor is not the parent
            return True
    return False

def is_tree(in_list):
    n=len(in_list)
    visited = [False]*n
    par_list=[-1]*n

    if visit_checker(0, -1, visited, par_list, in_list): #cycle?
        return False
    
    if False in visited:#All nodes are visited?
        return False
    
    for i in range(n): #check connection
        if len(in_list[i])==0 and i!=0:
            return False
        
    return True


def main():
    item, items = pytokr(iter = True)
    while True:
        n = int(item())
        adj_list = [[] for _ in range(n)]
        for i in range(n):
            neighbors = []
            for _ in range(int(item())):
                neighbors.append(int(item()))
            adj_list[i].extend(neighbors)
        if is_tree(adj_list):     
            print("es un arbre")
        else:
            print("NO es un arbre")

if __name__ == "__main__":
    main () 