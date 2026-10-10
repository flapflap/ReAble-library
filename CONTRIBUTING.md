# Contribuer

## 1. Tester un plugin dans Live (utilisateur)
1. `reable probe <dossier de sets>` : repère les plugins et leur type de conteneur d'état.
2. `reable plugins add <id> --match "<regex>" --adapter container-copy` (adaptateurs : `container-copy`, `izotope`, `none`).
3. Générez un pack de test (`reable convert … --state-mode transfer|header|none`), ouvrez les sets dans Live.
4. Enregistrez le résultat : `reable plugins validate <id> --result ok|ko --variant transfer --live 12.4`.

La définition devient « validée » **pour vous seulement**. Rien n'est envoyé sans votre action.

## 2. Partager (optionnel)
- **Programme bêta, anonyme** : `reable plugins export --beta --out resultat.json`. Le fichier ne contient ni chemin,
  ni nom de set ou de piste, ni donnée musicale : uniquement plugin, adaptateur, variante, résultat, versions de Live, macOS
  et ReAble, plus un pseudonyme aléatoire. Relisez-le, puis ouvrez une *issue* « Résultat bêta » ou une PR dans `reports/`.
- **Définition complète** : `reable plugins export --out definition.json` puis PR vers `definitions/<éditeur>/`.

## 3. Règles de promotion (mainteneurs)
- `experimental` → `validated` : au moins **un test des mainteneurs** dans Live (version indiquée) **ou deux bêta-testeurs
  indépendants** (pseudonymes différents) sur la même variante et des versions de Live proches.
- Un échec reproduit repasse la définition en `experimental` et ajoute une note.
- Chaque validation garde sa provenance (`live`, `date`, `variant`, `by`).
- Aucune définition ne doit contenir de chemin personnel, de nom de projet ou de donnée d'identification.
