# จุดพักงานล่าสุด — 26 ตุลาคม 2026 (Asia/Bangkok)

ผู้ใช้ให้ Claude ทำหน้าที่ PM/Controller แทน ChatGPT ตั้งแต่ 26 ต.ค. (ChatGPT ทำงานวิศวกรรมและทดสอบแทน Antigravity ตามที่ผู้ใช้อนุญาต) เอกสารนี้เป็น checkpoint ล่าสุด ต่อจาก SESSION_CHECKPOINT_2026-10-22_EVENING.md

## สถานะหลัก

- **BUG-THAI-003 (สระอำ + ไม้เอก/ไม้โท): FIX_VERIFIED_SCOPED ยังไม่ปิด.** แก้ที่ fonts bundle อย่างเดียว ข้อความไม่เปลี่ยน: เพิ่ม composite glyph 15 ตัว (ID 459–473, ฐาน + ำ + วรรณยุกต์ ช่องว่างถึงวงแหวน 74 units) และ TMP ligature 3 ส่วนประกอบ 15 รายการ (รวม 24 รายการ) ครอบคลุม 15 กลุ่ม 440 ครั้งใน corpus 005: น้ำ 250, ซ้ำ 55, ต่ำ 51, ล้ำ 36, ร่ำ 13, ค่ำ 10, ถ้ำ 6, ด่ำ 5, ฉ่ำ/ล่ำ 3, ค้ำ/ย้ำ/ว่ำ 2, น่ำ/ม่ำ 1
- **Candidate fresh-translation-006** = ข้อความและ UI ตรงกับ 005 ทุก byte + fonts bundle ตรงกับ probe-sara-am-glyph-002 ผ่านการทดสอบหน้าจอจริงขอบเขตจำกัดที่ UI Scale กลาง 3 จุด (Settings > Game, tooltip Video, modal เปิดด่านจริงที่เป็นจุดบั๊กเดิม)
- **006 ติดตั้งอยู่ในเกมจริงตามที่ผู้ใช้อนุญาต** (บันทึก reports/fresh-translation-006-install-20261026T0835Z.json): ไฟล์ที่ติดตั้ง = candidate ทั้ง 3 ไฟล์ (fonts 0d1f3dfe…, localisation 74a3c5ef…, UI 34c97796…) ต้นฉบับสำรองที่ local/backups/fresh-translation-006/ (fonts 33aa3489…, localisation c1e7ca97…, UI 2152e5ba…) เซฟสำรอง local/backups/gameplay-save-snapshots/20261026T083508277171Z.zip ยืนยันแล้ว ผมไม่ได้ re-hash ไฟล์ในโฟลเดอร์เกมเอง (นอกขอบเขต mount) อาศัยบันทึกการติดตั้งซึ่ง hash ตรง manifest
- ชุดติดตั้ง/ถอน: Install_Thai_Mod.bat และ Uninstall_Thai_Mod.bat (ผู้ใช้ commit แล้ว 457ec04) เรียก manage_probe.py/backup_gameplay_saves.py เดิม ยังไม่ได้ทดสอบบน Windows จริงโดย PM

## ลำดับงานที่ตรวจรับแล้ว (ทุกรายการมี *_ACCEPTANCE.md ใน docs/)

WO-004 วิเคราะห์ offline INCONCLUSIVE (ไม่รู้รุ่น TMP ที่เกมใช้; ทางหา provenance offline ถูกตัดทิ้ง) → WO-005 + LIG-001 probe ligature [118,42,82]→ก: EXECUTED (เกมรัน ligature 3 ส่วนประกอบจริง) → WO-006 + GLYPH-001: glyph ใหม่ที่ผูกผ่าน ligature อย่างเดียวแสดงผลถูก (STACKED_OK) → WO-007 + GLYPH-002: 15 กลุ่มผ่านครบ (ALL_STACKED_OK; ช่วงสังเกตขาด 110 วินาที PM รับหลักฐาน ห้ามอ้างเวลา modal) → WO-008 สร้าง 006 + แผน regression (ตัดให้แคบลง) → FRESH006-001 PASS_SCOPED → ติดตั้งจริง

PM ตรวจเองอิสระ: hash ของ bundle/ภาพทุกชุด, แกะฟอนต์จาก bundle เทียบด้วย fontTools (glyph เดิม 459 ตัวไม่เปลี่ยน, cmap เท่าเดิม, geometry ของ glyph ใหม่คำนวณซ้ำตรงรายงาน), ดูภาพ native/ขยายเอง ไม่ได้ parse TMP ligature records เอง (อาศัย readback ของ ChatGPT) และไม่ได้ re-hash ไฟล์ในโฟลเดอร์เกม

## ยังเปิด / NOT_TESTED / UNKNOWN

- UI Scale เล็ก/ใหญ่, หน้าจอในแคมปัส (พนักงาน, กิจกรรม, รายการสินค้า, หลักสูตร), กลุ่มที่พบน้อย (ค้ำ ย้ำ ม่ำ ล่ำ น่ำ), ข้อความ bold/rich-text, ผู้ใช้ข้อความอื่น, การเล่นนาน/atlas, ยอด glyph สูงกว่า ascent 19–22 units (ไม่เห็นการตัดในที่ทดสอบ)
- ข้อความแปลใหม่ในอนาคตที่มีรูป [พยัญชนะ][ไม้เอก/โท]ำ นอก 15 กลุ่ม ต้องเพิ่ม glyph+ligature ต่อกลุ่ม ไม่มีการสร้างอัตโนมัติ
- รุ่น/fork ของ TMP ที่เกมใช้ยัง UNKNOWN (IL2CPP ไม่มี package lock)
- BUG-THAI-002 (ตัดกลางคำ) OPEN; BUG-THAI-001 ผ่านเฉพาะ ถี่ ที่ทดสอบ OPEN ส่วนกว้าง; ศัพท์ Good Friends/Best Friends, Pastoral Support, ชื่อโรค/มุก ยังค้าง ไม่อนุมัติทั้งคลัง

