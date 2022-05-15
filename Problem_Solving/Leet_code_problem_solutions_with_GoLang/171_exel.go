package main

import "fmt"

func titleToNumber(columnTitle string) int {
	ans := 0
	for i := 0; i < len(columnTitle); i++ {
		num := int(columnTitle[i]) - int('A') + 1
		ans = ans*26 + num
	}
	return ans
}

func main() {
	columnTitle := "AB"
	fmt.Println(titleToNumber(columnTitle))

}
