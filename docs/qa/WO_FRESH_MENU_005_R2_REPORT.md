# WO-FRESH-MENU-005-R2 QA Report — ตรวจหน้าปลายทางของปุ่ม Mod (`fresh-translation-005`)

- **วันที่ทดสอบ:** 2026-10-22 (Asia/Bangkok)
- **ผู้รับงาน:** Antigravity — Desktop QA
- **อ้างอิงเอกสารก่อนหน้า:** [`WO_FRESH_MENU_005.md`](WO_FRESH_MENU_005.md), [`WO_FRESH_MENU_005_REPORT.md`](WO_FRESH_MENU_005_REPORT.md) (คงไฟล์รายงานและภาพชุดแรกไว้ครบถ้วน), และ [`../FRESH_MENU_005_DISPOSITION.md`](../FRESH_MENU_005_DISPOSITION.md)
- **ชุดทดสอบ (Candidate):** `fresh-translation-005` (ไม่เปลี่ยนแปลง; แก้เฉพาะ `I2LS_UI::UI/Modding/Mods::segment-964` จาก `ม็อด` เป็น **`Mod`**)
- **สรุปผลรวม (Verdict):** **`DESTINATION_PASS`** *(ปุ่ม **`Mod`** บนเมนูหลักผ่านการยืนยันแล้วในรอบแรก และในรอบ R2 เมื่อคลิกปุ่ม **`Mod`** ที่ยืนยันตำแหน่งและสถานะ hover จริงเพียง 1 ครั้ง สามารถเปิดเข้าสู่หน้าจอจัดการ Mod ได้ถูกต้องโดยใช้ `recovery = 0`)*
- **เวลาที่ใช้ทดสอบจริงหลังเมนูพร้อม (Active Elapsed Time):** ~2 นาที (`21:42–21:44` ICT; เพดานกำหนดไม่เกิน 5 นาที)
- **จำนวนภาพหลักฐานและ Recovery:** ภาพต้นฉบับขนาดเต็มจอ `3840 x 2160` PNG จำนวน **2 ภาพ** ใน `local/qa/WO-FRESH-MENU-005-R2/` และใช้ **Recovery = 0 ครั้ง** (เพดานกำหนดสูงสุด 2 ภาพ และ recovery สูงสุด 1 ครั้งก่อนคลิก)

---

## 1. ข้อมูล Candidate, Hash, Build เกม และเครื่องมือควบคุม

- **Game Build ที่แสดงบนหน้าจอจริง:** `10.3.169253+2024-12-06.1241` (มุมซ้ายบนของ [`01-main-menu.png`](../../local/qa/WO-FRESH-MENU-005-R2/01-main-menu.png))
- **การตรวจสอบ Manifest และ Build Report:**
  - ตรวจสอบ [`local/prototype/fresh-translation-005/manifest.json`](../../local/prototype/fresh-translation-005/manifest.json) เทียบกับ [`reports/fresh-translation-005-build.json`](../../reports/fresh-translation-005-build.json) ยืนยันตรงกันทุกฟิลด์ (`override_sha256: 30506337e6c8722173bbd49284230044907a98c5c8b7560ae08e969ea0dd211f`, `changed_records`: `[["I2LS_UI", 964, "UI/Modding/Mods=ม็อด", "UI/Modding/Mods=Mod"]]`)
- **SHA-256 ของทั้ง 3 Bundle (ตรวจสอบด้วย `tools/manage_probe.py`):**
  1. `fonts_assets_all.bundle`
     - Original SHA-256: `33aa34892719fbc7caaabd0a292c32bb135bc61978a4cd3ce73c6c40da8f4e6e`
     - Probe SHA-256: `588f15fad01635da3fb5b86d5c3946cbb7bd85b40304364294fb23d73c207f3e`
  2. `localisation_assets_localisationenglish.bundle`
     - Original SHA-256: `c1e7ca97f260813ccc9a1cf463f20d066631f8e5616bf797fe8d5ae93227878f`
     - Probe SHA-256: `74a3c5ef4466df886f6ee432f4bb02a136dd7b5377d6ed220b4770fd75d8565a`
  3. `ui-prefabs-general_assets_all.bundle`
     - Original SHA-256: `2152e5ba289ccb0414c462371cfdfe05cc7ac589a10a75b8b46d359afd99786d`
     - Probe SHA-256: `34c9779682b146bbab82569789622b978f807ff0efeca00317694543713d59df`
