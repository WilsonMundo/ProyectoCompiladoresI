; ModuleID = "main"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"


declare i32 @"printf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  %"valor" = alloca i32
  store i32 0, i32* %"valor"
  %".3" = call i32 @"bubbleSort3"(i32 3, i32 1, i32 2)
  store i32 %".3", i32* %"valor"
  %".5" = call i32 @"selectionSort3"(i32 3, i32 1, i32 2)
  store i32 %".5", i32* %"valor"
  %".7" = call i32 @"insertionSort3"(i32 3, i32 1, i32 2)
  store i32 %".7", i32* %"valor"
  ret i32 0
}

define i32 @"bubbleSort3"(i32 %"a", i32 %"b", i32 %"c")
{
entry:
  %"a.1" = alloca i32
  store i32 %"a", i32* %"a.1"
  %"b.1" = alloca i32
  store i32 %"b", i32* %"b.1"
  %"c.1" = alloca i32
  store i32 %"c", i32* %"c.1"
  %"x" = alloca i32
  %".8" = load i32, i32* %"a.1"
  store i32 %".8", i32* %"x"
  %"y" = alloca i32
  %".10" = load i32, i32* %"b.1"
  store i32 %".10", i32* %"y"
  %"z" = alloca i32
  %".12" = load i32, i32* %"c.1"
  store i32 %".12", i32* %"z"
  %"temp" = alloca i32
  store i32 0, i32* %"temp"
  %".15" = load i32, i32* %"x"
  %".16" = load i32, i32* %"y"
  %".17" = icmp sgt i32 %".15", %".16"
  br i1 %".17", label %"then", label %"merge"
then:
  %".19" = load i32, i32* %"x"
  store i32 %".19", i32* %"temp"
  %".21" = load i32, i32* %"y"
  store i32 %".21", i32* %"x"
  %".23" = load i32, i32* %"temp"
  store i32 %".23", i32* %"y"
  br label %"merge"
merge:
  %".26" = load i32, i32* %"y"
  %".27" = load i32, i32* %"z"
  %".28" = icmp sgt i32 %".26", %".27"
  br i1 %".28", label %"then.1", label %"merge.1"
then.1:
  %".30" = load i32, i32* %"y"
  store i32 %".30", i32* %"temp"
  %".32" = load i32, i32* %"z"
  store i32 %".32", i32* %"y"
  %".34" = load i32, i32* %"temp"
  store i32 %".34", i32* %"z"
  br label %"merge.1"
merge.1:
  %".37" = load i32, i32* %"x"
  %".38" = load i32, i32* %"y"
  %".39" = icmp sgt i32 %".37", %".38"
  br i1 %".39", label %"then.2", label %"merge.2"
then.2:
  %".41" = load i32, i32* %"x"
  store i32 %".41", i32* %"temp"
  %".43" = load i32, i32* %"y"
  store i32 %".43", i32* %"x"
  %".45" = load i32, i32* %"temp"
  store i32 %".45", i32* %"y"
  br label %"merge.2"
merge.2:
  %".48" = load i32, i32* %"x"
  %".49" = load i32, i32* %"y"
  %".50" = load i32, i32* %"z"
  %".51" = bitcast [3 x i8]* @".str3" to i8*
  %".52" = call i32 (i8*, ...) @"printf"(i8* %".51", i32 %".48")
  %".53" = bitcast [3 x i8]* @".str4" to i8*
  %".54" = call i32 (i8*, ...) @"printf"(i8* %".53", i32 %".49")
  %".55" = bitcast [3 x i8]* @".str5" to i8*
  %".56" = call i32 (i8*, ...) @"printf"(i8* %".55", i32 %".50")
  ret i32 0
}

