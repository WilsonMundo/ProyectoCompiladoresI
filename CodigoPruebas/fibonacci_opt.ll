; ModuleID = 'fibonacci.ll'
source_filename = "fibonacci.ll"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

@.str3 = internal constant [3 x i8] c"%d\0A"

; Function Attrs: nofree nounwind
declare noundef i32 @printf(ptr nocapture noundef readonly, ...) local_unnamed_addr #0

; Function Attrs: nofree nounwind
define noundef i32 @main() local_unnamed_addr #0 {
entry:
  %.2 = tail call i32 @ackermann(i32 2, i32 2)
  %.4 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @.str3, i32 %.2)
  ret i32 0
}

; Function Attrs: nofree nosync nounwind memory(none)
define i32 @ackermann(i32 %m, i32 %n) local_unnamed_addr #1 {
entry:
  %.76 = icmp eq i32 %m, 0
  br i1 %.76, label %then, label %merge

then:                                             ; preds = %tailrecurse.backedge, %entry
  %n.tr.lcssa = phi i32 [ %n, %entry ], [ %n.tr.be, %tailrecurse.backedge ]
  %.10 = add i32 %n.tr.lcssa, 1
  ret i32 %.10

merge:                                            ; preds = %entry, %tailrecurse.backedge
  %n.tr8 = phi i32 [ %n.tr.be, %tailrecurse.backedge ], [ %n, %entry ]
  %m.tr7 = phi i32 [ %m.tr.be, %tailrecurse.backedge ], [ %m, %entry ]
  %.13 = icmp eq i32 %n.tr8, 0
  br i1 %.13, label %tailrecurse.backedge, label %merge.1

tailrecurse.backedge:                             ; preds = %merge, %merge.1
  %n.tr.be = phi i32 [ %.24, %merge.1 ], [ 1, %merge ]
  %m.tr.be = add i32 %m.tr7, -1
  %.7 = icmp eq i32 %m.tr.be, 0
  br i1 %.7, label %then, label %merge

merge.1:                                          ; preds = %merge
  %.23 = add i32 %n.tr8, -1
  %.24 = tail call i32 @ackermann(i32 %m.tr7, i32 %.23)
  br label %tailrecurse.backedge
}

attributes #0 = { nofree nounwind }
attributes #1 = { nofree nosync nounwind memory(none) }
