# Pass 10 publish state (updated 2026-11-18)

Target folder: Research `1qEEDsGMhCy6JBd0hrrMPuZdFBfC8Zll2` (parent `1PL2w0kmxoLbw4osdoQ5xgdA2kg_DtNTT`).
Order: seq = sorted report filename (matches publish_log seq 1-17 from the first session).

## Status
- Seq 1-132: uploaded with upload_file; Drive MD5 and size match build/report_md5.tsv. Logged in build/publish_log.tsv and publish_log.tsv (verified = yes, 132 rows).
- Seq 133, 134, 135: NOT uploaded. Last attempts failed with file_transfer_failed (Drive rate limit) after seq 129-132 succeeded in the same reply. Resume at seq 133. Wait at least 15 s before the next upload.
  - 133 RR10_SUBMISSION_BATCH7_CH04_CH05_CH06_2026_11_17__1qbi6WbMMA.md
  - 134 RR10_SUBMISSION_COSTUME_BREAKDOWN_V001_2026_11_17__18Ehnq1cIc.md
  - 135 RR10_SUBMISSION_ORIGINAL_VA_2026_11_17_ADANNA_TURNAROUND_PENDING__1m32I8rIhe.md

## Content caveats (the uploads are not validated publications)
- Seq 1-17 (first session) were uploaded before the notes were rebuilt. They are drafts.
- The full set was regenerated after the first session. Its text is built from md_findings_pass10.py and gen_reports.py. Several entries are still unverified against bodies (see notes/ and the index).
- Some report texts quote values from bodies that are not yet re-checked (for example seq 86 SYNC_LOG v4 quotes a register MD5 514ebc3d that differs from the ledger file MD5 c1c96ac6 on Drive; the quoted value needs checking against the body).
- Drive copies of seq 1-132 therefore carry draft content until the validation pass is complete.

## Next steps
1. Upload seq 133-135 after the rate limit clears.
2. Validate each report against its source body. Start with the 18 unread md bodies and the caveats listed in the session notes.
3. Regenerate and re-upload any corrected report (update_file_content on the existing Drive ID, not a new upload). Re-log in both publish logs.
4. Write the pass-10 index and sync log with exceptions itemised (E1-E14 from gen_reports.py EXC; E2 resolved).
