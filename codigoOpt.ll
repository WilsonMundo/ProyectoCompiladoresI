; ModuleID = 'codigo.ll'
source_filename = "codigo.ll"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-unknown-linux-gnu"

@.str3 = internal constant [17 x i8] c"El valor de a es\00"
@.str4 = internal constant [7 x i8] c"%s %d\0A\00"
@.str5 = internal constant [6 x i8] c"datos\00"

; Function Attrs: nofree nounwind
declare noundef i32 @printf(ptr nocapture noundef readonly, ...) local_unnamed_addr #0

; Function Attrs: nofree nounwind
define noundef i32 @main() local_unnamed_addr #0 {
entry:
  %.6 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @.str4, ptr nonnull @.str3, i32 35)
  %puts = tail call i32 @puts(ptr nonnull dereferenceable(1) @.str5)
  ret i32 0
}

; Function Attrs: nofree nounwind
declare noundef i32 @puts(ptr nocapture noundef readonly) local_unnamed_addr #0

attributes #0 = { nofree nounwind }
