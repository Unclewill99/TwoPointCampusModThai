# WO-VISUAL-001 — probe-001 visual report

สถานะรวม: **FAIL — โหลดต้นแบบและแสดงไทยได้ แต่พบค่าของ dropdown ว่าง**
คืนไฟล์ต้นฉบับ: **PASS** ทั้งสองไฟล์; ปิดเกมแล้ว; เก็บ backup ไว้

## เวลาและสภาพแวดล้อม
- ทดสอบ 2026-10-15 ประมาณ 21:16–21:25 Asia/Bangkok (UTC+07:00); หลักฐานเริ่มใหม่ 21:23
- Game build เห็นจริงที่มุมซ้ายบนเมนู: 10.3.169253+2024-12-06.1241
- Unity 2020.3.47f1 อ้างอิง reports/initial-inspection.json ไม่ใช่การอ่านจาก UI
- Prototype revision: probe-001 ตาม local/prototype/probe-001/manifest.json (ไม่มี revision แยกเพิ่มเติม)
- English: เปิด Language และคลิก English จริง (ภาพ 06)
- UI Scale: ตัวเลือกจริง Small / Medium / Large; Medium ไฮไลต์ และคลิก Medium สำหรับการทดสอบ ไม่อ้างตัวเลขเปอร์เซ็นต์ที่เกมไม่ได้แสดง
- ความละเอียดปัจจุบัน: **BLOCKED สำหรับการอ่านค่ายืนยัน** เพราะช่อง Resolution ว่าง; เมื่อเปิด dropdown พบ 3840 x 2160 @ 60hz ไฮไลต์ (ภาพ 09) แต่ไม่ถือเป็นการยืนยันค่าที่ใช้งานโดยลำพัง ไม่ได้กด Apply หรือเปลี่ยนความละเอียด
- ภาพหลักฐานที่เครื่องมือส่งกลับมีขนาด 1920 x 1080; นี่คือขนาดภาพจับ ไม่ใช่หลักฐานความละเอียด render ของเกม
- ใช้ Windows computer-use (@oai/sky), มองเห็นหน้าต่าง TPC.exe จริงและกดเมนูได้; ไม่ใช่ localhost/browser-only
- ไม่โหลดเซฟ ไม่บันทึกทับเซฟ ไม่มีการล้าง cache; เริ่มเกมใหม่ไม่พิสูจน์ว่าล้าง persistent cache

## Manifest SHA-256
| Bundle | Original | Probe |
|---|---|---|
| fonts_assets_all.bundle | 33aa34892719fbc7caaabd0a292c32bb135bc61978a4cd3ce73c6c40da8f4e6e | d4ee75cb2a54f9f17384c55a9b397cb7a53acf3976301cb868cb2f5ab04e0549 |
| localisation_assets_localisationenglish.bundle | c1e7ca97f260813ccc9a1cf463f20d066631f8e5616bf797fe8d5ae93227878f | a15a40549f1c32b31acbf5a047245648344a0da3f8975ac2bb37768c1688c745 |

## ขั้นตอนและผลคำสั่ง
1. อ่าน handoff, test matrix, acceptance และ bug template ก่อนเริ่ม
2. เปิดเกมเดิมผ่าน Steam เพื่อตรวจความสามารถจริง เห็น startup และเมนู แล้วกด Quit; ไม่มีงาน gameplay ที่ยังไม่บันทึก
3. python tools/manage_probe.py check → exit 0, ทั้งสอง original
4. install ครั้งแรก → exit 1: tasklist ในตัวป้องกัน process คืน non-zero ก่อนถึงการเปลี่ยนไฟล์
5. รัน install เดิมด้วยสิทธิ์ที่ระบบอนุมัติ → exit 0, ทั้งสอง probe; ไม่แก้สคริปต์ ไม่คัดลอกเอง
6. check → exit 0, ทั้งสอง probe
7. เปิดด้วย Steam, เข้า Game / Video / Audio / Controls; ตรวจ Language และ UI Scale; กด Quit
8. เปิดซ้ำด้วย Steam, เข้าเมนูและ Game / Audio อีกครั้ง; กด Quit
9. restore ด้วยตัวจัดการเดิม → exit 0, ทั้งสอง original
10. check → exit 0, ทั้งสอง original; รายการหน้าต่างไม่มี Two Point Campus
ผลคำสั่งเก็บใน [command-evidence.json](../../local/qa/WO-VISUAL-001/command-evidence.json)
ผล check แรกในไฟล์หลักฐานเป็นการถอด JSON ที่แสดงจริงจาก tool output; ผล install/restore และ check ถัดมาเก็บ output ของเครื่องมือ
PowerShell มีข้อความ InitializeDefaultDrives ของสภาพแวดล้อมบางครั้ง แต่ check สำเร็จตาม exit code และ JSON

