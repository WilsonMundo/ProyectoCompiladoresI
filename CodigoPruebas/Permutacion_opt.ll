; ModuleID = 'Permutacion.ll'
source_filename = "Permutacion.ll"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

@.str3 = internal constant [3 x i8] c"%d\0A"
@.str4 = internal constant [3 x i8] c"%d\0A"
@.str5 = internal constant [3 x i8] c"%d\0A"

; Function Attrs: nofree nounwind
declare noundef i32 @printf(ptr nocapture noundef readonly, ...) local_unnamed_addr #0

; Function Attrs: nofree nounwind
define noundef i32 @main() local_unnamed_addr #0 {
entry:
  %.2 = tail call i32 @permutar(i32 0, i32 1, i32 2, i32 0)
  ret i32 0
}

; Function Attrs: nofree nounwind
define noundef i32 @mostrarPermutacion(i32 %a, i32 %b, i32 %c) local_unnamed_addr #0 {
entry:
  %.12 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @.str3, i32 %a)
  %.14 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @.str4, i32 %b)
  %.16 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @.str5, i32 %c)
  ret i32 0
}

; Function Attrs: nofree nounwind
define noundef i32 @permutar(i32 %a, i32 %b, i32 %c, i32 %etapa) local_unnamed_addr #0 {
entry:
  switch i32 %etapa, label %common.ret [
    i32 3, label %common.ret.sink.split
    i32 0, label %then.1.peel
    i32 1, label %then.3.loopexit
    i32 2, label %common.ret.sink.split
  ]

then.1.peel:                                      ; preds = %entry
  %.26.peel = tail call i32 @permutar(i32 %a, i32 %b, i32 %c, i32 1)
  %.31.peel = tail call i32 @permutar(i32 %b, i32 %a, i32 %c, i32 1)
  br label %then.3.loopexit

common.ret.sink.split:                            ; preds = %entry, %entry, %then.3.loopexit
  %a.tr.ph89 = phi i32 [ %a.tr.ph.lcssa88, %then.3.loopexit ], [ %a, %entry ], [ %a, %entry ]
  %b.tr.lcssa53.sink = phi i32 [ %c.tr.ph.lcssa86, %then.3.loopexit ], [ %b, %entry ], [ %b, %entry ]
  %c.tr.lcssa50.sink = phi i32 [ %b, %then.3.loopexit ], [ %c, %entry ], [ %c, %entry ]
  %.12.i.i = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @.str3, i32 %a.tr.ph89)
  %.14.i.i = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @.str4, i32 %b.tr.lcssa53.sink)
  %.16.i.i = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @.str5, i32 %c.tr.lcssa50.sink)
  br label %common.ret

common.ret:                                       ; preds = %entry, %common.ret.sink.split
  ret i32 0

then.3.loopexit:                                  ; preds = %then.1.peel, %entry
  %a.tr.ph.lcssa88 = phi i32 [ %a, %entry ], [ %c, %then.1.peel ]
  %c.tr.ph.lcssa86 = phi i32 [ %c, %entry ], [ %a, %then.1.peel ]
  %.45.peel = tail call i32 @permutar(i32 %a.tr.ph.lcssa88, i32 %b, i32 %c.tr.ph.lcssa86, i32 2)
  br label %common.ret.sink.split
}

attributes #0 = { nofree nounwind }
