# การ์ดข่าวภาษาไทย — news-thai-001

26 ตุลาคม 2026 (Asia/Bangkok). ผู้ใช้อนุญาตให้แปลการ์ด Discord และ Two Point Museum หลังเห็นร่างคำแปล ติดตั้งและทดสอบจริงแล้ว: **PASS_SCOPED**.

## ผลลัพธ์

- คำอธิบายทั้งสองใบเป็นไทย ปุ่มทั้งสองเป็น “ดูเพิ่มเติม”. ชื่อ Discord และ Two Point Museum คงเดิม.
- แบนเนอร์ Discord เป็นภาพที่สร้างด้วย imagegen จากภาพอ้างอิงของผู้ใช้ ใช้โลโก้ TWO POINT แคมปัส และริบบิ้น “มาร่วม Discord ของเรา!”. เป็นภาพสร้างใหม่ ไม่ใช่การคงพิกเซลตัวละครทุกจุด. ภาพ Museum เดิมไม่เปลี่ยน.
- ตรวจหน้าเมนูจริงทั้งสองใบ: ภาพโหลดสำเร็จ ข้อความอยู่ในกรอบ สลับหน้าการ์ดได้ และออกเกมปกติ. ไม่กดปุ่มออกไปเว็บหรือร้านค้า.
- หลักฐาน: `local/qa/news-thai-001/01-museum.png`, `02-discord.png`; SHA-256 อยู่ใน `reports/news-thai-001-verification.json`.
- เซฟเดิม 24 ไฟล์ตรง snapshot ก่อนทดสอบทั้งหมด ไม่มีไฟล์เดิมหาย. ไม่เข้าแคมปัส ไม่เปลี่ยน UI Scale. เกมปิดแล้วหลังทดสอบ.

## เหตุที่ต้องแก้เพิ่มจากไฟล์แปล

การ์ดออนไลน์จาก PlayFab ส่งข้อความตรงให้ TMP ผ่าน `FrontendNewsFeedUI.SetupNewsContent`. คำแปล I2 ของ Discord/Learn More ที่มีใน 007 ไม่ได้ถูกใช้กับข้อมูลข่าวออนไลน์ชุดนี้.

ชุดนี้จึงแก้ **GameAssembly.dll** แบบตรวจ hash รุ่นเกมเต็มไฟล์: เปลี่ยน call sites 3 จุด (19 bytes ใน code เดิม) และเพิ่ม section `.thnews` สำหรับแทนข้อความ/ภาพเฉพาะจุด พร้อม exception/unwind records ของ stubs. เป็น local patch ไม่มี DLL/plugin loader เพิ่ม และไม่ได้แก้ข้อมูลบนเซิร์ฟเวอร์.

- Body: เทียบข้อความอังกฤษครบประโยค (รองรับ apostrophe/ellipsis สองรูป) แล้วแทนด้วยไทยที่ใส่จุดตัดคำตรวจไว้. ข้อความอื่นผ่านตามเดิม.
- Button: เทียบชื่อ Discord / Two Point Museum และ label Learn More ก่อนแทน.
- Image: เปลี่ยนเฉพาะ ImageURL ที่ส่งให้ loader ของ Discord เป็น `file:///.../discord-banner-thai.png`; UnityWebRequest โหลดไฟล์นี้ได้ในการทดสอบจริง.
- ActionURL และ ActionDLCName ไม่ถูกเขียนหรือเปลี่ยน. ชุดแปล 007 และชุดโลโก้ thai-logo-001 แยกกัน.
- ASLR: ใช้ relative calls และ RIP-relative data; ไม่ฝัง image base ตายตัว.

## การตรวจสอบ

`test_news_thai_shim.py`: PASS 24 native execution cases ใช้ fake managed strings/callbacks แยกจากเกม ครอบคลุม match, unknown, null/empty และการรักษา argument ของ setter. ไม่โหลดเกมในการทดสอบนี้.

`verify_news_thai_001.py`: นอกช่วง header และ code patch ที่ประกาศไว้ ไบต์ต้นฉบับทุกไบต์ตรงเดิม; section headers เดิมไม่เปลี่ยน; exception records เดิม 279,611 รายการเก็บครบ และเพิ่ม 3 รายการ. รูปและ installed hash ตรง candidate.

ทดสอบ install → runtime → normal exit → restore → check original SHA → reinstall แล้ว. ต้นฉบับ `e4276817…`, final candidate `1de9cb33…` (ค่าเต็มใน manifest/report).

## ติดตั้ง / ถอน

ติดตั้งอยู่แล้ว และสำรองต้นฉบับที่ `local/backups/news-thai-001/GameAssembly.dll`.

ปิดเกมก่อนใช้ `Install_Thai_News.bat` หรือ `Uninstall_Thai_News.bat`. ตัวจัดการปฏิเสธไฟล์เกมที่ไม่ตรงต้นฉบับ/ชุดนี้ และตรวจ backup/candidate hash ก่อนเขียน.

```powershell
python tools/manage_news_thai.py check
python tools/manage_news_thai.py install
python tools/manage_news_thai.py restore
```

ถอนชุดนี้จะคืนเฉพาะระบบการ์ดข่าว ไม่ถอนคำแปล 007 หรือโลโก้ไทย. .bat ชุดแปลเดิมไม่ได้จัดการ binary patch นี้.

ชุดนี้รองรับ **GameAssembly.dll รุ่นปัจจุบันและข้อความข่าวสองใบชุดนี้เท่านั้น**. หาก Steam update/verify คืนไฟล์ หรือข้อความข่าวเปลี่ยน ต้องตรวจใหม่; ข้อความไม่ตรงจะใช้ต้นฉบับ. ห้ามย้าย/ลบภาพแบนเนอร์ระหว่างใช้งาน เพราะ file URI อ้างตำแหน่งในเครื่อง. ขนาด UI อื่น การเล่นระยะยาว และข่าวใบอื่นไม่ได้ทดสอบ.

## ภาพและ prompt

Built-in imagegen, edit input: ภาพการ์ด Discord ของผู้ใช้ + โลโก้ไทยที่อนุมัติ. Prompt: extract only the purple-curtain promotional artwork as a clean flat 16:10 banner; retain the five character roles, costumes and purple stage composition; use TWO POINT แคมปัส from the approved logo; replace ribbon text with exactly “มาร่วม Discord ของเรา!”; omit photo border, lower panel, buttons and screenshot scenery. Output saved at `local/review/news-thai-001/discord-banner-thai.png`.

Local-only required inputs: approved banner, candidate binary/manifest, original backup and screenshot evidence. Git clone alone cannot install this candidate.
