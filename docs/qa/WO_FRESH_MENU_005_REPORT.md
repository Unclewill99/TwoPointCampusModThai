# WO-FRESH-MENU-005 QA Report — ตรวจปุ่ม Mod (`fresh-translation-005`)

- **วันที่ทดสอบ:** 2026-10-22 (Asia/Bangkok)
- **ผู้รับงาน:** Antigravity — Desktop QA
- **ชุดทดสอบ (Candidate):** `fresh-translation-005` (ต่อยอดจาก `fresh-translation-004` โดยแก้เฉพาะ `I2LS_UI::UI/Modding/Mods::segment-964` จาก `ม็อด` เป็น **`Mod`**; ชุด `fresh-translation-004` เดิมคงสถานะ frozen ไม่เปลี่ยนแปลง และฟอนต์/UI เหมือนชุด `004`)
- **สรุปผลรวม (Overall Verdict):** **`SETUP_LIMIT` / `INCONCLUSIVE`** *(ข้อ 1 ปุ่ม **`Mod`** บนเมนูหลัก **`PASS`** จากภาพหน้าจอจริง; ข้อ 2 หน้าจอจัดการ Mod **`NOT_RUN` / `INCONCLUSIVE`** เนื่องจากคลิกแรกเลือกดัชนีปุ่มไปโดน `โหลดเกม` และการใช้สิทธิ์ recovery 1 ครั้งผ่าน `qa_driver.py` ไม่สามารถปิดหน้า `โหลดเกม` เพื่อกลับไปกดปุ่ม `Mod` ได้ภายในเพดาน recovery สูงสุด 1 ครั้ง)*
- **เวลาที่ใช้ทดสอบจริง (Active Elapsed Time):** ~3.5 นาทีหลังเมนูหลักพร้อม (`21:29–21:33` ICT; เพดานกำหนดไม่เกิน 5 นาที)
- **จำนวนภาพหลักฐานและ Recovery:** ภาพหลักฐานต้นฉบับ 2 ภาพ (`3840 x 2160` PNG ไม่ย่อขนาด) ใน `local/qa/WO-FRESH-MENU-005/` และใช้ recovery รวม **1 ครั้ง** (เพดานกำหนดสูงสุด 2 ภาพ และ recovery รวมสูงสุด 1 ครั้ง)

---

## 1. ข้อมูล Candidate, Hash, Build เกม และเครื่องมือควบคุม

- **Game Build ที่แสดงบนหน้าจอจริง:** `10.3.169253+2024-12-06.1241` (มุมซ้ายบนของ [`01-main-menu.png`](../../local/qa/WO-FRESH-MENU-005/01-main-menu.png))
- **การตรวจสอบ Manifest และ Build Report:**
  - ตรวจสอบ [`local/prototype/fresh-translation-005/manifest.json`](../../local/prototype/fresh-translation-005/manifest.json) เทียบกับ [`reports/fresh-translation-005-build.json`](../../reports/fresh-translation-005-build.json) ยืนยันข้อมูลตรงกันทุกฟิลด์ (`records_reloaded: 15677`, `translated: 12710`, `keep_as_source: 2967`, `override_sha256: 30506337e6c8722173bbd49284230044907a98c5c8b7560ae08e969ea0dd211f`, `changed_records`: `[["I2LS_UI", 964, "UI/Modding/Mods=ม็อด", "UI/Modding/Mods=Mod"]]`)
- **SHA-256 ของทั้ง 3 Bundle (ตรวจสอบด้วย `tools/manage_probe.py` ก่อนติดตั้ง):**
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
  - คัดเลือกหน้าต่างจากเจ้าของโปรเซสพาธ `D:\SteamLibrary\steamapps\common\Two Point Campus\TPC.exe` เท่านั้น (`qa_driver.find_tpc_window()` พบหน้าต่างเดียว `hwnd=921186`, `title='Two Point Campus'`) ยืนยัน foreground (`qa_driver.activate_tpc()`, `qa_driver.require_game_foreground()`) และตรวจสอบพิกเซลภาพเกมจริงก่อนส่ง input
  - ส่งเมาส์ด้วย [`tools/qa_driver.py`](../../tools/qa_driver.py) (`user32.SendInput`) และบันทึกภาพหน้าจอต้นฉบับขนาดจริง `3840 x 2160` PNG ด้วย `PIL.ImageGrab.grab()`
  - ปิดเกมตามปกติด้วย `WM_CLOSE` (เทียบเท่าการขอปิดหน้าต่างตามปกติด้วย `Alt+F4` ไม่ใช้การบังคับปิดโปรเซส) และยืนยันว่าไม่มีโปรเซส `TPC.exe` ค้างก่อนคืนไฟล์

