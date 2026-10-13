#!/usr/bin/env python3
"""Author-only reproducible student ZIP builder; standard library, no private answers."""
from pathlib import Path
import argparse,hashlib,zipfile,tempfile
ROOT=Path(__file__).resolve().parents[1]
EVIDENCE=ROOT/"evidence"
ARCHIVE=ROOT/"downloads/CENTINELL-The-Silent-Payload-STUDENT.zip"
ROOTS=("evidence","docs","BUSINESS_APPLICATIONS","tools")
EXTRA=("README.md",)
BLOCK=("answer_key","instructor","solution","walkthrough","private")
def sources():
    files={}
    for name in EXTRA:files[name]=(ROOT/name).read_bytes()
    for folder in ROOTS:
        for p in (ROOT/folder).rglob("*"):
            if p.is_file() and "__pycache__" not in p.parts and p.suffix not in (".pyc",".bak",".tmp"):
                rel=p.relative_to(ROOT).as_posix()
                if any(flag in rel.lower() for flag in BLOCK):
                    raise ValueError("Private or solution path excluded: "+rel)
                files[rel]=p.read_bytes()
    return dict(sorted(files.items()))
def render_manifest():
    lines=["# SHA-256 of synthetic, student-safe incident artifacts — not acquisition proof"]
    for p in sorted(EVIDENCE.rglob("*")):
        if p.is_file() and p.name!="MANIFEST.sha256":
            lines.append(f"{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.relative_to(ROOT).as_posix()}")
    return ("\n".join(lines)+"\n").encode("utf-8")
def validate(files):
    assert ARCHIVE.is_file(),"Missing student ZIP"
    with zipfile.ZipFile(ARCHIVE) as z:
        names=z.namelist()
        assert len(set(names))==len(names) and set(names)==set(files)
        assert z.testzip() is None
        for path,payload in files.items():
            assert z.read(path)==payload, "Packaged file inconsistent: "+path
    print(f"PASS: student archive ({len(files)} files) CRC and byte parity; no instructor keys")
def main():
    a=argparse.ArgumentParser()
    t=a.add_mutually_exclusive_group(required=True)
    t.add_argument("--write",action="store_true");t.add_argument("--check",action="store_true")
    args=a.parse_args()
    calculated=render_manifest()
    path=EVIDENCE/"MANIFEST.sha256"
    if args.check:
        assert path.read_bytes()==calculated,"Manifest stale or source evidence modified"
        validate(sources())
    else:
        path.write_bytes(calculated)
        files=sources()
        ARCHIVE.parent.mkdir(parents=True,exist_ok=True)
        with tempfile.NamedTemporaryFile(dir=ARCHIVE.parent,suffix=".zip",delete=False) as temp:
            target=Path(temp.name)
        try:
            with zipfile.ZipFile(target,"w",compression=zipfile.ZIP_DEFLATED,compresslevel=7) as z:
                for name,payload in files.items():
                    info=zipfile.ZipInfo(name,date_time=(2026,9,22,0,0,0))
                    info.compress_type=zipfile.ZIP_DEFLATED
                    info.external_attr=0o644<<16
                    z.writestr(info,payload)
            target.replace(ARCHIVE);validate(files)
        finally:target.unlink(missing_ok=True)
if __name__=="__main__":main()
