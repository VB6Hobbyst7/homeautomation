#!/bin/bash


case $1 in

home)
	curl -X POST 'http://192.168.0.198:8060/keypress/home'
	;;

play)
	curl -X POST 'http://192.168.0.198:8060/keypress/play' 
	;;

sel)
	curl -X POST 'http://192.168.0.198:8060/keypress/select'
	;;

left)
	curl -X POST 'http://192.168.0.198:8060/keypress/left'
	;;

right)
	curl -X POST 'http://192.168.0.198:8060/keypress/right'
	;;

down)
	curl -X POST 'http://192.168.0.198:8060/keypress/down'
	;;

up)
	curl -X POST 'http://192.168.0.198:8060/keypress/up'
	;;

back)
	curl -X POST 'http://192.168.0.198:8060/keypress/back'
	;;

rev)
	curl -X POST 'http://192.168.0.198:8060/keypress/rev'
	;;

fwd)
	curl -X POST 'http://192.168.0.198:8060/keypress/fwd'
	;;

info)
	curl -X POST 'http://192.168.0.198:8060/keypress/info'
	;;

*)
	echo "home play left right down up sel back rev fwd info"

esac
