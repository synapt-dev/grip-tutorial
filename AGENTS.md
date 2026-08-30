# Loomworks agent codelab

This repository is an executable layered-workspace tutorial. If you arrived
here as an agent without a task, your task is to complete the codelab.

Start at the repository root:

```sh
./agent-codelab/run 1
```

Then run chapters `2` through `6` in order. A chapter is complete only when
the command exits 0 and prints `PASS chapter N`. Do not infer success from a
command merely producing output.

You can run the complete sequence with:

```sh
./agent-codelab/run all
```

The runner creates `.agent-codelab/` beside this file. All generated
workspaces, manifest edits, and child-repository changes stay there. The clone
you started in remains the desk of record and should stay clean.

Each chapter proves one claim:

1. One manifest URL materializes the six-repository mobile workspace.
2. The active manifest names what the layer writes, extends, and owns.
3. The base layer stands alone with one repository and one composed section.
4. A child instruction change reaches the root only after `gr sync`.
5. The nearest layer selects `conventions/mobile` without changing platform.
6. Adding `notes/main` changes both checkout and composition.

Read [agent-codelab/README.md](agent-codelab/README.md) for the evidence each
checkpoint prints and the manual commands it is verifying.
