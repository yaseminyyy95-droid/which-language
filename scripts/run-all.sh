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
base_dir="$repo_root/artifacts/$codex/$problem"

bash "$script_dir/run-benchmark.sh" "$codex" "$problem" "$@"
bash "$script_dir/generate-report.sh" "$codex" "$problem"
bash "$script_dir/generate-figures.sh" "$codex" "$problem"

echo
echo "All artifacts written under: $base_dir"

