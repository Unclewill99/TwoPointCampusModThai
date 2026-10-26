# ติดตั้ง fresh-translation-006 ลงเกมจริง (ขั้นตอนสำหรับผู้ใช้)

2026-10-26. PM (Claude). ผู้ใช้เลือกติดตั้ง 006 ลงเกมจริง ไฟล์นี้เป็นขั้นตอนที่ต้องรันบน Windows เอง (หรือให้ ChatGPT/Antigravity ที่รันบนเครื่องเดียวกันทำตามนี้) PM ไม่ได้ติดตั้งเอง เพราะ `manage_probe.py` ใช้ API ของ Windows และโฟลเดอร์เกมอยู่นอกโฟลเดอร์ที่ PM เข้าถึงได้ และ PM จะไม่คัดลอกไฟล์ข้ามตัวป้องกันของ manager

## สิ่งที่จะเปลี่ยน

- แทนที่ 3 ไฟล์ใน `TPC_Data/StreamingAssets/aa/StandaloneWindows64/`: `fonts_assets_all.bundle` (ฟอนต์ไทยเพิ่ม 15 glyph + ligature 15 รายการ), `localisation_assets_localisationenglish.bundle` และ `ui-prefabs-general_assets_all.bundle` (ทั้งสองตรงกับชุดแปล 005)
- ไฟล์เซฟไม่ถูกแก้ ต้นฉบับ 3 ไฟล์ถูกสำรองไว้ที่ `local/backups/fresh-translation-006/` และ manager ตรวจ hash ก่อนเขียนทุกครั้ง

## ขั้นตอน (รันในโฟลเดอร์ ThaiCampusMod)

1. ปิดเกมให้สนิท (ถ้า Steam ยังเปิดเกมอยู่ manager จะปฏิเสธ)
2. `python tools/manage_probe.py check --probe fresh-translation-006` ต้องได้ original ทั้ง 3 ไฟล์ ถ้าได้ "Unknown installed file" แปลว่าไฟล์เกมถูกเปลี่ยน (เช่น Steam อัปเดต) ให้หยุดและแจ้ง PM ห้ามฝืนติดตั้ง
3. `python tools/backup_gameplay_saves.py` ต้องได้ `verified: true`
4. `python tools/manage_probe.py install --probe fresh-translation-006`
5. `python tools/manage_probe.py check --probe fresh-translation-006` ต้องได้ probe ทั้ง 3 ไฟล์ (ชื่อ state ว่า "probe" คือไฟล์ของ candidate)
6. เปิดเกมตามปกติ ดูข้อความที่มี ต่ำ / น้ำ (เช่น Settings > Game ตัวกรองที่ปรึกษา และ modal เปิดด่าน Freshleigh)

## ถอยกลับ

ปิดเกม แล้ว `python tools/manage_probe.py restore --probe fresh-translation-006` ตามด้วย `check` ต้องได้ original ทั้ง 3 ไฟล์

## ข้อควรระวัง

- Steam อัปเดตหรือ Verify integrity อาจเขียนทับไฟล์เกม ถ้าเกิดขึ้น ให้รัน `check` ก่อน ถ้าไฟล์เป็น original แล้ว ติดตั้งใหม่ได้ ถ้าเกมเปลี่ยนเวอร์ชันและ hash ต้นฉบับเปลี่ยน ต้องสร้าง candidate ใหม่
- ผลทดสอบที่ผ่านแล้วครอบคลุมเฉพาะ UI Scale กลาง และ 3 หน้าจอ (Settings Game, tooltip Video, modal เปิดด่านจริง) ยังไม่ได้ทดสอบ UI Scale เล็ก/ใหญ่, หน้าจอในแคมปัส, คำที่พบน้อย (ค้ำ ย้ำ ม่ำ ล่ำ น่ำ) และการใช้งานนานๆ ถ้าพบหน้าจอที่ ต่ำ/น้ำ แสดงเพี้ยน (ยอดถูกตัด ซ้อนทับ หรือมีสี่เหลี่ยมว่าง) ให้ถ่ายภาพ native แล้วแจ้ง PM พร้อมขนาด UI Scale
- ข้อความที่แปลใหม่ในอนาคตที่มีรูป [พยัญชนะ][ไม้เอก/ไม้โท]ำ นอก 15 กลุ่มนี้ จะยังซ้อนทับเหมือนเดิมจนกว่าจะเพิ่ม glyph + ligature สำหรับกลุ่มนั้น
- บันทึกสถานะหลังติดตั้งจริง: ให้แจ้ง PM ผลของข้อ 4–5 PM จะอัปเดต PROJECT_STATUS เป็น INSTALLED_006 หลังได้รับยืนยัน

## ติดตั้ง/ถอนด้วยไฟล์ .bat (เพิ่ม 2026-10-26)

ในโฟลเดอร์ ThaiCampusMod มี `Install_Thai_Mod.bat` และ `Uninstall_Thai_Mod.bat` ดับเบิลคลิกได้ ปิดเกมก่อน ไฟล์เหล่านี้เรียก `tools/manage_probe.py` และ `tools/backup_gameplay_saves.py` เดิม (ตรวจ hash, สำรองเซฟ, สำรอง original, ปฏิเสธถ้าเกมเปิดอยู่หรือไฟล์เกมไม่รู้จัก) ต้องมี Python 3 และโฟลเดอร์ `local/` (bundle ของ candidate และ backup) อยู่ในเครื่อง ยังไม่ได้ทดสอบรันบน Windows จริง ทดลองครั้งแรกให้ดูข้อความในหน้าต่างทุกขั้น
