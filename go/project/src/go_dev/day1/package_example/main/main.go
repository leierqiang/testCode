package main

import (
	"fmt"
	"go_dev/day1/package_example/calc" // 导入的包需要写与GOPATH的相对路径
)

func main() {
	sum := calc.Add(100, 200)
	sub := calc.Sub(100, 200)

	fmt.Println("Sum=", sum)
	fmt.Println("Sub=", sub)
}

// 构建 go build go_dev\day1\package_example\main
