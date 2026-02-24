package main

import (
	"errors"
)

var ErrTruckNotFound = errors.New("truck not found")

type FleetManager interface {
	AddTruck(id string, cargo int) error
	GetTruck(id string) (*Truck, error)
	RemoveTruck(id string) error
	UpdateTruckCargo(id string, cargo int) error
}

func (tm *truckManager) AddTruck(id string, cargo int) error {

	tm.trucks[id] = &Truck{ID: id, Cargo: cargo}
	return nil
}

func (tm *truckManager) GetTruck(id string) (*Truck, error) {
	value, exists := tm.trucks[id]
	if !exists {
		return nil, ErrTruckNotFound
	}
	return value, nil
}

func (tm *truckManager) RemoveTruck(id string) error {
	_, exists := tm.trucks[id]
	if !exists {
		return ErrTruckNotFound
	}
	delete(tm.trucks, id)
	return nil
}

func (tm *truckManager) UpdateTruckCargo(id string, cargo int) error {
	_, exists := tm.trucks[id]
	if !exists {
		return ErrTruckNotFound
	}
	tm.trucks[id].Cargo = cargo
	return nil
}

type Truck struct {
	ID    string
	Cargo int
}

type truckManager struct {
	trucks map[string]*Truck
}

func NewTruckManager() truckManager {
	return truckManager{
		trucks: make(map[string]*Truck),
	}
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

// Solution for Contains Duplicate
// func containsDuplicate(nums []int) bool {
// 	seen := make(map[int]int)

// 	for i := 0; i < len(nums); i++ {
// 		_, found := seen[nums[i]]
// 		if found {
// 			return true
// 		}
// 		seen[nums[i]] = i
// 	}
// 	return false
// }
