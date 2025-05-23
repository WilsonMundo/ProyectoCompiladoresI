; ModuleID = 'Ordenamiento.ll'
source_filename = "Ordenamiento.ll"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

@.str3 = internal constant [3 x i8] c"%d\0A"
@.str4 = internal constant [3 x i8] c"%d\0A"
@.str5 = internal constant [3 x i8] c"%d\0A"
@.str7 = internal constant [3 x i8] c"%d\0A"
@.str8 = internal constant [3 x i8] c"%d\0A"
@.str9 = internal constant [3 x i8] c"%d\0A"
@.str11 = internal constant [3 x i8] c"%d\0A"
@.str12 = internal constant [3 x i8] c"%d\0A"
@.str13 = internal constant [3 x i8] c"%d\0A"

; Function Attrs: nofree nounwind
declare noundef i32 @printf(ptr nocapture noundef readonly, ...) local_unnamed_addr #0

; Function Attrs: nofree nounwind
define noundef i32 @main() local_unnamed_addr #0 {
entry:
  %.52.i = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @.str3, i32 1)
  %.54.i = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @.str4, i32 2)
  %.56.i = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @.str5, i32 3)
  %.52.i1 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @.str7, i32 1)
  %.54.i2 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @.str8, i32 2)
  %.56.i3 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @.str9, i32 3)
  %.52.i4 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @.str11, i32 1)
  %.54.i5 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @.str12, i32 2)
  %.56.i6 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @.str13, i32 3)
  ret i32 0
}

; Function Attrs: nofree nounwind
define noundef i32 @bubbleSort3(i32 %a, i32 %b, i32 %c) local_unnamed_addr #0 {
entry:
  %spec.select = tail call i32 @llvm.smin.i32(i32 %a, i32 %b)
  %spec.select15 = tail call i32 @llvm.smax.i32(i32 %a, i32 %b)
  %y.1 = tail call i32 @llvm.smin.i32(i32 %spec.select15, i32 %c)
  %z.0 = tail call i32 @llvm.smax.i32(i32 %spec.select15, i32 %c)
  %.39 = icmp sgt i32 %spec.select, %c
  %x.1 = select i1 %.39, i32 %y.1, i32 %spec.select
  %y.2 = select i1 %.39, i32 %spec.select, i32 %y.1
  %.52 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @.str3, i32 %x.1)
  %.54 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @.str4, i32 %y.2)
  %.56 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @.str5, i32 %z.0)
  ret i32 0
}

; Function Attrs: nofree nounwind
define noundef i32 @selectionSort3(i32 %a, i32 %b, i32 %c) local_unnamed_addr #0 {
entry:
  %spec.select = tail call i32 @llvm.smin.i32(i32 %a, i32 %b)
  %spec.select15 = tail call i32 @llvm.smax.i32(i32 %a, i32 %b)
  %x.1 = tail call i32 @llvm.smin.i32(i32 %spec.select, i32 %c)
  %z.0 = tail call i32 @llvm.smax.i32(i32 %spec.select, i32 %c)
  %y.1 = tail call i32 @llvm.smin.i32(i32 %spec.select15, i32 %z.0)
  %z.1 = tail call i32 @llvm.smax.i32(i32 %spec.select15, i32 %z.0)
  %.52 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @.str7, i32 %x.1)
  %.54 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @.str8, i32 %y.1)
  %.56 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @.str9, i32 %z.1)
  ret i32 0
}

; Function Attrs: nofree nounwind
define noundef i32 @insertionSort3(i32 %a, i32 %b, i32 %c) local_unnamed_addr #0 {
entry:
  %spec.select = tail call i32 @llvm.smin.i32(i32 %b, i32 %a)
  %spec.select15 = tail call i32 @llvm.smax.i32(i32 %b, i32 %a)
  %.28 = icmp sgt i32 %spec.select15, %c
  %spec.select16 = tail call i32 @llvm.smin.i32(i32 %spec.select, i32 %c)
  %spec.select17 = tail call i32 @llvm.smax.i32(i32 %spec.select, i32 %c)
  %x.1 = select i1 %.28, i32 %spec.select16, i32 %spec.select
  %y.1 = select i1 %.28, i32 %spec.select17, i32 %spec.select15
  %z.0 = tail call i32 @llvm.smax.i32(i32 %spec.select15, i32 %c)
  %.52 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @.str11, i32 %x.1)
  %.54 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @.str12, i32 %y.1)
  %.56 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @.str13, i32 %z.0)
  ret i32 0
}

; Function Attrs: nocallback nofree nosync nounwind speculatable willreturn memory(none)
declare i32 @llvm.smin.i32(i32, i32) #1

; Function Attrs: nocallback nofree nosync nounwind speculatable willreturn memory(none)
declare i32 @llvm.smax.i32(i32, i32) #1

attributes #0 = { nofree nounwind }
attributes #1 = { nocallback nofree nosync nounwind speculatable willreturn memory(none) }
