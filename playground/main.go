package main

import (
	"fmt"
	"log"
	"strconv"
	"strings"
)

func Factorial(n int) int {
	if n <= 1 {
		return 1
	}
	return n * Factorial(n-1)
}

func sumOfDigits(n int) int {
	var sum int = 0
	for temp := n; temp != 0; temp = temp / 10 {
		remainder := temp % 10
		sum = sum + remainder
	}
	return sum
}

func main() {
	var i int
	fmt.Scan(&i)
	for index := 0; index < i; index++ {
		var n, d int
		var arr []int
		fmt.Scan(&n, &d)
		var x int = Factorial(n)
		number_big := strings.Repeat(strconv.Itoa(d), x)
		num, err := strconv.Atoi(number_big)

		if err != nil {
			log.Fatal(err)
		}
		if num%3 == 0 {
			arr = append(arr, 3)
		}
		if num%1 == 0 {
			arr = append(arr, 1)
		}
		if num%5 == 0 {
			arr = append(arr, 5)
		}
		if num%7 == 0 {
			arr = append(arr, 7)
		}
		if num%9 == 0 {
			arr = append(arr, 9)
		}
		fmt.Print(arr)
	}
}
