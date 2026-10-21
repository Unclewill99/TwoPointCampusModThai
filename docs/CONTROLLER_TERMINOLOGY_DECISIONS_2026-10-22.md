# Controller terminology decisions — 2026-10-22

Scope: contextual editorial direction for the next correction pass. These decisions are NOT yet applied to fresh-translation-003. They supersede conflicting provisional wording for the listed contexts only. All other212 glossary proposals retain pending status; do not treat automatic NON_TERM classification or majority usage as Controller approval. Full human language review and runtime acceptance remain absent.

| Source/context | Decision | Boundaries / evidence |
|---|---|---|
| Janitor, campus staff role | ภารโรง | Includes cleaning and maintenance/mechanics. Evidence UI/Tooltips/JanitorWithMechanics, Code/InspectorItem_TooltipRequiresJanitorMechanics, UI/Tutorial/Decorate. Do not replace generic cleaner/cleaning actions or unrelated dialogue. |
| Teacher, campus teaching role | อาจารย์ | University/campus course instructors, e.g. UI/General/Sims/Teacher and Rooms/Robotics_RoboticsDevelopment_Description_Long. Teacher in a joke, quoted school context, proper name or literal title needs separate judgment. Keep student=นักศึกษา in same campus context. |
| Assistant, staff category | ผู้ช่วย | UI/General/Sims/Assistant and Freshleigh library tutorial need librarian assistance, so never default to ผู้ช่วยสอน; explicit work duties may be explained separately. |
| Room Prestige, room quality stat | ระดับห้อง | UI/Tutorial/Decorate describes decoration/quality, not personal honor. Use ระดับห้อง for stat labels, เพิ่มระดับห้อง in relevant directions; do not replace all prestige references (person/reputation/proper item names need context). |
| Class/class session | คาบเรียน | A teaching session; course=หลักสูตร. Classroom=ห้องเรียน; social class/category/programming uses separate meanings. Avoid bulk replacing strings containing class. |
| Kudosh, currency | Kudosh | Preserve Latin fictional currency spelling consistently in visible currency context, with no invented exchange rate or meaning. |
| DLC titles Space Academy / School Spirits / Medical School | Preserve English title in DLC/store/entitlement/achievement-group title context | Not an assertion of official Thai names. Identically spelled course names may use proposed Thai course title by course ID; do not force DLC title into course prose. Preserve named entities/placeholders. |
| Doom & Gloom, treatable mood/condition | ภาวะหม่นหมอง | Challenge/CM6...SadiusGloomInspection_Tooltip says students suffer and need Pastoral Support. Do not blindly force this medical phrasing into challenge/course/title wordplay; title context remains flagged for source-based decision. |
| Dating, relationship status | คบหาดูใจ | Align UI/Relationships/Dating and Characters/Relationships/Romance_Tier_1. Narrative verbs may be adapted naturally. |
| Good Friends, relationship tier | เพื่อนสนิท | Align two matching status labels; inspect adjacent tiers first. If adjacent tier already uses this wording for a different English status, report collision and retain pending instead of collapsing distinct tiers. |
| Expelled, student status | ถูกไล่ออก | Align UI/Awards/Expelled: and UI/Leaving_Expelled; do not replace staff dismissal descriptions blindly. |
| View Tooltips, UI command | ดูคำอธิบาย | Align UI/General/ViewTooltips and UI/Overview/ViewTooltips. Distinguish advisor hints. |
| Changing Booth, PhoenixPod item | ตู้เปลี่ยนชุด | Match Items/DLC_Space/PhoenixPod_Name and Research/DLC_Space/Unlock_PhoenixPod_Name; it is an item, not a built room. |
| Robo Construction, room | ห้องสร้างหุ่นยนต์ | Match Rooms/Robotics_RoboticsDevelopment_Name and Research/Rooms/Robotics_Name. Source long description explicitly room for Robotics classes/assignments. A verb phrase 'robo construction' outside room context is not automatically a room label. |
| Training, staff training | การฝึกอบรม | Staff skill service. Sports training = การฝึกซ้อม; do not flatten distinct contexts. |
| Gold/Silver, medal or quality tier | ทอง / เงิน | Retain character names, brands, course puns and literal technical identifiers; annotate unclear meanings. |
| Order (customer request) | ออร์เดอร์ | If using a loanword, normalize spelling; prefer คำสั่งซื้อ where it fits. Order as instruction/order/sorting has distinct Thai. |

## Proposals that need further source/context review

Gastronomy and Molecular Gastronomy are distinct course/class names, not inconsistency solely because Thai differs. Proposed ศาสตร์แห่งอาหาร / ศาสตร์อาหารโมเลกุล are usable provisionally by those IDs, not a final whole-corpus replacement. Metalheadedness/Rootheadedness are disease wordplay: preserve current proposed names pending consistency/mapped-object review; do not reinterpret them as ordinary object names. Patisseriser II/III remain Latin machine names until source descriptions/reference IDs resolve them. Ghost=ผี is a base word; classifier ตน depends on sentence. Pastoral Support service versus room must be distinguished before approving ศูนย์... as a universal term.

Approve familiar context-supported basic vocabulary only as bounded direction: Robotics=วิทยาการหุ่นยนต์ (course); Bookcase=ตู้หนังสือ for same item family; Student Lounge=เลานจ์นักศึกษา as room name. Disease18-name proposal is not approved en bloc. Remaining glossary rows, including68 automated NON_TERM classifications, require per-context review if used as decisions.

## Next Claude correction delivery

Use output-merged-review-r1-4 as immutable baseline, not original output or stale UNCERTAIN_ITEMS. Apply the above only to matching contexts and all clearly linked references. First inspect adjacent relationship tiers. Produce NEW review-round5/corrections.json (id,batch,before,after,reason,decision reference), terminology_status.json and summary counts. Supply modified full batch files only under output-review-r5/; retain original IDs/order/fields/tokens/line structure. No global find/replace; no silent deletion of flags. Keep unresolved flags unless actually resolved with evidence. Do not relabel all1473 joke rows as reviewed. Save completed work and report before any runtime assignment.

BUG-THAI-003 ต่ำ and BUG-THAI-002 wrapping are independent renderer work; no Unicode decomposition, ZWSP or word avoidance to hide them. No game/font/UI/save edits, screenshot work, branch/commit/push or external uploads.
