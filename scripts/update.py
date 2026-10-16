"""Regenerate the auto-updated parts of the profile README and hero banner.

Pulls every pull request I've opened against other people's repositories
from the GitHub search API, then rewrites the README sections between
`<!-- name starts -->` / `<!-- name ends -->` markers and renders
assets/hero.svg from assets/hero.template.svg.

Stdlib only, so the workflow needs no install step.
"""

import json
import os
import pathlib
import re
import urllib.parse
import urllib.request

USER = "syahra712"
# My own repos and the org my side projects live in aren't "upstream".
EXCLUDE_OWNERS = {USER, "ahnaf-lab"}
REVIEW_ROWS = 12
# A PR title alone doesn't say what kind of system the fix touched. Projects
# not listed here fall back to their first GitHub topic.
AREAS = {
    "docling-project/docling": "document AI · VLMs",
    "BerriAI/litellm": "LLM gateway · billing",
    "sshuttle/sshuttle": "networking · firewalls",
    "tox-dev/tox": "Python test tooling",
    "aboutcode-org/scancode-toolkit": "license compliance",
    "fossasia/voxbento": "web API · access control",
    "pypa/distlib": "Python packaging",
}

ROOT = pathlib.Path(__file__).resolve().parent.parent
TOKEN = os.environ.get("GITHUB_TOKEN", "")


def api(path):
    req = urllib.request.Request("https://api.github.com" + path)
    req.add_header("Accept", "application/vnd.github+json")
    if TOKEN:
        req.add_header("Authorization", f"Bearer {TOKEN}")
    with urllib.request.urlopen(req) as resp:
        return json.load(resp)


def search_prs(qualifiers):
    exclude = " ".join(f"-user:{o}" for o in sorted(EXCLUDE_OWNERS))
    q = f"author:{USER} type:pr {qualifiers} {exclude}"
    items, page = [], 1
    while True:
        data = api(f"/search/issues?q={urllib.parse.quote(q)}&per_page=100&page={page}")
        items += data["items"]
        if len(items) >= data["total_count"] or not data["items"]:
            return items
        page += 1


def repo_of(pr):
    return pr["repository_url"].split("/repos/", 1)[1]


_repos = {}


def repo_info(repo):
    if repo not in _repos:
        _repos[repo] = api(f"/repos/{repo}")
    return _repos[repo]


def stars(repo):
    return repo_info(repo)["stargazers_count"]


def area(repo):
    if repo in AREAS:
        return AREAS[repo]
    topics = repo_info(repo).get("topics") or []
    return topics[0].replace("-", " ") if topics else ""


def short(n):
    if n >= 10_000:
        return f"{n / 1000:.0f}k"
    if n >= 1_000:
        return f"{n / 1000:.1f}k".replace(".0k", "k")
    return str(n)


# "fix(scope): ", "🐛 fix: ", "[FIX] ", "BUG: ", "BF: " -- commit-convention noise
# that reads fine in a changelog and badly in a list of accomplishments.
PREFIX = re.compile(r"^\W*(?:\[\w+\]\s*|(?:fix|feat|bug|bf|docs?|types?|refactor|chore)(?:\([^)]*\))?\s*:\s*)", re.I)


def md_title(title):
    title = PREFIX.sub("", title.strip())
    title = re.sub(r"\s+#\d+$", "", title)  # trailing "#5363" issue refs
    if len(title.split(" ", 1)[0]) > 2:  # leave short identifiers like "pf" alone
        title = title[:1].upper() + title[1:]
    # Titles are maintainers'-repo text; keep them from breaking the table.
    return title.replace("|", "\\|").replace("\n", " ").strip()


def merged_table(merged):
    by_repo = {}
    for pr in merged:
        by_repo.setdefault(repo_of(pr), []).append(pr)
    lines = ["| Project | ⭐ | Area | What I fixed |", "|---|:--:|---|---|"]
    for repo in sorted(by_repo, key=lambda r: (-stars(r), r)):
        prs = sorted(by_repo[repo], key=lambda p: p["closed_at"])
        fixes = "<br/>".join(f"[{md_title(p['title'])}]({p['html_url']})" for p in prs)
        lines.append(
            f"| [**{repo}**](https://github.com/{repo}) | `{short(stars(repo))}` | {area(repo)} | {fixes} |"
        )
    return "\n".join(lines)


def review_section(open_prs):
    repos = {repo_of(p) for p in open_prs}
    # One row per project, its most-starred first, so a busy repo can't crowd out the rest.
    best = {}
    for pr in sorted(open_prs, key=lambda p: p["created_at"], reverse=True):
        best.setdefault(repo_of(pr), pr)
    top = sorted(best.values(), key=lambda p: -stars(repo_of(p)))[:REVIEW_ROWS]
    names = ", ".join(repo_of(p).split("/")[1] for p in top[:7])
    lines = [
        "<details>",
        f"<summary><b>🕐 In review: {len(open_prs)} PRs across {len(repos)} projects</b>, including {names}…</summary>",
        "",
        "<br/>",
        "",
        "| Project | ⭐ | Fix |",
        "|---|:--:|---|",
    ]
    for pr in top:
        repo = repo_of(pr)
        lines.append(f"| [{repo}]({pr['html_url']}) | `{short(stars(repo))}` | {md_title(pr['title'])} |")
    q = urllib.parse.quote(f"is:pr is:open author:{USER} " + " ".join(f"-user:{o}" for o in sorted(EXCLUDE_OWNERS)))
    lines += ["", f"<sub>[See every open PR →](https://github.com/pulls?q={q})</sub>", "", "</details>"]
    return "\n".join(lines)


def latest_line(merged):
    pr = max(merged, key=lambda p: p["closed_at"])
    return f"**Latest merge:** [{md_title(pr['title'])}]({pr['html_url']}) in **{repo_of(pr)}** · {pr['closed_at'][:10]}"


def replace_section(text, name, body):
    pattern = re.compile(rf"(<!-- {name} starts -->\n).*?(<!-- {name} ends -->)", re.S)
    if not pattern.search(text):
        raise SystemExit(f"README is missing the '{name}' markers")
    return pattern.sub(lambda m: m.group(1) + body + "\n" + m.group(2), text)


def main():
    merged = search_prs("is:merged")
    open_prs = search_prs("is:open")
    if not merged:
        # An empty result is far likelier an API hiccup than reality; don't wipe the page.
        raise SystemExit("search returned no merged PRs, refusing to overwrite")

    merged_repos = {repo_of(p) for p in merged}
    counts = {
        "MERGED": str(len(merged)),
        "STARS": short(sum(stars(r) for r in merged_repos)) + "+",
        "OPEN": str(len(open_prs)),
        "PROJECTS": str(len(merged_repos | {repo_of(p) for p in open_prs})),
    }

    readme = ROOT / "README.md"
    text = readme.read_text()
    text = replace_section(text, "latest", latest_line(merged))
    text = replace_section(text, "merged", merged_table(merged))
    text = replace_section(text, "review", review_section(open_prs))
    readme.write_text(text)

    for variant in ("hero", "hero-light"):
        svg = (ROOT / f"assets/{variant}.template.svg").read_text()
        for key, value in counts.items():
            svg = svg.replace("{{" + key + "}}", value)
        (ROOT / f"assets/{variant}.svg").write_text(svg)
    print(counts)


if __name__ == "__main__":
    main()
