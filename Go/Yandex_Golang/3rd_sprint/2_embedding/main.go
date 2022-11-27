package main

import (
	"log"
	"os"
)

//В стандартной библиотеке Go уже есть логгер — в пакете log. У этой реализации отсутствует параметр уровня лога
//(log level), то есть для вывода есть только метод log.Println и log.Printf. Предлагаем расширить этот объект следующими методами:
//SetLogLevel(logLvl LogLevel);
//Infoln(msg string);
//Warnln(msg string);
//Errorln(msg string).
//LogLevel — перечисление с такими возможными значениями:
//Info;
//Warning;
//Error.
//Логгер можно писать долго, прикручивая множество нужных фич, но стоит остановиться на простом расширении типа.
//Функции Infoln, Warnln и Errorln должны оборачивать метод log.Println, добавляя соответствующий префикс.

type LogLevel int

func (l LogLevel) IsValid() bool {
	switch l {
	case LogLevelInfo, LogLevelWarning, LogLevelError:
		return true
	default:
		return false
	}
}

const (
	LogLevelError LogLevel = iota
	LogLevelWarning
	LogLevelInfo
)

type LogExtended struct {
	*log.Logger
	logLevel LogLevel
}

func NewLogExtended() *LogExtended {
	return &LogExtended{
		Logger:   log.New(os.Stderr, "", log.LstdFlags),
		logLevel: LogLevelError,
	}
}

func (l *LogExtended) SetLogLevel(logLevel LogLevel) {
	if !logLevel.IsValid() {
		return
	}
	l.logLevel = logLevel
}

func (l *LogExtended) println(srcLogLvl LogLevel, prefix, msg string) {
	if l.logLevel < srcLogLvl {
		return
	}

	l.Logger.Println(prefix + msg)
}

func (l *LogExtended) Infoln(s string) {
	l.println(LogLevelInfo, "INFO ", s)
}

func (l *LogExtended) Warnln(s string) {
	l.println(LogLevelWarning, "WARN ", s)
}

func (l *LogExtended) Errorln(s string) {
	l.println(LogLevelError, "ERR ", s)
}

func main() {
	logger := NewLogExtended()
	logger.SetLogLevel(LogLevelWarning)
	logger.Infoln("Не должно напечататься")
	logger.Warnln("Hello")
	logger.Errorln("World")
	logger.Println("Debug")
}
