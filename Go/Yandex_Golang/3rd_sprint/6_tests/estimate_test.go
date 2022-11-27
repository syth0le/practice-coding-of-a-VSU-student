package main

import (
	"testing"
)

func EstimateValue(value int) string {
	switch {
	case value < 10:
		return "small"

	case value < 100:
		return "medium"

	default:
		return "big"
	}
}

func TestEstimateValue(t *testing.T) {
	t.Run("< 10", func(t *testing.T) {
		result := EstimateValue(9)
		if result != "small" {
			t.Error("error")
		}
	})
	t.Run("< 100", func(t *testing.T) {
		result := EstimateValue(99)
		if result != "medium" {
			t.Error("error")
		}
	})
	t.Run("default", func(t *testing.T) {
		result := EstimateValue(101)
		if result != "big" {
			t.Error("error")
		}
	})
}

func TestEstimateValueTableDriven(t *testing.T) {
	testCases := []struct {
		Name          string
		InputValue    int
		ExpectedValue string
	}{
		{
			Name:          "Small",
			InputValue:    9,
			ExpectedValue: "small",
		},
		{
			Name:          "Medium",
			InputValue:    99,
			ExpectedValue: "medium",
		},
		{
			Name:          "Big",
			InputValue:    100,
			ExpectedValue: "big",
		},
	}

	for _, tc := range testCases {
		t.Run(tc.Name, func(t *testing.T) {
			result := EstimateValue(tc.InputValue)
			if result != tc.ExpectedValue {
				t.Error("error")
			}
		})
	}
}
