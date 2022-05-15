package main

import "fmt"

func get_total(array []int) int {
	var total int = 0
	for i := 0; i < len(array); i++ {
		total += array[i]
	}
	return total
}

func maximumWealth(accounts [][]int) int {
	var total_sum int = 0
	var total int = 0
	for i := 0; i < len(accounts); i++ {
		total = get_total(accounts[i])
		if total > total_sum {
			total_sum = total
		}
	}
	return total_sum
}

func main() {
	accounts := [][]int{{2, 8, 7}, {7, 1, 3}, {1, 9, 5}}
	fmt.Println(maximumWealth(accounts))
	fmt.Println(accounts)
}
