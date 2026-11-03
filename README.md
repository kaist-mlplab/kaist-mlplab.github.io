# KAIST MLP Lab — hub site

Source for the KAIST Multimodal Language Processing Lab website, `https://kaist-mlplab.github.io/`.
GitHub Pages builds it with Jekyll; you don't need GitHub Actions.

## Structure

| Path | Purpose |
|---|---|
| `_config.yml` | Site URL, title, and lab info. **To change the domain, edit only the `url` line.** |
| `_data/projects.yml` | Project list. Add one entry and it shows up in the home cards, `/projects/`, `sitemap.xml`, and `llms.txt`. |
| `index.html` | Home page (includes the `ResearchOrganization` JSON-LD). |
| `projects/index.html` | All projects, grouped by year. |
| `sitemap.xml` | Hand-written sitemap that also lists project pages hosted in other repos (`/<slug>/`). |
| `robots.txt` | Allows every crawler, including AI crawlers. |
| `llms.txt` | Lab and project summary for AI tools. |
| `_template/` | Ignored by Jekyll. `project-page-template/` is the template; `distribution-aware-language-neurons/` is a finished example. |

## Adding a project

1. Create a `kaist-mlplab/<slug>` repo from the `project-page-template` repo and fill in the content.
2. Turn on GitHub Pages in that repo (Settings > Pages > Deploy from branch `main` / root).
3. Add one entry to `_data/projects.yml` in this repo. The `date` field is required.
4. If you have a thumbnail, put it in `assets/img/projects/<slug>.png`.

## Local build

GitHub Pages pins Jekyll 3.9, which needs an extra shim on Ruby 3.2 and later.

```bash
bundle config set --local path vendor/bundle
bundle install
# Ruby 3.2+ only: create the taint shim (needed because liquid 4.0.3 calls tainted?)
printf 'class Object\n def tainted?; false; end\n def taint; self; end\n def untaint; self; end\nend\n' > /tmp/taint_shim.rb
RUBYOPT="-r/tmp/taint_shim.rb" bundle exec jekyll serve
```

Then open http://localhost:4000.
