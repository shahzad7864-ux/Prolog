"""Execute all practical checks using an installed SWI-Prolog."""
from pathlib import Path
import json, shutil, subprocess, sys
root=Path(__file__).resolve().parent
exe=shutil.which("swipl")
if not exe:
    sys.exit("SWI-Prolog (swipl) was not found. Install it and add its bin directory to PATH.")
failed=0
for case in json.loads((root/"checks.json").read_text()):
    try:
        result=subprocess.run([exe,"-q","-s",str(root/case["folder"]/"solution.pl"),"-g", "("+case["goal"]+")->halt(0);halt(1)"],capture_output=True,text=True,timeout=60)
        ok=result.returncode==0
        print(("PASS " if ok else "FAIL ")+case["folder"])
        if result.stderr: print(result.stderr.strip())
        failed+=not ok
    except subprocess.TimeoutExpired:
        print("TIMEOUT "+case["folder"]); failed+=1
sys.exit(1 if failed else 0)
