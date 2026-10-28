# เฟสวิทยุ — บันทึกงาน (เริ่ม 27 ตุลาคม 2026, Claude PM) — แผน: RADIO_THAI_PLAN_001.md

## R0 เตรียม (27 ต.ค. — ไม่ใช้เครดิต)

### สำรวจ `audio-radio_assets_english.bundle` (sha `6566f540…` 104 MB; สำรองไว้ `local/backups/radio-original/`)
- 342 AudioClip, 125.5 นาที, ทุกคลิป Vorbis ใน FSB5 (`mode 15`, FSB5 v1, 1 subsound, ไม่มี name table, chunk type 4 + type 11/VORBISDATA), `m_LoadType=2` streaming
- **คลิปพูดของ DJ ทั้งหมดเป็น mono 48 kHz ≈ 82–85 kbps**; sting/โฆษณา stereo ≈ 250–280 kbps (ต้องเลือก quality ของ fsbankcl ให้ใกล้เคียง)
- ความดัง: ทุกกลุ่ม ≈ −14 LUFS (−13…−15.5), peak −0.6…−2.4 dBFS, LRA ≈ 2–3 LU (บีบอัดแรง) → เป้าหมายเสียงไทย **−14 LUFS / −1 dBTP** (ดังกว่าชุด PA 1 dB)
- ชนิดคลิป (จากข้อความ I2LS): `voice` 274 (DJ พูดเปล่า มีช่วงเงียบจริง ไม่มีเพลงรอง), `voice_over_music` 44 (โฆษณา 33 + sting ที่มีคำพูด 11), `music_only` 24 (sting ล้วน ไม่ต้องทำ)
- ผล: `local/audio/radio-survey-001/radio_survey.json` (ต่อคลิป: วินาที, ช่อง, kbps, LUFS, peak, LRA, พื้นเสียงเงียบ, ผู้พูด, ชนิด) + `original_wav/` 3 คลิปตัวอย่าง; WAV ทั้ง 342 คลิปอยู่ชั่วคราวใน VM (`~/radio_wav`, ถอดใหม่ได้ด้วย UnityPy)

### บท
- `local/review/radio-lines-thai.json`: บทไทยจาก CLAUDE-FULL-RETRANSLATION-001 (review r5) 341/342 คลิป (`Socialite_Handover_2` ไม่มีบท) แยกเป็น segments: `speech` (speaker ชื่ออังกฤษจากต้นฉบับ, ตัดป้ายผู้พูดออกจากข้อความแล้ว) และ `nonvocal` (เพลง/เอฟเฟกต์ พร้อมวินาทีจากแท็ก `<non_vocal_audio=…>` ใช้วางตำแหน่งเสียงตอนผสม) — **รวมบทพูดไทย 76,009 ตัวอักษร ≈ 34k เครดิต** (ถูกกว่าที่ประเมิน): Nigel 14.7k, Harrison 14.4k, Ricky 14.2k, Felicity 7.1k, Narrator 5.6k, DJ Shorts 5.1k, Maggie 4.9k, Hugh 4.8k, Wanda 3.3k, ตัวประกอบ ≈ 1.8k
- ชื่อเฉพาะในบทไทยคงเป็นอักษรละติน 262 คำ (Two Point Radio, Hawthorne, Crumley…) — ให้ eleven_v4 อ่านเอง ถ้าเพี้ยนค่อยเพิ่ม `tannoy-pronounce.json`
- `local/review/radio-cast.json`: ตัวละคร 9 + ตัวประกอบ → voice_id (ยังว่าง รอ R1), แท็กอารมณ์, ค่าเริ่มต้น (eleven_v4, −14 LUFS, chain "radio"), ลำดับ R2

### เครื่องมือ
- `tools/fsb_vorbis_windows.py` — ห่อ `fsbankcl.exe` (FMOD Studio) แปลง `local/review/<probe>/src/*.wav` → `<probe>/fsb/*.fsb` (Vorbis, `--quality` ค่าเริ่ม 60) รันบน Windows
- `tools/build_radio_thai.py --probe <name>` — ใส่ .fsb แทน blob ของคลิปชื่อเดียวกัน สร้าง `.resource` ใหม่ อัปเดต m_Length/Frequency/Channels ตรวจ decode ผ่าน FMOD แบบออฟไลน์ เขียน manifest + `reports/<probe>-build.json`; ตัวเลือก `--header-tail original` คัดลอก flags/GUID จาก blob เดิมถ้า fsbankcl ให้ header ต่างแล้วเกมไม่เล่น
- **self-test ผ่าน**: ใส่ blob ต้นฉบับ 2 คลิปกลับผ่านสคริปต์ → bundle ใหม่ 103,963,424 ไบต์ (เดิม 103,963,286) decode ผ่าน non-AudioClip identical (ผลย้ายไป `local/_to_delete/radio-selftest-*`)
- `tools/manage_probe.py` รับ `radio-thai-001..003` แล้ว

