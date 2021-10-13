import org.junit.Test;
import static org.junit.Assert.assertEquals;


class lowestCommonAncestorTest {

    //Utkarsh Gupta 9 Oct 2021
    @org.junit.jupiter.api.Test
    void lca() {
        lowestCommonAncestor tree = new lowestCommonAncestor();
        tree.root = new Node(20);//adding 20 as the root
        tree.root.left = new Node(8);
        tree.root.right = new Node(22);
        tree.root.left.left = new Node(4);
        tree.root.left.right = new Node(12);
        tree.root.left.right.left = new Node(10);
        tree.root.left.right.right = new Node(14);
        Integer value1=10, value2=14;Integer result=12;

        //test case for leaf nodes with direct ancestor
        assertEquals("Checking that ancestor of 10 & 14 = 12",
                result, tree.lca(tree.root, value1, value2));
        //test case for a parent node and a child node
        value1=12; value2=14; result=12;
        assertEquals("Checking that ancestor of 12 & 14 = 12",
                result, tree.lca(tree.root, value1, value2));

        //test case for leaf nodes with no direct ancestor
        value1=22; value2=14; result=20;
        assertEquals("Checking that ancestor of 22 & 14 = 20",
                result, tree.lca(tree.root, value1, value2));

        //test case for common ancestor of root and a second node.
        value1=tree.root.data; value2=4; result=20;
        assertEquals("Checking that ancestor of root & 4 = 20",
                result, tree.lca(tree.root, value1, value2));
        //test case for nodes that are not in the binary tree.
        value1=60; value2=50;
        assertEquals("Checking if tree contains 50",
                null, tree.lca(tree.root, value1, value2));

    }
}