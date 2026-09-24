"""Re-run the validator and build Pamesa_DawnAndrei_CS0016_M4_AI_REST_API.zip."""
import subprocess, sys, zipfile
from pathlib import Path

here = Path(__file__).parent
work = here / "cs0016-m4-ai-rest-api"
out = subprocess.run([sys.executable, "validate_request_plan.py", "request_plan.json"],
                     cwd=work, capture_output=True, text=True).stdout
(work / "validator_output.txt").write_text(out, encoding="utf-8")
print(out)
shots = sorted((work / "evidence").glob("R*.json"))
if len(shots) < 11:
    print(f"WARNING: only {len(shots)} of 11 evidence files in evidence/")
zip_path = here / "Pamesa_DawnAndrei_CS0016_M4_AI_REST_API.zip"
with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
    for f in sorted(work.rglob("*")):
        if f.is_file() and f.name != ".keep":
            z.write(f, Path(work.name) / f.relative_to(work))
    sheet = "Pamesa_DawnAndrei_CS0016_M4_ActivitySheet.docx"
    z.write(here / sheet, Path(work.name) / sheet)
print("Wrote", zip_path.name)
