; ModuleID = 'codigo.ll'
source_filename = "codigo.ll"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-unknown-linux-gnu"

@.str6 = internal constant [6 x i8] c"Hola \00"
@concat_str7 = internal global [128 x i8] zeroinitializer
@.str8 = internal constant [6 x i8] c"%s%s\0A\00"
@.str10 = internal constant [18 x i8] c"Hola, bienvenido!\00"
@.str14 = internal constant [27 x i8] c"La suma total del for es :\00"
@.str15 = internal constant [7 x i8] c"%s %d\0A\00"
@.str16 = internal constant [29 x i8] c"Ciclo while en ejecuci\C3\B3n...\00"
@.str18 = internal constant [6 x i8] c"suma:\00"
@.str19 = internal constant [7 x i8] c"%s %d\0A\00"
@.str20 = internal constant [7 x i8] c"resta:\00"
@.str21 = internal constant [7 x i8] c"%s %d\0A\00"
@.str22 = internal constant [17 x i8] c"Multiplicaci\C3\B3n:\00"
@.str23 = internal constant [7 x i8] c"%s %d\0A\00"
@.str24 = internal constant [11 x i8] c"Divisi\C3\B3n:\00"
@.str25 = internal constant [7 x i8] c"%s %f\0A\00"
@.str26 = internal constant [20 x i8] c"c es diferente de b\00"
@.str28 = internal constant [27 x i8] c"b es mayor o igual que num\00"
@.str30 = internal constant [17 x i8] c"Resultado final:\00"
@.str31 = internal constant [7 x i8] c"%s %f\0A\00"
@.str32 = internal constant [6 x i8] c"Sofia\00"
@.str33 = internal constant [8 x i8] c"\C2\A1Hola \00"
@.str34 = internal constant [8 x i8] c"Adi\C3\B3s \00"
@.str35 = internal constant [2 x i8] c"!\00"
@.str36 = internal constant [10 x i8] c"%s %s %s\0A\00"
@.str37 = internal constant [2 x i8] c"!\00"
@.str38 = internal constant [10 x i8] c"%s %s %s\0A\00"
@.str39 = internal constant [19 x i8] c" es mayor de edad.\00"
@.str40 = internal constant [7 x i8] c"%s %s\0A\00"
@.str41 = internal constant [22 x i8] c" no es menor de edad.\00"
@.str42 = internal constant [7 x i8] c"%s %s\0A\00"
@.str43 = internal constant [17 x i8] c"x es mayor que 5\00"
@.str45 = internal constant [20 x i8] c"Resultado de sumar:\00"
@.str46 = internal constant [7 x i8] c"%s %d\0A\00"
@.str47 = internal constant [22 x i8] c"Resultado de dividir:\00"
@.str48 = internal constant [7 x i8] c"%s %f\0A\00"
@.str49 = internal constant [22 x i8] c"Saludo personalizado:\00"
@.str50 = internal constant [7 x i8] c"%s %s\0A\00"
@.str51 = internal constant [12 x i8] c" es adulto.\00"
@.str52 = internal constant [7 x i8] c"%s %s\0A\00"

; Function Attrs: nofree nounwind
declare noundef i32 @printf(ptr nocapture noundef readonly, ...) local_unnamed_addr #0

; Function Attrs: nofree nounwind
declare noundef i32 @sprintf(ptr noalias nocapture noundef writeonly, ptr nocapture noundef readonly, ...) local_unnamed_addr #0

; Function Attrs: nofree nounwind
define noundef i32 @main() local_unnamed_addr #0 {
entry:
  %puts = tail call i32 @puts(ptr nonnull dereferenceable(1) @.str10)
  %.35 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @.str15, ptr nonnull @.str14, i32 15)
  %puts6 = tail call i32 @puts(ptr nonnull dereferenceable(1) @.str16)
  %puts6.1 = tail call i32 @puts(ptr nonnull dereferenceable(1) @.str16)
  %puts6.2 = tail call i32 @puts(ptr nonnull dereferenceable(1) @.str16)
  %.58 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @.str19, ptr nonnull @.str18, i32 15)
  %.66 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @.str21, ptr nonnull @.str20, i32 15)
  %.74 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @.str23, ptr nonnull @.str22, i32 50)
  %.83 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @.str25, ptr nonnull @.str24, double 4.000000e+00)
  %puts3 = tail call i32 @puts(ptr nonnull dereferenceable(1) @.str26)
  %puts4 = tail call i32 @puts(ptr nonnull dereferenceable(1) @.str28)
  %.113 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @.str31, ptr nonnull @.str30, double 1.380000e+03)
  %.124 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @.str36, ptr nonnull @.str33, ptr nonnull @.str32, ptr nonnull @.str35)
  %.129 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @.str38, ptr nonnull @.str34, ptr nonnull @.str32, ptr nonnull @.str37)
  %.137 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @.str40, ptr nonnull @.str32, ptr nonnull @.str39)
  %.145 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @.str42, ptr nonnull @.str32, ptr nonnull @.str41)
  %puts5 = tail call i32 @puts(ptr nonnull dereferenceable(1) @.str43)
  %.161 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @.str46, ptr nonnull @.str45, i32 20)
  %.167 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @.str48, ptr nonnull @.str47, double 2.500000e+00)
  %.10.i = tail call i32 (ptr, ptr, ...) @sprintf(ptr nonnull dereferenceable(1) @concat_str7, ptr nonnull dereferenceable(1) @.str8, ptr nonnull @.str6, ptr nonnull @.str32)
  %.174 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @.str50, ptr nonnull @.str49, ptr nonnull @concat_str7)
  %.182 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @.str52, ptr nonnull @.str32, ptr nonnull @.str51)
  ret i32 0
}

; Function Attrs: mustprogress nofree norecurse nosync nounwind willreturn memory(none)
define i32 @sumar(i32 %a, i32 %b) local_unnamed_addr #1 {
entry:
  %.8 = add i32 %b, %a
  ret i32 %.8
}

; Function Attrs: mustprogress nofree norecurse nosync nounwind willreturn memory(none)
define double @dividir(double %a, double %b) local_unnamed_addr #1 {
entry:
  %.8 = fdiv double %a, %b
  ret double %.8
}

; Function Attrs: nofree nounwind
define noundef nonnull ptr @saludar(ptr %nombre) local_unnamed_addr #0 {
entry:
  %.10 = tail call i32 (ptr, ptr, ...) @sprintf(ptr nonnull dereferenceable(1) @concat_str7, ptr nonnull dereferenceable(1) @.str8, ptr nonnull @.str6, ptr %nombre)
  ret ptr @concat_str7
}

; Function Attrs: mustprogress nofree norecurse nosync nounwind willreturn memory(none)
define i1 @esMayor(i32 %edad) local_unnamed_addr #1 {
entry:
  %.5 = icmp sgt i32 %edad, 17
  ret i1 %.5
}

; Function Attrs: nofree nounwind
declare noundef i32 @puts(ptr nocapture noundef readonly) local_unnamed_addr #0

attributes #0 = { nofree nounwind }
attributes #1 = { mustprogress nofree norecurse nosync nounwind willreturn memory(none) }
