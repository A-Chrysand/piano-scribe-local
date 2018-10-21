package main

import "net/http"
import "fmt"

func main() {
	fmt.Println("http://127.0.0.1:8080")
	panic(http.ListenAndServe(":8080", http.FileServer(http.Dir("./"))))
}
