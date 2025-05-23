; ModuleID = "main"
target triple = "unknown-unknown-unknown"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  %".2" = call i32 @"fibonacci"(i32 10)
  %".3" = bitcast [3 x i8]* @".str3" to i8*
  %".4" = call i32 (i8*, ...) @"printf"(i8* %".3", i32 %".2")
  ret i32 0
}

define i32 @"fibonacci"(i32 %"n")
{
entry:
  %"n.1" = alloca i32
  store i32 %"n", i32* %"n.1"
  %".4" = load i32, i32* %"n.1"
  %".5" = icmp sle i32 %".4", 1
  br i1 %".5", label %"then", label %"merge"
then:
  %".7" = load i32, i32* %"n.1"
  ret i32 %".7"
merge:
  %".9" = load i32, i32* %"n.1"
  %".10" = sub i32 %".9", 1
  %".11" = call i32 @"fibonacci"(i32 %".10")
  %".12" = load i32, i32* %"n.1"
  %".13" = sub i32 %".12", 2
  %".14" = call i32 @"fibonacci"(i32 %".13")
  %".15" = add i32 %".11", %".14"
  ret i32 %".15"
}

@".str3" = internal constant [3 x i8] c"%d\0a"