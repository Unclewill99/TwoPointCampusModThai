# จุดพักงานล่าสุด — ค่ำ 22 ตุลาคม 2026 (Asia/Bangkok)

ผู้ใช้ขอหยุดวันนี้และกลับมาทำต่อพรุ่งนี้ 23 ตุลาคม 2026. บันทึก checkpoint ในเครื่องและ Git เท่านั้น ไม่ตั้ง automation ไม่ส่งข้อความ ไม่เริ่มทดสอบเพิ่มเติม

## สถานะหลัก

- ชุดแปลล่าสุด fresh-translation-005 ต่อยอด frozen004. 15,677 รายการ เปลี่ยนเฉพาะ I2LS_UI::UI/Modding/Mods::segment-964 จาก ม็อด เป็น Mod. อ่านกลับครบ; รายการอื่น/ฟอนต์/UIไม่เปลี่ยน. ข้อมูล Claude R5 และ frozen004 ยังเดิม
- Mod menu COMPLETE: Antigravity ยืนยันข้อความเมนู PASS และ R2 DESTINATION_PASS; Controllerตรวจภาพและรับผลแล้วใน FRESH_MENU_005_R2_ACCEPTANCE.md. ไม่ต้องทดสอบเมนูซ้ำ
- fresh004 smoke เข้าถึง Settings/Game และ opening modal; หยุดเวลาได้ แต่ staff NOT_RUN เพราะบทสอน. ไม่ใช่ full corpus/runtime/shaping approval
- คำสั่งผู้ใช้: **Controller ไม่ทดสอบหน้าจอเอง**. ทำ build/structural checks/WO/ตรวจรับ; Antigravityทำ visual/runtime QA. ไม่มีช่องทางส่ง Antigravityตรงที่เชื่อมอยู่ จึงส่งมอบ WO เป็นไฟล์และข้อความให้ผู้ใช้ส่งต่อ ห้ามอ้าง dispatch/receipt ก่อนมีหลักฐาน
- ตรวจล่าสุดก่อนพัก: manage_probe.py check --probe fresh-translation-005 ผ่าน original/original/original. ไม่มีชุดทดลองติดตั้งค้าง. local inputs/ภาพ/เซฟ/ZIP/bundleไม่เข้าGit

## BUG-THAI-003 — สระอำและไม้เอกใน ต่ำ

ยัง OPEN. ผลสำคัญอยู่ SARA_AM_002_AB_R2_ACCEPTANCE.md และรายงาน Antigravity docs/qa/WO_SARA_AM_002_AB_R2_REPORT.md

1. Same embedded Thai font reference ใน Chrome155/CSS64px แสดง atomic ต่ำแยกชั้นได้. Hash reference8d28b4497aca41967b15ee957d52bcf0a8c730195f011cd8e45063896cb20b22; font hash f9855a702e9899b9cfa1e8cb7cbf36c2c7bb6fe31ee0cd6860ae61ae012155d0. Reference accepted, ไม่ต้องรันซ้ำ
2. Source GPOSมี MarkToMark glyph59(nikkhahit)->42(mai-ek), serialized TMPเดิมไม่มีคู่นี้. Point30 anchors base(-3.45,23.16), mark(-2.58,16.08). Source GSUBมี sara-am decomposition แต่ serialized MultipleSubstitutionว่าง; อย่าอ้างว่านี่พิสูจน์ root cause หรือไม่มีruntime shapingทุกเส้นทาง
3. เตรียม probe-sara-am-001a/b: localisationเหมือนกัน เปลี่ยนเฉพาะ I2LS_Levels533 เป็นตัวอย่างวินิจฉัย3บรรทัด; bเพิ่ม mark pairหนึ่งคู่. ไม่ใช่ production wording/Unicode rewrite. Font raw object diffเฉพาะ TMP -1239755799206566947. frozen005ไม่เปลี่ยน
4. Antigravity A/B R2 ไปถึง modalจริงทั้งคู่ (สังเกตประมาณ50.8วินาทีหลังcampaign Continue). A: atomic 0E15 0E48 0E33 ซ้อนทั้งสองชุด; B: reordered0E15 0E4D 0E48 0E32 ซ้อนในa แต่แยกในb; C: original-order0E15 0E48 0E4D 0E32 เรียงชั้นกลับด้านเหมือนเดิมทั้งคู่. ถี่ controlไม่เปลี่ยน
5. Controllerเทียบภาพต้นฉบับซ้ำ:74pixelsเปลี่ยนเฉพาะแถวB; A/C=0. reports/sara-am-002-ab-r2-image-diff.json. การเพิ่มกฎช่วยเฉพาะdecomposed specimen **ยังแก้ atomic ต่ำไม่ได้**. ห้ามรวมprobe bเป็นfix005 ห้ามแปลงUnicodeทั้งคลังเพื่อข้ามปัญหา
6. Static modal provider: TPC.MessageTutorialUIหกprefab มี _text/ข้อมูลหลักสูตร/intake; MAIN controller4694779218175474965 -> TMP7894969370473676053, size36/kerning/rich-textเปิด. external8ตรงCABของfonts bundle; PalanquinDark_Regular1456777345258535221มีfallbackไปreusedThai TMP. Diagnostic recordยืนยันถึงmodal; ผลbสนับสนุนการใช้featureที่แก้ในบริบทนี้ แต่ไม่พิสูจน์font fallbackทุกconsumerหรือengine internalsทั้งหมด

