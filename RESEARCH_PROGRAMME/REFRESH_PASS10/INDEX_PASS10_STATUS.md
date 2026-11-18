# Pass 10 index and status (2026-11-18). Status: PARTIAL.

- Publish: 132 of 135 reports on Drive (seq 1-132, MD5 and size verified). Seq 133-135 pending (Drive rate limit). See PUBLISH_STATE.md.
- Validation: NOT complete. Uploads are drafts for seq 1-17 and for any report whose body has not been re-read. See PUBLISH_STATE.md caveats.
- Source manifest: pass10_manifest.tsv (135 rows). Local files: reports/ (135 .md), report_md5.tsv, report_index.tsv.
- Findings: notes/text_findings_ORIGINAL.md, notes/text_findings_ASSISTANT_part2.md (replaces part1), notes/image_findings_batch1.md, notes/image_findings_assistant.md. Generator inputs: build/md_findings_pass10.py (dict M), build/gen_reports.py.

## Exceptions (itemised)
- E1 ORIGINAL EXP-001 (1SsRkI8j): the Drive file is a 2,537-byte text report, not artwork. The artwork is not on Drive. Restore needs Drive version history (owner action).
- E2 resolved (no defect).
- E3 `1m32I8rI`: lists four candidate IDs that are not in the folder. Recorded as a discrepancy; not reconciled.
- E4 withdrawn (an earlier draft misread the BATCH7 body).
- E8 placement: PENDING/ASSISTANT_VA_SUBMISSIONS was created by the author rather than found; five live candidates were in wrong parents; the author's moves table lists seven rows. Not re-audited.
- Body-level discrepancies: WALL V005 and COSTUME V002 are listed approved in ledger v14 and live/unreviewed in ledger v9; 16_REJECTED_DESIGNS count 30 vs breakdown 31; ledger v9 says "eight" live candidates but lists nine.
- Unauthorised Research events (uploads, trash, restores) and unrecorded uploads (ESTABLISHING V013 21:47 UTC, Adanna V003) remain open. See session record.
- Open items (a)-(y) carried from the session record; not reconciled.
