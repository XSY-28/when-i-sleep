"""Validate release packaging and the provider-specific instruction boundary."""

from pathlib import Path
import re
from urllib.parse import unquote

import yaml


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills/when-i-sleep"
EXPECTED = {
    "SKILL.md", "agents/openai.yaml", "assets/run-record.md",
    "assets/checkpoint.md", "references/runtime.md",
    "references/codex.md", "references/other-hosts.md",
}


def main():
    files = {str(p.relative_to(SKILL)) for p in SKILL.rglob("*") if p.is_file()}
    assert files == EXPECTED, f"Unexpected or missing runtime files: {files ^ EXPECTED}"
    content = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", content, re.S)
    assert match, "Missing skill frontmatter"
    meta = yaml.safe_load(match.group(1))
    assert meta["name"] == "when-i-sleep"
    assert isinstance(meta["description"], str) and len(meta["description"]) <= 1024
    assert "TODO" not in content and "TBD" not in content

    ui = yaml.safe_load((SKILL / "agents/openai.yaml").read_text(encoding="utf-8"))["interface"]
    assert ui["display_name"] == "When I sleep"
    assert 25 <= len(ui["short_description"]) <= 64
    assert "$when-i-sleep" in ui["default_prompt"]

    account_ops = re.compile(
        r"consume_usage_reset|get_usage_limits|alreadyRedeemed|noCredit|"
        r"reset[ -](?:credit|card)|重置卡", re.I
    )
    for rel in EXPECTED - {"references/codex.md"}:
        text = (SKILL / rel).read_text(encoding="utf-8")
        assert not account_ops.search(text), f"Codex account operation leaked into shared file: {rel}"

    links = 0
    private_path = re.compile(r"/(?:Users|home)/[^\s/]+/")
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.relative_to(ROOT).parts:
            continue
        assert not path.is_symlink(), f"Symlink in release: {path}"
        if path.suffix in {".py", ".md", ".yaml", ".yml", ".txt"} or path.name == "LICENSE":
            text = path.read_text(encoding="utf-8")
            assert not private_path.search(text), f"Private machine path in {path.relative_to(ROOT)}"
            if path.suffix == ".md":
                for link in re.findall(r"\]\(([^)\s]+)\)", text):
                    if "://" in link or link.startswith(("#", "mailto:")):
                        continue
                    local = unquote(link.split("#", 1)[0])
                    target = (path.parent / local).resolve()
                    assert target.is_relative_to(ROOT), f"Link escapes package: {link}"
                    assert target.exists(), f"Broken link in {path.name}: {link}"
                    links += 1
    print(f"Package passed: {len(files)} runtime files; {links} local links; Codex boundary isolated")


if __name__ == "__main__":
    main()