- **เครื่องมือควบคุมและเก็บภาพ:**
  - เปิดเกมผ่าน Steam (`steam://rungameid/1649080`)
  - คัดเลือกหน้าต่างจากเจ้าของโปรเซสพาธ `D:\SteamLibrary\steamapps\common\Two Point Campus\TPC.exe` เท่านั้น (`qa_driver.find_tpc_window()` พบหน้าต่างเดียว `hwnd=200254`, `title='Two Point Campus'`)
  - ยืนยัน foreground (`qa_driver.activate_tpc()`, `qa_driver.require_game_foreground()`) และใช้ `qa_driver.move_mouse` / `qa_driver.click` จาก [`tools/qa_driver.py`](../../tools/qa_driver.py) ร่วมกับ `PIL.ImageGrab.grab()` บันทึกภาพต้นฉบับไม่ย่อขนาด (`3840 x 2160` PNG)

---

## 2. มิติหน้าจอ (Display/Capture Geometry), กรอบปุ่ม `Mod`, การแปลงพิกัด และหลักฐานก่อนคลิก

- **ขนาดจอแสดงผลหลักและหน้าต่างเกม (Display & Window Geometry):**
  - `GetSystemMetrics(0) x GetSystemMetrics(1)`: `3840 x 2160`
  - `GetWindowRect(hwnd=200254)`: `(left=0, top=0, right=3840, bottom=2160)` (Full Screen Window ครอบคลุมจอหลักเต็มพื้นที่ที่จุดกำเนิด `(0, 0)`)
  - ขนาดภาพต้นฉบับจาก `ImageGrab.grab()`: `W x H = 3840 x 2160` (จุดกำเนิด `(0, 0)`)
- **กรอบปุ่ม `Mod` ที่ระบุจากภาพเมนูหลักรอบ R2 ([`01-main-menu.png`](../../local/qa/WO-FRESH-MENU-005-R2/01-main-menu.png)) ก่อนส่ง Input:**
  - ตำแหน่งเชิงสายตา: ปุ่มสีฟ้าที่มีข้อความ **`Mod`** อยู่ระหว่างปุ่มสีเทา `แซนด์บ็อกซ์` ด้านบน (`y = 1389..1470`) และปุ่มสีฟ้า `การตั้งค่า` ด้านล่าง (`y = 1668..1750`)
  - กรอบพื้นปุ่มสีฟ้าของปุ่ม **`Mod`** (Native `3840 x 2160` rectangle): `x = 207..894`, `y = 1532..1595` (รวมขอบปุ่ม `x = 205..896`, `y = 1528..1610`)
  - จุดกึ่งกลางปุ่มในพิกัดภาพต้นฉบับ `(xc, yc)`: **`(550, 1563)`**
- **การแปลงพิกัดสำหรับ `qa_driver` (`(xc * 1920 / W, yc * 1080 / H)`):**
  - `driver_x = round(550 * 1920 / 3840) = 275`
  - `driver_y = round(1563 * 1080 / 2160) = 782`
  - เมื่อส่ง `(275, 782)` เข้า `qa_driver.to_phys(275, 782)` จะแปลงกลับเป็นพิกัดจริงบนจอ `(550, 1564)` ซึ่งอยู่ตรงกึ่งกลางกรอบปุ่ม `Mod` (`x = 207..894, y = 1532..1595`)
- **หลักฐานยืนยันเป้าหมายก่อนคลิก (Pre-Click Target & Hover Verification):**
  - ก่อนเลื่อนเมาส์: พิกเซลปุ่ม `แซนด์บ็อกซ์` `(250, 1429) = (126, 126, 126)`, ปุ่ม **`Mod`** `(250, 1563) = (0, 163, 186)`, ปุ่ม `การตั้งค่า` `(250, 1709) = (0, 163, 186)`
  - เลื่อนเมาส์แบบไม่คลิกด้วย `qa_driver.move_mouse(275, 782)`:
    - `GetCursorPos()` ยืนยันตำแหน่งเคอร์เซอร์จริงของระบบอยู่ที่ **`(550, 1564)`** (ภายในกรอบปุ่ม `Mod` `x = 207..894, y = 1532..1595`)
    - พิกเซลปุ่ม **`Mod`** ที่ `(250, 1563)` เปลี่ยนเป็นสีสว่างสถานะ hover **`(13, 190, 203)`** ในขณะที่ปุ่มข้างเคียง `แซนด์บ็อกซ์` `(126, 126, 126)` และ `การตั้งค่า` `(0, 163, 186)` ไม่เปลี่ยนแปลง

