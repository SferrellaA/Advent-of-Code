package main

import (
	"fmt"
	"strings"
	"strconv"
	"os"
	"log"
	"bufio"
)

// De-anogram a word
func alphabetize(word string) string {

	// Count how many of each letter there are
	count := make(map[rune]int)
	for _, r := range word {
		if _, exists := count[r]; !exists {
			count[r] = 0
		}
		count[r]++
	}

	/* Explanation:
		1. Iterate through the alphabet
		2. Check if each letter has value in count
		   (The letter is in the original word)
		3. Append a letter and a number to the string
		   ex: b7, x3, a2
	*/
	alpha := ""
	for _, l := range "abcdefghijklmnopqrstuvwxyz" {
		if _, exists := count[l]; exists {
			alpha += string(l) + strconv.Itoa(count[l])
		}
	}

	// Return the sorted string 
	return alpha
}

// Read through a single line
func handleLine(line string) bool{
	m := make(map[string]bool)
	phrase := strings.Split(line, " ")
	for _, word := range phrase {
	
		// De-anagram the string
		alpha := alphabetize(word)

		// Mark the word as true if it does exists
		if _, exists := m[alpha]; !exists {
			m[alpha] = true

		// The word already exists and the phrase is invalid
		} else {
			return false
		}
	}
	return true
}

func main() {
	// Open the input file responsibly
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	// Increment valid phrases as we go
	var count = 0

	// Read the file line by line
	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanLines)
	for scanner.Scan() {
		if handleLine(scanner.Text()) {
			count++
		}
	}

	// Unlikely, but there could be errors in the input file
	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	// Print the output
	fmt.Printf("%d valid passphrases\n", count)
}