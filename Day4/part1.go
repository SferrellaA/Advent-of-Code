package main

import (
	"fmt"
	"strings"
	"os"
	"log"
	"bufio"
)

func handleLine(line string) bool{
	m := make(map[string]bool)
	phrase := strings.Split(line, " ")
	for _, word := range phrase {
		_, exists := m[word]
		if !exists {
			m[word] = true
		} else {
			return false
		}
	}
	return true
}

func main() {
	fmt.Println("Let's start!")
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	var count = 0

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		if handleLine(scanner.Text()) {
			count++
		}
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	fmt.Println("All done!")
	fmt.Printf("%d valid passphrases\n", count)
}