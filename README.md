# grip-tutorial

One repository hosting several independent git roots — and one workspace
command that drives them all. Ten minutes, nothing installed beyond `gr`.

## What this repo actually is

Four orphan branches, each a root of its own history:

| branch | plays the role of |
|---|---|
| `main` | the workspace manifest (this branch — the one you clone) |
| `standards` | a shared-conventions gripspace another team owns |
| `api` | a backend repo |
| `web` | a frontend repo |

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
cd workspace
gr sync
```

`gr status` now shows `api/` and `web/`, each checked out on its own branch
with its own history. You did not run git once per repo.

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

The manifest declares that `CLAUDE.md` is BUILT from two fragments: shared
`CONVENTIONS.md` owned on the `standards` branch, then local `PROJECT.md`.
Change the shared fragment once; every workspace that composes it picks the
change up on next `gr sync`.

Try it: after `gr sync`, open `CLAUDE.md` — it is the two fragments joined,
built for you. This works today on gitgrip 1.0.2.

> ⚠ **One known limitation, honestly stated:** `gr sync` does not yet refresh
> the shared-fragment clone, so an UPSTREAM edit to `CONVENTIONS.md` will not
> flow into your workspace until the fix ships (in review). Workaround, if you
> want to see propagation now:
>
> ```bash
> git -C .gitgrip/spaces/grip-tutorial pull origin standards
> gr sync    # CLAUDE.md now carries the upstream change
> ```
>
> Initial composition needs no workaround; only the update loop does. And note
> the manifest nests `composefile` under `manifest:` — placed at top level it
> is silently ignored on current releases.

## What to look at next

- `docs/SKILL.md` in the main grip repo — every command family, written for
  an AI assistant to operate `gr` directly.
- The composition & layering page on synapt.dev.
