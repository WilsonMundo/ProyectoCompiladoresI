; ModuleID = "main"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"sprintf"(i8* %".1", i8* %".2", ...)

define i32 @"main"()
{
entry:
  %"x" = alloca i32
  store i32 10, i32* %"x"
  %"y" = alloca i32
  store i32 20, i32* %"y"
  %".4" = load i32, i32* %"x"
  %".5" = load i32, i32* %"y"
  %".6" = icmp slt i32 %".4", %".5"
  br i1 %".6", label %"then", label %"else"
then:
  %".8" = bitcast [18 x i8]* @".str10" to i8*
  %".9" = bitcast [4 x i8]* @".str11" to i8*
  %".10" = call i32 (i8*, ...) @"printf"(i8* %".9", i8* %".8")
  br label %"merge"
else:
  %".12" = bitcast [21 x i8]* @".str12" to i8*
  %".13" = bitcast [4 x i8]* @".str13" to i8*
  %".14" = call i32 (i8*, ...) @"printf"(i8* %".13", i8* %".12")
  br label %"merge"
merge:
  %"sumaTotal" = alloca i32
  store i32 0, i32* %"sumaTotal"
  %"i" = alloca i32
  store i32 1, i32* %"i"
  store i32 1, i32* %"i"
  br label %"for.cond"
for.cond:
  %".20" = load i32, i32* %"i"
  %".21" = icmp sle i32 %".20", 5
  br i1 %".21", label %"for.body", label %"for.exit"
for.body:
  %".23" = load i32, i32* %"sumaTotal"
  %".24" = load i32, i32* %"i"
  %".25" = add i32 %".23", %".24"
  store i32 %".25", i32* %"sumaTotal"
  br label %"for.step"
for.step:
  %".28" = load i32, i32* %"i"
  %".29" = add i32 %".28", 1
  store i32 %".29", i32* %"i"
  br label %"for.cond"
for.exit:
  %".32" = bitcast [27 x i8]* @".str14" to i8*
  %".33" = load i32, i32* %"sumaTotal"
  %".34" = bitcast [7 x i8]* @".str15" to i8*
  %".35" = call i32 (i8*, ...) @"printf"(i8* %".34", i8* %".32", i32 %".33")
  %"contador" = alloca i32
  store i32 0, i32* %"contador"
  br label %"while.cond"
while.cond:
  %".38" = load i32, i32* %"contador"
  %".39" = icmp slt i32 %".38", 3
  br i1 %".39", label %"while.body", label %"while.exit"
while.body:
  %".41" = bitcast [29 x i8]* @".str16" to i8*
  %".42" = bitcast [4 x i8]* @".str17" to i8*
  %".43" = call i32 (i8*, ...) @"printf"(i8* %".42", i8* %".41")
  %".44" = load i32, i32* %"contador"
  %".45" = add i32 %".44", 1
  store i32 %".45", i32* %"contador"
  br label %"while.cond"
while.exit:
  %"num" = alloca i32
  store i32 5, i32* %"num"
  %"b" = alloca i32
  store i32 10, i32* %"b"
  %"c" = alloca i32
  store i32 20, i32* %"c"
  %"suma" = alloca i32
  %".51" = load i32, i32* %"num"
  %".52" = load i32, i32* %"b"
  %".53" = add i32 %".51", %".52"
  store i32 %".53", i32* %"suma"
  %".55" = bitcast [6 x i8]* @".str18" to i8*
  %".56" = load i32, i32* %"suma"
  %".57" = bitcast [7 x i8]* @".str19" to i8*
  %".58" = call i32 (i8*, ...) @"printf"(i8* %".57", i8* %".55", i32 %".56")
  %"resta" = alloca i32
  %".59" = load i32, i32* %"c"
  %".60" = load i32, i32* %"num"
  %".61" = sub i32 %".59", %".60"
  store i32 %".61", i32* %"resta"
  %".63" = bitcast [7 x i8]* @".str20" to i8*
  %".64" = load i32, i32* %"resta"
  %".65" = bitcast [7 x i8]* @".str21" to i8*
  %".66" = call i32 (i8*, ...) @"printf"(i8* %".65", i8* %".63", i32 %".64")
  %"multiplicacion" = alloca i32
  %".67" = load i32, i32* %"num"
  %".68" = load i32, i32* %"b"
  %".69" = mul i32 %".67", %".68"
  store i32 %".69", i32* %"multiplicacion"
  %".71" = bitcast [17 x i8]* @".str22" to i8*
  %".72" = load i32, i32* %"multiplicacion"
  %".73" = bitcast [7 x i8]* @".str23" to i8*
  %".74" = call i32 (i8*, ...) @"printf"(i8* %".73", i8* %".71", i32 %".72")
  %"division" = alloca double
  %".75" = load i32, i32* %"c"
  %".76" = load i32, i32* %"num"
  %".77" = sdiv i32 %".75", %".76"
  %".78" = sitofp i32 %".77" to double
  store double %".78", double* %"division"
  %".80" = bitcast [11 x i8]* @".str24" to i8*
  %".81" = load double, double* %"division"
  %".82" = bitcast [7 x i8]* @".str25" to i8*
  %".83" = call i32 (i8*, ...) @"printf"(i8* %".82", i8* %".80", double %".81")
  %".84" = load i32, i32* %"c"
  %".85" = load i32, i32* %"b"
  %".86" = icmp ne i32 %".84", %".85"
  br i1 %".86", label %"then.1", label %"merge.1"
then.1:
  %".88" = bitcast [20 x i8]* @".str26" to i8*
  %".89" = bitcast [4 x i8]* @".str27" to i8*
  %".90" = call i32 (i8*, ...) @"printf"(i8* %".89", i8* %".88")
  br label %"merge.1"
merge.1:
  %".92" = load i32, i32* %"b"
  %".93" = load i32, i32* %"num"
  %".94" = icmp sge i32 %".92", %".93"
  br i1 %".94", label %"then.2", label %"merge.2"
then.2:
  %".96" = bitcast [27 x i8]* @".str28" to i8*
  %".97" = bitcast [4 x i8]* @".str29" to i8*
  %".98" = call i32 (i8*, ...) @"printf"(i8* %".97", i8* %".96")
  br label %"merge.2"
merge.2:
  %"resultadoFinal" = alloca double
  %".100" = load i32, i32* %"suma"
  %".101" = load i32, i32* %"resta"
  %".102" = add i32 %".100", %".101"
  %".103" = load i32, i32* %"multiplicacion"
  %".104" = load double, double* %"division"
  %".105" = sitofp i32 %".103" to double
  %".106" = fsub double %".105", %".104"
  %".107" = sitofp i32 %".102" to double
  %".108" = fmul double %".107", %".106"
  store double %".108", double* %"resultadoFinal"
  %".110" = bitcast [17 x i8]* @".str30" to i8*
  %".111" = load double, double* %"resultadoFinal"
  %".112" = bitcast [7 x i8]* @".str31" to i8*
  %".113" = call i32 (i8*, ...) @"printf"(i8* %".112", i8* %".110", double %".111")
  %"nombre" = alloca i8*
  %".114" = bitcast [6 x i8]* @".str32" to i8*
  store i8* %".114", i8** %"nombre"
  %"saludo" = alloca i8*
  %".116" = bitcast [8 x i8]* @".str33" to i8*
  store i8* %".116", i8** %"saludo"
  %"despedida" = alloca i8*
  %".118" = bitcast [8 x i8]* @".str34" to i8*
  store i8* %".118", i8** %"despedida"
  %".120" = load i8*, i8** %"saludo"
  %".121" = load i8*, i8** %"nombre"
  %".122" = bitcast [2 x i8]* @".str35" to i8*
  %".123" = bitcast [10 x i8]* @".str36" to i8*
  %".124" = call i32 (i8*, ...) @"printf"(i8* %".123", i8* %".120", i8* %".121", i8* %".122")
  %".125" = load i8*, i8** %"despedida"
  %".126" = load i8*, i8** %"nombre"
  %".127" = bitcast [2 x i8]* @".str37" to i8*
  %".128" = bitcast [10 x i8]* @".str38" to i8*
  %".129" = call i32 (i8*, ...) @"printf"(i8* %".128", i8* %".125", i8* %".126", i8* %".127")
  %"mayorEdad" = alloca i1
  store i1 1, i1* %"mayorEdad"
  %"menorEdad" = alloca i1
  store i1 0, i1* %"menorEdad"
  %".132" = load i1, i1* %"mayorEdad"
  br i1 %".132", label %"then.3", label %"merge.3"
then.3:
  %".134" = load i8*, i8** %"nombre"
  %".135" = bitcast [19 x i8]* @".str39" to i8*
  %".136" = bitcast [7 x i8]* @".str40" to i8*
  %".137" = call i32 (i8*, ...) @"printf"(i8* %".136", i8* %".134", i8* %".135")
  br label %"merge.3"
merge.3:
  %".139" = load i1, i1* %"menorEdad"
  %".140" = icmp eq i1 %".139", 0
  br i1 %".140", label %"then.4", label %"merge.4"
then.4:
  %".142" = load i8*, i8** %"nombre"
  %".143" = bitcast [22 x i8]* @".str41" to i8*
  %".144" = bitcast [7 x i8]* @".str42" to i8*
  %".145" = call i32 (i8*, ...) @"printf"(i8* %".144", i8* %".142", i8* %".143")
  br label %"merge.4"
merge.4:
  %"comparacion" = alloca i1
  %".147" = load i32, i32* %"x"
  %".148" = icmp sgt i32 %".147", 5
  store i1 %".148", i1* %"comparacion"
  %".150" = load i1, i1* %"comparacion"
  br i1 %".150", label %"then.5", label %"merge.5"
then.5:
  %".152" = bitcast [17 x i8]* @".str43" to i8*
  %".153" = bitcast [4 x i8]* @".str44" to i8*
  %".154" = call i32 (i8*, ...) @"printf"(i8* %".153", i8* %".152")
  br label %"merge.5"
merge.5:
  %"total" = alloca i32
  %".156" = call i32 @"sumar"(i32 5, i32 15)
  store i32 %".156", i32* %"total"
  %".158" = bitcast [20 x i8]* @".str45" to i8*
  %".159" = load i32, i32* %"total"
  %".160" = bitcast [7 x i8]* @".str46" to i8*
  %".161" = call i32 (i8*, ...) @"printf"(i8* %".160", i8* %".158", i32 %".159")
  %"divReal" = alloca double
  %".162" = call double @"dividir"(double 0x4024000000000000, double 0x4010000000000000)
  store double %".162", double* %"divReal"
  %".164" = bitcast [22 x i8]* @".str47" to i8*
  %".165" = load double, double* %"divReal"
  %".166" = bitcast [7 x i8]* @".str48" to i8*
  %".167" = call i32 (i8*, ...) @"printf"(i8* %".166", i8* %".164", double %".165")
  %"saludoPersonal" = alloca i8*
  %".168" = load i8*, i8** %"nombre"
  %".169" = call i8* @"saludar"(i8* %".168")
  store i8* %".169", i8** %"saludoPersonal"
  %".171" = bitcast [22 x i8]* @".str49" to i8*
  %".172" = load i8*, i8** %"saludoPersonal"
  %".173" = bitcast [7 x i8]* @".str50" to i8*
  %".174" = call i32 (i8*, ...) @"printf"(i8* %".173", i8* %".171", i8* %".172")
  %"esAdulto" = alloca i1
  %".175" = call i1 @"esMayor"(i32 20)
  store i1 %".175", i1* %"esAdulto"
  %".177" = load i1, i1* %"esAdulto"
  br i1 %".177", label %"then.6", label %"merge.6"
then.6:
  %".179" = load i8*, i8** %"nombre"
  %".180" = bitcast [12 x i8]* @".str51" to i8*
  %".181" = bitcast [7 x i8]* @".str52" to i8*
  %".182" = call i32 (i8*, ...) @"printf"(i8* %".181", i8* %".179", i8* %".180")
  br label %"merge.6"
merge.6:
  ret i32 0
}

