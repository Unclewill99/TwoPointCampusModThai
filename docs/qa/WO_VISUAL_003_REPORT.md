# WO-VISUAL-003 — PASS within target-word visual test scope

วันที่ทดสอบซ้ำ: 2026-10-16 ประมาณ 08:21–08:25 Asia/Bangkok (UTC+07:00)
สถานะล่าสุด: **PASS ตามขอบเขต WO-VISUAL-003** — คำเป้าหมายเทียบ same-font reference จากภาพผู้ใช้ผ่าน และยืนยัน browser zoom 100% แล้ว; ไม่ใช่ full shaping PASS และไม่ปิด BUG-THAI-001 ทั้งระบบ ส่วนบันทึก BLOCKED/zoom UNKNOWN ด้านล่างเป็นประวัติก่อนรับหลักฐานครบ
คืนต้นฉบับ: **PASS ทั้งสองไฟล์ original** หลัง restore และ check; เก็บ backup ไว้

## ผลหลัก
probe-003 แสดงไม้เอกใน “ถี่” เป็นขีดตั้งอยู่เหนือสระอี แยกชั้นชัดในภาพขยาย Medium/Large และยังเห็นการแยกใน Small เมื่อเทียบกับภาพ probe-002 ที่เครื่องหมายชิดรวมเป็นรูปแบน ผลคงอยู่หลังปิด/เปิดเกมใหม่หนึ่งรอบ
ไม่พบ glyph หาย ลอยห่างหรือถูกตัดชัดเจนในคำเป้าหมาย แต่ยังไม่รับรองความถูกต้องเทียบฟอนต์อ้างอิง เพราะ reference ไม่ได้เปิด/ยืนยันการโหลด
ไม่ปิด BUG-THAI-001 หรือให้ full shaping PASS จากคำเดียว

## เอกสารและสภาพแวดล้อม
อ่าน WO_VISUAL_003.md, BUG_THAI_001.md, WO_VISUAL_002_REPORT.md, PROBE_003_FINDINGS.md, manifest และ installer ก่อนทำงาน
- Game build ที่เห็นจริง: 10.3.169253+2024-12-06.1241
- Prototype: probe-003, Museum serialized font-feature experiment ตาม manifest; ไม่อนุมาน runtime consumption ของทุกรายการจากการโหลด bundle
- English; Medium เริ่มต้นและหลังจบ; ตรวจ Small และ Large แล้วคืน Medium
- Resolution ที่อ่านจริงใน Video: 3840 x 2160 @ 60hz; Full Screen Window; ไม่ Apply resolution
- ภาพจับ 1920 x 1080 ไม่ใช่การอนุมาน render resolution
- Windows @oai/sky จับภาพและควบคุม TPC.exe จริง เปิดผ่าน Steam ปิดด้วย Quit ไม่มี force-close
- ไม่โหลดเซฟ ไม่บันทึกทับเซฟ ไม่ล้าง cache; restart ไม่พิสูจน์ persistent-cache clearing
- ไม่แก้ font/translation/catalog/code/hash ระหว่างทดสอบ ไม่เปลี่ยน branch ไม่ commit/push ไม่ upload binary/font

## จุดตรวจ
Screen: Settings > Game, ป้าย Career Autosave Frequency
Key ตาม BUG_THAI_001.md: UI/Settings/CareerAutosaveFreq
Text: ความถี่บันทึกอัตโนมัติโหมดอาชีพ
ถี่: ถ U+0E16 + ี U+0E35 + ่ U+0E48

