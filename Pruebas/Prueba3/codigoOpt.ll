; ModuleID = 'codigo.ll'
source_filename = "codigo.ll"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-unknown-linux-gnu"

@.str6 = internal constant [7 x i8] c"doble:\00"
@.str7 = internal constant [7 x i8] c"%s %d\0A\00"
@.str8 = internal constant [17 x i8] c"sumatoria 1..10:\00"
@.str9 = internal constant [7 x i8] c"%s %d\0A\00"
@.str10 = internal constant [11 x i8] c"\C2\BFes par?:\00"
@.str11 = internal constant [7 x i8] c"%s %d\0A\00"

; Function Attrs: nofree nounwind
declare noundef i32 @printf(ptr nocapture noundef readonly, ...) local_unnamed_addr #0

; Function Attrs: nofree nounwind
define noundef i32 @main() local_unnamed_addr #0 {
entry:
  %.9 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @.str7, ptr nonnull @.str6, i32 14)
  %.15 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @.str9, ptr nonnull @.str8, i32 55)
  %.22 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @.str11, ptr nonnull @.str10, i1 false)
  ret i32 0
}

; Function Attrs: mustprogress nofree norecurse nosync nounwind willreturn memory(none)
define i32 @dobleViaSuma(i32 %x) local_unnamed_addr #1 {
entry:
  %0 = shl i32 %x, 1
  ret i32 %0
}

; Function Attrs: nofree norecurse nosync nounwind memory(none)
define i32 @sumatoria(i32 %n) local_unnamed_addr #2 {
entry:
  %.10.not4 = icmp slt i32 %n, 1
  br i1 %.10.not4, label %for.exit, label %for.body

for.body:                                         ; preds = %entry, %for.body
  %i.06 = phi i32 [ %.18, %for.body ], [ 1, %entry ]
  %acc.05 = phi i32 [ %.14, %for.body ], [ 0, %entry ]
  %.14 = add i32 %i.06, %acc.05
  %.18 = add i32 %i.06, 1
  %.10.not = icmp sgt i32 %.18, %n
  br i1 %.10.not, label %for.exit, label %for.body

for.exit:                                         ; preds = %for.body, %entry
  %acc.0.lcssa = phi i32 [ 0, %entry ], [ %.14, %for.body ]
  ret i32 %acc.0.lcssa
}

; Function Attrs: mustprogress nofree norecurse nosync nounwind willreturn memory(none)
define i1 @esPar(i32 %n) local_unnamed_addr #1 {
entry:
  %.14 = icmp eq i32 %n, 0
  ret i1 %.14
}

attributes #0 = { nofree nounwind }
attributes #1 = { mustprogress nofree norecurse nosync nounwind willreturn memory(none) }
attributes #2 = { nofree norecurse nosync nounwind memory(none) }
