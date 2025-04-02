; ModuleID = "main"
target triple = "unknown-unknown-unknown"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

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
  br label %"merge"
else:
  br label %"merge"
merge:
  %"sumaTotal" = alloca i32
  store i32 0, i32* %"sumaTotal"
  %"i" = alloca i32
  store i32 1, i32* %"i"
  store i32 1, i32* %"i"
  br label %"for.cond"
for.cond:
  %".14" = load i32, i32* %"i"
  %".15" = icmp sle i32 %".14", 5
  br i1 %".15", label %"for.body", label %"for.exit"
for.body:
  %".17" = load i32, i32* %"sumaTotal"
  %".18" = load i32, i32* %"i"
  %".19" = add i32 %".17", %".18"
  store i32 %".19", i32* %"sumaTotal"
  br label %"for.step"
for.step:
  %".22" = load i32, i32* %"i"
  %".23" = add i32 %".22", 1
  store i32 %".23", i32* %"i"
  br label %"for.cond"
for.exit:
  %".26" = load i32, i32* %"sumaTotal"
  %".27" = bitcast [3 x i8]* @".str7" to i8*
  %".28" = call i32 (i8*, ...) @"printf"(i8* %".27", i32 %".26")
  %"contador" = alloca i32
  store i32 0, i32* %"contador"
  br label %"while.cond"
while.cond:
  %".31" = load i32, i32* %"contador"
  %".32" = icmp slt i32 %".31", 3
  br i1 %".32", label %"while.body", label %"while.exit"
while.body:
  %".34" = load i32, i32* %"contador"
  %".35" = add i32 %".34", 1
  store i32 %".35", i32* %"contador"
  br label %"while.cond"
while.exit:
  %"num" = alloca i32
  store i32 5, i32* %"num"
  %"b" = alloca i32
  store i32 10, i32* %"b"
  %"c" = alloca i32
  store i32 20, i32* %"c"
  %"suma" = alloca i32
  %".41" = load i32, i32* %"num"
  %".42" = load i32, i32* %"b"
  %".43" = add i32 %".41", %".42"
  store i32 %".43", i32* %"suma"
  %".45" = load i32, i32* %"suma"
  %".46" = bitcast [3 x i8]* @".str8" to i8*
  %".47" = call i32 (i8*, ...) @"printf"(i8* %".46", i32 %".45")
  %"resta" = alloca i32
  %".48" = load i32, i32* %"c"
  %".49" = load i32, i32* %"num"
  %".50" = sub i32 %".48", %".49"
  store i32 %".50", i32* %"resta"
  %".52" = load i32, i32* %"resta"
  %".53" = bitcast [3 x i8]* @".str9" to i8*
  %".54" = call i32 (i8*, ...) @"printf"(i8* %".53", i32 %".52")
  %"multiplicacion" = alloca i32
  %".55" = load i32, i32* %"num"
  %".56" = load i32, i32* %"b"
  %".57" = mul i32 %".55", %".56"
  store i32 %".57", i32* %"multiplicacion"
  %".59" = load i32, i32* %"multiplicacion"
  %".60" = bitcast [3 x i8]* @".str10" to i8*
  %".61" = call i32 (i8*, ...) @"printf"(i8* %".60", i32 %".59")
  %"division" = alloca double
  %".62" = load i32, i32* %"c"
  %".63" = load i32, i32* %"num"
  %".64" = sdiv i32 %".62", %".63"
  %".65" = sitofp i32 %".64" to double
  store double %".65", double* %"division"
  %".67" = load double, double* %"division"
  %".68" = bitcast [3 x i8]* @".str11" to i8*
  %".69" = call i32 (i8*, ...) @"printf"(i8* %".68", double %".67")
  %".70" = load i32, i32* %"c"
  %".71" = load i32, i32* %"b"
  %".72" = icmp ne i32 %".70", %".71"
  br i1 %".72", label %"then.1", label %"merge.1"
then.1:
  br label %"merge.1"
merge.1:
  %".75" = load i32, i32* %"b"
  %".76" = load i32, i32* %"num"
  %".77" = icmp sge i32 %".75", %".76"
  br i1 %".77", label %"then.2", label %"merge.2"
then.2:
  br label %"merge.2"
merge.2:
  %"resultadoFinal" = alloca double
  %".80" = load i32, i32* %"suma"
  %".81" = load i32, i32* %"resta"
  %".82" = add i32 %".80", %".81"
  %".83" = load i32, i32* %"multiplicacion"
  %".84" = load double, double* %"division"
  %".85" = sitofp i32 %".83" to double
  %".86" = fsub double %".85", %".84"
  %".87" = sitofp i32 %".82" to double
  %".88" = fmul double %".87", %".86"
  store double %".88", double* %"resultadoFinal"
  %".90" = load double, double* %"resultadoFinal"
  %".91" = bitcast [3 x i8]* @".str12" to i8*
  %".92" = call i32 (i8*, ...) @"printf"(i8* %".91", double %".90")
  %"nombre" = alloca i8*
  %".93" = bitcast [6 x i8]* @".str13" to i8*
  store i8* %".93", i8** %"nombre"
  %"saludo" = alloca i8*
  %".95" = bitcast [7 x i8]* @".str14" to i8*
  store i8* %".95", i8** %"saludo"
  %"despedida" = alloca i8*
  %".97" = bitcast [7 x i8]* @".str15" to i8*
  store i8* %".97", i8** %"despedida"
  %".99" = load i8*, i8** %"saludo"
  %".100" = load i8*, i8** %"nombre"
  %".101" = bitcast [3 x i8]* @".str16" to i8*
  %".102" = call i32 (i8*, ...) @"printf"(i8* %".101", i8* %".99")
  %".103" = bitcast [3 x i8]* @".str17" to i8*
  %".104" = call i32 (i8*, ...) @"printf"(i8* %".103", i8* %".100")
  %".105" = load i8*, i8** %"despedida"
  %".106" = load i8*, i8** %"nombre"
  %".107" = bitcast [3 x i8]* @".str18" to i8*
  %".108" = call i32 (i8*, ...) @"printf"(i8* %".107", i8* %".105")
  %".109" = bitcast [3 x i8]* @".str19" to i8*
  %".110" = call i32 (i8*, ...) @"printf"(i8* %".109", i8* %".106")
  %"mayorEdad" = alloca i1
  store i1 1, i1* %"mayorEdad"
  %"menorEdad" = alloca i1
  store i1 0, i1* %"menorEdad"
  %".113" = load i1, i1* %"mayorEdad"
  br i1 %".113", label %"then.3", label %"merge.3"
