import java.util.ArrayList;
import java.util.HashMap;
import java.util.Arrays;

public class DAG {
    int size = 0;//number of vertices
    int edges = 0;//number of edges
    private int[][] adjacent;//adjacency matrix
    private int[] visited;
    private int out[];//number of edges going out


    public DAG(int size) {
        if (size <= 0) {
            throw new IllegalArgumentException("Graph size cannot have a negative value or zero.");
        } else {
            this.size = size;
            out = new int[size];
            visited = new int[size];
            adjacent = new int[size][size];
            for (int i = 0; i < size; i++) {
                for (int j = 0; j < size; j++) {
                    adjacent[i][j] = 0;
                }
            }
            this.edges = 0;

        }
    }

    public int getSize() {
        return size;
    }

    public int getEdges() {
        return edges;
    }

    //returns true if there is edge from a to b, else false
    public boolean containsEdge(int a, int b) {
        if (((a >= 0) && a < getSize()) && ((b >= 0) && b < getSize())) {
        return adjacent[a][b] == 1;
        } else {
            throw new IllegalArgumentException("Argument cannot have parameters bigger than the graph..");
        }
    }

    //adds edge to the graph
    public void addEdge(int a, int b) {
        if (((a >= 0) && a < getSize()) && ((b >= 0) && b < getSize())) {
            adjacent[a][b] = 1;
            edges++;//increment edges
            out[a] = out[a] + 1;//increment number of edges going out from a

        } else {
            throw new IllegalArgumentException("Graph size cannot have a negative value, or bigger value than its size.");
        }
    }

    //removes edge from the graph
    public void removeEdge(int a, int b) {
        if (((a >= 0) && a < getSize()) && ((b >= 0) && b < getSize())) {
            if (containsEdge(a, b)) {
                adjacent[a][b] = 0;
                edges--;//decrement edges
                out[a] = out[a] - 1;//decrement number of edges going out from a

            }
        } else {
            throw new IllegalArgumentException("Graph size cannot have a negative value, or bigger value than its size.");
        }
    }

    //returns number of edges going out from a
    public int outdegree(int a) {
        if (((a >= 0) && a < getSize())) {
        return out[a];
        } else {
            throw new IllegalArgumentException("Graph size cannot have a negative value, or bigger value than its size.");
        }
    }

    //helping method for Cyclic();
    public boolean isCyclicUtil(int i, boolean[] visited,
                                boolean[] Stack) {


        // part of recursion stack
        if (Stack[i])
            return true;

//if alredy visited return fasle
        if (visited[i])
            return false;
        // Mark the current vertex as visited and
        visited[i] = true;

        Stack[i] = true;
        ArrayList<Integer> children = new ArrayList<Integer>();
        //get all the children of i in children
        for (int j = 0; j < size; j++) {
            if (adjacent[j][i] == 1) {
                children.add(j);
            }
        }

        for (Integer c : children)
            if (isCyclicUtil(c, visited, Stack))
                return true;//recurssion

        Stack[i] = false;

        return false;
    }

    public boolean Cyclic() {
        //initialize visited array
        boolean[] visited = new boolean[size];
        //initialize stack
        boolean[] recStack = new boolean[size];


        //Call the recursive helper method isCyclicUtil
        for (int i = 0; i < size; i++)
            if (isCyclicUtil(i, visited, recStack))
                return true;

        return false;
    }

    //returns the list of all the common ancestors of a and b
    public ArrayList<Integer> LCA(DAG graph, int a, int b) {
        //reinitialize visited array
        Arrays.fill(visited, 0);
        if (((a >= 0) && a < getSize()) && ((b >= 0) && b < getSize())) {
            if (!graph.Cyclic()) {
                ArrayList<Integer> ancestors = new ArrayList<Integer>();
                ArrayList<Integer> ancA = new ArrayList<Integer>();
                ArrayList<Integer> ancB = new ArrayList<Integer>();
                //get all the ancestors of a
                ancA = DFS(graph, a);

                //get all the ancestors of B
                ancB = DFS(graph, b);

                int maxDepth = 0;
                //add the common ancestors in ancestors array
                for (int i = 0; i < ancA.size(); i++) {
                    for (int j = 0; j < ancB.size(); j++) {
                        if (ancA.get(i) == ancB.get(j)) {
                            ancestors.add(ancA.get(i));
                        }
                    }
                }


                //making subgraph
                for (int i = 0; i < ancestors.size(); i++) {
                    for (int j = 0; j < graph.getSize(); j++) {
                        if (!ancestors.contains(j)) {
                            graph.removeEdge(j, ancestors.get(i));

                            graph.removeEdge(ancestors.get(i), j);

                        }
                    }
                }

                System.out.println("Ancestors of " + a + " and " + b + " are : ");

                for (int i = 0; i < ancestors.size(); i++) {

                    if ((graph.outdegree(ancestors.get(i))) != 0) {
                        ancestors.remove(i);
                        i--;
                    }
                }
                System.out.println(ancestors);
                return ancestors;
            } else {
                throw new IllegalArgumentException("Graph is Cyclic. Only Acyclic graphs are allowed.");
            }
        } else {
            throw new IllegalArgumentException("Graph size cannot have a negative value, or bigger value than its size.");
        }
    }

    //returns all the ancestors of a node by doing Depth first Search
    public ArrayList<Integer> DFS(DAG graph, int a) {
        if (((a >= 0) && a < getSize()) ) {
        int[] visited = new int[size];
        int depth = 0;

        ArrayList<Integer> anc = new ArrayList<Integer>();
        ArrayList<Integer> ancestor = new ArrayList<Integer>();
        //recursive helper method
        anc = DFSutil(graph, a, visited, depth, ancestor);
        return anc;}
        else {
                throw new IllegalArgumentException("Graph size cannot have a negative value, or bigger value than its size.");
            }
    }

    //returns the ancestors of a and their depth
    public ArrayList<Integer> DFSutil(DAG graph, int a, int[] visited, int depth, ArrayList<Integer> anc) {
        if (((a >= 0) && a < getSize()) ) {
        visited[a] = 1;
        anc.add(a);

        for (int i = 0; i < size; i++) {
            if (graph.containsEdge(i, a) && visited[i] == 0) {
                int deep = depth + 1;
                DFSutil(graph, i, visited, deep, anc);
            }
        }
        return anc;
    }
        else {
            throw new IllegalArgumentException("Graph size cannot have a negative value, or bigger value than its size.");
        }
}
}