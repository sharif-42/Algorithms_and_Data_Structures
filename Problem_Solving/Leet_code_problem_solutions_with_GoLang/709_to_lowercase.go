package main

import (
	"fmt"
	"strings"
)

func toLowerCase(s string) string {
	return strings.ToLower(s)

}

func main() {
	s := "Hello"
	new_s := toLowerCase(s)
	fmt.Println(new_s)
}