## เริ่มงานครั้งหน้า

1. อ่าน checkpoint นี้, PROJECT_STATUS.md, SARA_AM_FRESH006_001_ACCEPTANCE.md; ตรวจ Git/ไฟล์จริงก่อน (ผู้ใช้อาจแก้เอง)
2. ถ้าผู้ใช้เล่นแล้วพบหน้าจอ ต่ำ/น้ำ เพี้ยน: ขอภาพ native + UI Scale แล้วออก WO ตามหลักฐาน ถ้าไม่พบ: ออก WO ทดสอบ UI Scale เล็ก/ใหญ่ (ต้องเปลี่ยนค่าแล้วคืน Medium) ก่อนขยายขอบเขต
3. ก่อนรัน manage_probe ใดๆ ต้องปิดเกมให้สนิท (ตอนนี้เกมอาจยังเปิดอยู่); ถ้า Steam อัปเดต ให้ `check` ก่อน ห้ามฝืนติดตั้ง
4. ถอยกลับ: ปิดเกม แล้ว `python tools/manage_probe.py restore --probe fresh-translation-006` + `check` ต้องได้ original ทั้ง 3 ไฟล์ (หรือ Uninstall_Thai_Mod.bat)

## สิ่งที่ต้องเก็บในเครื่อง (ไม่เข้า Git)

local/prototype/fresh-translation-005, 006 และ probe-sara-am-001a/b, lig-001, glyph-001, glyph-002; local/backups (original 3 ไฟล์ของแต่ละ candidate, gameplay-save-snapshots); local/qa/* (ภาพ native และผลวัด); local/review/sara-am-00x; local/translations/CLAUDE-FULL-RETRANSLATION-001/all-records-review-r5.json. Git clone อย่างเดียวสร้าง bundle ไม่ได้

## หมายเหตุ Git

commit bc60f83 (checkpoint sara-am) โดย PM ใช้ชื่อ/อีเมลของ commit ก่อนหน้า ไม่ได้แก้ git config; ผู้ใช้ commit เพิ่ม b03b05e (reports/sara-am-008-screen-map.json, 1.2 MB ข้อความแปล 410 record ซึ่ง PM เคยกันไว้นอก Git ตามกฎคลังข้อความเต็มอยู่ในเครื่อง ผู้ใช้เลือกรวมเอง) และ 457ec04 (ไฟล์ .bat + doc) ไฟล์ lock ตกค้างที่ PM ย้ายไว้: .git/stale-HEAD.lock-20261026, .git/stale-objects-maintenance.lock-20261026 ลบทิ้งได้; อาจมี tmp_obj_* ค้างใน .git/objects ไม่มีผล ยังไม่ push


## เพิ่มเติม 2026-10-26 (เย็น) — BUG-THAI-002 หลักฐานจริง + candidate 007

- ผู้ใช้รายงาน 2 หน้าจอบน 006 ที่ UI Scale Small: Tips_LS_Paths_Text ตัด `รอบวิ|ทยาเขต`, Freshleigh/Level_Description ตัด `ต่ำแล|ะมี` → local/qa/BUG-THAI-002/ (evidence.json + 2 PNG)
- เตรียม SEGMENTATION-002: cut-map.json ทั้งคลัง (PyThaiNLP newmm + extra-words 69 คำ + guard โครงสร้าง) 11,429 เรคคอร์ด / 84,223 ZWSP; 440 กลุ่ม ำ ไม่โดนแทรก; strip ZWSP = ข้อความ 006 เป๊ะ
- tools/build_fresh_translation_007.py (dry-run ผ่านกับบันเดิล 006 จริงบน Linux; ยังไม่รันบน Windows), manage_probe รับ fresh-translation-007 แล้ว
- ถัดไป: ผู้ใช้ปิดเกม → รัน build 007 → restore 006 / install 007 → WO-VISUAL-019 (docs/qa/WO_VISUAL_019.md) ถ่าย 2 จอเดิม Small+Medium + regression สั้น → ส่งภาพให้ PM ตัดสิน
- 006 ยังติดตั้งอยู่ ไม่มีการแตะไฟล์เกม; BUG-THAI-002 ยัง OPEN
- (ค่ำ) ผู้ใช้ build + install 007 บน Windows ผ่าน (ตัวเลขตรง dry-run); ภาพ WO-019 4 จอ: ต่ำ|และ แก้แล้ว, ทิป/จดหมายตัดถูกขอบคำ, ไม่มี artifact → BUG-THAI-002 = FIX_VERIFIED_SCOPED, **007 ติดตั้งอยู่ตอนนี้** (fallback 006); พบช่องว่างใน เยี่ ยม ที่หัวข้อตัวหนา → บันทึกใต้ BUG-THAI-001 รอเทียบ 006
