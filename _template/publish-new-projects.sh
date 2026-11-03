#!/bin/bash
# _template/<slug>/ 중 아직 GitHub 레포가 없는 프로젝트 페이지를
# kaist-mlplab/<slug> 공개 레포로 만들고 GitHub Pages를 켠다.
# 사용: bash _template/publish-new-projects.sh   (허브 레포 루트에서 실행, gh 로그인 필요)
set -u
cd "$(dirname "$0")/.."
WORK=$(mktemp -d)
for dir in _template/*/; do
  slug=$(basename "$dir")
  [ "$slug" = "project-page-template" ] && continue
  [ -f "$dir/index.html" ] || continue
  if gh repo view "kaist-mlplab/$slug" --json name >/dev/null 2>&1; then continue; fi
  title=$(sed -n 's:.*<title>\(.*\)</title>.*:\1:p' "$dir/index.html" | head -1)
  R="$WORK/$slug"; mkdir -p "$R"; cp -R "$dir". "$R/"; touch "$R/.nojekyll"
  printf '# %s\n\nProject page: https://kaist-mlplab.github.io/%s/\n\nStatic HTML + Bulma, no build step. Adapted from the [Nerfies](https://github.com/nerfies/nerfies.github.io) template (CC BY-SA 4.0). Listed on the [KAIST MLP Lab](https://kaist-mlplab.github.io/) hub.\n' "$title" "$slug" > "$R/README.md"
  desc="Project page: $title"; desc=${desc:0:340}
  if (cd "$R" && git init -q -b main && git add -A && git commit -q -m "Project page for $title" \
      && gh repo create "kaist-mlplab/$slug" --public --description "$desc" \
           --homepage "https://kaist-mlplab.github.io/$slug/" --source . --push >/dev/null \
      && gh api -X POST "repos/kaist-mlplab/$slug/pages" -f "source[branch]=main" -f "source[path]=/" >/dev/null); then
    echo "ok     $slug"
  else
    echo "FAILED $slug"
  fi
done
rm -rf "$WORK"
