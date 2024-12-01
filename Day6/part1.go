package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func handleBig(array []int) []int {
	X := 0
	I := array[X]
	for x, i := range array {
		if i > I {
			X = x
			I = i
		}
	}
	array[X] = 0
	for I > 0 {
		if X == len(array)-1 {
			X = 0
		} else {
			X++
		}
		array[X]++
		I--
	}

	return array
}

func main() {
	var array []int
	content, _ := os.ReadFile("input.txt")
	for _, i := range strings.Split(string(content), "\t") {
		x, _ := strconv.Atoi(i)
		array = append(array, x)
	}

	//array = []int{0, 2, 7, 0}
	//fmt.Println(handleBig(array))

	var past map[string]bool
	past = make(map[string]bool)
	past[fmt.Sprint(array)] = true
	steps := 0

	for true {
		steps++
		array = handleBig(array)
		sa := fmt.Sprint(array)
		fmt.Println(steps, sa)
		if past[sa] == true {
			fmt.Println(steps)
			os.Exit(0)
		} else {
			past[sa] = true
		}
	}
}
