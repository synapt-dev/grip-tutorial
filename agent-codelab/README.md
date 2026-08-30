# Agent-facing layered-workspace codelab

This is the runnable companion to the Loomworks tutorial. It is written for an
agent landing in an unfamiliar gripspace: one command performs each chapter,
then checks the same fruit the human codelab asks a reader to inspect.

Requirements:

- Bash
- `gr` on `PATH`
- `git`
- `python3`
- network access to the public `synapt-dev/grip-tutorial` repository

Run one chapter at a time:

```sh
./agent-codelab/run 1
./agent-codelab/run 2
./agent-codelab/run 3
./agent-codelab/run 4
./agent-codelab/run 5
./agent-codelab/run 6
```

Or run the full sequence:

```sh
./agent-codelab/run all
```

The runner also tests its own output classifier. This matters because some
`gr` operations can return exit 0 while printing an error:

```sh
./agent-codelab/run selftest
```

The default state directory is `.agent-codelab/` at the repository root. To
run a second cold trial without deleting the first one, give the runner a new
path:

```sh
LOOMWORKS_AGENT_LAB_DIR="$(mktemp -d)/loomworks" ./agent-codelab/run all
```

The runner refuses to skip prerequisites. Every successful chapter writes a
small checkpoint marker only after all of that chapter's assertions pass.

## What the commands verify

| Chapter | Action | Fruit required for `PASS` |
|---|---|---|
| 1 | Initialize from the public manifest URL | Six clean child repos, four composed sections, mobile conventions selected |
| 2 | Resolve and read the active manifest | Exactly one top-level `manifest`, `gripspaces`, and `repos` block, with the mobile override present |
| 3 | Clone and initialize `base/main` | One clean `config/main` child, one composed section, no conventions checkout |
| 4 | Change the conventions child and sync | The marker appears exactly once in the composed root and the root still has four sections |
| 5 | Initialize `platform/main` as a control | Mobile uses `conventions/mobile`, platform uses `conventions/main`, base has no conventions repo |
| 6 | Add `notes/main` to checkout and composition | Seven child repos, notes on `notes/main`, one notes contribution in the root, seven child voices total; only the chapter-4 conventions edit remains dirty |

Failures name the missing fruit and exit nonzero. The runner checks both the
process exit and rendered `gr` output before accepting a checkpoint. The
generated workspaces are the subject. This repository clone is only the
launcher and remains unchanged.
