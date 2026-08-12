# grip-tutorial

One repository hosting several independent git roots — and one workspace
command that drives them all. Ten minutes, nothing installed beyond `gr`.

## What this repo actually is

Four orphan branches, each a root of its own history. Three of them double as
**gripspaces** — fragment sources that compose into your instruction files:

| branch | plays the role of | also a gripspace? |
|---|---|---|
| `main` | the workspace manifest (this branch — the one you clone) | — |
| `standards` | a shared-conventions gripspace another team owns | yes |
| `api` | a backend repo, with its own contributed instructions | yes |
| `web` | a frontend repo, with its own contributed instructions | yes |

Real setups use separate repositories; this tutorial packs them into one so a
single clone gives you the whole world.

## 1. Install gr

```bash
brew tap synapt-dev/tap
brew install synapt-dev/tap/gitgrip
# or, with Rust: cargo install gitgrip
```

## 2. Materialize the workspace

```bash
gr init https://github.com/synapt-dev/grip-tutorial.git
cd grip-tutorial
gr sync
```

`gr status` shows `api/` and `web/`, each checked out on its own branch with
its own history. You did not run git once per repo.

## 3. Work across repos with one command

```bash
gr branch feat/hello
echo "hello" >> api/src/main.py
echo "hello" >> web/index.html
gr status          # both repos: dirty, on feat/hello
gr add . && gr commit -m "feat: hello in both repos"
```

One branch verb, one commit verb, both repos.

## 4. Composition — the part you cannot get elsewhere

The manifest builds files from **fragments owned in different places**. After
`gr sync`, open the three composed files:

- `CLAUDE.md` — the shared `CONVENTIONS.md` (owned on the `standards` branch) +
  this project's local `PROJECT.md`.
- `api/CLAUDE.md` — the same shared conventions + the `api` branch's OWN
  fragment. The api repo's assistant reads team rules and api rules together.
- `web/CLAUDE.md` — shared conventions + the `web` branch's OWN fragment.

None of these three files exists in any branch. `gr` builds each one at sync
from fragments that live, and are versioned, wherever they belong. Change the
shared `CONVENTIONS.md` once and all three pick it up.

The move that makes per-repo composition possible: **the manifest declares the
same repository three times as three gripspaces, at revisions `standards`,
`api`, and `web`.** Each materializes as its own space — `grip-tutorial`,
`grip-tutorial-api`, `grip-tutorial-web` — so a fragment from any branch can be
composed into any file.

> **Requires gitgrip ≥ 1.1.** Multiple gripspaces from one repository at
> different revisions is a 1.1 capability; on 1.0.x the second and third
> collapse into the first. Run `gr --version` if the `api/` and `web` fragments
> do not appear.

## 5. Look at what materialized

```bash
cat CLAUDE.md          # shared conventions + project notes
cat api/CLAUDE.md      # shared conventions + api's own instructions
cat web/CLAUDE.md      # shared conventions + web's own instructions
ls .gitgrip/spaces     # grip-tutorial, grip-tutorial-api, grip-tutorial-web
```

## What to look at next

- `docs/SKILL.md` in the main grip repo — every command family, written for an
  AI assistant to operate `gr` directly.
- The composition & layering page on synapt.dev.
