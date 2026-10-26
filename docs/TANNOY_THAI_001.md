# tannoy-thai-001 — probe เสียงประกาศ PA ภาษาไทย (26 ตุลาคม 2026, Claude)

เป้าหมาย: พิสูจน์ว่าเกมเล่นคลิป PA ที่เราใส่เองได้ (ไม่ใช่คุณภาพเสียง) ก่อนตัดสินใจทำทั้ง 467 คลิป ต่อจาก `TANNOY_AUDIO_SURVEY_001.md`

## สิ่งที่เปลี่ยน

- ไฟล์เดียว: `audio-tannoy_assets_english.bundle` (ต้นฉบับ sha256 `39d1997b…` 59,669,797 ไบต์ → candidate `9c0c44fe…` 60,691,324 ไบต์)
- แทนที่ 4 คลิป (เลือกเพราะเล่นบ่อยและไม่สุ่มข้ามชุด): `Tannoy_Calendar_ClassStart_1/2/3` (ตอนคาบเรียนเริ่ม) และ `Tannoy_Calendar_CampusOpen_1`
- เสียง: TTS ออฟไลน์ (MMS Thai VITS ผ่าน sherpa-onnx บนเครื่อง Claude) จากบทไทยในคลัง 007 ตัด prefix "ระบบเสียงประกาศ:" ออก; โมเดลไม่มีตัว ำ/ๆ จึงป้อนเป็น "ัม" และซ้ำคำ; ใส่เอฟเฟกต์ลำโพง PA ด้วย ffmpeg (band-pass 300–3400 Hz, compressor, echo สั้น, เว้นหัว 0.25 s ท้าย 0.4 s) ออกเป็น 48 kHz stereo 16-bit ต้นทางที่ `local/review/tannoy-thai-001/*.wav` + `lines.json`
- บรรจุ: FSB5 เวอร์ชัน 1 โหมด 2 (PCM16) เขียนเองใน `tools/build_tannoy_thai_001.py` (header 60 ไบต์ คัดลอก flags/hash จาก blob เดิมของคลิปนั้น, sample header 8 ไบต์ ไม่มี chunk, ไม่มี name table); AudioClip ที่แทนที่: `m_CompressionFormat` 1→0, `m_Length` ใหม่; `.resource` สร้างใหม่ทั้งก้อน (จัด 16 ไบต์) จึงต้องอัปเดต offset/size ของ AudioClip ทุกตัวที่อยู่หลังจุดแรก (309 object ต่างกันเพียง 3–4 ไบต์ offset; 4 คลิปที่แทนที่ต่าง 7–11 ไบต์); object ที่ไม่ใช่ AudioClip ทุกตัวเหมือนเดิมไบต์ต่อไบต์; directory flags ของ bundle คงเดิม
- ตรวจสอบออฟไลน์: ถอดรหัส 4 คลิปใหม่กลับผ่าน FMOD (UnityPy samples) ได้ PCM ตรงกับไฟล์ต้นทางทุกไบต์ → FMOD รับ container ที่เราเขียน; คลิปควบคุมที่ไม่แก้ 3 ตัว (General_01, YearStart_1, Weather_Rain_1) ถอดรหัสได้ตรงกับต้นฉบับ → offset ใหม่ถูกต้อง รายงาน `reports/tannoy-thai-001-build.json`

## สถานะ runtime: NOT_TESTED

สิ่งที่ต้องดูเมื่อติดตั้ง: เกมโหลดด่านได้ไม่ crash; เมื่อคาบเรียนเริ่ม ได้ยินเสียงไทย (ไม่ใช่เงียบ/ซ่า/เสียงอังกฤษ); คำบรรยายใต้ภาพตรงกับเสียง; คลิปอื่นที่ไม่แก้ยังเล่นปกติ (ตรวจว่า offset ใหม่ไม่ทำให้คลิปอื่นเพี้ยน); ระดับเสียงเทียบกับประกาศอังกฤษ

## ติดตั้ง / ถอน (ปิดเกมก่อน)

```powershell
python tools/manage_probe.py check --probe tannoy-thai-001
python tools/manage_probe.py install --probe tannoy-thai-001
python tools/manage_probe.py restore --probe tannoy-thai-001
```

อิสระจาก 007 / โลโก้ / ข่าว; .bat รวมยังไม่รวม probe นี้ (จงใจ จนกว่าจะผ่าน runtime)

