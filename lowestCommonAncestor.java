import java.util.ArrayList;
import java.util.HashMap;
public class DAG {
    static int size = 0;
    static int edges = 0;
    private static int[][] adjacent;
    private static int[] visited;
    private static int out[];
    private static int in[];


    public DAG(int size) {
        if (size < 0) {
            throw new IllegalArgumentException("Graph size cannot have a negative value.");
        } else {
            this.size = size;
            this.edges = 0;
            out = new int[size];
            in = new int[size];
            visited=new int[size];
            adjacent = new int[size][size];
            for (int i = 0; i < size; i++) {
                for (int j = 0; j < size; j++) {
                    adjacent[i][j] = 0;
                }
            }
        }

    }

    public static int getSize() {
        return size;
    }

    public int getEdges() {
        return edges;
    }

    public static boolean containsEdge(int a, int b) {
        return adjacent[a][b] == 1;
    }

    public void addEdge(int a, int b) {
        if (((a >=0) && a < getSize()) && ((b >= 0) && b < getSize())) {
            adjacent[a][b] = 1;
            edges++;
            out[a]=out[a]+1;
            in[b]=in[b]+1;
        } else {
            throw new IllegalArgumentException("Graph size cannot have a negative value, or bigger value than its size.");
        }
    }

    public void removeEdge(int a, int b) {
        if (((a >= 0) && a < getSize()) && ((b >=0) && b < getSize())) {
        if(containsEdge(a,b))
        {
            adjacent[a][b] = 0;
            edges--;
            out[a]=out[a]-1;
            in[b]=in[b]-1;
        }

        } else {
            throw new IllegalArgumentException("Graph size cannot have a negative value, or bigger value than its size.");
        }
    }

    public static int outdegree(int a){
        return out[a];
    }

    public static int[] isAdj(int a) {
        if (((a >=0) && a < getSize())) {
            int inc = 0;
            int[] adj = new int[out[a]];
            for (int i = 0; i < size; i++) {
                if (containsEdge(a, i)) {
                    adj[inc] = i;
                    inc++;
                }
            }
            return adj;
        } else {
            throw new IllegalArgumentException("Graph size cannot have a negative value, or bigger value than its size.");
        }
    }

    public static boolean Cyclic() {
        boolean cyclic = false;
        int inc = 0;
        for (int i = 0; i < size; i++) {
            visited[inc] = i;
            for (int j = 0; j < size; j++) {
                for (int k = 0; k < size; k++) {
                    if (visited[k] == j && adjacent[i][j] == 1) {
                        cyclic = true;
                        return cyclic;
                    }
                }
            }
            inc++;
        }
        return cyclic;
    }

    public static void LCA(DAG graph, int a, int b){
        if (((a >= 0) && a < getSize()) && ((b >=0) && b < getSize())) {
            ArrayList<Integer> ancestors=new ArrayList<Integer>();
            HashMap<String, Integer> ancA=new HashMap<String, Integer>();
            HashMap<String, Integer> ancB=new HashMap<String, Integer>();
            ancA=DFS(graph,a);
            ancB=DFS(graph,b);
            int maxDepth=0;
            for (String key : ancA.keySet())
                {
                    for (String keyB : ancB.keySet()) {
                    if((key).equals(keyB)){
                            ancestors.add(Integer.parseInt(key));
                            System.out.println("Common Ancestor"+key);
                    }
                }
            }
//making subgraph
        for(int i=0; i<ancestors.size();i++){
            for(int j=0;j<graph.getSize();j++){
            if(!ancestors.contains(j)) {
                graph.removeEdge(j, ancestors.get(i));
                graph.removeEdge(ancestors.get(i), j);
            }
            }
        }
            System.out.println("The common ancestors of "+a+" and "+b+" are:");
            for(int i=0; i<ancestors.size();i++){
            if((graph.outdegree(ancestors.get(i)))==0){
            System.out.println(ancestors.get(i));
            }
            }

        }
        else{
            throw new IllegalArgumentException("Graph size cannot have a negative value, or bigger value than its size.");
        }
    }

    public static HashMap<String, Integer> DFS(DAG graph,int a){
        int[] visited =new int[size];
        int depth =0;
        HashMap<String, Integer> anc=new HashMap<String, Integer>();
        HashMap<String, Integer> ancestor=new HashMap<String, Integer>();
        anc=DFSutil(graph,a,visited, depth, ancestor);
        return anc;
    }

  public static HashMap<String, Integer> DFSutil(DAG graph,int a, int[] visited , int depth, HashMap<String, Integer>anc){
        visited[a] = 1;
        String s=Integer.toString(a);
        anc.put(s, depth);
        System.out.println(a+": depth = "+depth);
        for(int i=0;i<size;i++){
            if(graph.containsEdge(i,a)&&visited[i]==0){
                int deep=depth+1;
                DFSutil(graph, i, visited, deep, anc);
            }
        }
        return anc;
    }


    public static void main(String args[]) {
    DAG  graph=new DAG(9);
    graph.addEdge(0,1);
    graph.addEdge(0,2);
    graph.addEdge(1,4);
    graph.addEdge(1,6);
        graph.addEdge(2,4);
        graph.addEdge(2,6);
        graph.addEdge(2,3);
        graph.addEdge(3,6);
        graph.addEdge(6,5);
        graph.addEdge(6,7);
        graph.addEdge(7,8);
        LCA(graph, 4, 7);
    }

}