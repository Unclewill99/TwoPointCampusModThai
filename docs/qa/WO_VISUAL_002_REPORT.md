# WO-VISUAL-002 — original / probe-002 Settings comparison

**ผลรวม: PASS เฉพาะขอบเขตการเปรียบเทียบนี้**
ค่าปัจจุบันของ dropdown แสดงได้ในเกมเดิมและ probe-002 ทั้งขณะปิดและเปิดรายการ ภาษาไทยในชุดนำร่องยังแสดงได้ และผลยังคงเดิมหลังปิด/เปิดเกมใหม่หนึ่งรอบ
**คืนต้นฉบับ: PASS — ทั้งสอง bundle เป็น original หลัง restore และ check**

## สภาพแวดล้อมและวิธีทดสอบ
- วันที่ 2026-10-15, ประมาณ 21:34–21:40 Asia/Bangkok (UTC+07:00)
- baseline Game capture: 21:35:23; เริ่ม Steam รอบ restart: 21:38:35; ตรวจคืนค่าจบ: 21:39:47
- Game build ที่เห็นจริงบนเมนู: 10.3.169253+2024-12-06.1241
- Prototype revision: probe-002; manifest ไม่ระบุ revision ย่อย
- กลยุทธ์ตาม manifest: คง English font mappings/materials เดิมและเพิ่ม Thai dynamic slot เป็น fallback ลำดับท้าย
- ใช้ทักษะ computer-use ที่อ่านในรอบก่อนและ Windows @oai/sky; มองเห็น TPC.exe จริง คลิกเมนู และบันทึกภาพได้
- ภาษา English, UI Scale **Medium** เห็นค่าขณะปิดทั้ง baseline/probe/restart; ไม่เปลี่ยน scale
- Resolution **3840 x 2160 @ 60hz**, Fullscreen Mode **Full Screen Window** อ่านจากช่องค่าปิดจริงทั้ง baseline/probe/restart
- ภาพเครื่องมือขนาด 1920 x 1080 ไม่ใช้ขนาดภาพมาคาดเดาความละเอียดเกม
- ไม่กด Apply ความละเอียด ไม่โหลดเซฟ ไม่แก้คำแปล/font/catalog/hash ไม่เปลี่ยน branch ไม่ commit/push ไม่อัปโหลด binary/font
- อ่าน WO_VISUAL_002.md, WO_VISUAL_001_REPORT.md และ PROBE_001_HANDOFF.md ก่อนติดตั้ง
- ทุกคำสั่งจัดการ probe ในรอบนี้มี --probe probe-002; ไม่ติดตั้ง probe-001
- ปิดด้วย Quit ตามเมนูก่อน install/restore; ตัวจัดการตรวจ process ก่อนแก้ไฟล์ ไม่มี force-close
- ไม่ล้าง cache; restart ไม่พิสูจน์ว่า persistent cache ถูกล้าง

## Manifest SHA-256
| Bundle | original_sha256 | probe_sha256 |
|---|---|---|
| fonts_assets_all.bundle | 33aa34892719fbc7caaabd0a292c32bb135bc61978a4cd3ce73c6c40da8f4e6e | 167c3cabce9bdf40a1a9f5efc19dc9ad58e4d9bf26143248ecd6ac2648e9757a |
| localisation_assets_localisationenglish.bundle | c1e7ca97f260813ccc9a1cf463f20d066631f8e5616bf797fe8d5ae93227878f | 4f1e6033cd54b3bf6f97a3f644dd9598514bac6d53781dcc235fe8d3177dd567 |

## คำสั่งและการคืนค่า
รันจากโฟลเดอร์ ThaiCampusMod; ผลทุกคำสั่ง exit 0

| คำสั่ง | ผลทั้งสองไฟล์ |
|---|---|
| python tools/manage_probe.py check --probe probe-002 | original ก่อน baseline; ตรวจ original อีกครั้งก่อน install |
| python tools/manage_probe.py install --probe probe-002 | probe |
| python tools/manage_probe.py check --probe probe-002 | probe |
| python tools/manage_probe.py restore --probe probe-002 | original |
| python tools/manage_probe.py check --probe probe-002 | original |

ผล output แบบตรงจากเครื่องมือ พร้อม exit code เก็บใน [command-evidence.json](../../local/qa/WO-VISUAL-002/command-evidence.json) และไฟล์ .txt รายคำสั่งในโฟลเดอร์เดียวกัน (check ที่เก็บเป็น exact output คือครั้งก่อน install หลัง baseline)
install/restore ใช้สิทธิ์ที่ระบบอนุมัติเพื่อให้ตัวตรวจ tasklist ทำงาน โดยใช้สคริปต์เดิม ไม่มีการข้าม hash
ข้อความ InitializeDefaultDrives บางครั้งเป็นข้อความเริ่มต้น PowerShell; command exit 0 และ JSON แสดงผลตรวจสำเร็จ
หลัง restore ไม่มีหน้าต่าง Two Point Campus ในรายการ Windows; backup local/backups/probe-002 คงไว้ ไม่ลบ

## ผลจับคู่ก่อน/หลัง
ภาพอยู่ local/qa/WO-VISUAL-002/screenshots/ ทุกภาพในตารางเปิดดูจากผล screenshot จริงก่อนบันทึก ไม่อ้างการโหลดจาก log แทนภาพ

