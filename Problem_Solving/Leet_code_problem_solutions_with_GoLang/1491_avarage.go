package main

import "fmt"

func min_max(array []int) (int, int) {
	var min int = array[0]
	var max int = array[0]

	for _, value := range array {
		if min > value {
			min = value
		}
		if max < value {
			max = value
		}
	}
	return min, max
}

func get_index(array []int, search_value int) int {
	var search_index int = 0

	for index, value := range array {
		if value == search_value {
			search_index = index
		}
	}
	return search_index
}

func get_sum_of_salary(array []int) float64 {
	var sum float64 = 0

	for _, value := range array {
		sum += float64(value)
	}
	return sum
}

func average(salary []int) float64 {
	var avg float64 = 0
	min, max := min_max(salary)
	min_index := get_index(salary, min)
	salary = append(salary[:min_index], salary[min_index+1:]...)

	max_index := get_index(salary, max)
	salary = append(salary[:max_index], salary[max_index+1:]...)

	sum := get_sum_of_salary(salary)

	avg = (sum / float64(len(salary)))
	return avg
}

func main() {
	salary := []int{4000, 3000, 1000, 2000}
	avg := average(salary)
	fmt.Println(avg)
	// min, max := min_max(salary)

	// min_index := get_index(salary, min)
	// salary = append(salary[:min_index], salary[min_index+1:]...)

	// max_index := get_index(salary, max)
	// salary = append(salary[:max_index], salary[max_index+1:]...)

	// sum := get_sum_of_salary(salary)
	// fmt.Println(sum / float32(len(salary)))
}
