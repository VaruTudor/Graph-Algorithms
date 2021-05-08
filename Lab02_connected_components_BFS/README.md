@ First manual execution
the graph used was
----
8 8 
0 1 
0 2 
0 3
1 2
1 3
2 3
5 6
6 7 
----
connected component 1 : 
vertices: 0  1  2  3
edges: ( 0  1 ) ( 0  2 ) ( 0  3 ) ( 1  0 ) ( 1  2 ) ( 1  3 ) ( 2  0 ) ( 2  1 ) ( 2  3 ) ( 3  0 ) ( 3  1 ) ( 3  2 )
connected component 2 :
vertices: 4
edges:
connected component 3 :
vertices: 5  6  7
edges: ( 5  6 ) ( 6  5 ) ( 6  7 ) ( 7  6 )


@ Secont manual execution
the graph used was
----
5 8
0 2
0 4
1 2
1 3
1 4
2 3
2 4
3 4
----
connected component 1 : 
vertices: 0  2  1  3  4
edges: ( 0  2 ) ( 0  4 ) ( 2  0 ) ( 2  1 ) ( 2  3 ) ( 2  4 ) ( 1  2 ) ( 1  3 ) ( 1  4 ) ( 3  2 ) ( 3  1 ) ( 3  4 ) ( 4  0 ) ( 4  2 ) ( 4  1 ) ( 4  3 )