## ผลแต่ละกรณี
| กรณี | ผล | หลักฐานและขอบเขต |
|---|---|---|
| เปิดเกมและเข้าเมนู | PASS | 01-probe-menu.jpg |
| เทียบอาการกับ probe-002 | PASS เฉพาะเห็นการเปลี่ยนแปลง | baseline-probe002-close.png เทียบ 02-medium-close.png; ไม่ติดตั้ง probe-002 ซ้ำ |
| ี/่ แยกชั้นในเกม Medium | PASS เฉพาะ visual separation | 02-game-medium.jpg และ 02-medium-close.png; ยังไม่ใช่ trusted-reference conformance |
| Small/Large | PASS เฉพาะคำเป้าหมาย | 05/06 ภาพเต็มและ close; Small มีรายละเอียดน้อยจากขนาดภาพ แต่ไม้เอกยังอยู่เหนือสระ |
| Restart แล้วคำเป้าหมาย | PASS เฉพาะ separation | 08-restart-medium.jpg และ 08-restart-close.png |
| Language ปิด/เปิด | PASS | English อ่านได้ทั้งช่อง selected และ options ภาพ 02/03 |
| UI Scale ปิด/เปิด | PASS | Medium และ Small/Medium/Large options ภาพ 02/04; คืน Medium ก่อน Video/restart |
| Video current values | PASS | 07-video-medium.jpg: Full Screen Window, 3840 x 2160 @ 60hz, On, SMAA อ่านได้ |
| ไทยยังอยู่ | PASS เฉพาะที่เห็น | ป้าย Career Autosave, ภาษาเสียงพากย์, การตั้งค่าขั้นสูง |
| same-font browser reference | BLOCKED | file URL ถูก browser security policy ปฏิเสธ; ไม่ใช้ทางอ้อม |
| document.fonts.load/check | NOT_RUN | ไม่เข้าถึงหน้าที่เปิดอยู่; ไม่มี loaded FontFace evidence |
| browser zoom / reference screenshot | NOT_RUN | ไม่เปิดหน้า; ไม่เดา zoom |
| full shaping / synthetic corpus / wrapping | NOT_RUN | นอกขอบเขตและไม่ได้ฉีด corpus |
| restore/hash | PASS | ทั้งสอง original และไม่มีหน้าต่างเกมหลัง Quit |

## หลักฐานภาพ
อยู่ local/qa/WO-VISUAL-003/screenshots/ ทุกภาพที่อ้างถูกเปิดตรวจจริง
- 00-steam-retry.jpg — ยืนยันควบคุม Steam ได้ในรอบ retry
- 01-probe-menu.jpg — build และเมนู
- 02-game-medium.jpg — คำเป้าหมาย, English, Medium และ dropdown ปิด
- 03-language-open.jpg — Language options
- 04-scale-open.jpg — Scale options
- 05-game-small.jpg, 06-game-large.jpg — เปรียบเทียบ scale
- 07-video-medium.jpg — ค่าปัจจุบัน Video
- 08-restart-medium.jpg — ผลซ้ำหลังเริ่มเกมใหม่
- baseline-probe002-close.png — crop จาก local/qa/WO-VISUAL-002/screenshots/06-probe-game-closed.jpg ที่เปิดดูจริง
- 02-medium-close.png, 05-small-close.png, 06-large-close.png, 08-restart-close.png — crop ขยาย nearest-neighbor 4 เท่าจาก screenshot ที่บันทึก ไม่ใช่ภาพ render ใหม่ ไม่ sharpen หรือแก้ glyph
Medium/baseline crop พิกัด (25,495)-(350,545); Small (20,435)-(290,480); Large (25,535)-(385,585) ของภาพ 1920x1080
ขนาดและ antialiasing ไม่ใช้วัดความเท่ากันระดับ pixel ของ font reference

## Reference blocker และประวัติรอบแรก
ก่อน retry เคยหยุดก่อนติดตั้งเพราะ Steam minimized/user-input detection; รอบ retry นี้กู้ Steam และตรวจเกมสำเร็จ จึงแทนรายงาน BLOCKED เดิม โดยสำรองรายงานเดิมไว้ previous-blocked-report.md
การเปิด local/prototype/probe-003/same-font-reference.html ผ่าน browser tool ถูก URL policy ปฏิเสธ protocol file: จึงไม่เปลี่ยนช่องทาง/serve ผ่าน protocol อื่นเพื่อข้ามข้อจำกัด
ได้ขอผู้ใช้เปิดหน้าเองระหว่างตรวจเกม แต่จนจบ runtime ยังไม่พบ reference window หรือคำตอบว่าเปิดแล้ว จึงไม่อ้างว่า reference โหลดสำเร็จ
matching_font_sha256 ใน manifest คือ f9855a702e9899b9cfa1e8cb7cbf36c2c7bb6fe31ee0cd6860ae61ae012155d0 เป็นข้อมูล manifest ไม่ใช่การยืนยัน loaded browser font
ต้องตรวจ reference ต่อก่อนรับรองว่าตำแหน่งตรงกับฟอนต์เดียวกันอย่างครบตาม WO

