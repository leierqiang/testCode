// 选择语句 switch
package main

import "fmt"

func main() {
	num := 2
	switch num { // switch后面写的是变量本身
	case 1:
		fmt.Printf("按下的是1楼\n")
		//break //go语言默认带跳出，要是不用跳出可以带fallthrough
	case 2:
		fmt.Printf("按下的是2楼\n")
		fallthrough
	case 3:
		fmt.Printf("按下的是3楼\n")
	}
	score := 85
	switch {
	case score > 90:
		fmt.Println("当前大于90")
	default:
		fmt.Println("当没有符合的case时默认输出这句话")
	}
}