## ถ้าผ่าน: ทางไปทั้งชุด

- ขนาด: PCM16 48k stereo ทั้ง 467 คลิป ≈ 400 MB; ทางเลือก mono 24 kHz (PA band-limited อยู่แล้ว ไม่เสียคุณภาพ) ≈ 100 MB หรือเข้ารหัส Vorbis ด้วย FMOD fsbankcl ให้เท่าเดิม
- เสียง: ตัดสินใจ TTS (ตัวนี้หรือบริการที่ดีกว่า ซึ่งต้องรันจากเครื่องผู้ใช้เพราะเครือข่ายฝั่ง Claude ถูกบล็อก) หรือคนพากย์; 46 คลิป Session1 ยังไม่มีบทไทยที่ key ตรง

## ผลทดสอบจริงและรุ่นถัดไป (26 ต.ค. ค่ำ)

- **tannoy-thai-001 (4 คลิป)**: ติดตั้งแล้วผู้ใช้ได้ยินแต่อังกฤษ Player.log ไม่มี error → สรุปไม่ได้ว่าไฟล์ถูกใช้หรือไม่ (คลิปที่เลือกอาจไม่ถูกเรียก)
- **tannoy-thai-002 (ทั้ง 467 คลิป, TTS ออฟไลน์; 46 คลิป Session1 ที่ไม่มีบทใส่ "ประกาศทดสอบ หมายเลข N")**: **runtime PASS_SCOPED — ผู้ใช้ได้ยินเสียงไทย** เกมใช้ bundle นี้จริง FSB5 PCM16 ที่เขียนเองเล่นได้ แต่**เสียงเบามาก** (ผู้ใช้ประเมิน ~20 เทียบต้นฉบับ 100) วัดได้: ต้นฉบับ ≈ −14…−16 LUFS, peak −1…−6 dBFS; ของเรา ≈ −30 LUFS, peak −16 dBFS (ต่างราว 15 dB ตรงกับที่ได้ยิน) bundle 210 MB; build จาก original ที่สำรองไว้ `local/backups/tannoy-thai-001/` (ต้องใช้เพราะไฟล์ในเกมขณะ build คือ 001) ผ่าน `tools/build_tannoy_thai_002.py`
- **tannoy-thai-003**: 002 ปรับระดับเสียงทุกคลิปเป็น −15 LUFS (gain +13.4…+19 dB ต่อคลิป) + limiter −1 dBTP ผลวัดหลังปรับ I = −14.8…−15.8 LUFS, peak −1.0…−2.8 dBFS (`local/review/tannoy-thai-003/loudness.json`) build `tools/build_tannoy_thai_003.py` runtime NOT_TESTED
- ลำดับติดตั้งเมื่อมี probe tannoy ตัวอื่นอยู่: `restore --probe <ตัวเดิม>` ก่อนเสมอ แล้ว `install --probe tannoy-thai-003`
- ค้าง: ขนาดไฟล์ (PCM), คุณภาพเสียง TTS, บท 46 คลิป Session1, ระยะเวลาคลิปใหม่เทียบเดิม (สั้นกว่าเฉลี่ย 4.33 vs 4.54 s ไม่พบปัญหา), ยังไม่ใส่ใน .bat รวม

## เสียงธรรมชาติกว่า — ทดลองผู้ให้บริการ (26 ต.ค. ค่ำ)

