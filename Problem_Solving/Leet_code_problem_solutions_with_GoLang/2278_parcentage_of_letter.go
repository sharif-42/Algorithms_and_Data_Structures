package main

import (
	"fmt"
	// "strings"
)

func percentageLetter(s string, letter byte) int {
    count := 0

    for i := range s {
        if s[i] == letter {
            count++
        }
    }

    return int(count * 100 / len(s))
}

func main() {
	s := "ssawtb"
	var letter byte = 's'
	fmt.Println(percentageLetter(s, letter))
}