## Manifest bundle hashes
| ไฟล์ | Original SHA-256 | Probe SHA-256 |
|---|---|---|
| fonts_assets_all.bundle | 33aa34892719fbc7caaabd0a292c32bb135bc61978a4cd3ce73c6c40da8f4e6e | 588f15fad01635da3fb5b86d5c3946cbb7bd85b40304364294fb23d73c207f3e |
| localisation_assets_localisationenglish.bundle | c1e7ca97f260813ccc9a1cf463f20d066631f8e5616bf797fe8d5ae93227878f | 4f1e6033cd54b3bf6f97a3f644dd9598514bac6d53781dcc235fe8d3177dd567 |

## คำสั่งและคืนค่า
ทุกคำสั่งจัดการ probe ใช้ --probe probe-003 และ exit 0:
1. python tools/manage_probe.py check --probe probe-003 → original/original
2. python tools/manage_probe.py install --probe probe-003 → probe/probe
3. python tools/manage_probe.py check --probe probe-003 → probe/probe
4. python tools/manage_probe.py restore --probe probe-003 → original/original
5. python tools/manage_probe.py check --probe probe-003 → original/original

output ตรงพร้อม exit code: local/qa/WO-VISUAL-003/command-evidence-retry.json และ .txt รายคำสั่ง
install/restore ใช้สิทธิ์ที่ระบบอนุมัติเพื่อ process guard ไม่ลบ guard ไม่คัดลอกเอง
เวลา check สุดท้ายประมาณ 08:25:06; list_windows ไม่พบ Two Point Campus; backup local/backups/probe-003 คงไว้

## แจ้ง Controller
ผลไม่ใช่ no-change: “ถี่” แยกชั้นดีขึ้นจาก probe-002 และคงหลัง restart โดย dropdown ยังผ่านในหน้าที่ตรวจ แต่ same-font reference comparison ยัง BLOCKED จึงยังไม่ให้ overall mark-fix acceptance PASS
คืนต้นฉบับสำเร็จทั้งสองไฟล์ ไม่มี commit/push


## Reference follow-up 2026-10-16

Static verification completed: embedded reference TTF SHA-256 matches manifest
`f9855a702e9899b9cfa1e8cb7cbf36c2c7bb6fe31ee0cd6860ae61ae012155d0`.
Font name table identifies Noto Sans Thai Medium, Version 2.002 (PostScript NotoSansThai-Medium).
Evidence: local/qa/WO-VISUAL-003/reference-static-verification.json.
Both installed game bundles were hashed again and match originals; no installation, commit or push performed.

The local reference page now includes a visible font-load evidence panel reporting FontFace load count,
family/status/weight and document.fonts.check. Font bytes, reference text and font styling are unchanged.
This panel has NOT yet been executed/observed in a browser, so static checks do not establish loaded-font evidence.
Window inventory found Chrome on ChatGPT, with no reference window identified.
Prior file URL security refusal remains respected: no alternate server/protocol used.
Next required step: user opens local/prototype/probe-003/same-font-reference.html directly in their browser;
then inspect the evidence panel, record browser zoom and capture BUG-THAI-001 for comparison with saved game screenshots.
Overall reference acceptance remains BLOCKED pending that observation.

## User-supplied reference evidence — 2026-10-16

ผู้ใช้ส่งภาพ Chrome ของหน้า same-font-reference.html หลังเปิดเอง เก็บสำเนาไว้ที่
`local/qa/WO-VISUAL-003/screenshots/09-user-same-font-reference.png`
SHA-256: `4065e366626edaa6b5b24d4e63756e2bec6de8d1d05030401b870a7273c542c1`.
ภาพนี้เป็นหลักฐานจากผู้ใช้ ไม่ใช่การจับ browser session โดย agent; browser tool ยังปฏิเสธ file URL และไม่ได้ใช้ช่องทางอ้อม