- **tannoy-thai-003** runtime PASS: ผู้ใช้พอใจระดับเสียง
- **Edge TTS** (`tools/tts_edge_windows.py`, ฟรี, รันบน Windows): th-TH-NiwatNeural ใช้ได้ Premwadee เจอ NoAudioReceived ชั่วคราว; อ่าน ภารโรง เป็น ภา-ระ-โรง → เพิ่มตารางสะกดตามเสียง `local/review/tannoy-pronounce.json` (ภารโรง→พานโรง ใช้กับทุกสคริปต์ TTS เฉพาะเสียง ไม่กระทบคำบรรยาย); ผู้ใช้ว่าน้ำเสียงเรียบไป ไม่ได้โทนผู้ประกาศ
- **ElevenLabs** (`tools/tts_elevenlabs_windows.py`, key ใน `local/secrets/elevenlabs.key` — gitignore; Claude สร้าง key ผ่านเบราว์เซอร์ของผู้ใช้ ชื่อ ThaiCampusMod-tannoy-2 สิทธิ์ TTS/Voices read/Models; key ตัวแรก ThaiCampusMod-tannoy ไม่ได้คัดลอกทัน ควรลบ): บัญชีมีโมเดลไทย eleven_v4, v4_turbo, v3, v3_conversational ทดลอง 3 เสียงด้วย eleven_v4 + แท็ก `[sarcastic]`: Daniel onwK4e9ZLuTAKqWW03F9, Callum N2lVS1w4EtoT3dr4eOWO, George JBFqnCBsd6RMkjVDRZzb → ผู้ใช้ว่าใช้ได้ทั้งสาม **เลือก George**
- **tannoy-thai-004 (รุ่นปัจจุบัน)** = 003 + คลิป `Tannoy_Calling_Janitor_BlockedToilets_1` จาก George (ตัด silence หัว, PA effect, −15 LUFS, 4.9 s) build `tools/build_tannoy_thai_004.py` (ไฟล์ใน `local/review/tannoy-thai-004/` ทับชุด 003) probe sha `550bdd54…` runtime NOT_TESTED; รุ่น 004 ก่อนหน้า (Edge Niwat) ย้ายไป `local/_to_delete/`
- ถัดไปถ้าผ่าน: `--all --voice-id JBFqnCBsd6RMkjVDRZzb --model eleven_v4 --tag "[sarcastic] "` (421 คลิป ≈ 20k ตัวอักษร ตรวจโควตาแพ็กเกจก่อน) แล้วแปลงทั้งชุด + build 005; พิจารณาแท็กต่อคลิปใน `local/review/tannoy-tags.json`; 46 คลิป Session1 ยังไม่มีบท

## tannoy-thai-006 — ชุดเต็มเสียง George (26 ต.ค. ดึก)

- ผู้ใช้เลือก **George** (JBFqnCBsd6RMkjVDRZzb) หลังฟัง 004 (George) และ 005 (Daniel) ในเกม; อัปเกรด ElevenLabs เป็น Starter (30k เครดิต/เดือน) แล้วรัน `--all --model eleven_v4 --tag "[sarcastic] "` ได้ 421 mp3 (ยาว 1.7–7.2 s เฉลี่ย 3.9 s รวม 27 นาที)
- ประมวลผลบน VM: ตัด silence หัว, PA effect, gain ต่อคลิปเป็น −15 LUFS (ผล −15.2…−14.9, peak −4.8…−1.0) → `local/review/tannoy-thai-006/` (+ `loudness.json`)
- build `tools/build_tannoy_thai_006.py`: 421 คลิปทับฐาน 003; 46 คลิป Session1 (ไม่มีบท) ยังเป็น placeholder TTS ออฟไลน์ของ 003; probe sha `04123074…` 211 MB; ตรวจ decode 7 คลิป PASS, non-AudioClip identical; runtime NOT_TESTED
- ลำดับสลับ: restore probe ที่ติดตั้งอยู่ (004/005) → `install --probe tannoy-thai-006`
- ค้าง: บท Session1 46 คลิป (หา key ของข้อความ), คำอ่านเพี้ยนที่พบระหว่างเล่น → เพิ่ม `tannoy-pronounce.json` แล้ว regen เฉพาะคลิป (`--clips … --force`) และ build ใหม่, ขนาดไฟล์ (PCM), ใส่ชุดเสียงใน .bat รวม, เฟสวิทยุ (342 คลิป 2 ชม. ~85k เครดิต หลายตัวละคร มีเพลงประกอบ; `local/audio/tannoy-survey-001/radio_clips.json`)
- **เครดิต ElevenLabs จริง (27 ต.ค. 00:00)**: ใช้ไป 9,103 / 39,823 (Starter ต่ออายุ 26 พ.ย.) → ชุด 421 คลิป ≈ 8,900 เครดิต ≈ 21 เครดิต/คลิป ≈ 0.45 เครดิต/ตัวอักษร (ถูกกว่าที่ประเมิน 1/ตัวอักษร ราว 2.5 เท่า) เหลือ 30,720; ประเมินเฟสวิทยุใหม่ ≈ 36–40k เครดิต (ทำได้ ~80% ในรอบนี้ ที่เหลือรอบหน้า หรือ Creator)