## ผลตามรายการ WO
| กรณี | ผล | สิ่งที่เห็น / ขอบเขต |
|---|---|---|
| เปิดเกมและเข้าเมนู | PASS | เปิดผ่าน Steam สองรอบพร้อม probe; ไม่เห็น error dialog หรือค้างในช่วงตรวจ |
| Settings pilot แสดงไทย | PASS | เห็น “ภาษาเสียงพากย์”, “เสียง”, “การตั้งค่าขั้นสูง”, ป้ายความไวกล้อง; เป็นบางรายการ ไม่ใช่ 50/50 |
| ไม่มีตัวหาย / สี่เหลี่ยม / ช่องว่าง | FAIL | ค่าปัจจุบันของ dropdown หลายช่องว่าง ทั้ง Game และ Video; ไม่พบ tofu ชัดเจนในข้อความที่อ่านได้ |
| ตำแหน่งสระ/วรรณยุกต์ทั้งหมด | NOT_RUN | ตัวอย่าง pilot อ่านได้ในภาพ แต่ยังไม่มีการเทียบ trusted shaping reference และไม่มี diagnostic corpus; ไม่ให้ PASS รวม |
| อังกฤษ ตัวเลข สัญลักษณ์ | PASS | เฉพาะที่พบ: เมนูอังกฤษ, 0, build, รายการความละเอียด x และ @; ไม่ใช่ coverage ทุกตัว |
| ป้ายเมนูล้น/ทับ/เล็กเกินอ่าน | PASS | เฉพาะป้ายที่มองเห็นในหน้าและ scale ที่ตรวจ; ไม่พบการล้นชัดเจน; ไม่ครอบคลุมทุก scroll position |
| ปิดและเปิดใหม่ | PASS | เมนูและไทยยังโหลด; ช่อง dropdown ยังว่าง; ไม่ได้ยืนยัน cache ว่าง |
| หลายหน้า Settings | PASS | รอบแรก Game/Video/Audio/Controls; รอบสอง Game/Audio; ไม่ใช่ atlas stress test เต็มรูปแบบ |
| คืนไฟล์ | PASS | restore + check = original ทั้งสอง |

## Test matrix
- TM-VOWEL-01, TM-VOWEL-02, TM-VOWEL-03: BLOCKED — synthetic input ยังไม่ฉีด
- TM-DESC-01, TM-DESC-02: BLOCKED — synthetic input ยังไม่ฉีด และยังไม่มี trusted reference สำหรับรูป glyph
- TM-STACK-01, TM-STACK-02: BLOCKED — synthetic input ยังไม่ฉีด
- TM-AM-01, TM-AM-02, TM-AM-03: BLOCKED — synthetic input ยังไม่ฉีด
- TM-WRAP-01, TM-WRAP-02, TM-WRAP-03: BLOCKED — synthetic input ยังไม่ฉีด
- TM-MIX-01, TM-MIX-02: BLOCKED — ไม่ใช่ corpus เดียวกับข้อความอังกฤษ/ตัวเลขที่เห็นในเมนู
- TM-CAND-01, TM-CAND-02: BLOCKED — ยังไม่มี input/parser grammar และ runtime substitution evidence
- TM-UI-01, TM-UI-02: BLOCKED — ไม่ได้ฉีดป้ายแต่ละคำหรือ tooltip corpus
- TM-SCALE-01: NOT_RUN — ไม่ได้ทดสอบข้ามความละเอียด; ค่าปัจจุบันอ่านยืนยันไม่ได้
- TM-SCALE-02: NOT_RUN — พบ Small/Medium/Large จริง แต่ทดสอบเพียง Medium; ไม่ผ่านช่วงค่าต่ำสุด/สูงสุด
- Notifications/classes และ pilot ที่ไม่พบ: NOT_RUN — จำกัดเมนู/Settings ไม่เล่นเกมเพื่อเปิดข้อความ
- N/A: ไม่มีรายการที่ยืนยันว่าเกมไม่รองรับ; UI Scale มีจริงจึงไม่ใช้ N/A

