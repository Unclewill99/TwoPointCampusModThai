# WO-SARA-AM-002-AB QA Report — การทดลองเปรียบเทียบลำดับ Atomic/Decomposed × คู่ MarkToMark (`probe-sara-am-001a` / `probe-sara-am-001b`)

- **วันที่ทดสอบ:** 2026-10-22 (Asia/Bangkok)
- **ผู้รับงาน:** Antigravity — Desktop QA
- **อ้างอิงเอกสาร:** [`BUG_THAI_003.md`](BUG_THAI_003.md), [`../SARA_AM_001_REFERENCE_ACCEPTANCE.md`](../SARA_AM_001_REFERENCE_ACCEPTANCE.md), และ [`../SARA_AM_002_NATIVE_FINDINGS.md`](../SARA_AM_002_NATIVE_FINDINGS.md)
- **สรุปผลรวม (Verdict):** **`SETUP_LIMIT` / `INCONCLUSIVE`** *(เข้าสู่แผนที่แคมเปญ `Slot1` ในรอบ `probe-sara-am-001a` ได้แล้ว แต่หน้าต่างเกมหลุด foreground ระหว่างโหลดแผนที่แคมเปญ จึงใช้สิทธิ์ recovery รวม 1 ครั้ง (`1/1 total`) ดึงหน้าต่างกลับมาและคลิกปุ่มสีเขียว `ต่อไป` บนการ์ดแคมเปญที่ `(224, 846)` หนึ่งครั้ง แต่เกมไม่รับคลิกหลังสลับโฟกัสทำให้ยังไปไม่ถึงหน้าต่าง Modal เริ่มต้นภายในเพดาน recovery รวมสูงสุด 1 ครั้ง จึงปิดเกมตามปกติ คืนไฟล์เป็น `original` ทั้งสาม และคงสถานะ `probe-sara-am-001b` เป็น `NOT_RUN` ตามเกณฑ์ใบงาน)*
- **เวลาที่ใช้จริง (Active Elapsed Time):** ~5.5 นาที (`22:25–22:31` ICT; เพดานกำหนดไม่เกิน 15 นาทีรวมทั้งสองชุด)
- **จำนวนภาพหลักฐานและ Recovery:** ภาพ Modal ต้นฉบับ `0` ภาพใน `local/qa/WO-SARA-AM-002-AB/` (เนื่องจากยังไปไม่ถึงหน้าต่าง Modal เริ่มต้น และใบงานห้ามบันทึกภาพหน้าจอเกมอื่นนอกเหนือจาก Modal เริ่มต้น 1 ภาพต่อชุดทดสอบ), ใช้ **Recovery รวม = 1 ครั้ง** (ครบเพดานสูงสุด 1 ครั้งรวมทั้งใบงาน)

---

## 1. ข้อมูลชุดทดสอบ (Candidates), ค่า Hash และลำดับ Codepoints ตัวอย่างวินิจฉัย

ตรวจสอบ [`reports/sara-am-001-build.json`](../../reports/sara-am-001-build.json) เทียบกับ [`local/prototype/probe-sara-am-001a/manifest.json`](../../local/prototype/probe-sara-am-001a/manifest.json) และ [`local/prototype/probe-sara-am-001b/manifest.json`](../../local/prototype/probe-sara-am-001b/manifest.json) ยืนยันค่า SHA-256 ตรงกันทุกฟิลด์:

| Bundle File | Original SHA-256 | `probe-sara-am-001a` SHA-256 | `probe-sara-am-001b` SHA-256 |
|---|---|---|---|
| `fonts_assets_all.bundle` | `33aa34892719fbc7caaabd0a292c32bb135bc61978a4cd3ce73c6c40da8f4e6e` | `588f15fad01635da3fb5b86d5c3946cbb7bd85b40304364294fb23d73c207f3e` *(เหมือน `005`, ไม่แก้ฟอนต์)* | `6cb840337007c4fb7d6807828276ddef1ae51c2b7809e507f90a53b7c243b133` *(เพิ่ม TMP `MarkToMark` 1 คู่: `glyph59 -> glyph42` ที่ point30, base anchor `(-3.45, 23.16)`, combining adjustment `(-2.58, 16.08)`)* |
| `localisation_assets_localisationenglish.bundle` | `c1e7ca97f260813ccc9a1cf463f20d066631f8e5616bf797fe8d5ae93227878f` | `02a6d2864ea5fcef910e01644b224da2859df3aa58d54b25ed09e83a40727bf4` *(แก้เฉพาะ `I2LS_Levels` segment 533 เป็น 3 บรรทัดวินิจฉัย)* | `02a6d2864ea5fcef910e01644b224da2859df3aa58d54b25ed09e83a40727bf4` *(ชุดเดียวกับ `001a`)* |
| `ui-prefabs-general_assets_all.bundle` | `2152e5ba289ccb0414c462371cfdfe05cc7ac589a10a75b8b46d359afd99786d` | `34c9779682b146bbab82569789622b978f807ff0efeca00317694543713d59df` | `34c9779682b146bbab82569789622b978f807ff0efeca00317694543713d59df` |

