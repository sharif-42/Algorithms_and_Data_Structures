package main

import (
	"fmt"
)

func countOdds(low int, high int) int {
	var diff int
	var count int

	diff = high - low

	if high%2 == 1 && low%2 == 1 {
		count = (diff / 2) + 1
	} else if high%2 == 0 && low%2 == 0 {
		count = int(diff / 2)
	} else {
		count = int(diff/2) + 1
	}
	return count
}

func main() {
	low := 1
	high := 10
	fmt.Println(countOdds(low, high))

}
