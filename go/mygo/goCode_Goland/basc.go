package main

import "fmt"  //Printf 和 Println 在fmt库中

//声明变量
func variableZeroValue()  {
	var a  int
	var s string
	//fmt.Println(a, s)
	fmt.Printf("%d %q\n", a, s)
}

//初始化变量
func variableInitialValue() {
	var a, b int  = 3, 4
	var s string = "abc"
	fmt.Println(a, b, s)
}

func main() {
	//fmt.Print("hello world")
	variableZeroValue()
	variableInitialValue()
}