แผงในภาพอ่านได้ว่า referenceFont=ProbeThai, loadCount=1, family=ProbeThai,
status=loaded, weight=500, check=true, verifiedLoaded=true, devicePixelRatio=2,
visualViewportScale=1. จึงมีหลักฐานการโหลด custom FontFace จากภาพจริงแล้ว
ประกอบกับ static hash verification ก่อนหน้า ซึ่งระบุ Noto Sans Thai Medium Version 2.002
และ hash ของ embedded font ตรง manifest ไม่ใช่การตรวจ bytes ใน browser memory โดยตรง

ตรวจภาพอ้างอิงส่วน BUG-THAI-001: ใน “ความถี่” และ “ถี่” ไม้เอกเป็นขีดตั้งเหนือสระอี มีช่องแยกชั้น
เปิดตรวจ 02-medium-close.png กับ baseline-probe002-close.png ซ้ำในรอบนี้:
probe-003 แสดงลักษณะขีดตั้งและการแยกเหนือสระอีสอดคล้องกับ reference ในเชิงสัมพัทธ์
ขณะที่ probe-002 ชิดรวมเป็นแนวนอนกว่า จึงให้ PASS เฉพาะ visual separation ของคำเป้าหมายเทียบ reference
ไม่รับรองระยะ offset เท่ากันระดับ pixel หรือผล shaping ของคำอื่นจากภาพนี้
ผล restart/Small/Large/dropdown อาศัยหลักฐาน runtime ที่ตรวจไว้ก่อนหน้า ไม่ได้รันเกมซ้ำในรอบรับภาพ

Browser zoom ยัง UNKNOWN: ไม่มีเมนู zoom ในภาพ; devicePixelRatio=2 และ visualViewportScale=1
ไม่พิสูจน์ว่า browser zoom=100%. ข้อนี้ยังต้องบันทึกตาม WO ก่อนปิดเอกสารเต็ม
PDF ที่ผู้ใช้ให้มาไม่ได้ใช้แทนหลักฐาน screen rendering หรือ zoom ในการตัดสินรอบนี้
ไม่มีการติดตั้ง probe ซ้ำ แก้ game bundles, commit หรือ push ในรอบรับหลักฐาน

## Final zoom evidence and scoped acceptance — 2026-10-16

ผู้ใช้ส่งภาพเมนู Chrome ซึ่งแสดง Zoom **100%** ชัดเจน โดยยังเห็นหน้า reference อยู่ด้านหลัง
เก็บต้นฉบับภาพที่ `local/qa/WO-VISUAL-003/screenshots/10-user-browser-zoom-100.png`.
หลักฐานนี้ยืนยันค่าจากเมนูโดยตรง แทนการอนุมานจาก devicePixelRatio/visualViewportScale
จึงปลดข้อค้างเรื่อง zoom และ same-font reference ของ WO นี้แล้ว

ผลสรุป **PASS ภายในขอบเขต WO-VISUAL-003**: probe-003 แยก ี/่ ใน “ความถี่”
สอดคล้องกับ reference ฟอนต์เดียวกัน และดีขึ้นจาก probe-002; ผล runtime ที่บันทึกไว้คงอยู่หลัง restart,
Small/Large และ dropdown ผ่านตามกรณีที่ตรวจ พร้อมคืน original/hash ผ่านทั้งสองไฟล์
การรับรองอาศัย runtime evidence เดิมร่วมกับภาพ reference และ zoom ที่ผู้ใช้ส่งภายหลัง
ไม่มีการอ้างว่าได้เทียบ live side-by-side หรือรันเกมซ้ำในรอบรับภาพ
ไม่รับรอง pixel-identical placement, corpus shaping/wrapping ทั้งชุด หรือปิด BUG-THAI-001 ทั้งระบบ
ไม่ติดตั้งถาวร ไม่มี commit/push; backups ยังคงไว้ตาม WO