define i32 @"sumar"(i32 %"a", i32 %"b")
{
entry:
  %"a.1" = alloca i32
  store i32 %"a", i32* %"a.1"
  %"b.1" = alloca i32
  store i32 %"b", i32* %"b.1"
  %"resultado" = alloca i32
  %".6" = load i32, i32* %"a.1"
  %".7" = load i32, i32* %"b.1"
  %".8" = add i32 %".6", %".7"
  store i32 %".8", i32* %"resultado"
  %".10" = load i32, i32* %"resultado"
  ret i32 %".10"
}

define double @"dividir"(double %"a", double %"b")
{
entry:
  %"a.1" = alloca double
  store double %"a", double* %"a.1"
  %"b.1" = alloca double
  store double %"b", double* %"b.1"
  %"resultado" = alloca double
  %".6" = load double, double* %"a.1"
  %".7" = load double, double* %"b.1"
  %".8" = fdiv double %".6", %".7"
  store double %".8", double* %"resultado"
  %".10" = load double, double* %"resultado"
  ret double %".10"
}

define i8* @"saludar"(i8* %"nombre")
{
entry:
  %"nombre.1" = alloca i8*
  store i8* %"nombre", i8** %"nombre.1"
  %"mensaje" = alloca i8*
  %".4" = bitcast [6 x i8]* @".str6" to i8*
  store i8* %".4", i8** %"mensaje"
  %".6" = load i8*, i8** %"mensaje"
  %".7" = load i8*, i8** %"nombre.1"
  %".8" = bitcast [128 x i8]* @"concat_str7" to i8*
  %".9" = bitcast [6 x i8]* @".str8" to i8*
  %".10" = call i32 (i8*, i8*, ...) @"sprintf"(i8* %".8", i8* %".9", i8* %".6", i8* %".7")
  ret i8* %".8"
}

