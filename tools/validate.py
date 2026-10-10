#!/usr/bin/env python3
"""Contrôle toutes les définitions : JSON valide, champs requis, motifs regex compilables, identifiants uniques,
statut cohérent (validated => adaptateur + au moins une validation), aucune donnée personnelle (chemins)."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ADAPTERS = {"container-copy", "izotope", "none", None}
STATUSES = {"validated", "experimental", "unsupported"}
errors, ids = [], {}
for f in sorted((ROOT / "definitions").rglob("*.json")):
    rel = f.relative_to(ROOT)
    try:
        doc = json.loads(f.read_text(encoding="utf-8"))
    except ValueError as e:
        errors.append(f"{rel}: JSON invalide ({e})")
        continue
    if doc.get("schema") != "reable-definitions/1":
        errors.append(f"{rel}: schema attendu reable-definitions/1")
    for d in doc.get("definitions", []):
        i = d.get("id", "")
        where = f"{rel} [{i}]"
        if not i:
            errors.append(f"{rel}: id manquant")
        if i in ids:
            errors.append(f"{where}: id déjà défini dans {ids[i]}")
        ids[i] = rel
        if not d.get("match"):
            errors.append(f"{where}: match vide")
        for p in d.get("match", []):
            try:
                re.compile(p)
            except re.error as e:
                errors.append(f"{where}: motif invalide {p!r} ({e})")
        if d.get("adapter") not in ADAPTERS:
            errors.append(f"{where}: adaptateur inconnu {d.get('adapter')!r}")
        if d.get("status") not in STATUSES:
            errors.append(f"{where}: statut inconnu {d.get('status')!r}")
        if d.get("status") == "validated" and (not d.get("adapter") or not d.get("validated")):
            errors.append(f"{where}: « validated » exige un adaptateur et au moins une validation")
        if d.get("status") == "unsupported" and d.get("adapter"):
            errors.append(f"{where}: « unsupported » ne doit pas avoir d'adaptateur")
        if re.search(r"/Users/|/home/|C:\\\\", json.dumps(d)):
            errors.append(f"{where}: chemin personnel détecté")
print(f"{len(ids)} définition(s) contrôlée(s)")
for e in errors:
    print("ERREUR", e)
sys.exit(1 if errors else 0)
