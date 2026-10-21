# จุดพักงาน — 22 ตุลาคม 2026 (Asia/Bangkok)

ผู้ใช้ขอพักงานและบันทึกความคืบหน้าลง Git ก่อนกลับมาทำต่อ ไม่มีการตั้งงานอัตโนมัติหรือส่งข้อความให้ agent อื่น

## สถานะล่าสุด

- ชุดรวมปัจจุบัน fresh-translation-004:15,677 รายการ, แปล12,710 และคงต้นฉบับ2,967; ทั้งหมดยังรอตรวจ ไม่ใช่ runtime PASS ทั้งคลัง
- รวม Claude R1–4 จำนวน292แถว และ R5 อีก321แถวแล้ว (เป็นจำนวนแก้แต่ละรอบ ห้ามบวกเป็นยอดแถวไม่ซ้ำโดยไม่ตรวจ)
- R5 ตรวจ321แถว/62ชุด เทียบฐานและ corrections.json ผ่าน; ไม่ลบแฟลกเดิม เพิ่ม PROPER_NAME11แถว ต้นฉบับ/ตัวแปร/แท็ก/โค้ดคงเดิม
- Build อ่านกลับตรงครบ15,677ค่า; ฟอนต์/UI เท่ากับ community-merge-006 ซึ่งมีการแก้ Dropdown ที่ค่าที่สังเกตผ่านแล้ว แต่ข้อความใหม่ไม่ได้รับผลผ่านเดิมโดยอัตโนมัติ
- WO-FRESH-SMOKE-001 ติด SETUP_LIMIT: ถึงแค่เมนูหลักและ Mods ไม่ถึง Settings/มหาวิทยาลัย/ป้ายบุคลากร จึงยัง NOT_RUN ไม่ใช่ translation FAIL
- ตรวจล่าสุดก่อน commit: bundle เกมทั้ง3เป็น original; ไม่มีม็อดค้างติดตั้ง
- เซฟ Slot1 มี Freshleigh Meadows (8000.sav); รอบ smokeล่าสุดเซฟมหาวิทยาลัย/อาชีพไม่เปลี่ยน มีเพียง preferences/userprofileเปลี่ยน สำเนา10ไฟล์ ZIP+manifestตรวจแล้ว ไม่มีไฟล์ใหม่หรือหาย

## สิ่งที่เตรียมแล้วและยังไม่ยืนยันในเกม

- tools/qa_driver.py แก้การเลือกหน้าต่างจากชื่อกว้างเป็นเจ้าของโปรเซส/พาธ TPC.exeจริง ต้องได้หน้าต่างเดียวและforegroundตรงก่อน input/capture พร้อมปรับฐานพิกัดตามจอปัจจุบัน
- ตรวจ compile และ8กรณีจำลองผ่าน แต่ยังไม่ได้พิสูจน์กับเกมจริง ไม่อ้างว่า overlay/การคลิกแก้หมดแล้ว
- ใบงาน qa/WO_FRESH_SMOKE_001_RESUME.md ให้ยืนยันการควบคุมเกมต้นฉบับก่อนติดตั้งชุดทดสอบ:เพดาน5นาที/1recovery หากไม่ผ่านให้หยุด ไม่ติดตั้งซ้ำ
- ผู้ใช้กำหนดปุ่มเมนูเป็น **Mod** (Mใหญ่,ไม่ใช่Mods/ม็อด/ม๊อด) ที่ UI/Modding/Mods, FRESH-036 ยังเป็น USER_APPROVED_PENDING_INTEGRATION; frozen fresh-translation-004ไม่เปลี่ยน
- Overrideอยู่ local/review/user-menu-corrections/mod-menu-override.json และ USER_TEXT_CORRECTIONS.md ต้องรวมใน candidateถัดไป ไม่แทนข้อความทั้งคลังแบบเหมารวม

## งานครั้งหน้า ตามลำดับ

1. อ่าน checkpointนี้, PROJECT_STATUS.md, FRESH_SMOKE_001_DISPOSITION.md และตรวจ Git/ไฟล์เกมจริงก่อนทำต่อ ห้ามสมมติว่าชุดที่ค้างเป็นสถานะล่าสุดหากมีผู้อื่นแก้ไฟล์
2. รวมคำเมนู Modในชุดใหม่เมื่อเริ่มรอบแก้ข้อความ (เก็บcandidateเดิม ไม่เขียนทับfrozen output); เปลี่ยนชื่อcandidateในใบงานและhashให้ตรงหากใช้ชุดใหม่
3. ให้ Antigravity ผ่าน original-game capability gateก่อนติดตั้ง แล้วจึงทำruntimeตัวอย่างจำกัดตามใบงาน ไม่วนคำสั่งเดิมหากยังเลือกหน้าต่างผิด
4. งานฟอนต์: BUG-THAI-003 ไม้เอก/นิคหิตในต่ำ OPEN; มีภาพผู้ใช้ละเอียด ไม่ต้องถ่ายซ้ำเพื่อยืนยันว่าพบปัญหา ห้ามเปลี่ยนคำเพื่อซ่อนบั๊ก
5. BUG-THAI-002 ตัดกลางคำ OPEN; BUG-THAI-001 ถี่เคยผ่านเฉพาะคำเป้าหมาย ยังเปิดการติดตามregression ไม่กล่าวว่าเกิดซ้ำจากรอบที่ไม่ได้เข้าSettings
6. ศัพท์ค้าง Good FriendsชนBest Friends, Pastoral Supportบริการ/ห้อง, ชื่อโรค18ชนิด, มุก1,473แถว และข้อเสนอศัพท์ที่ยังไม่ได้ตรวจ ไม่อนุมัติรวมทั้งชุด

## ไฟล์สำคัญ

- CLAUDE_REVIEW_R5_RECEIPT.md และ CONTROLLER_TERMINOLOGY_DECISIONS_2026-10-22.md
- reports/claude-review-r5-validation.json, reports/fresh-translation-004-build.json
- local/translations/CLAUDE-FULL-RETRANSLATION-001/all-records-review-r5.json เป็นข้อมูลฉบับรวมล่าสุดในเครื่อง ไม่อยู่ในGit
- local/prototype/fresh-translation-004/manifest.json และ bundleเป็นlocal-only
- local/translations/.../output/ คือของClaudeรอบแรก ห้ามแก้หรือใช้แทนฐานรอบ5

Gitเก็บเครื่องมือ/เอกสาร/รายงานโครงสร้างเท่านั้น ไม่รวมคลังข้อความเต็ม คำแปลJSONเต็ม เซฟ ภาพ ZIP ฟอนต์หรือไฟล์เกม (local/ถูกignore) การcloneGitอย่างเดียวจึงสร้างbundleไม่ได้โดยไม่มีlocal inputsเหล่านี้ เก็บโฟลเดอร์localบนเครื่องนี้ไว้
