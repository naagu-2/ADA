# ADA
#include <stdio.h>


void main() {

int adjMatrix[MAX_VERTICES][MAX_VERTICES] = {0};


int numVertices, numEdges;

int i, j, u, v;

printf("Enter the number of vertices in the graph: ");

scanf("%d", &numVertices);

printf("Enter the number of edges in the graph: ");

scanf("%d", &numEdges);

printf("Enter the edges (u, v):\n");

for (i = 0; i < numEdges; i++) {

scanf("%d %d", &u, &v);

adjMatrix[u][v] = 1;

adjMatrix[v][u] = 1; 
}


printf("\nAdjacency Matrix:\n");

for (i = 1; i <= numVertices; i++) {

for (j = 1; j <=numVertices; j++) {

printf("%d ", adjMatrix[i][j]);

}

printf("\n");
}
getch();

}

correct adjacency ,atrix program
