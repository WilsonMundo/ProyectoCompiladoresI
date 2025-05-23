; ModuleID = "main"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"sprintf"(i8* %".1", i8* %".2", ...)

define i32 @"main"()
{
entry:
  %"num" = alloca i32
  store i32 7, i32* %"num"
  %"doble" = alloca i32
  %".3" = load i32, i32* %"num"
  %".4" = call i32 @"dobleViaSuma"(i32 %".3")
  store i32 %".4", i32* %"doble"
  %".6" = bitcast [7 x i8]* @".str6" to i8*
  %".7" = load i32, i32* %"doble"
  %".8" = bitcast [7 x i8]* @".str7" to i8*
  %".9" = call i32 (i8*, ...) @"printf"(i8* %".8", i8* %".6", i32 %".7")
  %"suma10" = alloca i32
  %".10" = call i32 @"sumatoria"(i32 10)
  store i32 %".10", i32* %"suma10"
  %".12" = bitcast [17 x i8]* @".str8" to i8*
  %".13" = load i32, i32* %"suma10"
  %".14" = bitcast [7 x i8]* @".str9" to i8*
  %".15" = call i32 (i8*, ...) @"printf"(i8* %".14", i8* %".12", i32 %".13")
  %"par" = alloca i1
  %".16" = load i32, i32* %"num"
  %".17" = call i1 @"esPar"(i32 %".16")
  store i1 %".17", i1* %"par"
  %".19" = bitcast [11 x i8]* @".str10" to i8*
  %".20" = load i1, i1* %"par"
  %".21" = bitcast [7 x i8]* @".str11" to i8*
  %".22" = call i32 (i8*, ...) @"printf"(i8* %".21", i8* %".19", i1 %".20")
  ret i32 0
}

define i32 @"dobleViaSuma"(i32 %"x")
{
entry:
  %"x.1" = alloca i32
  store i32 %"x", i32* %"x.1"
  %"sum" = alloca i32
  store i32 0, i32* %"sum"
  %"i" = alloca i32
  store i32 0, i32* %"i"
  store i32 0, i32* %"i"
  br label %"for.cond"
for.cond:
  %".8" = load i32, i32* %"i"
  %".9" = icmp slt i32 %".8", 2
  br i1 %".9", label %"for.body", label %"for.exit"
for.body:
  %".11" = load i32, i32* %"sum"
  %".12" = load i32, i32* %"x.1"
  %".13" = add i32 %".11", %".12"
  store i32 %".13", i32* %"sum"
  br label %"for.step"
for.step:
  %".16" = load i32, i32* %"i"
  %".17" = add i32 %".16", 1
  store i32 %".17", i32* %"i"
  br label %"for.cond"
for.exit:
  %".20" = load i32, i32* %"sum"
  ret i32 %".20"
}

define i32 @"sumatoria"(i32 %"n")
{
entry:
  %"n.1" = alloca i32
  store i32 %"n", i32* %"n.1"
  %"acc" = alloca i32
  store i32 0, i32* %"acc"
  %"i" = alloca i32
  store i32 1, i32* %"i"
  store i32 1, i32* %"i"
  br label %"for.cond"
for.cond:
  %".8" = load i32, i32* %"i"
  %".9" = load i32, i32* %"n.1"
  %".10" = icmp sle i32 %".8", %".9"
  br i1 %".10", label %"for.body", label %"for.exit"
for.body:
  %".12" = load i32, i32* %"acc"
  %".13" = load i32, i32* %"i"
  %".14" = add i32 %".12", %".13"
  store i32 %".14", i32* %"acc"
  br label %"for.step"
for.step:
  %".17" = load i32, i32* %"i"
  %".18" = add i32 %".17", 1
  store i32 %".18", i32* %"i"
  br label %"for.cond"
for.exit:
  %".21" = load i32, i32* %"acc"
  ret i32 %".21"
}

define i1 @"esPar"(i32 %"n")
{
entry:
  %"n.1" = alloca i32
  store i32 %"n", i32* %"n.1"
  %"d" = alloca i32
  store i32 0, i32* %"d"
  br label %"while.cond"
while.cond:
  %".6" = load i32, i32* %"d"
  %".7" = icmp sgt i32 %".6", 1
  br i1 %".7", label %"while.body", label %"while.exit"
while.body:
  %".9" = load i32, i32* %"n.1"
  %".10" = sub i32 %".9", 2
  store i32 %".10", i32* %"d"
  br label %"while.cond"
while.exit:
  %".13" = load i32, i32* %"n.1"
  %".14" = icmp eq i32 %".13", 0
  ret i1 %".14"
}

@".str6" = internal constant [7 x i8] c"doble:\00"
@".str7" = internal constant [7 x i8] c"%s %d\0a\00"
@".str8" = internal constant [17 x i8] c"sumatoria 1..10:\00"
@".str9" = internal constant [7 x i8] c"%s %d\0a\00"
@".str10" = internal constant [11 x i8] c"\c2\bfes par?:\00"
@".str11" = internal constant [7 x i8] c"%s %d\0a\00"