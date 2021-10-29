public class DAG {
    int size=0;
    int edges=0;

    public DAG(int size){
        if(size<0){
            throw new IllegalArgumentException("Graph size cannot have a negative value.");
        }
        else{
            this.size=size;
            this.edges=0;
        }

    }

public int getSize(){
        return size;
}

public int getEdges(){
        return edges;
    }

}