---

## 3. ผลการตรวจสอบหน้าจอปลายทางของปุ่ม `Mod`

| ลำดับภาพ | ไฟล์ภาพต้นฉบับ (`3840 x 2160` PNG) | การกระทำ | ผลที่ปรากฏจริงบนหน้าจอ (Actual Observation) | สถานะ |
|:---:|---|---|---|---|
| **1** | [`01-main-menu.png`](../../local/qa/WO-FRESH-MENU-005-R2/01-main-menu.png) | เก็บภาพเมนูหลักสดก่อนระบุพิกัดปุ่ม `Mod` | ปุ่มระหว่าง `แซนด์บ็อกซ์` และ `การตั้งค่า` แสดง **`Mod`** ตรงตัว (`M` ใหญ่, `od` เล็ก ไม่มี `s`) ไม่ว่าง ไม่ตัดขอบ ไม่ชนขอบ ไม่มี raw tags | **`PASS`** *(ยืนยันซ้ำตรงกับรอบแรก)* |
| **2** | [`02-mod-destination.png`](../../local/qa/WO-FRESH-MENU-005-R2/02-mod-destination.png) | เลื่อนเมาส์ไปที่ `(275, 782)` ยืนยัน hover บนปุ่ม `Mod` แล้วคลิก `qa_driver.click(275, 782)` เพียง 1 ครั้ง | เปิดเข้าสู่ **หน้าจอจัดการ Mod** ถูกต้องทันทีโดยไม่ต้องใช้ recovery:<br>- **แถบนำทางด้านบน:** ปุ่มซ้าย `ย้อนกลับ`, แท็บกลาง `เรียกดู` (กำลังเลือกอยู่ มีขีดคั่นสีส้ม) และ `คอลเลกชัน`, ปุ่มขวา `ไปที่ Mod.io`, `ค้นหาและกรอง`, และไอคอนโปรไฟล์<br>- **หัวข้อที่แสดงบนหน้าจอ (Actual Headings):** หัวข้อหมวดด้านบนซ้ายแสดง **`ม็อดแนะนำ`** (การ์ดตัวอย่าง `Arcade Machines - Pack 1 of 3` พร้อมปุ่ม `สมัครรับ` และ `ตัวเลือกเพิ่มเติม`) และหัวข้อหมวดด้านล่างซ้ายแสดง **`คะแนนสูงสุด`**<br>- **ข้อสังเกตการใช้คีย์ร่วม (`UI/Modding/Mods`):** หน้าจอจัดการ Mod มุมมองเริ่มต้น (`เรียกดู`) ไม่มีป้ายหัวเรื่องหลักด้านบนสุดที่ใช้คีย์ `UI/Modding/Mods` จึงไม่ปรากฏคำว่า `Mod` ซ้ำในหัวข้อหน้านี้ (มีเพียงปุ่ม `ไปที่ Mod.io` ซึ่งเป็นคีย์แยกเดิม และหัวข้อย่อย `ม็อดแนะนำ` ที่ใช้คีย์แยกต่างหากและยังคงแสดง `ม็อดแนะนำ` ตามขอบเขตของ `fresh-translation-005` ที่แก้เฉพาะคีย์ `UI/Modding/Mods` เพียงคีย์เดียว) | **`DESTINATION_PASS`** |

---

## 4. ขอบเขตและข้อจำกัดที่ยังคงเปิดอยู่

- ไม่มีการติดตั้ง ดาวน์โหลด เปิด/ปิดใช้งาน Mod ล็อกอิน สมัครรับ (`สมัครรับ`) หรือเปลี่ยนการตั้งค่าใดๆ
- ไม่ได้เข้าเมนู `การตั้งค่า` (`Settings`) ไม่ได้เข้ามหาวิทยาลัย และไม่ได้ทดสอบหมวดบุคลากร (`NOT_RUN`)
- การทดสอบนี้ยืนยันเฉพาะปุ่ม **`Mod`** บนเมนูหลักและการกดเปิดเข้าสู่หน้าจอจัดการ Mod เบื้องต้นเท่านั้น ไม่ได้ยืนยันผู้ใช้งานคีย์ `UI/Modding/Mods` ทั้งหมดในรันไทม์ และไม่ได้รับรองฟอนต์หรือข้อความทั้งคลัง
- ปัญหา [`BUG-THAI-002`](BUG_THAI_002.md), [`BUG-THAI-003`](BUG_THAI_003.md) และการติดตาม regression ของ [`BUG-THAI-001`](BUG_THAI_001.md) ยังคงมีสถานะ **OPEN** ตามเดิม

