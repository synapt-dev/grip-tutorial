# Loomworks — the gitgrip layered-workspace tutorial

This repository is a fictional company packed into one repo: four gripspace
layers (base → standards → platform → mobile) and the working repos they
declare, each living as a `<repo>/main` branch. Clone your altitude and the
layers beneath it materialize with it.

Start here: https://synapt.dev/grip/tutorial/

- `main` (this branch) is the mobile altitude — the top of the stack.
- `gr init <this repo> --rev base/main` enters at the bottom instead.
- Working repos (config, conventions, web, api, android, ios, notes) are
  plain branches: code plus a CLAUDE.md their parent layer composes upward.

Requires gitgrip >= 1.1 (cross-layer composition and repo-sourced parts).
