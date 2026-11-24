# THE WORLD TODAY — Monday 23 November 2026

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/akbare12/news-23-b30-front-page-dense/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/akbare12/news-23-b30-front-page-dense/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

A one-page front page summing up 23 November 2026's world news in a single
1024×1024 image: 31 stories across 6 regions.

**The day's three big stories**

1. **AI rout hits Asia** — Kospi −3.3% closes 4,708.54, sheds 161 pts,
   intraday −5.8%. Samsung −3.1%, SK Hynix −2.5%.
2. **Guterres: regulate AI before it's too late** — Bridgetown summit,
   Barbados; 150 delegates back a risk framework, blueprint not treaty.
3. **US lead over China at record low** — Asia Power Index 2026: US 78.9,
   China 73.6, gap 5.3, narrowest since 2018; India third at 40.5.

Plus 10 more stories, a world map with numbered pins, an 18-item ALSO list,
and a red DATE CHECK box that keeps out stories dated other days
(Democrats reach 258, Sparta II fire, El Chapo Isidro captured,
EU–Indonesia pact, Nigeria boat, ICJ Myanmar ruling).

**How it is built**

- `draw.py` draws the page with PIL and writes `entry.png` (1024×1024,
  under 1 MiB). Scenes are drawn illustrations, not photographs.
- `main.py` is stdlib-only: it validates the PNG header (signature, IHDR
  1024×1024, IEND trailer, ≤1 MiB) and copies `entry.png` to
  `$MAKEFUN_OUTPUT_DIR/entry.png`. It never writes next to itself, so it
  also runs from a read-only copy.

Run it:

```sh
python3 draw.py
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Sources: Reuters · AP · Bloomberg · AFP · Yonhap · BBC · WSJ · NYT · ESPN ·
Lowy Institute (Asia Power Index 2026).

Chips: REPORTED = confirmed by wires · CLAIM = one side's claim, not
independently confirmed · ONGOING = still developing.

## License

MIT — see [LICENSE](LICENSE).