### radio-thai-001 (probe เทคนิค) — รอผู้ใช้
ต้นทางพร้อม: `local/review/radio-thai-001/src/Host_Intro_1.wav` (mono 15.7 s) และ `CR_Sting_Intro_1.wav` (stereo 13.3 s) ถอดจากต้นฉบับ ไม่มีเสียงไทย

ขั้นผู้ใช้ (Windows):
1. ติดตั้ง FMOD Studio (fmod.com/download → FMOD Studio, ต้องสมัครบัญชี) ซึ่งมี `fsbankcl.exe`
2. `python tools/fsb_vorbis_windows.py --probe radio-thai-001` (ถ้าหา exe ไม่เจอใช้ `--fsbankcl "<path>"`; ถ้า flag ไม่ตรงเวอร์ชันดู `--help-fsbankcl`) → ได้ `local/review/radio-thai-001/fsb/*.fsb` + `_encode_report.json`
3. แจ้ง Claude → Claude รัน `build_radio_thai.py --probe radio-thai-001` บน VM → ผู้ใช้ `manage_probe.py install --probe radio-thai-001` แล้วเปิดวิทยุในเกม ฟัง Host_Intro / sting ว่าเล่นได้ ไม่ซ่า ไม่เงียบ

ผ่านแล้ว → R1 (คัดเสียง + Host_Intro 10 คลิป)

### ผล radio-thai-001 (27 ต.ค. ค่ำ)
- fsbankcl อยู่ใน **FMOD Engine** (ไม่ใช่ FMOD Studio): `C:\Program Files (x86)\FMOD SoundSystem\FMOD Studio API Windows\bin\fsbankcl.exe` (2.04.00); flag ที่ใช้ได้: `-o <out> -format vorbis -quality N <wav>` (`-cache_dir` ใช้ไม่ได้ในเวอร์ชันนี้ ตัดออกแล้ว)
- quality 60: Host_Intro_1 → 168,832 ไบต์ (ต้นฉบับ 165,472 ≈ เท่ากัน); CR_Sting_Intro_1 → 246,272 (ต้นฉบับ 418,656 — sting/โฆษณาควรใช้ quality สูงกว่า เช่น 80–90)
- FSB5 จาก fsbankcl: v1, mode 15, chunk 11 (VORBISDATA) เท่านั้น (ต้นฉบับมี chunk 4 เพิ่ม — เป็น user data "Tempo:" ไม่จำเป็น), มี name table 1 ชื่อ, CRC setup header ต่างจากต้นฉบับ (d4bbe0d6 vs e3f54737 สำหรับ mono 48k) → ต้องพิสูจน์ในเกมว่า FMOD รุ่นในเกมรู้จัก setup นี้
- build (VM): `local/prototype/radio-thai-001/` sha `ba0cc807…` 103,795,070 ไบต์, decode ออฟไลน์ผ่านทั้ง 2 คลิป, non-AudioClip identical; `manage_probe.py check` = original → **runtime NOT_TESTED**
- ถ้าเกมไม่เล่น: ลอง `build_radio_thai.py --probe radio-thai-001 --header-tail original --force`; ถ้ายังไม่ได้ ถอยไป PCM mono 24 kHz

- **runtime (27 ต.ค.)**: ผู้ใช้รายงานว่าเล่นเกมแล้วเสียงวิทยุไม่ขาดหาย แต่ `manage_probe.py check` ขณะนั้นพบว่าไฟล์ในเกมยังเป็น **ต้นฉบับ** (probe ไม่ได้ติดตั้งอยู่) → ติดตั้งใหม่ (check = probe) แล้วเล่นเกมเปิดวิทยุ: **PASS — เสียงวิทยุปกติ** ท่อ fsbankcl → FSB5 Vorbis (quality 60) → bundle ใช้ได้กับ FMOD ในเกม; radio-thai-001 คงติดตั้งไว้ได้ (เสียงเท่าต้นฉบับ)