### ลำดับ Codepoints ของตัวอย่างวินิจฉัยชั่วคราวใน `I2LS_Levels` segment 533
*(ตัวอย่างวินิจฉัยชั่วคราวเท่านั้น ไม่ใช่คำแปลสำหรับใช้งานจริง)*

| Row | ข้อความใน Segment 533 | ชนิดตัวอย่าง | Codepoints ของคำเป้าหมาย | Codepoints ทั้งบรรทัด |
|:---:|---|---|---|---|
| **A** | `A: ต่ำ ถี่` | Atomic `ต่ำ` + ตัวควบคุม `ถี่` | `U+0E15 U+0E48 U+0E33` | `U+0041 U+003A U+0020 U+0E15 U+0E48 U+0E33 U+0020 U+0E16 U+0E35 U+0E48` |
| **B** | `B: ตํ่า ถี่` | Reordered decomposed (`ํ` ก่อน `่`) + ตัวควบคุม `ถี่` | `U+0E15 U+0E4D U+0E48 U+0E32` | `U+0042 U+003A U+0020 U+0E15 U+0E4D U+0E48 U+0E32 U+0020 U+0E16 U+0E35 U+0E48` |
| **C** | `C: ต่ํา ถี่` | Original-order decomposed (`่` ก่อน `ํ`) + ตัวควบคุม `ถี่` | `U+0E15 U+0E48 U+0E4D U+0E32` | `U+0043 U+003A U+0020 U+0E15 U+0E48 U+0E4D U+0E32 U+0020 U+0E16 U+0E35 U+0E48` |

---

## 2. Build เกม, ขนาด UI, มิติหน้าจอ และการแปลงพิกัด (Coordinate Mapping)

- **Game Build:** `10.3.169253+2024-12-06.1241`
- **UI Scale:** คงค่าเดิมที่ `Medium` (`กลาง` ตาม `preferences.json` และ `localpreferences.json` ไม่ได้เข้าไปแก้ไข)
- **มิติหน้าจอและหน้าต่างเกม (`probe-sara-am-001a`):**
  - `GetSystemMetrics(0) x GetSystemMetrics(1)`: `3840 x 2160`
  - หน้าต่างเดียวของโปรเซส `D:\SteamLibrary\steamapps\common\Two Point Campus\TPC.exe`: `hwnd=724366`, `title='Two Point Campus'`, `GetWindowRect = (0, 0, 3840, 2160)`
  - ขนาดภาพ `ImageGrab.grab()`: `W x H = 3840 x 2160` (จุดกำเนิด `(0, 0)`)