---

## 2. ผลการตรวจสอบรายข้อ (Expected / Actual / Status)

| ข้อ | รายการตรวจตามใบงาน | ภาพหลักฐานที่ถึงจริง | Expected | Actual | สถานะ |
|:---:|---|---|---|---|---|
| **1** | **เมนูหลัก: ปุ่มระหว่าง Sandbox และ Settings** | [`01-main-menu.png`](../../local/qa/WO-FRESH-MENU-005/01-main-menu.png) *(หน้าจอเมนูหลัก `3840 x 2160`)* | ปุ่มระหว่าง `แซนด์บ็อกซ์` (`Sandbox`) และ `การตั้งค่า` (`Settings`) แสดงข้อความ **`Mod`** ตรงตัว (`M` ใหญ่, `od` เล็ก ไม่มี `s`) ไม่ว่าง ไม่ตัด ไม่ชนขอบ ไม่มี raw tags | บนหน้าจอเมนูหลักจริง ปุ่มลำดับที่ 6 (`y=1528..1610` อยู่ระหว่าง `แซนด์บ็อกซ์` ที่ `y=1389..1470` และ `การตั้งค่า` ที่ `y=1668..1750`) แสดงคำว่า **`Mod`** ตรงตัว (`M` ใหญ่, `od` เล็ก ไม่มี `s`) จัดกึ่งกลางปุ่มชัดเจน ไม่ว่าง ไม่ตัดขอบ ไม่ชนขอบปุ่ม และไม่มี raw tags | **`PASS`** |
| **2** | **กดปุ่ม Mod หนึ่งครั้งเพื่อยืนยันเปิดหน้าจอจัดการ Mod และระบุหัวข้อที่แสดง** | [`02-mod-screen.png`](../../local/qa/WO-FRESH-MENU-005/02-mod-screen.png) *(หน้าจอ `โหลดเกม` `3840 x 2160`)* | กดปุ่ม `Mod` หนึ่งครั้งแล้วเปิดหน้าจอจัดการ Mod ถูกต้อง เก็บภาพและระบุหัวข้อที่แสดง (หากหัวข้อใช้คีย์ร่วมให้บันทึกว่าปรากฏ `Mod` ด้วย) | **Base attempt:** สคริปต์อ่านแถบปุ่มสีฟ้าจากภาพ `01-main-menu.png` ในช่วง `y=700..1800` ทำให้ปุ่มที่ 8 (`ออก` ที่ `y=1808..1890`) อยู่นอกช่วงค้นหา ดัชนี `bands[-3]` จึงชี้ไปที่ปุ่มลำดับที่ 3 (`โหลดเกม` ที่ `x=402, y=1149`, logical `(201, 574)`) แทนปุ่มลำดับที่ 6 (`Mod` ที่ `y=1528..1610`, logical `(275, 784)`) และเปิดหน้าจอ `โหลดเกม` ดังภาพ `02-mod-screen.png`<br>**Recovery (1/1):** สั่งคลิกปุ่มกากบาทสีแดงมุมขวาบนของหน้า `โหลดเกม` (`x=3712, y=96`, logical `(1856, 48)`) ผ่าน `qa_driver.click` เพื่อย้อนกลับเมนูหลัก แต่หน้า `โหลดเกม` ไม่ปิดลง (พิกเซลที่ `(250, 1569)` ยังคงเป็น `(42, 62, 75)` ของหน้า `โหลดเกม`) จึงหยุดทันทีตามกฎเพดาน recovery 1 ครั้ง ไม่วนทดสอบซ้ำ และไม่อ้างผลจากชื่อ asset หรือผลของชุด `004` | **`NOT_RUN` / `INCONCLUSIVE` (`SETUP_LIMIT`)** |

---

## 3. ขอบเขตและข้อจำกัดที่ยังคงเปิดอยู่

