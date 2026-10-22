# WO-FRESH-MENU-005 — ตรวจปุ่ม Mod

วันที่ 2026-10-22 (Asia/Bangkok). ผู้รับงาน: Antigravity — Desktop QA.
สถานะ: READY_FOR_HANDOFF / ยังไม่ยืนยันการรับงาน. Controller ไม่ทดสอบหน้าจอเองตามคำสั่งผู้ใช้

## เป้าหมายและชุดทดสอบ

ตรวจ fresh-translation-005 เท่านั้น ที่ local/prototype/fresh-translation-005/manifest.json เทียบ reports/fresh-translation-005-build.json. Working directory: D:/SteamLibrary/steamapps/common/Two Point Campus/ThaiCampusMod.

เปลี่ยนเพียง I2LS_UI::UI/Modding/Mods::segment-964 จาก ม็อด เป็น **Mod** (M ใหญ่, od เล็ก ไม่มี s). ชุด 004 frozen ไม่เปลี่ยน; ฟอนต์/UI เหมือน 004. Localisation candidate SHA256: 74a3c5ef4466df886f6ee432f4bb02a136dd7b5377d6ed220b4770fd75d8565a. ตรวจ hash ทั้งสามตาม manifest ด้วย manager ก่อนติดตั้ง ห้ามสร้างใหม่หรือแก้ข้อความระหว่างทดสอบ

## ขอบเขต

หนึ่งรอบ ไม่เกิน 5 นาทีหลังเมนูพร้อม หลักฐานหลักสูงสุด 2 ภาพ และ recovery รวมสูงสุด 1 ครั้ง. เปิดผ่าน Steam; เลือกหน้าต่างจากเจ้าของโปรเซสพาธ D:/SteamLibrary/steamapps/common/Two Point Campus/TPC.exe ที่มีหน้าต่างเดียว ยืนยัน foreground และภาพเกมจริงก่อน input. ไม่เลือกด้วยชื่อหน้าต่างอย่างเดียว ไม่ใช้พิกัดเก่า หากเลือกผิด/overlay/ควบคุมไม่ได้หลัง recovery ให้หยุดและรายงาน SETUP_LIMIT ไม่วนทดสอบ

1. เมนูหลัก: เก็บภาพยืนยันว่าปุ่มระหว่าง Sandbox และ Settings เป็น **Mod** ตรงตัว ไม่ว่าง ไม่ตัด ไม่ชนขอบ ไม่มี raw tags.
2. กดปุ่ม Mod หนึ่งครั้งเพื่อยืนยันเปิดหน้าจอจัดการ Mod ถูกต้อง เก็บภาพและระบุหัวข้อที่แสดง หากหัวข้อใช้คีย์ร่วมให้บันทึกว่าปรากฏ Mod ด้วย ไม่อ้างว่าตรวจผู้ใช้คีย์ครบทั้งหมด. ไม่ติดตั้ง/เปิดปิด/ดาวน์โหลด/สมัครบริการ/ล็อกอินหรือแก้รายการ Mod. หากติด modal หรือไม่สามารถย้อนกลับ ให้หยุดการสังเกตและออกเกมตามปกติ

ไม่เข้า Settings หรือมหาวิทยาลัย ไม่ทดสอบบุคลากร ไม่เปลี่ยนค่าหรือเล่นเซฟ. งานบุคลากรที่บทสอนบังยัง NOT_RUN และไม่อยู่ในใบงานนี้. BUG-THAI-002/003 และ regression BUG-THAI-001 ยังคงเปิด; การทดสอบนี้ไม่รับรองฟอนต์หรือข้อความทั้งคลัง

## สำรอง ติดตั้ง และคืนไฟล์

ตรวจเกมปิดและสามไฟล์เป็น original ก่อนเริ่ม ด้วยคำสั่งแต่ละขั้นแยกกันและตรวจผลก่อนขั้นถัดไป:

1. `python tools/manage_probe.py check --probe fresh-translation-005`
2. `python tools/backup_gameplay_saves.py` ต้อง verified=true เก็บ ZIP/manifest ใหม่
3. `python tools/manage_probe.py install --probe fresh-translation-005`
4. `python tools/manage_probe.py check --probe fresh-translation-005` ต้อง probe ทั้งสาม
5. เปิด Steam และทดสอบตามขอบเขต
6. ออกเกมตามปกติจากปุ่มที่เห็น; หากบทบังเมนู ใช้ Alt+F4 เพื่อขอปิดหน้าต่างตามปกติได้ ไม่ force-kill. ยืนยัน TPC.exe ปิดแล้ว
7. `python tools/manage_probe.py restore --probe fresh-translation-005`
8. `python tools/manage_probe.py check --probe fresh-translation-005` ต้อง original ทั้งสาม

ทุกเส้นทางหลังติดตั้งต้องคืนไฟล์ แม้ทดสอบไม่สำเร็จ. หากปิด/คืนไฟล์ไม่ได้ให้แจ้งทันที ห้ามข้าม guard. เปรียบเทียบ hash เซฟก่อน/หลัง ระบุ changed/new/missing เก็บเซฟจริงและ backup ไม่ rollback อัตโนมัติ ไม่ลบไฟล์ ไม่เปลี่ยน Steam Cloud. ไม่ commit/push

## ส่งผล

เขียน docs/qa/WO_FRESH_MENU_005_REPORT.md และภาพต้นฉบับ local/qa/WO-FRESH-MENU-005/. ระบุ candidate/hash, build เกม, เครื่องมือควบคุม, เวลาและจำนวน recovery, ภาพสองหน้าจอที่ถึงจริง, expected/actual, PASS/FAIL/NOT_RUN ต่อข้อ, lifecycle สาม bundle, ZIP/manifest และผลเปรียบเทียบเซฟ. สรุป SAMPLE_PASS / NEW_BLOCKER / SETUP_LIMIT / INCONCLUSIVE. ห้ามอ้าง PASS จากชื่อ asset หรือผลชุด 004 และห้ามแก้ปัญหาอื่นนอก WO. หยุดหลังส่งรายงานให้ Controller ตรวจรับ
