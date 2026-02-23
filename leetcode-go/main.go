package main

import "fmt"

func containsDuplicate(nums []int) bool {
	seen := make(map[int]int)

	for i := 0; i < len(nums); i++ {
		_, found := seen[nums[i]]
		if found {
			return true
		}
		seen[nums[i]] = i
	}
	return false
}

func main() {
	nums := []int{2, 7, 11, 15}

	result := containsDuplicate(nums)
	fmt.Println("Result:", result)
}

//Solution for Two SUM problem
// func twoSum(nums []int, target int) []int {

// 	seen_map := make(map[int]int)

// 	for index, value := range nums {
// 		val, found := seen_map[target-value]
// 		if found {
// 			return []int{val, index}
// 		}
// 		seen_map[value] = index
// 	}

// 	return []int{}
// }
