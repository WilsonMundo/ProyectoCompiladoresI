; ModuleID = "main"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"sprintf"(i8* %".1", i8* %".2", ...)

define i32 @"main"()
{
entry:
  %"a" = alloca i32
  store i32 35, i32* %"a"
  %".3" = bitcast [17 x i8]* @".str3" to i8*
  %".4" = load i32, i32* %"a"
  %".5" = bitcast [7 x i8]* @".str4" to i8*
  %".6" = call i32 (i8*, ...) @"printf"(i8* %".5", i8* %".3", i32 %".4")
  %".7" = bitcast [6 x i8]* @".str5" to i8*
  %".8" = bitcast [4 x i8]* @".str6" to i8*
  %".9" = call i32 (i8*, ...) @"printf"(i8* %".8", i8* %".7")
  ret i32 0
}

@".str3" = internal constant [17 x i8] c"El valor de a es\00"
@".str4" = internal constant [7 x i8] c"%s %d\0a\00"
@".str5" = internal constant [6 x i8] c"datos\00"
@".str6" = internal constant [4 x i8] c"%s\0a\00"