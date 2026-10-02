#!/bin/sh
# Apply the bulk-discount feature as one local commit in each member, then write the rows file that
# `gr2 review bind` reads: one row per member, base = the live remote head, head = your new commit.
set -eu
cd "$(dirname "$0")/.."
ROOT=$(pwd)
rows=""
for pair in "demo-core:core:demo-core/main" "demo-web:web:demo-web/main"; do
  m=${pair%%:*}; rest=${pair#*:}; p=${rest%%:*}; branch=${rest#*:}
  git -C "$m" apply "$ROOT/feature/$p.patch"
  git -C "$m" add -A
  git -C "$m" -c user.name=demo -c user.email=demo@example.com commit -q -m "$m: bulk discount"
  base=$(git -C "$m" rev-parse "origin/$branch")
  head=$(git -C "$m" rev-parse HEAD)
  remote=$(git -C "$m" remote get-url origin)
  rows="$rows{\"key\":\"$m\",\"remote\":\"$remote\",\"base\":\"$base\",\"head\":\"$head\",\"path\":\"$m\",\"ref\":\"refs/heads/$branch\",\"source\":\"$ROOT/$m\"},"
done
printf '[%s]\n' "${rows%,}" > "$ROOT/feature/rows.json"
echo "applied the feature in demo-core and demo-web; rows written to feature/rows.json"
