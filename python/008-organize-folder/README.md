# 008 — ترتيب أي فولدر | Organize any folder

سكريبت Python بيرتّب أي فولدر تشغّله عليه: كل نوع ملفات بيروح فولدر لوحده.

| النوع | الامتدادات |
|---|---|
| Images | .jpg .jpeg .png .gif .webp |
| Videos | .mp4 .mov .mkv .avi |
| Audio | .mp3 .wav .m4a |
| PDF | .pdf |
| Documents | .doc .docx .txt .xlsx .pptx |
| Archives | .zip .rar .7z |
| Other | أي حاجة تانية |

**الحلقة:** «تتعلم برمجة من الصفر إزاي في 2026؟» — [رابط الحلقة]

## إزاي تشغّله

1. سطّب Python من الموقع الرسمي: https://www.python.org/downloads/
2. افتح **IDLE** (بيتسطّب مع Python).
3. File ← Open، وافتح `organize.py`.
4. دوس **F5**.
5. اكتب مسار الفولدر واضغط Enter. مثال: `C:\Users\you\Downloads`

## أمان

- السكريبت **بينقل بس، مش بيمسح** أي ملف.
- لو فيه ملف بنفس الاسم في الفولدر اللي رايح له، بيسيبه مكانه ويكتب «Skipped».
- مش بيلمس الفولدرات اللي جوه الفولدر.
- **أول مرة، جرّبه على نسخة من الفولدر.**

## اتعلم الأفكار اللي فيه

السكريبت مبني على 4 أفكار: `input`، و`for`، و`if`، ومكتبة `shutil` اللي بتنقل الملفات. لو عايز تتعلمهم:

- CS50P من Harvard: https://cs50.harvard.edu/python/
- Automate the Boring Stuff with Python، الفصل 11 «Organizing Files»: https://automatetheboringstuff.com
- كورس Python بالعربي من Elzero: https://www.youtube.com/playlist?list=PLDoPjvoNmBAyE_gei5d18qkfIe-Z8mocs