- **พิกัดปุ่มและการแปลงพิกัด (`(xc * 1920 / W, yc * 1080 / H)`) ที่ใช้จริงในรอบ `probe-sara-am-001a`:**
  1. **ปุ่ม `ต่อไป` (`Continue`) บนเมนูหลัก (ใต้การ์ดเซฟ `Two Point` / `Slot1`):**
     - กรอบปุ่มสีฟ้าในพิกัด `3840 x 2160`: `x = 171..928`, `y = 793..882`
     - จุดกึ่งกลาง `(xc, yc)` = `(549, 837)` -> แปลงเป็นพิกัด `qa_driver` = **`(274, 418)`**
     - ผลลัพธ์: คลิก 1 ครั้งที่ `(274, 418)` เกมรับคลิกและโหลดเข้าสู่หน้าแผนที่แคมเปญของ `Slot1` สำเร็จ
  2. **เหตุการณ์หลุด Foreground และการใช้สิทธิ์ Recovery ครั้งที่ 1 (`1/1 total`) บนหน้าแผนที่แคมเปญ:**
     - ระหว่างรอแผนที่แคมเปญเปิดการ์ด `เฟรชลีห์ เมโดวส์` หน้าต่าง `TPC.exe` หลุดจากสถานะ foreground ทำให้ guard `qa_driver.require_game_foreground()` หยุดส่ง input ทันที (`RuntimeError: Foreground is not the verified TPC.exe window; no input sent`)
     - ใช้สิทธิ์ **Recovery ครั้งที่ 1 (1/1 รวมทั้งใบงาน)** เรียก `qa_driver.activate_tpc()` ดึง `hwnd=724366` กลับมาเป็น foreground และตรวจพบปุ่มสีเขียว `ต่อไป` (`Continue`) บนการ์ดแคมเปญซ้ายมือที่กรอบพิกัด `3840 x 2160`: `x = 230..666`, `y = 1634..1748`, จุดกึ่งกลาง `(xc, yc) = (448, 1691)` -> แปลงเป็นพิกัด `qa_driver` = **`(224, 846)`**
     - ส่งคลิก 1 ครั้งที่ `(224, 846)` แต่เกมไม่รับคลิกเดี่ยวหลังการสลับโฟกัสหน้าต่าง (ยังคงค้างอยู่บนหน้าแผนที่แคมเปญ พิกเซลกลางจอ `(1920, 1080) = (122, 172, 173)` จนครบเวลาเฝ้ารอ)
     - เนื่องจากใช้สิทธิ์ recovery ครบเพดาน **1 ครั้งรวมทั้งใบงาน** แล้ว จึงขอปิดหน้าต่างตามปกติด้วย `WM_CLOSE` (ยืนยันไม่มีโปรเซส `TPC.exe` ค้าง) คืนไฟล์ `probe-sara-am-001a` กลับเป็น `original` ทั้งสามไฟล์ และหยุดไม่รัน `probe-sara-am-001b` ต่อตามเงื่อนไขใบงาน (*"Repeat with probe-sara-am-001b only after successful restore/check and capability remains usable"*)

---

## 3. ตารางผลการสังเกต 2 × 3 แถว และตัวควบคุม `ถี่`

| ชุดทดสอบ (Variant) | Row A (`A: ต่ำ ถี่` — `0E15 0E48 0E33`) | Row B (`B: ตํ่า ถี่` — `0E15 0E4D 0E48 0E32`) | Row C (`C: ต่ํา ถี่` — `0E15 0E48 0E4D 0E32`) | ตัวควบคุม `ถี่` (`0E16 0E35 0E48`) | การยืนยันการผูกฟอนต์/ข้อความของ Modal |
|---|---|---|---|---|---|
| **`probe-sara-am-001a`** *(ไม่แก้ฟอนต์)* | **`NOT_RUN` / `INCONCLUSIVE`** *(`SETUP_LIMIT`)* | **`NOT_RUN` / `INCONCLUSIVE`** *(`SETUP_LIMIT`)* | **`NOT_RUN` / `INCONCLUSIVE`** *(`SETUP_LIMIT`)* | **`NOT_RUN` / `INCONCLUSIVE`** *(`SETUP_LIMIT`)* | ยังไปไม่ถึงหน้าต่าง Modal เริ่มต้นภายในเพดาน 1 recovery |
| **`probe-sara-am-001b`** *(เพิ่มคู่ `MarkToMark 59->42`)* | **`NOT_RUN`** *(หยุดหลังหมดงบ recovery 1 ครั้ง)* | **`NOT_RUN`** *(หยุดหลังหมดงบ recovery 1 ครั้ง)* | **`NOT_RUN`** *(หยุดหลังหมดงบ recovery 1 ครั้ง)* | **`NOT_RUN`** *(หยุดหลังหมดงบ recovery 1 ครั้ง)* | `NOT_RUN` |

---

## 4. Lifecycle ของทั้ง 3 Bundle (รันแยกทีละขั้น)

