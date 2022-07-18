package main

import "fmt"

func hammingDistance(x int, y int) int {

	cnt := 0
	for x != 0 || y != 0 {
		if (x&1 ^ y&1) == 1 {
			cnt += 1
		}
		x = x >> 1
		y = y >> 1
	}
	return cnt
}

func main() {
	ans := hammingDistance(5, 4)
	fmt.Println(ans)
}
