# สำรวจเสียงประกาศ PA (Tannoy) — 26 ตุลาคม 2026 (Claude, อ่านอย่างเดียว)

ผู้ใช้ถามว่าเปลี่ยนเสียงประกาศ PA เป็นภาษาไทยได้ไหม ผลสำรวจไฟล์เกมจริง (ไม่ได้แก้ไฟล์ใด)

## ข้อเท็จจริงที่ตรวจพบ

- เสียงเกมไม่ได้ใช้ Wwise: ทุกอย่างอยู่ใน Unity Addressables bundle ที่ `TPC_Data/StreamingAssets/aa/StandaloneWindows64/` ชุดเสียง: `audio-config`, `audio-cutscenes`, `audio-music`, `audio-sfx`, `audio-radio_assets_{english,german,mandarin}`, `audio-tannoy_assets_{english,german,mandarin}`.
- **PA = `audio-tannoy_assets_english.bundle`** (59.7 MB, sha256 `39d1997b…`): AudioClip 467 คลิป รวม 2,119 วินาที (~35 นาที) ยาวคลิปละ 2.0–8.1 วินาที (เฉลี่ย 4.5) ทุกคลิป 48 kHz stereo, `m_CompressionFormat=1` (Vorbis ใน FSB5), `m_LoadType=2` (streaming) ข้อมูลเสียงอยู่ใน `.resource` ของ CAB เดียวกัน; TextAsset 1 ไฟล์ (`Campus_Tannoy_Session1_Colour_Line_1.srt`) และ AssetBundle container 468 รายการ path `Assets/Data/Audio/Tannoy/English/...`.
- แยกตามหมวดจากชื่อคลิป: Colour 141, RoomColour 51, Janitor 46, Calendar 37, Calling 30, Scripted 24, Issue 23, CourseColour 21, CourseStart 19, Event 17, Weather 15, Attribute 15, ArchetypeColour 10, Visitor 8, Research/Expansion/Marketing 3 ละ, General 1.
- เกมเลือก bundle ตามภาษา; ม็อดไทยใช้ช่องภาษาอังกฤษอยู่แล้ว จึงแทนที่ `audio-tannoy_assets_english.bundle` ได้โดยไม่ต้องแตะ catalog.
- **บทไทยมีอยู่แล้ว**: คลัง 007 มี `I2LS_VO_Tannoy::VO/Tannoy_*` 551 รายการ (คำบรรยายใต้ภาพ) ตรงชื่อคลิป 421/467 คลิป; 46 คลิปที่ไม่มีข้อความคือชุด `Campus_Tannoy_Session1_*` (ประกาศช่วงสอน/ด่านแรก น่าจะใช้ key อื่น ต้องหา); 130 key มีข้อความแต่ไม่มีคลิป (คอร์ส DLC เช่น Alien, Astronaut, GhostBusting — คลิปอยู่ bundle DLC หรือไม่มีเสียง)
- ถอดรหัสคลิปด้วย UnityPy + fmod ได้ (ตัวอย่าง `local/audio/tannoy-survey-001/Campus_Tannoy_Session1_Colour_Line_1.decoded.wav`); รายการคลิปทั้งหมด `local/audio/tannoy-survey-001/clips.json`.

## แนวทางทำ

1. **เสียง**: ต้องการไฟล์เสียงไทย 467 คลิป (ขั้นต่ำสำหรับ probe: 1–3 คลิป) จากคนพากย์หรือ TTS ไทย ใส่เอฟเฟกต์ลำโพง PA (band-pass + reverb) ด้วย ffmpeg ให้เนียนกับต้นฉบับ
2. **บรรจุกลับ**: ทางที่ไม่ต้องใช้ FMOD encoder คือเขียน FSB5 แบบ PCM16 เอง (`m_CompressionFormat=0`) แล้วอัปเดต `m_Length`, `m_Resource.offset/size` ต่อคลิป และสร้าง `.resource` ใหม่ ผ่าน UnityPy แบบเดียวกับ bundle โลโก้; ข้อแลก: ขนาด (PCM stereo 48k ทั้งชุด ≈ 400 MB; mono 24k ≈ 100 MB) หากต้องการเล็กเท่าเดิมต้องใช้ FSB5 Vorbis ซึ่งต้อง FMOD `fsbankcl` (FMOD Studio ดาวน์โหลดฟรีสำหรับใช้ส่วนตัว)
3. **ติดตั้ง**: เพิ่ม probe ใหม่ใน `manage_probe.py` (1 ไฟล์) hash-guarded เหมือนเดิม + เพิ่มใน .bat รวม
4. **ทดสอบ**: probe แรกเปลี่ยน 1–3 คลิปที่ได้ยินง่าย (เช่น `Tannoy_General_01`, Weather, Calendar) ตรวจว่าเกมเล่นคลิปใหม่ ไม่ crash ไม่ตัดกลางคัน คำบรรยายตรงเสียง แล้วค่อยตัดสินใจทั้งชุด

## ยังไม่รู้ / ข้อจำกัด

- รูปแบบ FSB5 ที่เกมรับ (PCM ใช้ได้กับ FMOD ทั่วไป แต่ยังไม่ได้ทดสอบในเกมนี้); ขีดจำกัดความยาวคลิป (ถ้าเสียงไทยยาวกว่าเดิมมาก อาจชนคิวประกาศถัดไป); ชุด Session1 ใช้ข้อความ key ไหน; เสียงวิทยุ (`audio-radio`) เป็นอีกชุดแยก ไม่ได้สำรวจ