```json
// 1. ตรวจสอบก่อนติดตั้ง probe-sara-am-001a
{"action": "check", "files": [{"name": "fonts_assets_all.bundle", "state": "original"}, {"name": "localisation_assets_localisationenglish.bundle", "state": "original"}, {"name": "ui-prefabs-general_assets_all.bundle", "state": "original"}]}

// 2. สำรองเซฟเกมก่อนติดตั้ง probe-sara-am-001a
{"backup": "D:\\SteamLibrary\\steamapps\\common\\Two Point Campus\\ThaiCampusMod\\local\\backups\\gameplay-save-snapshots\\20261022T152433019385Z.zip", "files": 11, "verified": true}

// 3. ติดตั้ง probe-sara-am-001a
{"action": "install", "files": [{"name": "fonts_assets_all.bundle", "state": "probe"}, {"name": "localisation_assets_localisationenglish.bundle", "state": "probe"}, {"name": "ui-prefabs-general_assets_all.bundle", "state": "probe"}]}

// 4. ตรวจสอบหลังติดตั้ง probe-sara-am-001a
{"action": "check", "files": [{"name": "fonts_assets_all.bundle", "state": "probe"}, {"name": "localisation_assets_localisationenglish.bundle", "state": "probe"}, {"name": "ui-prefabs-general_assets_all.bundle", "state": "probe"}]}

// 5. เปิดเกมผ่าน Steam -> คลิก ต่อไป บนเมนูหลัก (274, 418) -> ใช้ recovery 1/1 ดึงหน้าต่างกลับมาและคลิก ต่อไป บนการ์ดแคมเปญ (224, 846) -> เกมไม่รับคลิกหลังสลับโฟกัส -> ปิดเกมตามปกติด้วย WM_CLOSE (ยืนยันไม่มี TPC.exe ค้าง)

// 6. คืนไฟล์จาก probe-sara-am-001a
{"action": "restore", "files": [{"name": "fonts_assets_all.bundle", "state": "original"}, {"name": "localisation_assets_localisationenglish.bundle", "state": "original"}, {"name": "ui-prefabs-general_assets_all.bundle", "state": "original"}]}

// 7. ตรวจสอบยืนยันสถานะ original ทั้งสามไฟล์หลังคืนไฟล์ probe-sara-am-001a
{"action": "check", "files": [{"name": "fonts_assets_all.bundle", "state": "original"}, {"name": "localisation_assets_localisationenglish.bundle", "state": "original"}, {"name": "ui-prefabs-general_assets_all.bundle", "state": "original"}]}

// 8. ตรวจสอบยืนยันสถานะเทียบกับ probe-sara-am-001b (NOT_RUN)
{"action": "check", "files": [{"name": "fonts_assets_all.bundle", "state": "original"}, {"name": "localisation_assets_localisationenglish.bundle", "state": "original"}, {"name": "ui-prefabs-general_assets_all.bundle", "state": "original"}]}
```

---

## 5. ข้อมูลสำรองเซฟและการเปรียบเทียบ Hash ก่อน/หลังทดสอบ

- **ไฟล์ ZIP สำรองเซฟก่อนเริ่ม:** `D:\SteamLibrary\steamapps\common\Two Point Campus\ThaiCampusMod\local\backups\gameplay-save-snapshots\20261022T152433019385Z.zip` (`verified=true`, 11 ไฟล์)
- **ไฟล์ Manifest คู่กัน:** `D:\SteamLibrary\steamapps\common\Two Point Campus\ThaiCampusMod\local\backups\gameplay-save-snapshots\20261022T152433019385Z.json`
- **สรุปผลการเปรียบเทียบ Hash หลังรัน `probe-sara-am-001a`:**
  - **Changed:** `7` ไฟล์ (`career.csav`, `career.csav.2.bak` ถึง `.6.bak`, และ `userprofile.sav` จากการเข้าสู่หน้าแผนที่แคมเปญ `Slot1` และปิดเกมตามปกติ)
  - **Unchanged:** `4` ไฟล์ (**รวมถึงไฟล์เซฟมหาวิทยาลัย `Cloud/<AccountID>/Saves/Slot1/8000.sav` ที่ยังคงเดิมทุกไบต์** `5b4dac72e35d877f6b7f2d6933a8b0c44717ec2578052d1d9f218f983d050d0d`, `preferences.json`, `steam_autocloud.vdf`, และ `localpreferences.json`)
  - **New:** `0` ไฟล์
  - **Missing:** `0` ไฟล์
  - เก็บเซฟจริงและไฟล์ backup ไว้ตามเดิม ไม่มีการ rollback อัตโนมัติ ไม่ลบไฟล์ และไม่เปลี่ยนการตั้งค่า Steam Cloud

