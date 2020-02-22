package main

import "time"

func main() {
	for i := 0; i < 100; i++ {
		go testGoroute(i)
	}

	time.Sleep(time.Second)
}

// 编辑的时候 go build go_dev/day1/goroute
