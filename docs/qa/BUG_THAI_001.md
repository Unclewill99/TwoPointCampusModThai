# BUG-THAI-001 — สระอีและไม้เอกทับกันใน “ความถี่”

- **สถานะ:** MITIGATED / TARGET-WORD VERIFIED ใน probe-003 — WO-VISUAL-003 ผ่านเฉพาะคำเป้าหมายเทียบ reference พร้อมผล Small/Large/restart ตามรายงาน; ยังเปิดเพื่อตรวจ regression ของอักษรซ้อนเพิ่มเติม ไม่ปิดทั้งระบบ
- **ระดับผลกระทบ:** Moderate เบื้องต้น — รูปสระ/วรรณยุกต์ไม่แยกชั้นชัดเจน แต่ยังอ่านคำจากบริบทได้; ปรับระดับหากพบว่าทำให้อ่านความหมายผิด
- **ผู้รายงาน:** ผู้ใช้ / Project Owner
- **Build:** Campus 10.3.169253+2024-12-06.1241
- **ต้นแบบ:** probe-002; ใช้ primary font เดิมและ Thai dynamic fallback
- **หน้าจอ:** Settings > Game — ป้าย Career Autosave Frequency
- **Key ที่สอดคล้องกับข้อความใน pilot:** `UI/Settings/CareerAutosaveFreq`
- **ข้อความ:** `ความถี่บันทึกอัตโนมัติโหมดอาชีพ`
- **กลุ่มเป้าหมาย:** `ถี่` = `ถ` U+0E16 + `ี` U+0E35 + `่` U+0E48
- **UI Scale:** Medium ตามรายงาน WO-VISUAL-002
- **ความละเอียด:** 3840 x 2160 @ 60hz ตามค่าที่ผู้ทดสอบอ่านจากเกม; ภาพหลักฐาน 1920 x 1080 ไม่ใช่หลักฐานความละเอียด render โดยลำพัง
- **หลักฐาน:** `local/qa/WO-VISUAL-002/screenshots/06-probe-game-closed.jpg` — ผู้ใช้ชี้ปัญหาที่คำว่า “ความถี่” ในภาพนี้

## ผลที่คาดหวังและผลที่พบ

คาดหวังให้ไม้เอกวางเหนือสระอีโดยแยกตำแหน่งและไม่ทับกัน ตามรูปแบบการจัดอักษรไทยของฟอนต์อ้างอิงที่เหมาะสม

ผู้ใช้สังเกตว่าสระอีและไม้เอกใน “ถี่” ทับกันอยู่ จึงถือเป็นข้อบกพร่องด้าน mark positioning ที่ต้องตรวจต่อ ไม่ใช่เพียงสถานะยังไม่ทดสอบ และไม่ถือว่าการมองเห็น glyph ครบเท่ากับ shaping ถูกต้อง

## การทำซ้ำและขอบเขตหลักฐาน

ใช้ probe-002 เลือก English / Medium เปิด Settings > Game แล้วตรวจป้ายดังกล่าว ภาพที่อ้างเป็นหลักฐานการพบครั้งนี้; ยังไม่ได้ทำการทดลองใหม่หรือยืนยันอาการเฉพาะจุดนี้หลัง restart/ทุก scale ข้อความเดิมและลำดับ Unicode ต้องคงไว้ ไม่แก้การสะกดเพื่อกลบข้อบกพร่อง renderer

สาเหตุยังไม่ยืนยัน สมมติฐานคือเส้นทาง Dynamic TMP อาจไม่ได้ใช้ข้อมูล mark-to-base/mark-to-mark ตามที่ต้องการ ต้องตรวจ glyph positioning และเทียบ trusted reference ที่ใช้ฟอนต์เดียวกันก่อนเลือกวิธีแก้

## ผลต่อการรับงาน

WO-VISUAL-002 ยังคง PASS เฉพาะ dropdown และป้ายที่มองเห็นตามขอบเขตเดิม แต่ข้อสรุปว่าไม่พบข้อบกพร่องใหม่ถูกเพิ่มเติมด้วยบั๊กนี้ การจัดวางอักษรไทยซ้อนมี observed FAIL สำหรับ “ถี่”; diagnostic corpus และ coverage อื่นยังไม่ผ่านหรือไม่ได้ทดสอบ ห้ามขยายผลว่าภาษาไทยทั้งระบบผ่าน


## Follow-up item — 2026-10-26 (from WO-VISUAL-019)

Bold section header `การประเมินการเยี่ ยมชมโดยพิจารณาจาก:` (UI/Messages/Visit segment-956) shows a visible gap inside เยี่ยม on 007. No U+200B is placed there, so this is header-font shaping (ี + ่ stack advance), not segmentation. Needs the same screen captured on 006 to confirm it pre-exists. Image: local/qa/WO-VISUAL-019/04-messages-visit.png.
