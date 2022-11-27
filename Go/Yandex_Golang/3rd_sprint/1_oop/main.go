package main

import (
	"fmt"
	"time"
)

//Реализуйте тип Stopwatch, который будет сохранять время каждой промежуточной фиксации секундомера и выдавать
//результаты относительно общего времени старта.
//Тип должен обладать следующими методами:
//Start() — запустить/сбросить секундомер;
//SaveSplit() — сохранить промежуточное время;
//GetResults() []time.Duration — вернуть текущие результаты.

type Stopwatch struct {
	start     time.Time
	durations []time.Duration
}

func (st *Stopwatch) Start() {
	st.start = time.Now()
}

func (st *Stopwatch) SaveSplit() {
	current := time.Now()
	st.durations = append(st.durations, current.Sub(st.start))
}

func (st *Stopwatch) GetResults() []time.Duration {
	return st.durations
}

func main() {
	sw := Stopwatch{}
	sw.Start()

	time.Sleep(1 * time.Second)
	sw.SaveSplit()

	time.Sleep(500 * time.Millisecond)
	sw.SaveSplit()

	time.Sleep(300 * time.Millisecond)
	sw.SaveSplit()

	fmt.Println(sw.GetResults())
}
