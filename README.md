# Loomworks — the gitgrip layered-workspace tutorial

This repository is a fictional company packed into one repo: four gripspace
layers (base → standards → platform → mobile) and the working repos they
declare, each living as a `<repo>/main` branch. Clone your altitude and the
layers beneath it materialize with it.

Start here: this README walks the whole flow. The guided codelab is live at
[synapt.dev/grip/tutorial](https://synapt.dev/grip/tutorial/).

- `main` (this branch) is the mobile altitude — the top of the stack.
- To enter at the bottom instead, clone the layer branch and init from it:
  `git clone -b base/main <this repo> loomworks-base && gr init ./loomworks-base -p loomworks-ws`
- Working repos (config, conventions, web, api, android, ios, notes) are
  plain branches: code plus a CLAUDE.md their parent layer composes upward.

Requires gitgrip >= 1.1 (cross-layer composition and repo-sourced parts).