- ไม่ได้เข้าเมนู `การตั้งค่า` (`Settings`) หรือเข้ามหาวิทยาลัยใดๆ ไม่ได้ทดสอบหมวดบุคลากร (`NOT_RUN`) ไม่ได้เปลี่ยนค่าการตั้งค่า และไม่ได้เล่นเซฟเกม
- ไม่มีการติดตั้ง เปิด/ปิด ดาวน์โหลด สมัครบริการ ล็อกอิน หรือแก้ไขรายการ Mod ใดๆ
- การตรวจในข้อ 1 ยืนยันเฉพาะการแสดงผลปุ่ม **`Mod`** บนเมนูหลักจากภาพจริงเท่านั้น ยังไม่ได้ยืนยันหน้าจอจัดการ Mod หรือผู้ใช้งานคีย์ `UI/Modding/Mods` จุดอื่นๆ ในรันไทม์
- ปัญหา [`BUG-THAI-002`](BUG_THAI_002.md), [`BUG-THAI-003`](BUG_THAI_003.md) และการติดตาม regression ของ [`BUG-THAI-001`](BUG_THAI_001.md) ยังคงมีสถานะ **OPEN** ตามเดิม การทดสอบนี้ไม่ได้รับรองฟอนต์หรือข้อความทั้งคลัง

---

## 4. Lifecycle ของทั้ง 3 Bundle

คำสั่งทั้งหมดรันแยกทีละขั้นและตรวจสอบผลก่อนขั้นถัดไป โดยยืนยันว่า `TPC.exe` ปิดสนิทก่อนแก้ไขไฟล์ทุกครั้ง:

```json
// ขั้นที่ 1: python tools/manage_probe.py check --probe fresh-translation-005 (ก่อนติดตั้ง)
{"action": "check", "files": [{"name": "fonts_assets_all.bundle", "state": "original"}, {"name": "localisation_assets_localisationenglish.bundle", "state": "original"}, {"name": "ui-prefabs-general_assets_all.bundle", "state": "original"}]}

// ขั้นที่ 2: python tools/backup_gameplay_saves.py
{"backup": "D:\\SteamLibrary\\steamapps\\common\\Two Point Campus\\ThaiCampusMod\\local\\backups\\gameplay-save-snapshots\\20261022T142530176901Z.zip", "files": 11, "verified": true}

// ขั้นที่ 3: python tools/manage_probe.py install --probe fresh-translation-005
{"action": "install", "files": [{"name": "fonts_assets_all.bundle", "state": "probe"}, {"name": "localisation_assets_localisationenglish.bundle", "state": "probe"}, {"name": "ui-prefabs-general_assets_all.bundle", "state": "probe"}]}

// ขั้นที่ 4: python tools/manage_probe.py check --probe fresh-translation-005 (หลังติดตั้ง)
{"action": "check", "files": [{"name": "fonts_assets_all.bundle", "state": "probe"}, {"name": "localisation_assets_localisationenglish.bundle", "state": "probe"}, {"name": "ui-prefabs-general_assets_all.bundle", "state": "probe"}]}

// ขั้นที่ 5–6: เปิดผ่าน Steam, เก็บภาพ 01-main-menu.png และ 02-mod-screen.png, ใช้ recovery 1 ครั้ง, ขอปิดหน้าต่างตามปกติ (WM_CLOSE) และยืนยัน TPC.exe ปิดสนิท

// ขั้นที่ 7: python tools/manage_probe.py restore --probe fresh-translation-005
{"action": "restore", "files": [{"name": "fonts_assets_all.bundle", "state": "original"}, {"name": "localisation_assets_localisationenglish.bundle", "state": "original"}, {"name": "ui-prefabs-general_assets_all.bundle", "state": "original"}]}

// ขั้นที่ 8: python tools/manage_probe.py check --probe fresh-translation-005 (ยืนยันคืนไฟล์เป็น original ทั้งสาม)
{"action": "check", "files": [{"name": "fonts_assets_all.bundle", "state": "original"}, {"name": "localisation_assets_localisationenglish.bundle", "state": "original"}, {"name": "ui-prefabs-general_assets_all.bundle", "state": "original"}]}
```

---

## 5. ข้อมูลสำรองเซฟและการเปรียบเทียบ Hash ก่อน/หลังทดสอบ

- **ไฟล์ ZIP สำรองเซฟก่อนเริ่ม:** `D:\SteamLibrary\steamapps\common\Two Point Campus\ThaiCampusMod\local\backups\gameplay-save-snapshots\20261022T142530176901Z.zip` (`verified=true`, 11 ไฟล์)
- **ไฟล์ Manifest คู่กัน:** `D:\SteamLibrary\steamapps\common\Two Point Campus\ThaiCampusMod\local\backups\gameplay-save-snapshots\20261022T142530176901Z.json`
- **สรุปผลการเปรียบเทียบ Hash ก่อน/หลังทดสอบ:**
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
