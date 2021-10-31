import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;

import static org.junit.Assert.*;
import static org.junit.jupiter.api.Assertions.*;

class DAGTest {

    DAG cyclic = new DAG(5);
    DAG acyclic = new DAG(9);
    //This is the Binary tree from part 1 in form of DAG
    DAG oldTree = new DAG(23);


    //test case for leaf nodes with direct ancestor
    @Test
    void oldLCA1() {
        createOldBinaryTree();
        ArrayList<Integer> ancestors = new ArrayList<Integer>();
        ancestors.add(12);
        assertEquals("Test Passed-Ancestors of 10, 14 is 12.", ancestors, oldTree.LCA(oldTree, 10, 14));
    }

    //test case for a parent node and a child node
    @Test
    void oldLCA2() {
        createOldBinaryTree();
        ArrayList<Integer> ancestors = new ArrayList<Integer>();
        ancestors.add(12);
        assertEquals("Test Passed-Ancestors of 12, 14 is 12.", ancestors, oldTree.LCA(oldTree, 12, 14));
    }

    //test case for leaf nodes with no direct ancestor
    @Test
    void oldLCA3() {
        createOldBinaryTree();
        ArrayList<Integer> ancestors = new ArrayList<Integer>();
        ancestors.add(20);
        assertEquals("Test Passed-Ancestors of 22, 14 is 20.", ancestors, oldTree.LCA(oldTree, 22, 14));
    }

    //test case for common ancestor of root and a second node.
    @Test
    void oldLCA4() {
        createOldBinaryTree();
        ArrayList<Integer> ancestors = new ArrayList<Integer>();
        ancestors.add(20);
        assertEquals("Test Passed-Ancestors of 10, 4 is 20.", ancestors, oldTree.LCA(oldTree, 20, 4));
    }

    //test case for nodes that are not in the binary tree.
    @Test
    void oldLCA5() {
        createOldBinaryTree();
        Assertions.assertThrows(IllegalArgumentException.class, () -> {
            oldTree.LCA(oldTree, 50, 60);
        });
    }

    //------------------------------------------------New Tests-------------------------------------------------------------
    //tests that negative value cannot be entered for a DAG
    @Test
    void negativeDAG() {
        Assertions.assertThrows(IllegalArgumentException.class, () -> {
            DAG graph = new DAG(-5);
        });
    }

    //tests for addEdge
    @Test
    void testAddEdge() {
        DAG graph = new DAG(3);
        graph.addEdge(1, 2);
        assertEquals("add Edge passed for legal parameters.", true, graph.containsEdge(1, 2));

        //tests that negative value cannot be entered for addEdge
        Assertions.assertThrows(IllegalArgumentException.class, () -> {
            graph.addEdge(-1, 4);
        });

        //tests that value higher than size cannot be entered for addEdge
        Assertions.assertThrows(IllegalArgumentException.class, () -> {
            graph.addEdge(1, 4);
        });
    }

    //tests for addEdge
    @Test
    void testRemoveEdge() {
        DAG graph = new DAG(4);
        graph.addEdge(1, 2);
        graph.addEdge(2, 3);
        graph.removeEdge(1, 2);
        assertEquals("add Edge passed for legal parameters.", false, graph.containsEdge(1, 2));

        //tests that negative value cannot be entered for removeEdge
        Assertions.assertThrows(IllegalArgumentException.class, () -> {
            graph.removeEdge(-1, 2);
        });

        //tests that value higher than size cannot be entered for removeEdge
        Assertions.assertThrows(IllegalArgumentException.class, () -> {
            graph.removeEdge(1, 9);
        });
    }


    //test that LCA thows IllegalArgumentException for a cyclic graph
    @Test
    void testCyclic() {
        createAcyclicGraph();
        createCyclicGraph();
        assertEquals("", false, acyclic.Cyclic());
        assertEquals("", true, cyclic.Cyclic());

        //removing the cyclic edge for cyclic graph to make it acyclic
        cyclic.removeEdge(3, 1);
        assertEquals("", false, cyclic.Cyclic());
    }

    //testing the LCA method to find the lowest common ancestor
    @Test
    void testLCA() {
        //creating cyclic graph
        createCyclicGraph();

        //creating cyclic graph
        createAcyclicGraph();

        ArrayList<Integer> ancestors = new ArrayList<Integer>();
        ancestors.add(1);
        ancestors.add(2);
        assertEquals("Test Passed-Ancestors of 7, 4 are 1 and 2.", ancestors, acyclic.LCA(acyclic, 7, 4));

        //testing -ve value will throw exception
        Assertions.assertThrows(IllegalArgumentException.class, () -> {
            acyclic.LCA(acyclic, -3, 4);
        });

        //testing higher than size value will throw exception
        Assertions.assertThrows(IllegalArgumentException.class, () -> {
            acyclic.LCA(acyclic, 3, 10);
        });

        //testing cyclic graph will throw exception
        Assertions.assertThrows(IllegalArgumentException.class, () -> {
            cyclic.LCA(cyclic, 2, 3);
        });
    }

    //testing the LCA method for two vertexes whose one vertex is the ancestor itself
    @Test
    void testLCA2() {
        createAcyclicGraph();
        ArrayList<Integer> ancestors = new ArrayList<Integer>();
        ancestors.add(1);
        assertEquals("Test Passed-Ancestors of 6, 1 is 1 .", ancestors, acyclic.LCA(acyclic, 1, 6));
    }

    //creating a cyclic graph
    //0->1->2->3->4
    //   ^-----|
    public void createCyclicGraph() {
        cyclic.addEdge(0, 1);
        cyclic.addEdge(1, 2);
        cyclic.addEdge(2, 3);
        cyclic.addEdge(3, 1);
        cyclic.addEdge(3, 4);
    }

    //creating a Acyclic graph
    //Graph can be seen here: https://www.baeldung.com/cs/lowest-common-ancestor-acyclic-graph#approach-of-finding-lca-in-dag
    public void createAcyclicGraph() {
        acyclic.addEdge(0, 1);
        acyclic.addEdge(0, 2);
        acyclic.addEdge(1, 4);
        acyclic.addEdge(1, 6);
        acyclic.addEdge(2, 4);
        acyclic.addEdge(2, 6);
        acyclic.addEdge(2, 3);
        acyclic.addEdge(3, 6);
        acyclic.addEdge(6, 5);
        acyclic.addEdge(6, 7);
        acyclic.addEdge(7, 8);
    }

    public void createOldBinaryTree() {
        oldTree.addEdge(20, 8);
        oldTree.addEdge(20, 22);
        oldTree.addEdge(8, 4);
        oldTree.addEdge(8, 12);
        oldTree.addEdge(12, 14);
        oldTree.addEdge(12, 10);
    }

}