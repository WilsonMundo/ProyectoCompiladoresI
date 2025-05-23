; ModuleID = "main"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"sprintf"(i8* %".1", i8* %".2", ...)

define i32 @"main"()
{
entry:
  %"n" = alloca i32
  store i32 5, i32* %"n"
  %"m" = alloca i32
  store i32 7, i32* %"m"
  %"r" = alloca i32
  %".4" = load i32, i32* %"n"
  %".5" = load i32, i32* %"m"
  %".6" = call i32 @"suma"(i32 %".4", i32 %".5")
  store i32 %".6", i32* %"r"
  %".8" = bitcast [11 x i8]* @".str8" to i8*
  %".9" = load i32, i32* %"n"
  %".10" = bitcast [2 x i8]* @".str9" to i8*
  %".11" = load i32, i32* %"m"
  %".12" = bitcast [3 x i8]* @".str10" to i8*
  %".13" = load i32, i32* %"r"
  %".14" = bitcast [19 x i8]* @".str11" to i8*
  %".15" = call i32 (i8*, ...) @"printf"(i8* %".14", i8* %".8", i32 %".9", i8* %".10", i32 %".11", i8* %".12", i32 %".13")
  %"msj" = alloca i8*
  %".16" = bitcast [6 x i8]* @".str12" to i8*
  %".17" = bitcast [6 x i8]* @".str13" to i8*
  %".18" = call i8* @"concat"(i8* %".16", i8* %".17")
  store i8* %".18", i8** %"msj"
  %".20" = load i8*, i8** %"msj"
  %".21" = bitcast [4 x i8]* @".str14" to i8*
  %".22" = call i32 (i8*, ...) @"printf"(i8* %".21", i8* %".20")
  %"par" = alloca i1
  %".23" = load i32, i32* %"r"
  %".24" = call i1 @"esPar"(i32 %".23")
  store i1 %".24", i1* %"par"
  %".26" = bitcast [18 x i8]* @".str15" to i8*
  %".27" = load i1, i1* %"par"
  %".28" = bitcast [7 x i8]* @".str16" to i8*
  %".29" = call i32 (i8*, ...) @"printf"(i8* %".28", i8* %".26", i1 %".27")
  ret i32 0
}

define i32 @"suma"(i32 %"x", i32 %"y")
{
entry:
  %"x.1" = alloca i32
  store i32 %"x", i32* %"x.1"
  %"y.1" = alloca i32
  store i32 %"y", i32* %"y.1"
  %".6" = load i32, i32* %"x.1"
  %".7" = load i32, i32* %"y.1"
  %".8" = add i32 %".6", %".7"
  ret i32 %".8"
}

define i8* @"concat"(i8* %"a", i8* %"b")
{
entry:
  %"a.1" = alloca i8*
  store i8* %"a", i8** %"a.1"
  %"b.1" = alloca i8*
  store i8* %"b", i8** %"b.1"
  %".6" = load i8*, i8** %"a.1"
  %".7" = load i8*, i8** %"b.1"
  %".8" = bitcast [128 x i8]* @"concat_str5" to i8*
  %".9" = bitcast [6 x i8]* @".str6" to i8*
  %".10" = call i32 (i8*, i8*, ...) @"sprintf"(i8* %".8", i8* %".9", i8* %".6", i8* %".7")
  ret i8* %".8"
}

@"concat_str5" = internal global [128 x i8] c"\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00"
@".str6" = internal constant [6 x i8] c"%s%s\0a\00"
define i1 @"esPar"(i32 %"n")
{
entry:
  %"n.1" = alloca i32
  store i32 %"n", i32* %"n.1"
  %".4" = load i32, i32* %"n.1"
  %".5" = srem i32 %".4", 2
  %".6" = icmp eq i32 %".5", 0
  br i1 %".6", label %"then", label %"else"
then:
  ret i1 1
else:
  ret i1 0
merge:
  ret i1 0
}

@".str8" = internal constant [11 x i8] c"La suma de\00"
@".str9" = internal constant [2 x i8] c"y\00"
@".str10" = internal constant [3 x i8] c"es\00"
@".str11" = internal constant [19 x i8] c"%s %d %s %d %s %d\0a\00"
@".str12" = internal constant [6 x i8] c"Hola \00"
@".str13" = internal constant [6 x i8] c"mundo\00"
@".str14" = internal constant [4 x i8] c"%s\0a\00"
@".str15" = internal constant [18 x i8] c"\c2\bfLa suma es par?\00"
@".str16" = internal constant [7 x i8] c"%s %d\0a\00"