---

## 5. Lifecycle ของทั้ง 3 Bundle (รันแยกทีละขั้น)

```json
// ขั้นที่ 1: python tools/manage_probe.py check --probe fresh-translation-005 (ก่อนติดตั้ง)
{"action": "check", "files": [{"name": "fonts_assets_all.bundle", "state": "original"}, {"name": "localisation_assets_localisationenglish.bundle", "state": "original"}, {"name": "ui-prefabs-general_assets_all.bundle", "state": "original"}]}

// ขั้นที่ 2: python tools/backup_gameplay_saves.py
{"backup": "D:\\SteamLibrary\\steamapps\\common\\Two Point Campus\\ThaiCampusMod\\local\\backups\\gameplay-save-snapshots\\20261022T144107015797Z.zip", "files": 11, "verified": true}

// ขั้นที่ 3: python tools/manage_probe.py install --probe fresh-translation-005
{"action": "install", "files": [{"name": "fonts_assets_all.bundle", "state": "probe"}, {"name": "localisation_assets_localisationenglish.bundle", "state": "probe"}, {"name": "ui-prefabs-general_assets_all.bundle", "state": "probe"}]}

// ขั้นที่ 4: python tools/manage_probe.py check --probe fresh-translation-005 (หลังติดตั้ง)
{"action": "check", "files": [{"name": "fonts_assets_all.bundle", "state": "probe"}, {"name": "localisation_assets_localisationenglish.bundle", "state": "probe"}, {"name": "ui-prefabs-general_assets_all.bundle", "state": "probe"}]}

// ขั้นที่ 5–6: เปิดผ่าน Steam, เก็บภาพ 01-main-menu.png, เลื่อนเมาส์ยืนยัน hover ปุ่ม Mod ที่ (275, 782), คลิก 1 ครั้งเปิดหน้าจัดการ Mod เก็บภาพ 02-mod-destination.png, ปิดหน้าต่างตามปกติ (WM_CLOSE) และยืนยันไม่มีโปรเซส TPC.exe ค้าง

// ขั้นที่ 7: python tools/manage_probe.py restore --probe fresh-translation-005
{"action": "restore", "files": [{"name": "fonts_assets_all.bundle", "state": "original"}, {"name": "localisation_assets_localisationenglish.bundle", "state": "original"}, {"name": "ui-prefabs-general_assets_all.bundle", "state": "original"}]}

// ขั้นที่ 8: python tools/manage_probe.py check --probe fresh-translation-005 (ยืนยันคืนไฟล์เป็น original ทั้งสาม)
{"action": "check", "files": [{"name": "fonts_assets_all.bundle", "state": "original"}, {"name": "localisation_assets_localisationenglish.bundle", "state": "original"}, {"name": "ui-prefabs-general_assets_all.bundle", "state": "original"}]}
```

---

## 6. ข้อมูลสำรองเซฟและการเปรียบเทียบ Hash ก่อน/หลังทดสอบรอบ R2

- **ไฟล์ ZIP สำรองเซฟก่อนเริ่มรอบ R2:** `D:\SteamLibrary\steamapps\common\Two Point Campus\ThaiCampusMod\local\backups\gameplay-save-snapshots\20261022T144107015797Z.zip` (`verified=true`, 11 ไฟล์)
- **ไฟล์ Manifest คู่กัน:** `D:\SteamLibrary\steamapps\common\Two Point Campus\ThaiCampusMod\local\backups\gameplay-save-snapshots\20261022T144107015797Z.json`
- **สรุปผลการเปรียบเทียบ Hash ก่อน/หลังทดสอบรอบ R2:**
  - **Changed:** `0` ไฟล์
  - **New:** `0` ไฟล์
  - **Missing:** `0` ไฟล์
  - **Unchanged:** `11` ไฟล์ (ตรงกันทุกไบต์ทั้ง 11 ไฟล์; เก็บเซฟจริงและไฟล์ backup ไว้ตามเดิม ไม่มีการ rollback อัตโนมัติ ไม่ลบไฟล์ และไม่เปลี่ยนการตั้งค่า Steam Cloud)

