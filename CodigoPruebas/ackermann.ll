; ModuleID = "main"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

declare i32 @"printf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  %".2" = call i32 @"ackermann"(i32 2, i32 2)
  %".3" = bitcast [3 x i8]* @".str3" to i8*
  %".4" = call i32 (i8*, ...) @"printf"(i8* %".3", i32 %".2")
  ret i32 0
}

define i32 @"ackermann"(i32 %"m", i32 %"n")
{
entry:
  %"m.1" = alloca i32
  store i32 %"m", i32* %"m.1"
  %"n.1" = alloca i32
  store i32 %"n", i32* %"n.1"
  %".6" = load i32, i32* %"m.1"
  %".7" = icmp eq i32 %".6", 0
  br i1 %".7", label %"then", label %"merge"
then:
  %".9" = load i32, i32* %"n.1"
  %".10" = add i32 %".9", 1
  ret i32 %".10"
merge:
  %".12" = load i32, i32* %"n.1"
  %".13" = icmp eq i32 %".12", 0
  br i1 %".13", label %"then.1", label %"merge.1"
then.1:
  %".15" = load i32, i32* %"m.1"
  %".16" = sub i32 %".15", 1
  %".17" = call i32 @"ackermann"(i32 %".16", i32 1)
  ret i32 %".17"
merge.1:
  %".19" = load i32, i32* %"m.1"
  %".20" = sub i32 %".19", 1
  %".21" = load i32, i32* %"m.1"
  %".22" = load i32, i32* %"n.1"
  %".23" = sub i32 %".22", 1
  %".24" = call i32 @"ackermann"(i32 %".21", i32 %".23")
  %".25" = call i32 @"ackermann"(i32 %".20", i32 %".24")
  ret i32 %".25"
}

@".str3" = internal constant [3 x i8] c"%d\0a"