## การควบคุมและเซฟ

- ห้ามกลับไปใช้negative color-band index/พิกัดเก่า. qa_driverรับnormalized1920x1080; จากnativeWxHใช้ x*1920/W,y*1080/H เก็บprecisionจนdriverround. ในsubprocessเรียกset_desktopก่อนqueryforeground. การqueryก่อนattachให้0เคยพบ แต่ไม่ใช่หลักฐานว่าfocusเสียจริงทุกครั้ง
- เพิ่มSendInput signatureและตรวจreturn1/1; mock guard+compileผ่าน. Accepted input countไม่เท่ากับgame action. Native load+flyoverใช้มากกว่า30วินาที; WOล่าสุดให้รอ60วินาทีโดยไม่คลิกข้ามและเก็บภาพตามหน้าจอจริง
- A/Bรอบแรกและoriginal gateติดsetup/time limit ไม่ใช่font FAIL. รักษารายงานประวัติไว้; R2ให้diagnostic resultแล้ว ไม่ต้องรันA/Bเดิมซ้ำ
- Antigravityรายงานrestoreครบและ8000.savไม่เปลี่ยน hash5b4dac72e35d877f6b7f2d6933a8b0c44717ec2578052d1d9f218f983d050d0d. สำรองA/B R2:20261022T155048899070Z.zip และ20261022T155759988590Z.zip พร้อมmanifestในlocal/backups/gameplay-save-snapshots/. Career/profileอาจเปลี่ยนตามการเข้าเกม; เก็บlive+backup ไม่rollbackอัตโนมัติ. Controllerตรวจสามbundleเองแต่ไม่ได้คำนวณsavecomparisonทุกครั้งซ้ำ

## เริ่มงานพรุ่งนี้

1. อ่านcheckpointนี้, PROJECT_STATUS.md, SARA_AM_002_AB_R2_ACCEPTANCE.md; ตรวจGit/ไฟล์จริงก่อนทำต่อ อย่าสมมติว่าไม่มีคนแก้
2. เลือกทางแก้ที่รักษาatomicข้อความเดิม: ตรวจความเป็นไปได้renderer-level decomposition/reordering หรือatomic glyph-pair adjustmentที่มีขอบเขตชัด. วิเคราะห์offlineก่อนออกruntimeWOใหม่; ห้ามglobalglyphshiftหรือpatchbinaryแบบเดา
3. ถ้าทำcandidateใหม่ แยกจากfrozen005/diagnostic001a/b; ตรวจstructural diff/readback/hash แล้วออกWOให้Antigravityพร้อมatomic ต่ำและถี่ regression. ยังไม่มีactive runtimeWOค้างหลังรับR2
4. BUG-THAI-002ตัดกลางคำยังOPEN; BUG-THAI-001ผ่านเฉพาะถี่เดิมและติดตามbroaderregression. ศัพท์ Good Friends/Best Friends, Pastoral Support, ชื่อโรค/มุก/ข้อเสนอศัพท์ยังค้าง ไม่อนุมัติทั้งคลัง

## สิ่งที่ต้องเก็บในเครื่อง

local/translations/CLAUDE-FULL-RETRANSLATION-001/all-records-review-r5.json; local/prototype/fresh-translation-004,005 และprobe-sara-am-001a/b; local/review/sara-am-001/reference.html+manifest; ภาพuser/native reference/Antigravityทั้งหมด และverifiedsavebackups. Gitcloneอย่างเดียวสร้างbundleไม่ได้

เครื่องมือใหม่ tools/build_fresh_translation_005.py, build_sara_am_001.py, audit_sara_am.py, trace_sara_am_modal.py; managerรองรับ005/001a/001b. Build scriptsไม่เขียนทับoutputเดิม (exist_ok=False). รายงานสำรวจบางไฟล์สร้างด้วยone-off read-only inspection จึงไม่ควรอ้างว่าทุกรายงานสร้างซ้ำได้จากauditสคริปต์เดียว
