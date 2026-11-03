# HorizonLogic

**A Benchmark for Long-Horizon Robot Reasoning**

A research website for 40 manipulation tasks across five reasoning families: conditional dependencies, memory, branching, resource allocation and ordering. The collection covers single-arm and dual-arm robots.

The site includes task search and filters, instructions and controller contracts, recorded simulation previews, links to the dual-arm review recordings, and a separate overview of LeRobot training-data availability.

## Website

[Open HorizonLogic](https://yutaod-crypto.github.io/horizonlogic/)

Published with GitHub Pages from the `dist/` directory. The Pages deployment workflow runs on changes to `dist/` on `main`, and can also be started manually in the Actions tab.

## Local preview

```bash
python3 -m http.server 8788 --bind 127.0.0.1 --directory dist
```

Open http://127.0.0.1:8788. No npm installation or build step is required. All website assets use relative paths and work under a GitHub Pages project URL.

## Editing

- `dist/index.html`: page content and structure.
- `dist/styles.css`: responsive layout and styling.
- `dist/app.js`: search, category/embodiment filters, dialogs and preview controls.
- `dist/catalog.json`: task descriptions, release inventory and recording links.
- `dist/catalog.js`: the same catalog assigned to `window.BENCHMARK`; keep it synchronized with `catalog.json`.
- `dist/assets/`: the project's simulation images, original SVG mark and legacy preview assets.

Run `python3 validate_site.py` after editing. Dataset inventory is a dated snapshot, not a live mirror.

## Task records and training data

The [Drive archive](https://drive.google.com/drive/folders/187xmzTLwyRDAonEgDWIq0Jn323kA4czJ) tracks task recordings and development history. Each of its 20 dual-arm task manifests lists 50 trajectories; five selected review videos per task are linked from the website. These combined-camera recordings are separate from full training camera streams.

The [LeRobot dataset repository](https://github.com/yutaod-crypto/robodataSim-data) is private and requires authorized access. As checked on 3 November 2026, it contains 50 episodes for each of the four Category 1 tasks in each embodiment, plus one episode for each of the other 16 dual-arm tasks: 416 published episodes total. The 20 canonical single-arm exports contain 1,000 episodes locally; publication availability is indicated separately.

The active single-arm previews are native saved-state renders: a 960 × 720 main camera and an optional 1920 × 720 combined view with two 480 × 360 wrist cameras. They play at 20 fps and normal speed, matching the dual-arm review view sizes. The 40 MP4s are hosted in the [native-resolution review release](https://github.com/yutaod-crypto/horizonlogic/releases/tag/review-v2-20261103); the catalog points to those assets. Canonical training streams remain 480 × 360.

Website previews are presentation derivatives, not training videos. Technical validation, human review and learned-policy performance are separate claims. No policy leaderboard or held-out evaluation result is implied.

## Design references

The presentation was informed by [LIBERO](https://libero-project.github.io/main.html), [RoboCasa](https://robocasa.ai/) and [BEHAVIOR](https://behavior.stanford.edu/). Website styling and the SVG mark are original; simulation media come from the benchmark project. No external benchmark images or copy are reused.