## R1 เตรียมไว้ (27 ต.ค. ค่ำ) — รอผล radio-thai-001 ก่อนใช้เครดิต
- `tools/radio_tts_windows.py`: `--list-voices`, `--cast-samples [--dry-run]` (ตัวอย่าง 1 ประโยคจาก `sample_clip` ของแต่ละตัวละคร × ผู้สมัครใน `radio-cast.json` → `local/review/radio-cast-samples/<ตัวละคร>/<ชื่อเสียง>.mp3`; dry-run = 2,062 ตัวอักษร ≈ 930 เครดิต), `--character X --clips …|--all [--dry-run]` → `local/review/radio-eleven-raw/<X>/<clip>.mp3` (คลิปหลายผู้พูดแยกเป็น `__s<N>` ต่อ segment) อ่านตาราง tannoy-pronounce.json ร่วมกัน; ผู้สมัครอ้างด้วย "ชื่อ" เสียง premade แล้วสคริปต์ค้น id จาก /voices
- ผู้สมัครเริ่มต้น (premade ElevenLabs; George สงวนให้ PA): Felicity: Sarah/Jessica/Matilda · Harrison: Chris/Eric/Will · Nigel: Brian/Bill/Daniel · Ricky: Roger/Daniel/Brian · Maggie: Alice/Laura/Lily · DJ Shorts: Liam/Charlie/Will · Wanda: Charlotte/Matilda/Aria · Hugh: Callum/Liam/Roger · Narrator: Bill/Chris
- ยังต้องเขียน: `tools/radio_process.py` (ตัด silence หัว, โทนวิทยุ, −14 LUFS/−1 dBTP, mono 48k สำหรับ DJ) และขั้น fsbankcl → build

## R1 — คัดเสียง (27 ต.ค. ดึก) ✔
- `--cast-samples` ใช้ ≈ 930 เครดิต (ตัวอย่าง 26 ไฟล์ ใน `local/review/radio-cast-samples/`); premade voices ในบัญชีมี 21 เสียง (ไม่มี Charlotte/Aria → Wanda ใช้ Lily/Matilda/Bella)
- **ผู้ใช้เลือก** (บันทึกใน `radio-cast.json` → `voice_name`): Felicity = **Sarah**, Harrison = **Chris**, Nigel = **Bill**, Ricky = **Brian**, Maggie = **Alice**, DJ Shorts = **Liam**, Wanda = **Lily**, Hugh = **Liam** (ซ้ำ DJ Shorts), Narrator = **Chris** (ซ้ำ Harrison; โฆษณาเป็น R3) — ถ้าฟังในเกมแล้วสับสนค่อยแยกด้วยแท็ก/ความเร็ว
- `tools/radio_process.py --probe <p> --character <c>`: mp3 → ตัด silence หัว/ท้าย (เว้นหัว 0.12 s ท้าย 0.35 s), HPF 80/LPF 14k, compressor 3:1, gain เป็น −14 LUFS + limiter −1 dBTP, PCM16 48k mono (ช่องตาม survey ของคลิปเดิม) → `local/review/<p>/src/*.wav` + `loudness.json`; ทดสอบกับตัวอย่าง Sarah ได้ −14.0 LUFS / −0.9 dB
- ถัดไป (นำร่อง radio-thai-002): `python tools/radio_tts_windows.py --character Felicity --clips Host_Intro_1 … Host_Intro_10` (2,126 ตัวอักษร ≈ 960 เครดิต) → process (VM) → `python tools/fsb_vorbis_windows.py --probe radio-thai-002 --quality 60` (Windows) → build (VM) → install → ฟังในเกม

## radio-thai-002 — นำร่อง Felicity Host_Intro 1–10 (27 ต.ค. ดึก)
- TTS Sarah/eleven_v4/[cheerful] 10 คลิป 2,126 ตัวอักษร (≈ 960 เครดิต) → process −14 LUFS ความยาว 11–22 s ใกล้ต้นฉบับ (ต่างไม่เกิน ±2.8 s) → fsbankcl q60 → build: 10 คลิปแทนที่ (ไม่รวม 2 คลิปของ 001 ซึ่งเป็นต้นฉบับอยู่แล้ว) sha `dd8c8f89…` 104,108,064 ไบต์ decode ผ่านทั้งหมด runtime NOT_TESTED
- ผู้ใช้สังเกตจาก VLC ว่าชื่อภาษาอังกฤษในคลิปฟังเหมือนขาดหาย; silencedetect ไม่พบช่องว่าง > 0.5 s → รอฟังในเกม
- ติดตั้ง: `restore --probe radio-thai-001` → `install --probe radio-thai-002`