then.3:
  %".115" = load i8*, i8** %"nombre"
  %".116" = bitcast [3 x i8]* @".str20" to i8*
  %".117" = call i32 (i8*, ...) @"printf"(i8* %".116", i8* %".115")
  br label %"merge.3"
merge.3:
  %".119" = load i1, i1* %"menorEdad"
  %".120" = fcmp oeq i1 %".119", 0
  br i1 %".120", label %"then.4", label %"merge.4"
then.4:
  %".122" = load i8*, i8** %"nombre"
  %".123" = bitcast [3 x i8]* @".str21" to i8*
  %".124" = call i32 (i8*, ...) @"printf"(i8* %".123", i8* %".122")
  br label %"merge.4"
merge.4:
  %"comparacion" = alloca i1
  %".126" = load i32, i32* %"x"
  %".127" = icmp sgt i32 %".126", 5
  store i1 %".127", i1* %"comparacion"
  %".129" = load i1, i1* %"comparacion"
  br i1 %".129", label %"then.5", label %"merge.5"
then.5:
  br label %"merge.5"
merge.5:
  %"total" = alloca i32
  %".132" = call i32 @"sumar"(i32 5, i32 15)
  store i32 %".132", i32* %"total"
  %".134" = load i32, i32* %"total"
  %".135" = bitcast [3 x i8]* @".str22" to i8*
  %".136" = call i32 (i8*, ...) @"printf"(i8* %".135", i32 %".134")
  %"divReal" = alloca double
  %".137" = call double @"dividir"(double 0x4024000000000000, double 0x4010000000000000)
  store double %".137", double* %"divReal"
  %".139" = load double, double* %"divReal"
  %".140" = bitcast [3 x i8]* @".str23" to i8*
  %".141" = call i32 (i8*, ...) @"printf"(i8* %".140", double %".139")
  %"saludoPersonal" = alloca i8*
  %".142" = load i8*, i8** %"nombre"
  %".143" = call i8* @"saludar"(i8* %".142")
  store i8* %".143", i8** %"saludoPersonal"
  %".145" = load i8*, i8** %"saludoPersonal"
  %".146" = bitcast [3 x i8]* @".str24" to i8*
  %".147" = call i32 (i8*, ...) @"printf"(i8* %".146", i8* %".145")
  %"esAdulto" = alloca i1
  %".148" = call i1 @"esMayor"(i32 20)
  store i1 %".148", i1* %"esAdulto"
  %".150" = load i1, i1* %"esAdulto"
  br i1 %".150", label %"then.6", label %"merge.6"
then.6:
  %".152" = load i8*, i8** %"nombre"
  %".153" = bitcast [3 x i8]* @".str25" to i8*
  %".154" = call i32 (i8*, ...) @"printf"(i8* %".153", i8* %".152")
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
  %".4" = bitcast [6 x i8]* @".str5" to i8*
  store i8* %".4", i8** %"mensaje"
  %".6" = load i8*, i8** %"mensaje"
  %".7" = load i8*, i8** %"nombre.1"
  %".8" = add i8* %".6", %".7"
  ret i8* %".8"
}

@".str5" = internal constant [6 x i8] c"Hola \00"
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

@".str7" = internal constant [3 x i8] c"%d\0a"
@".str8" = internal constant [3 x i8] c"%d\0a"
@".str9" = internal constant [3 x i8] c"%d\0a"
@".str10" = internal constant [3 x i8] c"%d\0a"
@".str11" = internal constant [3 x i8] c"%f\0a"
@".str12" = internal constant [3 x i8] c"%f\0a"
@".str13" = internal constant [6 x i8] c"Sofia\00"
@".str14" = internal constant [7 x i8] c"\c2\a1Hola \00"
@".str15" = internal constant [7 x i8] c"Adi\c3\b3s \00"
@".str16" = internal constant [3 x i8] c"%d\0a"
@".str17" = internal constant [3 x i8] c"%d\0a"
@".str18" = internal constant [3 x i8] c"%d\0a"
@".str19" = internal constant [3 x i8] c"%d\0a"
@".str20" = internal constant [3 x i8] c"%d\0a"
@".str21" = internal constant [3 x i8] c"%d\0a"
@".str22" = internal constant [3 x i8] c"%d\0a"
@".str23" = internal constant [3 x i8] c"%f\0a"
@".str24" = internal constant [3 x i8] c"%d\0a"
@".str25" = internal constant [3 x i8] c"%d\0a"