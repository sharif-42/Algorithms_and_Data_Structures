package main

import (
	"fmt"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func checkTree(root *TreeNode) bool {
	if root.Left.Val+root.Right.Val == root.Val {
		return true
	}
	return false

}

func main() {
	t2 := TreeNode{
		Val: 6,
	}
	t3 := TreeNode{
		Val: 7,
	}
	t1 := TreeNode{
		Val:   10,
		Left:  &t2,
		Right: &t3,
	}
	fmt.Println(checkTree(&t1))
}