| Relative Path | สถานะ | Pre-Run SHA-256 (Size) | Post-Run SHA-256 (Size) |
|---|---|---|---|
| `Cloud/<AccountID>/preferences.json` | **UNCHANGED** | `f2ff575ab51636cd0b380f6f12f9221b905acce7e89a4677824d16e118877c9e` (761 B) | `f2ff575ab51636cd0b380f6f12f9221b905acce7e89a4677824d16e118877c9e` (761 B) |
| `Cloud/<AccountID>/Saves/Slot1/8000.sav` | **UNCHANGED** | `5b4dac72e35d877f6b7f2d6933a8b0c44717ec2578052d1d9f218f983d050d0d` (179,866 B) | `5b4dac72e35d877f6b7f2d6933a8b0c44717ec2578052d1d9f218f983d050d0d` (179,866 B) |
| `Cloud/<AccountID>/Saves/Slot1/career.csav` | **UNCHANGED** | `c51ca1bc4f0fcb92a45e285ba530bb02adeb47babf87556d5dbade325cc808d9` (18,520 B) | `c51ca1bc4f0fcb92a45e285ba530bb02adeb47babf87556d5dbade325cc808d9` (18,520 B) |
| `Cloud/<AccountID>/Saves/Slot1/career.csav.2.bak` | **UNCHANGED** | `27fd1082d3b44549301f56fe4308fd5238d92e1f3c73a19287ae1f4d7e39ed51` (18,505 B) | `27fd1082d3b44549301f56fe4308fd5238d92e1f3c73a19287ae1f4d7e39ed51` (18,505 B) |
| `Cloud/<AccountID>/Saves/Slot1/career.csav.3.bak` | **UNCHANGED** | `cbbded52fde65f46da0c874a403280936286b31746ea6f17b5b38d0acadafc0b` (18,521 B) | `cbbded52fde65f46da0c874a403280936286b31746ea6f17b5b38d0acadafc0b` (18,521 B) |
| `Cloud/<AccountID>/Saves/Slot1/career.csav.4.bak` | **UNCHANGED** | `f9730de46047fd6673d6ab5e408c0c5a3c71468b310809f4643fb341bd84219f` (18,521 B) | `f9730de46047fd6673d6ab5e408c0c5a3c71468b310809f4643fb341bd84219f` (18,521 B) |
| `Cloud/<AccountID>/Saves/Slot1/career.csav.5.bak` | **UNCHANGED** | `dfd0601d068aa18807108560da1e16ad21da553a63e95cd4ea5b6bafbb1d5bba` (10,128 B) | `dfd0601d068aa18807108560da1e16ad21da553a63e95cd4ea5b6bafbb1d5bba` (10,128 B) |
| `Cloud/<AccountID>/Saves/Slot1/career.csav.6.bak` | **UNCHANGED** | `91998459ebcd62690c4cd54ef4d9ed16b9e0f379360c791a5709c4d1ee1f8e7c` (10,128 B) | `91998459ebcd62690c4cd54ef4d9ed16b9e0f379360c791a5709c4d1ee1f8e7c` (10,128 B) |
| `Cloud/<AccountID>/steam_autocloud.vdf` | **UNCHANGED** | `b5d31412181fb1e37bed11e0bfbc2ed973c01ba5eb4aa00b3da786a625ded124` (52 B) | `b5d31412181fb1e37bed11e0bfbc2ed973c01ba5eb4aa00b3da786a625ded124` (52 B) |
| `Cloud/<AccountID>/userprofile.sav` | **UNCHANGED** | `664d887974edcdf87f4e7c20c4abc31964029ac87d38f3aab138f3d54bc28350` (1,064 B) | `664d887974edcdf87f4e7c20c4abc31964029ac87d38f3aab138f3d54bc28350` (1,064 B) |
| `localpreferences.json` | **UNCHANGED** | `3a32b89c9050ee0dea84c4ba8b632e0f81d82da25da517babd0442b5889fab8b` (1,050 B) | `3a32b89c9050ee0dea84c4ba8b632e0f81d82da25da517babd0442b5889fab8b` (1,050 B) |
