; ModuleID = "main"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

declare i32 @"printf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  %"valor" = alloca i32
  %".2" = call i32 @"permutar"(i32 0, i32 1, i32 2, i32 0)
  store i32 %".2", i32* %"valor"
  ret i32 0
}

define i32 @"mostrarPermutacion"(i32 %"a", i32 %"b", i32 %"c")
{
entry:
  %"a.1" = alloca i32
  store i32 %"a", i32* %"a.1"
  %"b.1" = alloca i32
  store i32 %"b", i32* %"b.1"
  %"c.1" = alloca i32
  store i32 %"c", i32* %"c.1"
  %".8" = load i32, i32* %"a.1"
  %".9" = load i32, i32* %"b.1"
  %".10" = load i32, i32* %"c.1"
  %".11" = bitcast [3 x i8]* @".str3" to i8*
  %".12" = call i32 (i8*, ...) @"printf"(i8* %".11", i32 %".8")
  %".13" = bitcast [3 x i8]* @".str4" to i8*
  %".14" = call i32 (i8*, ...) @"printf"(i8* %".13", i32 %".9")
  %".15" = bitcast [3 x i8]* @".str5" to i8*
  %".16" = call i32 (i8*, ...) @"printf"(i8* %".15", i32 %".10")
  ret i32 0
}

@".str3" = internal constant [3 x i8] c"%d\0a"
@".str4" = internal constant [3 x i8] c"%d\0a"
@".str5" = internal constant [3 x i8] c"%d\0a"
define i32 @"permutar"(i32 %"a", i32 %"b", i32 %"c", i32 %"etapa")
{
entry:
  %"a.1" = alloca i32
  store i32 %"a", i32* %"a.1"
  %"b.1" = alloca i32
  store i32 %"b", i32* %"b.1"
  %"c.1" = alloca i32
  store i32 %"c", i32* %"c.1"
  %"etapa.1" = alloca i32
  store i32 %"etapa", i32* %"etapa.1"
  %"valor" = alloca i32
  store i32 0, i32* %"valor"
  %".11" = load i32, i32* %"etapa.1"
  %".12" = icmp eq i32 %".11", 3
  br i1 %".12", label %"then", label %"merge"
then:
  %".14" = load i32, i32* %"a.1"
  %".15" = load i32, i32* %"b.1"
  %".16" = load i32, i32* %"c.1"
  %".17" = call i32 @"mostrarPermutacion"(i32 %".14", i32 %".15", i32 %".16")
  store i32 %".17", i32* %"valor"
  ret i32 0
merge:
  %".20" = load i32, i32* %"etapa.1"
  %".21" = icmp eq i32 %".20", 0
  br i1 %".21", label %"then.1", label %"merge.1"
then.1:
  %".23" = load i32, i32* %"a.1"
  %".24" = load i32, i32* %"b.1"
  %".25" = load i32, i32* %"c.1"
  %".26" = call i32 @"permutar"(i32 %".23", i32 %".24", i32 %".25", i32 1)
  store i32 %".26", i32* %"valor"
  %".28" = load i32, i32* %"b.1"
  %".29" = load i32, i32* %"a.1"
  %".30" = load i32, i32* %"c.1"
  %".31" = call i32 @"permutar"(i32 %".28", i32 %".29", i32 %".30", i32 1)
  store i32 %".31", i32* %"valor"
  %".33" = load i32, i32* %"c.1"
  %".34" = load i32, i32* %"b.1"
  %".35" = load i32, i32* %"a.1"
  %".36" = call i32 @"permutar"(i32 %".33", i32 %".34", i32 %".35", i32 1)
  store i32 %".36", i32* %"valor"
  br label %"merge.1"
merge.1:
  %".39" = load i32, i32* %"etapa.1"
  %".40" = icmp eq i32 %".39", 1
  br i1 %".40", label %"then.2", label %"merge.2"
then.2:
  %".42" = load i32, i32* %"a.1"
  %".43" = load i32, i32* %"b.1"
  %".44" = load i32, i32* %"c.1"
  %".45" = call i32 @"permutar"(i32 %".42", i32 %".43", i32 %".44", i32 2)
  store i32 %".45", i32* %"valor"
  %".47" = load i32, i32* %"a.1"
  %".48" = load i32, i32* %"c.1"
  %".49" = load i32, i32* %"b.1"
  %".50" = call i32 @"permutar"(i32 %".47", i32 %".48", i32 %".49", i32 2)
  store i32 %".50", i32* %"valor"
  br label %"merge.2"
merge.2:
  %".53" = load i32, i32* %"etapa.1"
  %".54" = icmp eq i32 %".53", 2
  br i1 %".54", label %"then.3", label %"merge.3"
then.3:
  %".56" = load i32, i32* %"a.1"
  %".57" = load i32, i32* %"b.1"
  %".58" = load i32, i32* %"c.1"
  %".59" = call i32 @"permutar"(i32 %".56", i32 %".57", i32 %".58", i32 3)
  store i32 %".59", i32* %"valor"
  br label %"merge.3"
merge.3:
  ret i32 0
}
