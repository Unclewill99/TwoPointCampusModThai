# จุดพักงานล่าสุด — 27 ตุลาคม 2026 00:05 (Asia/Bangkok) — Claude (PM)

ต่อจาก SESSION_CHECKPOINT_2026-10-26.md ครอบคลุมงานช่วงค่ำ 26 ต.ค. ถึงเที่ยงคืน

## ติดตั้งในเกมจริงตอนนี้ (ซ้อนกัน ถอนแยกได้)

| ชุด | ไฟล์ | สถานะ | ถอน |
|---|---|---|---|
| fresh-translation-007 | 3 bundle แปล/ฟอนต์/UI | ใช้งานจริง | `manage_probe.py restore --probe fresh-translation-007` |
| thai-logo-001 | 2 bundle โลโก้ | ใช้งานจริง | `restore --probe thai-logo-001` |
| county-logo-001 | 1 bundle | ใช้งานจริง | `restore --probe county-logo-001` |
| news-thai-001 | GameAssembly.dll | ใช้งานจริง | `Uninstall_Thai_News.bat` |
| **tannoy-thai-006** (เสียง PA) | audio-tannoy_assets_english.bundle | ใช้งานจริง — ยืนยันด้วย `check` 27 ต.ค. และผู้ใช้ทดลองเล่น: **เสียงใช้ได้ทุกคลิป ไม่ต้องแก้คำอ่าน** (ไม่ต้อง build 007 เพื่อแก้เสียง) | `restore --probe tannoy-thai-006` |

## งานที่เสร็จวันนี้ (ดู TANNOY_THAI_001.md, TANNOY_AUDIO_SURVEY_001.md)

- Install_Thai_Mod.bat / Uninstall_Thai_Mod.bat ครอบคลุม 4 ชุดแรก (ยังไม่รวมเสียง PA; **ยังไม่ทดสอบบน Windows**)
- เสียงประกาศ PA ภาษาไทย: พิสูจน์ pipeline (FSB5 PCM16 เขียนเอง → เกมเล่นได้), ปรับความดังเท่าต้นฉบับ (−15 LUFS), เลือกเสียง ElevenLabs **George** (eleven_v4, แท็ก [sarcastic]) ผู้ใช้ฟังในเกมแล้วพอใจ; **tannoy-thai-006** = George ครบ 421 คลิป (+46 คลิป Session1 ยัง placeholder) build แล้ว รอผลในเกม
- โครงสร้าง: `local/review/tannoy-lines-thai.json` (บท), `tannoy-pronounce.json` (สะกดตามเสียง: ภารโรง→พานโรง), `tannoy-tags.json` (แท็กต่อคลิป ยังว่าง), `tools/tts_edge_windows.py`, `tools/tts_elevenlabs_windows.py` (key ที่ `local/secrets/elevenlabs.key` gitignored), `tools/build_tannoy_thai_00{1..6}.py` (004–006 ใช้ฐาน 003 + โฟลเดอร์ทับ)
- ElevenLabs: Starter plan ต่ออายุ 26 พ.ย.; ใช้ 9,103/39,823 เหลือ 30,720 (≈0.45 เครดิต/ตัวอักษร)
- สำรวจเสียงวิทยุ: 342 คลิป 2 ชม. 5 นาที บทไทย 341/342 ≈ 80k ตัวอักษร ≈ 36–40k เครดิต หลายตัวละคร มีเพลงประกอบ ต้อง Vorbis (FMOD) เพราะ PCM ใหญ่เกิน — `local/audio/tannoy-survey-001/radio_clips.json`
- จาก Player.log: ฟอนต์ `PalanquinDark_Regular` ไม่มีอักษรไทย ใน `[SaveText]` → รายการใหม่ใต้ BUG-THAI-001

## Git

ผู้ใช้ commit งานทั้งหมดแล้วใน 892cb6c "thai speach" (26 ต.ค.) เหลือเฉพาะ checkpoint นี้ที่ยังไม่ commit. โฟลเดอร์ `Claude outputs/` และ `local/_to_delete/` ลบได้.

## เริ่มงานครั้งหน้า

1. ~~ยืนยัน 006 + แก้คำอ่านเพี้ยน~~ **เสร็จ 27 ต.ค.** — 006 ผ่านการใช้งานจริง ไม่มีคำอ่านเพี้ยน (build 007 จะทำเมื่อมีคลิป Session1 ครบเท่านั้น)
2. หา key ข้อความของ 46 คลิป `Campus_Tannoy_Session1_*` ในคลัง (น่าจะอยู่ชุด UI/Tutorial) แล้ว generate
3. ใส่ชุดเสียง PA ใน Install/Uninstall_Thai_Mod.bat หลังผ่านใช้งานจริง; ทดสอบ .bat รอบ Uninstall→Install บน Windows
4. เฟสวิทยุ: ทดลอง Host_Intro 10 คลิป + ทดสอบเข้ารหัส Vorbis ด้วย FMOD fsbankcl ก่อนทำทั้งชุด
5. ค้างเดิม: UI Scale เล็ก/ใหญ่, ช่องว่าง เยี่ยม หัวข้อตัวหนา, SaveText font, ศัพท์ที่ยังไม่อนุมัติ, TMP version UNKNOWN


## อัปเดต 27 ต.ค. (บ่าย)

- `manage_probe.py check --probe tannoy-thai-006` → state `probe` (ติดตั้งจริง); 005 ไม่ตรง
- ผู้ใช้ทดลองเล่นเกม: เสียงประกาศ PA ภาษาไทย (George) ใช้ได้ทั้งหมด ไม่ต้องแก้ไขคำอ่านใด ๆ → ปิดข้อ 1 ของแผน; `tannoy-pronounce.json` คงเดิม
- ขั้นต่อไป: ข้อ 2 (46 คลิป Session1), ข้อ 3 (ใส่ PA ลง .bat), ข้อ 4 (วิทยุ)