| Relative Path | สถานะ | Pre-Run SHA-256 (Size) | Post-Run SHA-256 (Size) |
|---|---|---|---|
| `Cloud/<AccountID>/Saves/Slot1/career.csav` | **CHANGED** | `c51ca1bc4f0fcb92a45e285ba530bb02adeb47babf87556d5dbade325cc808d9` (18,520 B) | `072f2ac9449f60467140e5e08576e85d14c253afefd60cfdccf68b8f371fa16d` (18,520 B) |
| `Cloud/<AccountID>/Saves/Slot1/career.csav.2.bak` | **CHANGED** | `27fd1082d3b44549301f56fe4308fd5238d92e1f3c73a19287ae1f4d7e39ed51` (18,505 B) | `d61a300fd9156feec475b10ba9fb65a34163bcc507f49c12afe7ca124c37dd00` (18,520 B) |
| `Cloud/<AccountID>/Saves/Slot1/career.csav.3.bak` | **CHANGED** | `cbbded52fde65f46da0c874a403280936286b31746ea6f17b5b38d0acadafc0b` (18,521 B) | `c51ca1bc4f0fcb92a45e285ba530bb02adeb47babf87556d5dbade325cc808d9` (18,520 B) |
| `Cloud/<AccountID>/Saves/Slot1/career.csav.4.bak` | **CHANGED** | `f9730de46047fd6673d6ab5e408c0c5a3c71468b310809f4643fb341bd84219f` (18,521 B) | `27fd1082d3b44549301f56fe4308fd5238d92e1f3c73a19287ae1f4d7e39ed51` (18,505 B) |
| `Cloud/<AccountID>/Saves/Slot1/career.csav.5.bak` | **CHANGED** | `dfd0601d068aa18807108560da1e16ad21da553a63e95cd4ea5b6bafbb1d5bba` (10,128 B) | `cbbded52fde65f46da0c874a403280936286b31746ea6f17b5b38d0acadafc0b` (18,521 B) |
| `Cloud/<AccountID>/Saves/Slot1/career.csav.6.bak` | **CHANGED** | `91998459ebcd62690c4cd54ef4d9ed16b9e0f379360c791a5709c4d1ee1f8e7c` (10,128 B) | `f9730de46047fd6673d6ab5e408c0c5a3c71468b310809f4643fb341bd84219f` (18,521 B) |
| `Cloud/<AccountID>/userprofile.sav` | **CHANGED** | `664d887974edcdf87f4e7c20c4abc31964029ac87d38f3aab138f3d54bc28350` (1,064 B) | `df3dcfc0b8429eebbc2fc365ce6da3355e70ec618e9ee1582c8ace57a3cb301e` (1,064 B) |
| `Cloud/<AccountID>/Saves/Slot1/8000.sav` | **UNCHANGED** | `5b4dac72e35d877f6b7f2d6933a8b0c44717ec2578052d1d9f218f983d050d0d` (179,866 B) | `5b4dac72e35d877f6b7f2d6933a8b0c44717ec2578052d1d9f218f983d050d0d` (179,866 B) |
| `Cloud/<AccountID>/preferences.json` | **UNCHANGED** | `f2ff575ab51636cd0b380f6f12f9221b905acce7e89a4677824d16e118877c9e` (761 B) | `f2ff575ab51636cd0b380f6f12f9221b905acce7e89a4677824d16e118877c9e` (761 B) |
| `Cloud/<AccountID>/steam_autocloud.vdf` | **UNCHANGED** | `b5d31412181fb1e37bed11e0bfbc2ed973c01ba5eb4aa00b3da786a625ded124` (52 B) | `b5d31412181fb1e37bed11e0bfbc2ed973c01ba5eb4aa00b3da786a625ded124` (52 B) |
| `localpreferences.json` | **UNCHANGED** | `3a32b89c9050ee0dea84c4ba8b632e0f81d82da25da517babd0442b5889fab8b` (1,050 B) | `3a32b89c9050ee0dea84c4ba8b632e0f81d82da25da517babd0442b5889fab8b` (1,050 B) |
