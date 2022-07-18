package main

import (
	"fmt"
)

func sum(num1 int, num2 int) int {
	return num1 + num2
}

func main() {
	num1 := 1
	num2 := -5
	fmt.Println(sum(num1, num2))
	fmt.Println("Test..")
}
