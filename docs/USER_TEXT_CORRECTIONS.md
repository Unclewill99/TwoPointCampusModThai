# User text corrections

Latest status 2026-10-22: Mod correction COMPLETE in fresh-translation-005. Menu label PASS plus destination PASS accepted from Antigravity rounds 1/R2. See FRESH_MENU_005_R2_ACCEPTANCE.md. Earlier pending/NOT_RUN entries below are historical. No global text or shaping approval.

## 2026-10-22 — ปุ่มเมนู Mod

ผู้ใช้กำหนดให้ปุ่มเมนูใช้ **Mod** (ตัว M ใหญ่ ตามด้วย od) แทนคำทับศัพท์ไทย

- ข้อความปัจจุบันในไฟล์คือ ม็อด; คำที่ผู้ใช้ขอใหม่คือ Mod แม้ source จะเป็น Mods
- รายการที่เกี่ยวข้อง: I2LS_UI::UI/Modding/Mods::segment-964, FRESH-036
- สถานะ: USER_APPROVED_PENDING_INTEGRATION; เก็บ override แยกไว้ที่ local/review/user-menu-corrections/mod-menu-override.json
- เก็บภาพผู้ใช้แบบไม่แก้ไขที่ local/review/user-menu-corrections/2026-10-22-menu-mod.png
- ยังไม่แก้ไฟล์ Claude เดิมหรือ frozen candidate fresh-translation-004 และยังไม่ติดตั้งเกม
- ห้ามแทนคำ ม็อด/Mods ทั้งคลังโดยอัตโนมัติ รายการ Mod.io แยก (I2LS_Mods segment54) ยังไม่ได้รับคำสั่งเปลี่ยนเฉพาะในบันทึกนี้ หากคีย์เมนูถูกใช้ร่วมที่อื่นให้ระบุขอบเขตตอนรวมชุดใหม่


## Integration completed — fresh-translation-005

2026-10-22: รวมคำ Mod แล้วใน candidate ใหม่ fresh-translation-005; อ่านกลับครบ 15,677 รายการ เปลี่ยนเพียง I2LS_UI segment 964. ชุด 004 และข้อมูล Claude R5 เดิมไม่เปลี่ยน ฟอนต์/UI เหมือน 004 ทุก byte. ยังไม่ติดตั้งและ runtime NOT_RUN. ทุกจุดที่อ้างคีย์ UI/Modding/Mods จะใช้ Mod; ยังไม่ได้พิสูจน์ผู้ใช้คีย์ทั้งหมดในเกม. Mod.io และรายการอื่นไม่เปลี่ยน. รายงาน reports/fresh-translation-005-build.json.
