# KAIST MLP Lab project page template

A template for paper project pages. It is plain HTML with Bulma CSS and has no build step.
It is adapted from [Nerfies](https://github.com/nerfies/nerfies.github.io) and licensed under CC BY-SA 4.0.
**Do not remove the template credit in the page footer.**

## How to use

1. Click **Use this template** at the top of the repo to create a new repo.
   - Owner: `kaist-mlplab`
   - Repository name: a short name with lowercase letters and hyphens, e.g. `fooformer`. This becomes the URL: `https://kaist-mlplab.github.io/fooformer/`.
   - Visibility: Public
2. **Edit the content.** Find every `TODO` comment in `index.html` and replace it. Text you need to change is marked `PAPER TITLE`, `REPO-NAME`, and `XXXX.XXXXX`.
   - Images go in `static/images/`: `teaser.png` and `method.png`. Compress them to 1000–1600px wide and put the real pixel size in `width`/`height`.
   - Write a meaningful `alt` for every image.
   - Also state the key numbers from the figures in the captions or body text. AI tools cannot read numbers inside images.
   - Write tables as HTML `<table>`, not as images.
   - Remove buttons you don't need (Code, Demo, Dataset, Model).
   - Check that the JSON-LD is valid at https://validator.schema.org.
   - For a finished example, see `_template/distribution-aware-language-neurons/` in the hub repo.
3. Go to **Settings > Pages**, set Source to `Deploy from a branch` and Branch to `main` / `(root)`, then save.
4. **Register it in the hub.** Add one entry to `_data/projects.yml` in the `kaist-mlplab/kaist-mlplab.github.io` repo. It then appears in the project list and the sitemap automatically.

## Checks

- `curl -s https://kaist-mlplab.github.io/<repo>/ | grep -i abstract`: the body should be visible without JavaScript.
- Put the page URL into https://search.google.com/test/rich-results.

## When the domain changes

Project pages are plain HTML, so the absolute URLs (canonical, og:image, JSON-LD) are written directly in the file.
If the domain changes, replace `https://kaist-mlplab.github.io` in `index.html` all at once.
