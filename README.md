# SleepSort

I first came across the concept of a _sleepsort_ while viewing a recording of
the Kevlin Henney talk _"Get Kata"_. The talk revolves around the value of
practice exercises for software engineers. During the Q&A portion of the talk,
a member of the audience brings up sleep sort and, among other things, Kevlin
has this to say about it:

> It is beautiful in a way that is insane.

You can catch the sleepsort portion at [1:11:10](https://www.youtube.com/watch?v=_M4o0ExLQCs&feature=youtu.be&t=4270) of [the talk](https://www.youtube.com/watch?v=_M4o0ExLQCs).

Kevlin shares an Unix shell implementation that looks like this:

```sh
while [ -n "$1" ]
do
    (sleep $1; echo $1) &
    shift
done
wait
```

The program expects a list of numbers. For each number _N_, a sub-shell is
spawned with a single task. Wait for _N_ seconds, then display _N_. Lower
numbers will naturally appear earlier than higher numbers with the resulting
output being a sorted list of numbers.

Is this practical? Of course not. If your highest value is around 3600, for
example, you are looking at waiting an hour for results, even with two value.
However, an efficient sort is that what I am looking for. I feel _sleepsort_
makes for a rather elegant means for  practicing concurrent programming in a
variety of languages.

# Goal & Purpose

This repository will host my various attempts at implementing _sleepsort_.
I may reimplement _sleepsort_ multiple times in the same language. I intend
to keep each implementation self contained. The interface will follow Kevlin
Henney's shell example (i.e. Numbers are given as command-line arguments).
Any necessary build parameters will be provided as comments at the top of
source files.
