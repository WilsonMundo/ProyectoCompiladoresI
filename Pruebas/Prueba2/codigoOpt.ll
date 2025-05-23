; ModuleID = 'codigo.ll'
source_filename = "codigo.ll"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-unknown-linux-gnu"

@.str6 = internal constant [10 x i8] c"cuadrado:\00"
@.str7 = internal constant [7 x i8] c"%s %d\0A\00"
@.str8 = internal constant [16 x i8] c"resultado suma:\00"
@.str9 = internal constant [7 x i8] c"%s %d\0A\00"
@.str10 = internal constant [8 x i8] c"a vale:\00"
@.str11 = internal constant [7 x i8] c"%s %d\0A\00"

; Function Attrs: nofree nounwind
declare noundef i32 @printf(ptr nocapture noundef readonly, ...) local_unnamed_addr #0

; Function Attrs: nofree nounwind
define noundef i32 @main() local_unnamed_addr #0 {
entry:
  %.7 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @.str7, ptr nonnull @.str6, i32 80)
  %.13 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @.str9, ptr nonnull @.str8, i32 60)
  %.28 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @.str11, ptr nonnull @.str10, i32 1)
  ret i32 0
}

; Function Attrs: mustprogress nofree norecurse nosync nounwind willreturn memory(none)
define i32 @cuadradoConstante(i32 %x) local_unnamed_addr #1 {
entry:
  %.7 = shl i32 %x, 4
  ret i32 %.7
}

; Function Attrs: mustprogress nofree norecurse nosync nounwind willreturn memory(none)
define i32 @sumaHasta(i32 %n) local_unnamed_addr #1 {
entry:
  %.103 = icmp sgt i32 %n, 0
  %0 = mul i32 %n, 6
  %spec.select = select i1 %.103, i32 %0, i32 0
  ret i32 %spec.select
}

; Function Attrs: mustprogress nofree norecurse nosync nounwind willreturn memory(none)
define i1 @dummy(i1 returned %b) local_unnamed_addr #1 {
entry:
  ret i1 %b
}

attributes #0 = { nofree nounwind }
attributes #1 = { mustprogress nofree norecurse nosync nounwind willreturn memory(none) }
