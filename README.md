# reable-library

Base de **définitions de plugins** pour [ReAble](https://github.com/flapflap/ReAble) : pour chaque plugin (ou famille), comment son état
est rangé dans un set Ableton Live et s'il peut être converti d'un format ou d'une version à l'autre (AU/VST2 → VST3,
Ozone 9 → 10…). Le code de ReAble est dans un autre dépôt ; ce dépôt ne contient que des données (JSON).

## Contenu
- `definitions/<éditeur>/<plugin>.json` : une définition par plugin ou famille (voir `schema/definition.schema.json`).
- `reports/` : résultats de tests envoyés par les bêta-testeurs (JSON anonymes, voir `CONTRIBUTING.md`).
- `tools/validate.py` : contrôle le format de toutes les définitions (lancé aussi en intégration continue).

## Statuts
| Statut | Signification | Comportement par défaut dans ReAble |
|---|---|---|
| `validated` | testé dans Live par les mainteneurs (ou confirmé par plusieurs bêta-testeurs) | converti |
| `experimental` | adaptateur écrit, pas encore validé | **bloqué** (à activer explicitement) |
| `unsupported` | aucun adaptateur : détection et fiche de recréation seulement | non converti |

## Utiliser ce dépôt avec ReAble
```bash
reable plugins config --repo-url <url de ce dépôt>
reable plugins sync        # clone ou met à jour la copie locale
reable plugins list
```
Vos propres définitions restent **locales** (`~/Library/Application Support/ReAble/definitions/`) tant que
vous ne les envoyez pas ici.

## Licence
Les définitions (données) sont publiées sous **[CC BY 4.0](LICENSE-DATA.md)** : réutilisables, y compris commercialement, avec mention de l'auteur. Les noms de plugins et d'éditeurs appartiennent à leurs propriétaires ; ce dépôt n'est affilié à aucun d'eux. Ableton et Ableton Live sont des marques d'Ableton AG.
Les contributions (définitions, résultats bêta) sont acceptées sous la même licence.
