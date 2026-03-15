#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 2 ]]; then
  echo "Usage: $0 <codex> <problem> [benchmark args...]" >&2
  exit 1
fi

codex="$1"
problem="$2"
shift 2

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(cd "$script_dir/.." && pwd)"
output_root="$repo_root/artifacts/$codex/$problem"

mkdir -p "$output_root"

echo "==> Running benchmark"
echo "    codex: $codex"
echo "    problem: $problem"
echo "    output: $output_root"

exec ruby "$repo_root/benchmark.rb" \
  --codex "$codex" \
  --problem "$problem" \
  --output-root "$output_root" \
  "$@"