## radio-thai-003 — Felicity Host_Intro 10 + Harrison 53 คลิป (27 ต.ค. ดึก)
- ผู้ใช้เล่นแคมปัสที่วิทยุเป็นรายการ Harrison → ทำ Harrison ก่อน: TTS Chris/[excited] 56 คลิป 14,918 ตัวอักษร (≈ 6.7k เครดิต); 3 sting (HW_Sting_1_A/2_A/3_A มีเพลง) กันออก (R3) — `radio_process.py` ตอนนี้ข้าม kind voice_over_music/music_only อัตโนมัติ
- process: HW 53 คลิป −14.0…−14.5 LUFS ความยาวเทียบต้นฉบับ median 0.81 (0.63–1.00) → fsbankcl q60 → build 63 คลิป sha `83ee2e7f…` 102,859,398 ไบต์ decode ผ่านทั้งหมด runtime NOT_TESTED
- ติดตั้ง: `restore --probe radio-thai-00N` (ตัวที่ติดตั้งอยู่) → `install --probe radio-thai-003`
- **เครดิต ElevenLabs 28 ต.ค. (ก่อน Nigel)**: เหลือ 23,080/39,823 → ใช้ไปในเฟสวิทยุ ≈ 7,640 (ตัวอย่าง ≈ 930 + Felicity 10 คลิป ≈ 960 + Harrison ≈ 5,750 → จริง ≈ 0.39 เครดิต/ตัวอักษร ถูกกว่าประเมิน) แผนรอบนี้: Nigel ≈ 6.0k → Ricky ≈ 5.5k → Felicity ที่เหลือ ≈ 2.0k → Maggie ≈ 1.9k → DJ Shorts ≈ 2.0k → Hugh ≈ 1.9k (รวม ≈ 19.3k) เหลือ ≈ 3.8k; Wanda (≈ 1.3k) + โฆษณา/sting + แก้คำอ่าน รอรอบ 26 พ.ย.

## radio-thai-004 — + Nigel 49 คลิป (28 ต.ค.)
- TTS Bill/[sarcastic] 53 คลิป 15,382 ตัวอักษร; 4 sting มีเพลง (NB_Sting_1_A/2_A/3_A + segment) ข้ามไว้ R3 → process 49 คลิป −14 LUFS ความยาว median 0.91 (0.73–1.11)
- build 112 คลิป (Felicity 10 + Harrison 53 + Nigel 49) sha `0a2af32d…` 102,397,635 ไบต์ decode ผ่าน runtime NOT_TESTED; manage_probe รับ radio-thai-004..008 แล้ว
- **เครดิต ElevenLabs 28 ต.ค. (หลัง Nigel)**: เหลือ **16,927/39,823** → Nigel ใช้จริง ≈ 6,153 (15,382 ตัวอักษร ≈ 0.40 เครดิต/ตัวอักษร) ; เหลือสำหรับรอบนี้ ≈ 16.9k: Ricky ≈ 5.7k → Felicity ที่เหลือ ≈ 2.0k → Maggie ≈ 1.9k → DJ Shorts ≈ 2.0k → Hugh ≈ 1.9k (รวม ≈ 13.5k) เหลือกัน ≈ 3.4k สำหรับแก้คำอ่าน; Wanda + โฆษณา/sting รอ 26 พ.ย.

## radio-thai-005 — + Ricky 52 คลิป (28 ต.ค.)
- คัดคลิปก่อน TTS: Ricky 56 คลิป ตัด 4 (RH_Sting_2_A/3_A มีเพลง, Ad_Crumley_Ricky โฆษณา, RH_S6_L5 มีเสียง Professor → R3) เหลือ 52 รายชื่อ `local/review/radio-thai-005/clips_ricky.txt` → TTS Brian/[serious] 14,078 ตัวอักษร (ใช้ `--clips` แทน `--all` ประหยัด ≈ 1k เครดิต)
- process 52 คลิป −14.1…−14.4 LUFS ความยาว median 0.89 (RH_S5_L7 สั้น 15.8/43.3 s เพราะต้นฉบับมีช่วงเสียงกินของ; บทมี stage direction `[Ricky begins to stuff…]` ให้ตรวจในเกมว่าไม่ถูกอ่านออกเสียง)
- src/fsb ของ 005 = คัดลอกจาก 004 (112) + Ricky 52 = 164; fsbankcl q60 → build 164 คลิป sha `def3f83d…` 102,805,970 ไบต์ decode ผ่านทั้งหมด non-AudioClip identical runtime NOT_TESTED
- ติดตั้ง: `restore --probe radio-thai-00N` (ตัวที่ติดตั้งอยู่) → `install --probe radio-thai-005`
- VM หมายเหตุ: UnityPy หายทุก session ใหม่ → `pip install --user UnityPy` + `pip install --user --force-reinstall --no-deps "attrs>=23"`