| กรณี | Original | probe-002 | หลัง restart | ผล |
|---|---|---|---|---|
| Game dropdown ปิด | ภาพ 01 ค่าปัจจุบันแสดงครบ | ภาพ 06 ค่าเดิมครบ พร้อมป้ายไทย | ภาพ 11 ค่าเดิมครบ พร้อมป้ายไทย | PASS |
| Language เปิด | ภาพ 02 อ่าน English/French/Italian/German ได้ | ภาพ 07 รายการเดียวกันอ่านได้ ช่อง selected ยังเห็น English | ไม่จำเป็นตาม WO | PASS |
| Video dropdown ปิด | ภาพ 03 Full Screen Window, Resolution, VSync On, SMAA แสดง | ภาพ 08 ค่าเดิมแสดง พร้อมหัวข้อไทย | ภาพ 12 ค่าเดิมแสดง | PASS |
| Resolution เปิด | ภาพ 04 ช่อง selected และ options อ่านได้ | ภาพ 09 ช่อง selected และ options อ่านได้ตรงกัน | ไม่จำเป็นตาม WO | PASS |
| Audio Language ไทย | baseline ภาพ 01 เป็นอังกฤษ | ภาพ 06 “ภาษาเสียงพากย์”; ค่า English ยังคงอยู่ | ภาพ 11 ยังเป็นไทยและค่าอยู่ | PASS |
| Camera sensitivity ไทย | ไม่ใช่ baseline dropdown ที่กำหนด | ภาพ 10 แพน/ก้มเงย/หมุน/ซูม เป็นไทยอ่านได้ | ไม่ได้ตรวจ Controls ซ้ำ | PASS เฉพาะรอบแรก |
| เปิดเมนู/Settings | ภาพ 00 | ภาพ 05 และ 06–10 ไม่มี error dialog | เข้า Game/Video ได้ | PASS |
| Latin/ตัวเลข/สัญลักษณ์ | อ่านได้ในหน้าที่เทียบ | English, Every Month, Every Change, 3840 x 2160 @ 60hz, SMAA อ่านได้ | ค่าเดิมอ่านได้ | PASS เฉพาะตัวที่พบ |

ค่าที่อ่านได้ใน Game ตรงกันทั้งหมดในภาพปิด: Log Level = Error; Game Autosave Frequency = Every Month; Career Autosave Frequency = Every Change; Language = English; Audio Language = English; UI Scale = Medium
Video: Full Screen Window; 3840 x 2160 @ 60hz; VSync = On; Framerate Limit = Unlimited; Antialiasing Mode = SMAA
Resolution options ที่มองเห็น: 3840 x 2160 @ 60hz, 2560 x 1600 @ 60hz, 2048 x 1536 @ 60hz, 2560 x 1440 @ 60hz
ไม่ได้กดเลือก resolution หรือ Apply; การคลิกนอก dropdown ครั้งแรกปิดรายการก่อน จึงคลิกแท็บ/ปิด Settings อีกครั้งหลัง refresh

## การอ่านภาพและข้อจำกัด
- **ข้อสังเกต:** original dropdown ไม่ว่าง ใน probe-002 ค่าปัจจุบันกลับมาเมื่อเทียบกับหลักฐาน probe-001 รอบก่อน และไม่พบค่าหายหลัง restart
- **ข้อสังเกต:** ป้ายไทย “ความถี่บันทึกอัตโนมัติโหมดอาชีพ”, “ภาษาเสียงพากย์”, “การตั้งค่าขั้นสูง” และป้ายความไวกล้องยังอ่านได้ ไม่พบ tofu, glyph หาย หรือ clipping/ทับกันที่เด่นชัดในป้ายที่ตรวจ
- **สมมติฐาน:** ผลสอดคล้องกับแนวทางคง primary font/material แล้วใช้ fallback แต่ยังไม่พิสูจน์ root cause ของ probe-001 หรือกลไก selected-value rendering
- ใช้ชื่อหน้าจอและตำแหน่งแทน key เพราะระบุ key จากภาพไม่ได้ ไม่เดา key
- Full shaping, mark positioning เทียบ trusted reference, wrapping และ synthetic corpus: **NOT_RUN / นอกขอบเขต** ไม่ให้ผ่านจากเมนู Settings
- ไม่ได้ทดสอบทุก resolution, UI Scale หรือทุกรายการใน 50-record pilot; ไม่ถือว่าไทยทั้งระบบผ่าน
- ไม่มีข้อบกพร่องใหม่ที่ยืนยันในขอบเขตนี้ และไม่มีการแก้ปัญหาระหว่างทดสอบ

## ดัชนีภาพ
- 00-original-menu.jpg — build/เมนูเกมเดิม
- 01-original-game-closed.jpg ↔ 06-probe-game-closed.jpg ↔ 11-restart-game-closed.jpg
- 02-original-language-open.jpg ↔ 07-probe-language-open.jpg
- 03-original-video-closed.jpg ↔ 08-probe-video-closed.jpg ↔ 12-restart-video-closed.jpg
- 04-original-resolution-open.jpg ↔ 09-probe-resolution-open.jpg
- 05-probe-menu.jpg — เมนู probe
- 10-probe-controls-thai.jpg — ป้ายความไวกล้องไทย

## แจ้ง Controller
WO-VISUAL-002 ผ่านขอบเขต original/probe-002 dropdown comparison และการคงป้ายไทยที่ตรวจ หลัง restart ค่าปิด Game/Video ยังอยู่ คืนต้นฉบับสำเร็จทั้งสอง bundle และตรวจ hash ผ่าน ไม่มี commit/push