## BUG-WOVIS-001 — ค่าปัจจุบันใน dropdown ของ Settings ไม่ปรากฏ
- Status: FAIL
- Severity: Major — อ่านค่าปัจจุบันของภาษา, UI Scale, autosave และ video ไม่ได้ ลดความสามารถในการตรวจ/ตั้งค่า
- Environment: build และ probe ตามด้านบน; English; Medium หลังเลือกจริง
- Screen/location: Settings > Game ช่องค่าด้านขวา Log Level, Game Autosave Frequency, ความถี่บันทึกอัตโนมัติโหมดอาชีพ, Language, ภาษาเสียงพากย์, UI Scale; Settings > Video ช่อง Fullscreen Mode, Resolution, VSync, Antialiasing
- String key: ระบุไม่ได้จากภาพ ใช้ชื่อหน้าจอ/ตำแหน่ง ไม่เดา key
- Steps: install/check probe → Steam Play → Settings → สังเกตค่าที่ปิดรายการ → เปิด dropdown Language/UI Scale/Resolution → ปิดและเปิดเกมใหม่ → ตรวจซ้ำ
- Expected: มองเห็นข้อความของค่าปัจจุบันขณะ dropdown ปิด
- Observed: กล่องมีพื้นหลังและลูกศรแต่ข้อความค่าปัจจุบันว่าง; รายการเมื่อเปิดกลับแสดง English, Medium และรายการความละเอียดได้; เกิดซ้ำหลัง restart
- Evidence: ภาพ 05–09 และ 13
- Font/atlas: กลยุทธ์ manifest ใช้ dynamic Arabic slot กับ Thai source font; runtime source identity และ atlas state ไม่ได้ตรวจ
- Hypothesis: อาจเกี่ยวกับเส้นทาง font/material ของข้อความ selected value หรือการโหลด reference; ยังไม่มีหลักฐานระบุสาเหตุ และไม่ได้ทดลองแพตช์
- ข้อจำกัด: ไม่ได้ตรวจหน้า Settings เดิมก่อนติดตั้งหรือหลัง restore เพื่อเทียบ A/B จึงยังไม่ยืนยันว่าข้อบกพร่องนี้เกิดจาก probe เพียงสาเหตุเดียว

## ภาพหลักฐานที่เปิดดูจริง
ทุกภาพในรายการด้านล่างถูกแสดงและตรวจด้วยสายตาจากเครื่องมือก่อนบันทึก; ไม่มีการอ้างภาพที่ยังไม่เปิดดู
โฟลเดอร์: local/qa/WO-VISUAL-001/screenshots/

| ภาพ | หน้าจอ / ผลที่รองรับ |
|---|---|
| 00-steam-preflight.jpg | Steam library / ปุ่ม Play |
| 01-original-startup.jpg | เกมเดิม หน้าลิขสิทธิ์ |
| 02-original-menu.jpg | เมนูเดิมและ build |
| 03-probe-startup.jpg | หน้าลิขสิทธิ์เมื่อใส่ probe; อังกฤษยังอ่านได้ |
| 04-probe-menu.jpg | เมนู probe รอบแรก |
| 05-probe-game-settings.jpg | ไทยใน Game และค่าหลายช่องว่าง |
| 06-language-english.jpg | Language dropdown เปิด แสดง English |
| 07-ui-scale-options.jpg | Small/Medium/Large; Medium ไฮไลต์ก่อนคลิกเลือก |
| 08-video-settings.jpg | ไทยการตั้งค่าขั้นสูงและค่า Video ว่าง |
| 09-resolution-options.jpg | รายการจริง 3840 x 2160 @ 60hz ไฮไลต์; ไม่แทนการยืนยัน current value |
| 10-audio-settings.jpg | หัวข้อ “เสียง” |
| 11-controls-settings.jpg | ป้ายความไวกล้องภาษาไทย |
| 12-restart-menu.jpg | เมนูหลังเปิดใหม่ |
| 13-restart-game-settings.jpg | ไทยและช่องว่างเกิดซ้ำ |
| 14-restart-audio.jpg | หัวข้อไทยหลังเปิดใหม่ |

## ส่งมอบ Controller
probe-001 โหลดและแสดงไทยบางรายการใน Settings ได้จริง แต่ยังไม่ผ่าน visual acceptance เพราะค่าปัจจุบันใน dropdown ว่าง ต้องตรวจสาเหตุโดยงานวิศวกรรมแยกต่างหาก ไม่มีการแก้คำแปล โค้ด catalog หรือ hash ในรอบนี้ ไม่มี branch/commit/push หรือ upload bundle/font
ยืนยันคืน bundle ต้นฉบับสำเร็จทั้งสองไฟล์และคง backup ไว้
รายงาน BLOCKED เดิมที่มีอยู่ก่อนงานนี้สำรองไว้ local/qa/WO-VISUAL-001/previous-blocked-report.md; รายงานนี้เป็นผลรอบ Windows จริงแทนรายงานเดิม