## radio-thai-006 — + Felicity ที่เหลือ 30 + Maggie 28 (28 ต.ค.)
- Felicity (Sarah) Host_1–5/Handover_1–15/Outro_1–10 5,457 ตัวอักษร; Maggie (Alice/[friendly]) STF_* 28 คลิป 5,205 ตัวอักษร (รายชื่อ `local/review/radio-thai-006/clips_*.txt`) ไม่มีคลิปปนเพลง/ปนคนอื่น
- process: Felicity −14 LUFS ความยาว median 1.04; Maggie median 0.99; STF_Handover_4 + STF_StudentLife_3 true peak ถึง 0 dB → re-limit ด้วย alimiter −2 dB เป็น −0.9 dB (บันทึก note ใน loudness.json) — ถ้าเจออีกควรลด limit ใน radio_process.py เป็น −1.5 dB
- src/fsb = 005 (164) + 58 = 222 → fsbankcl q60 → build 222 คลิป sha `aee66726…` 103,473,283 ไบต์ decode ผ่านทั้งหมด runtime NOT_TESTED
- ติดตั้ง: `restore` ตัวที่ติดตั้งอยู่ → `install --probe radio-thai-006`; เหลือรอบนี้: DJ Shorts → Hugh

## radio-thai-007 — + DJ Shorts 20 + Hugh 12 (28 ต.ค.)
- DJ Shorts (Liam) Pseudo_* 20 คลิป 5,331 ตัวอักษร; Hugh (Liam) Correspondent_1–5 + SobStory_1–3,5–8 12 คลิป 4,557 ตัวอักษร (SobStory_4 มี Student ปน → R3); รายชื่อ `local/review/radio-thai-007/clips_*.txt` (+ `clips_wanda.txt` 13 คลิป เตรียมไว้รอบหน้า)
- process: ทั้งคู่ −14.1…−14.5 LUFS peak ≤ −0.8 dB ความยาว median 0.88; src/fsb = 006 (222) + 32 = 254
- **เครดิต ElevenLabs 28 ต.ค. (หลัง DJ Shorts + Hugh): เหลือ 3,703/39,823** — รอบนี้ใช้ไป ≈ 36.1k (Felicity/Harrison/Nigel/Ricky/Maggie/DJ Shorts/Hugh = DJ พูดเปล่าครบ 7 คน 254 คลิป); Wanda (≈ 1.3k) ทำได้ถ้าจะใช้ที่เหลือ แต่ควรเก็บ ≈ 2k ไว้แก้คำอ่านที่พบในเกม → ตัดสินใจหลังฟัง 007; โฆษณา/sting/คลิปปนคนอื่น (R3) รอ 26 พ.ย.
- build 254 คลิป sha `0f1d360d…` 103,441,489 ไบต์ decode ผ่านทั้งหมด non-AudioClip identical runtime NOT_TESTED; ติดตั้ง: `restore` ตัวที่ติดตั้งอยู่ → `install --probe radio-thai-007`
- `which` 28 ต.ค. ค่ำ: radio = radio-thai-005, tannoy = **tannoy-thai-007 ติดตั้งแล้ว** (ผลฟังในเกมยังไม่รายงาน); ผู้ใช้กำลัง restore 005 → install 007
- **runtime radio-thai-007 (28 ต.ค. ค่ำ): PASS** — ผู้ใช้: "Perfect" เสียงบรรยายดีมาก ทั้ง 7 DJ ไม่มีคำอ่านเพี้ยนต้องแก้; ข้อสังเกตเดียว: ชื่อ/คำอังกฤษในบทไทยถูกอ่านด้วยสำเนียงเจ้าของภาษา (ไม่ใช่สำเนียงอังกฤษแบบไทย) ฟังไม่ค่อย match แต่รับได้ → ตัวเลือกอนาคต (R3+): แปลงชื่อที่พบบ่อยเป็นคำอ่านไทยใน tannoy-pronounce.json (เช่น Two Point Radio → ทูพอยต์เรดิโอ) แล้ว generate ใหม่เฉพาะคลิปที่มีชื่อเหล่านั้น — ใช้เครดิตมาก รอรอบ 26 พ.ย. และทดลองกับ 2–3 คลิปก่อน