@".str3" = internal constant [3 x i8] c"%d\0a"
@".str4" = internal constant [3 x i8] c"%d\0a"
@".str5" = internal constant [3 x i8] c"%d\0a"
define i32 @"selectionSort3"(i32 %"a", i32 %"b", i32 %"c")
{
entry:
  %"a.1" = alloca i32
  store i32 %"a", i32* %"a.1"
  %"b.1" = alloca i32
  store i32 %"b", i32* %"b.1"
  %"c.1" = alloca i32
  store i32 %"c", i32* %"c.1"
  %"x" = alloca i32
  %".8" = load i32, i32* %"a.1"
  store i32 %".8", i32* %"x"
  %"y" = alloca i32
  %".10" = load i32, i32* %"b.1"
  store i32 %".10", i32* %"y"
  %"z" = alloca i32
  %".12" = load i32, i32* %"c.1"
  store i32 %".12", i32* %"z"
  %"temp" = alloca i32
  store i32 0, i32* %"temp"
  %".15" = load i32, i32* %"x"
  %".16" = load i32, i32* %"y"
  %".17" = icmp sgt i32 %".15", %".16"
  br i1 %".17", label %"then", label %"merge"
then:
  %".19" = load i32, i32* %"x"
  store i32 %".19", i32* %"temp"
  %".21" = load i32, i32* %"y"
  store i32 %".21", i32* %"x"
  %".23" = load i32, i32* %"temp"
  store i32 %".23", i32* %"y"
  br label %"merge"
merge:
  %".26" = load i32, i32* %"x"
  %".27" = load i32, i32* %"z"
  %".28" = icmp sgt i32 %".26", %".27"
  br i1 %".28", label %"then.1", label %"merge.1"
then.1:
  %".30" = load i32, i32* %"x"
  store i32 %".30", i32* %"temp"
  %".32" = load i32, i32* %"z"
  store i32 %".32", i32* %"x"
  %".34" = load i32, i32* %"temp"
  store i32 %".34", i32* %"z"
  br label %"merge.1"
merge.1:
  %".37" = load i32, i32* %"y"
  %".38" = load i32, i32* %"z"
  %".39" = icmp sgt i32 %".37", %".38"
  br i1 %".39", label %"then.2", label %"merge.2"
then.2:
  %".41" = load i32, i32* %"y"
  store i32 %".41", i32* %"temp"
  %".43" = load i32, i32* %"z"
  store i32 %".43", i32* %"y"
  %".45" = load i32, i32* %"temp"
  store i32 %".45", i32* %"z"
  br label %"merge.2"
merge.2:
  %".48" = load i32, i32* %"x"
  %".49" = load i32, i32* %"y"
  %".50" = load i32, i32* %"z"
  %".51" = bitcast [3 x i8]* @".str7" to i8*
  %".52" = call i32 (i8*, ...) @"printf"(i8* %".51", i32 %".48")
  %".53" = bitcast [3 x i8]* @".str8" to i8*
  %".54" = call i32 (i8*, ...) @"printf"(i8* %".53", i32 %".49")
  %".55" = bitcast [3 x i8]* @".str9" to i8*
  %".56" = call i32 (i8*, ...) @"printf"(i8* %".55", i32 %".50")
  ret i32 0
}

@".str7" = internal constant [3 x i8] c"%d\0a"
@".str8" = internal constant [3 x i8] c"%d\0a"
@".str9" = internal constant [3 x i8] c"%d\0a"
define i32 @"insertionSort3"(i32 %"a", i32 %"b", i32 %"c")
{
entry:
  %"a.1" = alloca i32
  store i32 %"a", i32* %"a.1"
  %"b.1" = alloca i32
  store i32 %"b", i32* %"b.1"
  %"c.1" = alloca i32
  store i32 %"c", i32* %"c.1"
  %"x" = alloca i32
  %".8" = load i32, i32* %"a.1"
  store i32 %".8", i32* %"x"
  %"y" = alloca i32
  %".10" = load i32, i32* %"b.1"
  store i32 %".10", i32* %"y"
  %"z" = alloca i32
  %".12" = load i32, i32* %"c.1"
  store i32 %".12", i32* %"z"
  %"temp" = alloca i32
  store i32 0, i32* %"temp"
  %".15" = load i32, i32* %"y"
  %".16" = load i32, i32* %"x"
  %".17" = icmp slt i32 %".15", %".16"
  br i1 %".17", label %"then", label %"merge"
then:
  %".19" = load i32, i32* %"x"
  store i32 %".19", i32* %"temp"
  %".21" = load i32, i32* %"y"
  store i32 %".21", i32* %"x"
  %".23" = load i32, i32* %"temp"
  store i32 %".23", i32* %"y"
  br label %"merge"
merge:
  %".26" = load i32, i32* %"z"
  %".27" = load i32, i32* %"y"
  %".28" = icmp slt i32 %".26", %".27"
  br i1 %".28", label %"then.1", label %"merge.1"
then.1:
  %".30" = load i32, i32* %"y"
  store i32 %".30", i32* %"temp"
  %".32" = load i32, i32* %"z"
  store i32 %".32", i32* %"y"
  %".34" = load i32, i32* %"temp"
  store i32 %".34", i32* %"z"
  %".36" = load i32, i32* %"y"
  %".37" = load i32, i32* %"x"
  %".38" = icmp slt i32 %".36", %".37"
  br i1 %".38", label %"then.2", label %"merge.2"
merge.1:
  %".48" = load i32, i32* %"x"
  %".49" = load i32, i32* %"y"
  %".50" = load i32, i32* %"z"
  %".51" = bitcast [3 x i8]* @".str11" to i8*
  %".52" = call i32 (i8*, ...) @"printf"(i8* %".51", i32 %".48")
  %".53" = bitcast [3 x i8]* @".str12" to i8*
  %".54" = call i32 (i8*, ...) @"printf"(i8* %".53", i32 %".49")
  %".55" = bitcast [3 x i8]* @".str13" to i8*
  %".56" = call i32 (i8*, ...) @"printf"(i8* %".55", i32 %".50")
  ret i32 0
then.2:
  %".40" = load i32, i32* %"x"
  store i32 %".40", i32* %"temp"
  %".42" = load i32, i32* %"y"
  store i32 %".42", i32* %"x"
  %".44" = load i32, i32* %"temp"
  store i32 %".44", i32* %"y"
  br label %"merge.2"
merge.2:
  br label %"merge.1"
}

@".str11" = internal constant [3 x i8] c"%d\0a"
@".str12" = internal constant [3 x i8] c"%d\0a"
@".str13" = internal constant [3 x i8] c"%d\0a"