@".str6" = internal constant [6 x i8] c"Hola \00"
@"concat_str7" = internal global [128 x i8] c"\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00"
@".str8" = internal constant [6 x i8] c"%s%s\0a\00"
define i1 @"esMayor"(i32 %"edad")
{
entry:
  %"edad.1" = alloca i32
  store i32 %"edad", i32* %"edad.1"
  %"resultado" = alloca i1
  %".4" = load i32, i32* %"edad.1"
  %".5" = icmp sge i32 %".4", 18
  store i1 %".5", i1* %"resultado"
  %".7" = load i1, i1* %"resultado"
  ret i1 %".7"
}

@".str10" = internal constant [18 x i8] c"Hola, bienvenido!\00"
@".str11" = internal constant [4 x i8] c"%s\0a\00"
@".str12" = internal constant [21 x i8] c"Adi\c3\b3s, hasta luego!\00"
@".str13" = internal constant [4 x i8] c"%s\0a\00"
@".str14" = internal constant [27 x i8] c"La suma total del for es :\00"
@".str15" = internal constant [7 x i8] c"%s %d\0a\00"
@".str16" = internal constant [29 x i8] c"Ciclo while en ejecuci\c3\b3n...\00"
@".str17" = internal constant [4 x i8] c"%s\0a\00"
@".str18" = internal constant [6 x i8] c"suma:\00"
@".str19" = internal constant [7 x i8] c"%s %d\0a\00"
@".str20" = internal constant [7 x i8] c"resta:\00"
@".str21" = internal constant [7 x i8] c"%s %d\0a\00"
@".str22" = internal constant [17 x i8] c"Multiplicaci\c3\b3n:\00"
@".str23" = internal constant [7 x i8] c"%s %d\0a\00"
@".str24" = internal constant [11 x i8] c"Divisi\c3\b3n:\00"
@".str25" = internal constant [7 x i8] c"%s %f\0a\00"
@".str26" = internal constant [20 x i8] c"c es diferente de b\00"
@".str27" = internal constant [4 x i8] c"%s\0a\00"
@".str28" = internal constant [27 x i8] c"b es mayor o igual que num\00"
@".str29" = internal constant [4 x i8] c"%s\0a\00"
@".str30" = internal constant [17 x i8] c"Resultado final:\00"
@".str31" = internal constant [7 x i8] c"%s %f\0a\00"
@".str32" = internal constant [6 x i8] c"Sofia\00"
@".str33" = internal constant [8 x i8] c"\c2\a1Hola \00"
@".str34" = internal constant [8 x i8] c"Adi\c3\b3s \00"
@".str35" = internal constant [2 x i8] c"!\00"
@".str36" = internal constant [10 x i8] c"%s %s %s\0a\00"
@".str37" = internal constant [2 x i8] c"!\00"
@".str38" = internal constant [10 x i8] c"%s %s %s\0a\00"
@".str39" = internal constant [19 x i8] c" es mayor de edad.\00"
@".str40" = internal constant [7 x i8] c"%s %s\0a\00"
@".str41" = internal constant [22 x i8] c" no es menor de edad.\00"
@".str42" = internal constant [7 x i8] c"%s %s\0a\00"
@".str43" = internal constant [17 x i8] c"x es mayor que 5\00"
@".str44" = internal constant [4 x i8] c"%s\0a\00"
@".str45" = internal constant [20 x i8] c"Resultado de sumar:\00"
@".str46" = internal constant [7 x i8] c"%s %d\0a\00"
@".str47" = internal constant [22 x i8] c"Resultado de dividir:\00"
@".str48" = internal constant [7 x i8] c"%s %f\0a\00"
@".str49" = internal constant [22 x i8] c"Saludo personalizado:\00"
@".str50" = internal constant [7 x i8] c"%s %s\0a\00"
@".str51" = internal constant [12 x i8] c" es adulto.\00"
@".str52" = internal constant [7 x i8] c"%s %s\0a\00"