## radio-thai-008 — + Wanda 13 คลิป (28 ต.ค. ดึก) — R2 ครบ 8 DJ
- Wanda (Lily/[gossipy]) Socialite_* 13 คลิป 3,466 ตัวอักษร (รายชื่อ `local/review/radio-thai-008/clips_wanda.txt`); process −14.0…−14.2 LUFS ความยาว median 0.90
- src/fsb = 007 (254) + 13 = 267 → fsbankcl q60 → build 267 คลิป sha `0b8c11b4…` 103,363,582 ไบต์ decode ผ่านทั้งหมด runtime NOT_TESTED
- ติดตั้ง: `restore --probe radio-thai-007` → `install --probe radio-thai-008`
- เครดิตคาดว่าเหลือ ≈ 2.3k (รอผู้ใช้ยืนยัน); ที่เหลือของ bundle = โฆษณา/sting/คลิปปนคนอื่น (R3 หลัง 26 พ.ย.)
- **เครดิต 28 ต.ค. ดึก (หลัง Wanda): ใช้ไป 38,135/39,823 → เหลือ 1,688** (Wanda ใช้จริง 2,015 สำหรับ 3,466 ตัวอักษร ≈ 0.58/ตัวอักษร สูงกว่าคนอื่น — แท็ก [gossipy]/คลิปสั้นอาจมี overhead) ต่ออายุ 26 พ.ย.; radio-thai-008 ติดตั้งแล้ว (which = radio-thai-008) รอผลฟัง Wanda ในเกม

## R4 — Install/Uninstall_Thai_Mod.bat รวมเสียง PA + วิทยุ (28 ต.ค. ดึก, Claude)
- Install: เพิ่ม `TANNOY=tannoy-thai-007` / `RADIO=radio-thai-008` พร้อมรายการรุ่นเก่า (`OLD_TANNOY`, `OLD_RADIO`); ก่อนยืนยัน subroutine `:detect_audio` ตรวจว่าไฟล์เกมเป็น original/รุ่นปัจจุบัน หรือเป็นรุ่นเก่าตัวไหน (ถ้าไม่รู้จัก → หยุดก่อนเปลี่ยนอะไร); ขั้น [6/7] PA และ [7/7] วิทยุ `:install_audio` จะ restore รุ่นเก่าก่อนแล้ว install รุ่นปัจจุบัน; verify ท้ายรวม 2 ชุดเสียง (รวมเป็น 8 bundle + GameAssembly.dll)
- Uninstall: รายการ `AUDIO` ทุกรุ่น radio-thai-001..008 + tannoy-thai-001..007; ตรวจตัวที่ check ผ่านและเป็น "probe" → เก็บใน `AUDIO_INSTALLED` → ขั้น [1/4] restore ก่อน news/logos/translation
- เปลี่ยนรุ่นในอนาคต: แก้ค่า `TANNOY`/`RADIO` และเติมรุ่นเก่าใน `OLD_*` (Install) กับ `AUDIO` (Uninstall) — manage_probe.py ต้องรับชื่อรุ่นใหม่ด้วย
- **ยังไม่ทดสอบบน Windows** → ผู้ใช้ทดสอบรอบ Uninstall → Install (สถานะปัจจุบัน: ทุกชุดติดตั้งอยู่ รวม radio-thai-008 + tannoy-thai-007)
- **ทดสอบ .bat บน Windows 28 ต.ค. (07:12–07:13 UTC): PASS ทั้งรอบ** — Uninstall ตรวจพบ 6 ชุด (รวม radio-thai-008, tannoy-thai-007) คืน original ครบ; Install 7 ขั้น (สำรองเซฟ 49 ไฟล์ → translation → logos → news → PA → radio) verify "probe" ครบ 8 bundle + news "installed"; สถานะเกมตอนนี้ = ทุกชุดติดตั้งอยู่ → R4 ปิด
- **ล้างพื้นที่ 28 ต.ค.**: ลบ local/_to_delete และ radio-thai-001..007 (prototype/backups/review) ≈ 3.5 GB; เหลือ radio-original, radio-thai-008 (src/fsb สะสม 267 + clips_*.txt ทุกคน), radio-eleven-raw, radio-cast-samples; local/ รวม 9.0 GB. หมายเหตุ: Uninstall/Install .bat และ manage_probe ยังอ้างชื่อรุ่นเก่าได้ (ข้ามถ้าไม่มี manifest)
