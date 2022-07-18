package main

import (
	"fmt"
	"strconv"
	"strings"
)

func main() {
	fmt.Printf("write a sequence of ints seprated by comma\n")
	var text string
	fmt.Scan(&text)
	stringNumbers := strings.Split(text, ",")
	numbers := make([]int, 0, 3)
	for _, str := range stringNumbers {
		number, err := strconv.Atoi(str)
		if err == nil {
			numbers = append(numbers, number)
		}
	}
	fmt.Println("Unsorted: ", numbers)
	BubbleSort(numbers)
	fmt.Println("Sorted: ", numbers)
}

func BubbleSort(numSlice []int) {
	n := len(numSlice)
	for i := 0; i < n-1; i++ {
		for j := 0; j < n-1-i; j++ {
			if numSlice[j] > numSlice[j+1] {
				Swap(numSlice, j)
			}
		}
	}
}

func Swap(numSlice []int, index int) {
	temp := numSlice[index]
	numSlice[index] = numSlice[index+1]
	numSlice[index+1] = temp
}
