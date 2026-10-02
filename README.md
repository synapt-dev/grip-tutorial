# grip-tutorial

This repository teaches two tools. The gr2 walk comes first. Looking for the gr1 tutorial, the Loomworks layered gripspace? It is the section headed "gr1 second" further down, and its branches and commands are unchanged.

## gr2 first: one feature, two repositories, one review

A tiny shop with two repositories, `demo-core` (prices) and `demo-web` (the quote service). A bulk-discount feature touches both. This walk takes that one feature through `gr2` review: one commit in each repository, bound into a single review, rebuilt in a clean lane from exactly those commits, and tested together. Nothing here is real shop code; the point is the walk.

You need Python 3.11 or newer, `git`, network access (the review lane installs `pytest` into its own virtual environment) and `gr2` 2.0.0a6 or newer, the first release with `gr2 store materialize`:

```sh
uv tool install --pre gitgrip      # or: pip install --pre gitgrip; the command is gr2
```

```sh
git clone https://github.com/synapt-dev/grip-tutorial.git gr2-demo
cd gr2-demo
gr2 store materialize                              # clone the two member repositories
sh feature/apply.sh                                # one commit in each: "bulk discount"
gr2 review bind . --rows-json feature/rows.json    # prints a review id, gr:<40 hex>
gr2 review open . <that id> --lane-dir ../lane --enter
gr2 review run ../lane
gr2 review close ../lane
```

`review open` rebuilds both repositories from the review and checks each tree against what you bound (`tree_match=True` twice). `review run` prints one line per member and one for the lane:

```
demo-core: green: selected=4 passed=4 failed=0 skipped=0 errors=0
demo-web: green: selected=4 passed=4 failed=0 skipped=0 errors=0
lane green: members=2 passed=8 failed=0
order: demo-core, demo-web
```

Your review id depends on your commit times, so it will differ from anyone else's; the counts will not. `review close` removes the lane but keeps the run's receipt and each member's test log in a `lane.review-run/` folder beside it.

The verdict is about the commits you bound, not about whatever is on your disk. If something changes the reviewed files while the run is going, the run refuses and names the member and the path, instead of reading green about a different tree.

The branches: `main` (this one) is the workspace root; `demo-core/main` and `demo-web/main` are the two member repositories, pinned by commit from `main`. The other `<name>/main` branches belong to the gr1 tutorial below.

## gr1 second: the Loomworks layered-gripspace tutorial

The text below is the original gr1 tutorial, unchanged, and still works from this branch.

---

# Loomworks — the gitgrip layered-workspace tutorial

This repository is a fictional company packed into one repo: four gripspace
layers (base → standards → platform → mobile) and the working repos they
declare, each living as a `<repo>/main` branch. Clone your altitude and the
layers beneath it materialize with it.

Start here: this README walks the whole flow. The guided codelab is live at
[synapt.dev/grip/tutorial](https://synapt.dev/grip/tutorial/).

Agents can work through the same fixture as an executable contract. Start with
`./agent-codelab/run 1`, then continue through chapter 6 only when each command
prints `PASS` and exits 0. See [AGENTS.md](AGENTS.md) for the cold-start task.

- `main` (this branch) is the mobile altitude — the top of the stack.
- To enter at the bottom instead, clone the layer branch and init from it:
  `git clone -b base/main <this repo> loomworks-base && gr init ./loomworks-base -p loomworks-ws`
- Working repos (config, conventions, web, api, android, ios, notes) are
  plain branches: code plus a CLAUDE.md their parent layer composes upward.

Requires gitgrip >= 1.1 (cross-layer composition and repo-sourced parts).
