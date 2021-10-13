// Recursive Java program to print lca of two nodes

// A binary tree node
class Node
{
    int data;
    Node left, right;

    Node(int item)
    {
        data = item;
        left = right = null;
    }
}

public class lowestCommonAncestor
{
    Node root;

    /* Function to find LCA of n1 and n2. The function assumes that both
       n1 and n2 are present in BST */
    Integer lca(Node node, int n1, int n2)
    {
    if(Contains(root, n1) && Contains(root, n2)) {
    while (root != null) {
        // If both n1 and n2 are smaller than root, then LCA lies in left
        if (node.data > n1 && node.data > n2)
            return lca(node.left, n1, n2);

            // If both n1 and n2 are greater than root, then LCA lies in right
        else if (node.data < n1 && node.data < n2)
            return lca(node.right, n1, n2);
        else {
            break;
        }
    }
    return node.data;
}
else {
    System.out.println("Value does not exist in the tree.");
    return null;
}
    }

    public static boolean Contains(Node root, int value)
    {
        if (root == null) return false;
        if (root.data == value) return true;
        if (root.data > value) return Contains(root.left, value);
        return Contains(root.right, value);
    }

}
