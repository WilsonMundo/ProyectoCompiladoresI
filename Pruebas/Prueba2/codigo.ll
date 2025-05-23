; ModuleID = "main"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"sprintf"(i8* %".1", i8* %".2", ...)

define i32 @"main"()
{
entry:
  %"res1" = alloca i32
  %".2" = call i32 @"cuadradoConstante"(i32 5)
  store i32 %".2", i32* %"res1"
  %".4" = bitcast [10 x i8]* @".str6" to i8*
  %".5" = load i32, i32* %"res1"
  %".6" = bitcast [7 x i8]* @".str7" to i8*
  %".7" = call i32 (i8*, ...) @"printf"(i8* %".6", i8* %".4", i32 %".5")
  %"res2" = alloca i32
  %".8" = call i32 @"sumaHasta"(i32 10)
  store i32 %".8", i32* %"res2"
  %".10" = bitcast [16 x i8]* @".str8" to i8*
  %".11" = load i32, i32* %"res2"
  %".12" = bitcast [7 x i8]* @".str9" to i8*
  %".13" = call i32 (i8*, ...) @"printf"(i8* %".12", i8* %".10", i32 %".11")
  %"a" = alloca i32
  store i32 0, i32* %"a"
  %"t" = alloca i1
  store i1 1, i1* %"t"
  %"r" = alloca i1
  %".16" = load i1, i1* %"t"
  %".17" = call i1 @"dummy"(i1 %".16")
  store i1 %".17", i1* %"r"
  %".19" = load i1, i1* %"r"
  br i1 %".19", label %"then", label %"else"
then:
  store i32 1, i32* %"a"
  br label %"merge"
else:
  store i32 2, i32* %"a"
  br label %"merge"
merge:
  %".25" = bitcast [8 x i8]* @".str10" to i8*
  %".26" = load i32, i32* %"a"
  %".27" = bitcast [7 x i8]* @".str11" to i8*
  %".28" = call i32 (i8*, ...) @"printf"(i8* %".27", i8* %".25", i32 %".26")
  ret i32 0
}

define i32 @"cuadradoConstante"(i32 %"x")
{
entry:
  %"x.1" = alloca i32
  store i32 %"x", i32* %"x.1"
  %"k" = alloca i32
  store i32 16, i32* %"k"
  %".5" = load i32, i32* %"x.1"
  %".6" = mul i32 %".5", 4
  %".7" = mul i32 %".6", 4
  ret i32 %".7"
}

define i32 @"sumaHasta"(i32 %"n")
{
entry:
  %"n.1" = alloca i32
  store i32 %"n", i32* %"n.1"
  %"i" = alloca i32
  store i32 0, i32* %"i"
  %"s" = alloca i32
  store i32 0, i32* %"s"
  store i32 0, i32* %"i"
  br label %"for.cond"
for.cond:
  %".8" = load i32, i32* %"i"
  %".9" = load i32, i32* %"n.1"
  %".10" = icmp slt i32 %".8", %".9"
  br i1 %".10", label %"for.body", label %"for.exit"
for.body:
  %"tmp" = alloca i32
  %".12" = mul i32 2, 3
  store i32 %".12", i32* %"tmp"
  %".14" = load i32, i32* %"s"
  %".15" = load i32, i32* %"tmp"
  %".16" = add i32 %".14", %".15"
  store i32 %".16", i32* %"s"
  br label %"for.step"
for.step:
  %".19" = load i32, i32* %"i"
  %".20" = add i32 %".19", 1
  store i32 %".20", i32* %"i"
  br label %"for.cond"
for.exit:
  %".23" = load i32, i32* %"s"
  ret i32 %".23"
}

define i1 @"dummy"(i1 %"b")
{
entry:
  %"b.1" = alloca i1
  store i1 %"b", i1* %"b.1"
  br i1 0, label %"then", label %"merge"
then:
  %".5" = load i1, i1* %"b.1"
  %".6" = icmp eq i1 %".5", 0
  ret i1 %".6"
merge:
  %".8" = load i1, i1* %"b.1"
  ret i1 %".8"
}

@".str6" = internal constant [10 x i8] c"cuadrado:\00"
@".str7" = internal constant [7 x i8] c"%s %d\0a\00"
@".str8" = internal constant [16 x i8] c"resultado suma:\00"
@".str9" = internal constant [7 x i8] c"%s %d\0a\00"
@".str10" = internal constant [8 x i8] c"a vale:\00"
@".str11" = internal constant [7 x i8] c"%s %d\0a\00"