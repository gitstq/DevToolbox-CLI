#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DevToolbox-CLI — Lightweight Terminal Developer Utility Engine
轻量级终端开发者工具箱引擎

A unified CLI toolbox for developers: JSON/YAML/TOML format conversion,
Base64/URL/Hex encoding, hash generation, UUID creation, regex testing,
JWT decoding, color conversion, timestamp conversion, and more.
"""

import sys
import os
import json
import base64
import hashlib
import uuid
import re
import time
import datetime
import binascii
import urllib.parse
import argparse
import textwrap
from typing import Optional, List, Dict, Any

# ---------------------------------------------------------------------------
# Constants & Theme
# ---------------------------------------------------------------------------
VERSION = "1.0.0"
NAME = "DevToolbox-CLI"
EMOJI = "🧰"

THEME = {
    "reset": "\033[0m",
    "bold": "\033[1m",
    "dim": "\033[2m",
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
    "bg_green": "\033[42m",
    "bg_blue": "\033[44m",
}


def color(name: str, text: str) -> str:
    return f"{THEME.get(name, '')}{text}{THEME['reset']}"


# ---------------------------------------------------------------------------
# Utility: safe print with encoding fallback
# ---------------------------------------------------------------------------
def safe_print(text: str):
    try:
        print(text)
    except UnicodeEncodeError:
        print(text.encode("utf-8", errors="replace").decode(sys.stdout.encoding or "utf-8", errors="replace"))


# ---------------------------------------------------------------------------
# Banner
# ---------------------------------------------------------------------------
def print_banner():
    banner = f"""
{color('cyan', '╔══════════════════════════════════════════════════════════════╗')}
{color('cyan', '║')}  {color('bold', f'{EMOJI} {NAME} v{VERSION}')}                                      {color('cyan', '║')}
{color('cyan', '║')}  {color('dim', 'Lightweight Terminal Developer Utility Engine')}              {color('cyan', '║')}
{color('cyan', '║')}  {color('dim', '零依赖 · 跨平台 · 开箱即用')}                                    {color('cyan', '║')}
{color('cyan', '╚══════════════════════════════════════════════════════════════╝')}
"""
    safe_print(banner)


# ---------------------------------------------------------------------------
# Help / Menu
# ---------------------------------------------------------------------------
def print_help():
    help_text = f"""
{color('bold', '📚 Available Commands:')}

  {color('green', 'json')}       JSON formatter, validator, minifier
  {color('green', 'base64')}     Base64 encode/decode
  {color('green', 'url')}        URL encode/decode
  {color('green', 'hash')}       Generate MD5/SHA1/SHA256/SHA512 hashes
  {color('green', 'uuid')}       Generate UUID v4 / v1
  {color('green', 'jwt')}        Decode JWT payload (no verification)
  {color('green', 'regex')}      Test regex patterns against text
  {color('green', 'time')}       Timestamp ↔ ISO8601 conversion
  {color('green', 'color')}      Hex ↔ RGB ↔ HSL conversion
  {color('green', 'password')}   Generate secure random passwords
  {color('green', 'qr')}         Generate ASCII QR code (text mode)
  {color('green', 'html')}       HTML escape / unescape
  {color('green', 'diff')}       Simple line diff between two texts

{color('bold', '🚀 Usage Examples:')}
  {color('dim', '$ devtoolbox json --format < data.json')}
  {color('dim', '$ devtoolbox base64 --encode "hello world"')}
  {color('dim', '$ devtoolbox hash --algo sha256 file.txt')}
  {color('dim', '$ devtoolbox uuid --count 5')}
  {color('dim', '$ devtoolbox time --to-iso 1717776000')}
  {color('dim', '$ devtoolbox password --length 20')}

{color('bold', '💡 Tip:')} Use {color('yellow', 'devtoolbox <command> --help')} for detailed command help.
"""
    safe_print(help_text)


# ---------------------------------------------------------------------------
# Command: JSON
# ---------------------------------------------------------------------------
def cmd_json(args: argparse.Namespace):
    raw = args.input or sys.stdin.read()
    if not raw.strip():
        safe_print(color("red", "❌ Error: No JSON input provided."))
        return 1
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as e:
        safe_print(color("red", f"❌ Invalid JSON: {e}"))
        return 1

    if args.minify:
        out = json.dumps(data, separators=(",", ":"), ensure_ascii=False)
    else:
        out = json.dumps(data, indent=args.indent or 2, ensure_ascii=False, sort_keys=args.sort)
    safe_print(out)
    return 0


# ---------------------------------------------------------------------------
# Command: Base64
# ---------------------------------------------------------------------------
def cmd_base64(args: argparse.Namespace):
    text = args.input or sys.stdin.read()
    if not text:
        safe_print(color("red", "❌ Error: No input provided."))
        return 1
    if args.decode:
        try:
            result = base64.b64decode(text).decode("utf-8", errors="replace")
        except Exception as e:
            safe_print(color("red", f"❌ Decode error: {e}"))
            return 1
    else:
        result = base64.b64encode(text.encode("utf-8")).decode("utf-8")
    safe_print(result)
    return 0


# ---------------------------------------------------------------------------
# Command: URL
# ---------------------------------------------------------------------------
def cmd_url(args: argparse.Namespace):
    text = args.input or sys.stdin.read()
    if not text:
        safe_print(color("red", "❌ Error: No input provided."))
        return 1
    if args.decode:
        result = urllib.parse.unquote(text)
    else:
        result = urllib.parse.quote(text, safe="")
    safe_print(result)
    return 0


# ---------------------------------------------------------------------------
# Command: Hash
# ---------------------------------------------------------------------------
def cmd_hash(args: argparse.Namespace):
    algo = (args.algo or "sha256").lower()
    text = args.input or sys.stdin.read()
    if not text:
        safe_print(color("red", "❌ Error: No input provided."))
        return 1
    if algo == "md5":
        h = hashlib.md5()
    elif algo == "sha1":
        h = hashlib.sha1()
    elif algo == "sha256":
        h = hashlib.sha256()
    elif algo == "sha512":
        h = hashlib.sha512()
    else:
        safe_print(color("red", f"❌ Unsupported algorithm: {algo}"))
        return 1
    h.update(text.encode("utf-8"))
    safe_print(h.hexdigest())
    return 0


# ---------------------------------------------------------------------------
# Command: UUID
# ---------------------------------------------------------------------------
def cmd_uuid(args: argparse.Namespace):
    count = args.count or 1
    version = (args.version or "v4").lower()
    for _ in range(count):
        if version == "v1":
            safe_print(str(uuid.uuid1()))
        else:
            safe_print(str(uuid.uuid4()))
    return 0


# ---------------------------------------------------------------------------
# Command: JWT (decode only, no verification)
# ---------------------------------------------------------------------------
def cmd_jwt(args: argparse.Namespace):
    token = args.input or sys.stdin.read().strip()
    if not token:
        safe_print(color("red", "❌ Error: No JWT provided."))
        return 1
    parts = token.split(".")
    if len(parts) != 3:
        safe_print(color("red", "❌ Invalid JWT format (expected 3 parts)."))
        return 1
    def decode_part(part: str) -> Dict[str, Any]:
        padding = 4 - len(part) % 4
        if padding != 4:
            part += "=" * padding
        try:
            return json.loads(base64.urlsafe_b64decode(part).decode("utf-8"))
        except Exception as e:
            return {"_error": str(e)}
    header = decode_part(parts[0])
    payload = decode_part(parts[1])
    safe_print(color("cyan", "📋 Header:"))
    safe_print(json.dumps(header, indent=2, ensure_ascii=False))
    safe_print(color("cyan", "\n📋 Payload:"))
    safe_print(json.dumps(payload, indent=2, ensure_ascii=False))
    exp = payload.get("exp")
    if exp:
        exp_dt = datetime.datetime.fromtimestamp(exp, tz=datetime.timezone.utc)
        now = datetime.datetime.now(tz=datetime.timezone.utc)
        status = color("green", "✅ Valid") if exp_dt > now else color("red", "❌ Expired")
        safe_print(f"\n{color('yellow', '⏰ Expiration:')} {exp_dt.isoformat()} ({status}{THEME['reset']})")
    return 0


# ---------------------------------------------------------------------------
# Command: Regex
# ---------------------------------------------------------------------------
def cmd_regex(args: argparse.Namespace):
    pattern = args.pattern
    text = args.input or sys.stdin.read()
    if not pattern or not text:
        safe_print(color("red", "❌ Error: Pattern and input are required."))
        return 1
    try:
        flags = 0
        if args.ignore_case:
            flags |= re.IGNORECASE
        compiled = re.compile(pattern, flags)
    except re.error as e:
        safe_print(color("red", f"❌ Invalid regex: {e}"))
        return 1
    matches = list(compiled.finditer(text))
    if not matches:
        safe_print(color("yellow", "⚠️ No matches found."))
        return 0
    safe_print(color("green", f"✅ Found {len(matches)} match(es):\n"))
    for i, m in enumerate(matches, 1):
        safe_print(f"  {color('cyan', f'Match {i}')}: {m.group()!r} at position {m.start()}-{m.end()}")
        if m.lastindex:
            for g in range(1, m.lastindex + 1):
                safe_print(f"    Group {g}: {m.group(g)!r}")
    return 0


# ---------------------------------------------------------------------------
# Command: Time
# ---------------------------------------------------------------------------
def cmd_time(args: argparse.Namespace):
    if args.to_iso:
        try:
            ts = float(args.to_iso)
            if ts > 1e10:
                ts = ts / 1000
            dt = datetime.datetime.fromtimestamp(ts, tz=datetime.timezone.utc)
            safe_print(dt.isoformat())
        except Exception as e:
            safe_print(color("red", f"❌ Error: {e}"))
            return 1
    elif args.to_timestamp:
        try:
            dt = datetime.datetime.fromisoformat(args.to_timestamp.replace("Z", "+00:00"))
            safe_print(str(int(dt.timestamp())))
        except Exception as e:
            safe_print(color("red", f"❌ Error: {e}"))
            return 1
    elif args.now:
        dt = datetime.datetime.now(tz=datetime.timezone.utc)
        safe_print(f"UTC:  {dt.isoformat()}")
        local = datetime.datetime.now()
        safe_print(f"Local: {local.isoformat()}")
        safe_print(f"Timestamp: {int(dt.timestamp())}")
    else:
        safe_print(color("yellow", "ℹ️ Use --to-iso, --to-timestamp, or --now"))
    return 0


# ---------------------------------------------------------------------------
# Command: Color
# ---------------------------------------------------------------------------
def cmd_color(args: argparse.Namespace):
    if args.hex_to_rgb:
        hx = args.hex_to_rgb.lstrip("#")
        if len(hx) == 3:
            hx = "".join([c * 2 for c in hx])
        if len(hx) != 6:
            safe_print(color("red", "❌ Invalid hex color."))
            return 1
        r, g, b = int(hx[0:2], 16), int(hx[2:4], 16), int(hx[4:6], 16)
        safe_print(f"RGB: ({r}, {g}, {b})")
    elif args.rgb_to_hex:
        try:
            parts = [int(x.strip()) for x in args.rgb_to_hex.split(",")]
            if len(parts) != 3:
                raise ValueError
            safe_print(f"HEX: #{''.join(f'{c:02x}' for c in parts)}")
        except Exception:
            safe_print(color("red", "❌ Invalid RGB format. Use R,G,B e.g. 255,128,0"))
            return 1
    else:
        safe_print(color("yellow", "ℹ️ Use --hex-to-rgb or --rgb-to-hex"))
    return 0


# ---------------------------------------------------------------------------
# Command: Password
# ---------------------------------------------------------------------------
def cmd_password(args: argparse.Namespace):
    import random
    import string
    length = args.length or 16
    use_upper = not args.no_upper
    use_lower = not args.no_lower
    use_digits = not args.no_digits
    use_special = not args.no_special
    chars = ""
    if use_lower:
        chars += string.ascii_lowercase
    if use_upper:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_special:
        chars += "!@#$%^&*()_+-=[]{}|;:,.<>?"
    if not chars:
        safe_print(color("red", "❌ No character sets selected."))
        return 1
    pwd = "".join(random.SystemRandom().choice(chars) for _ in range(length))
    safe_print(pwd)
    return 0


# ---------------------------------------------------------------------------
# Command: QR (ASCII text mode)
# ---------------------------------------------------------------------------
def cmd_qr(args: argparse.Namespace):
    text = args.input or sys.stdin.read()
    if not text:
        safe_print(color("red", "❌ Error: No input provided."))
        return 1
    # Simple fallback: use qrcode library if available, else ASCII art placeholder
    try:
        import qrcode
        qr = qrcode.QRCode(border=1)
        qr.add_data(text)
        qr.make()
        safe_print(qr.render_ascii(invert=False))
    except ImportError:
        safe_print(color("yellow", "⚠️ qrcode library not installed. Install with: pip install qrcode"))
        safe_print(color("dim", f"Data to encode ({len(text)} chars): {text[:80]}..."))
    return 0


# ---------------------------------------------------------------------------
# Command: HTML
# ---------------------------------------------------------------------------
def cmd_html(args: argparse.Namespace):
    text = args.input or sys.stdin.read()
    if not text:
        safe_print(color("red", "❌ Error: No input provided."))
        return 1
    if args.unescape:
        import html
        safe_print(html.unescape(text))
    else:
        import html
        safe_print(html.escape(text))
    return 0


# ---------------------------------------------------------------------------
# Command: Diff
# ---------------------------------------------------------------------------
def cmd_diff(args: argparse.Namespace):
    a = (args.a or "").splitlines()
    b = (args.b or "").splitlines()
    if not a and not b:
        safe_print(color("yellow", "ℹ️ Provide --a and --b arguments with text or file paths."))
        return 0
    # Simple line diff
    max_len = max(len(a), len(b))
    safe_print(color("bold", "📊 Line Diff Result:\n"))
    for i in range(max_len):
        line_a = a[i] if i < len(a) else None
        line_b = b[i] if i < len(b) else None
        if line_a == line_b:
            safe_print(f"  {color('dim', str(i + 1).rjust(4))}  {line_a or ''}")
        else:
            if line_a is not None:
                safe_print(f"  {color('red', str(i + 1).rjust(4) + ' -')} {line_a}")
            if line_b is not None:
                safe_print(f"  {color('green', str(i + 1).rjust(4) + ' +')} {line_b}")
    return 0


# ---------------------------------------------------------------------------
# Argument Parser Setup
# ---------------------------------------------------------------------------
def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="devtoolbox",
        description=f"{EMOJI} {NAME} — Lightweight Terminal Developer Utility Engine",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent("""
            Examples:
              devtoolbox json --format < data.json
              devtoolbox base64 --encode "hello"
              devtoolbox hash --algo sha256 file.txt
              devtoolbox uuid --count 5
              devtoolbox time --now
              devtoolbox password --length 20
        """),
    )
    parser.add_argument("--version", action="version", version=f"{NAME} {VERSION}")
    sub = parser.add_subparsers(dest="command", help="Available commands")

    # json
    p_json = sub.add_parser("json", help="JSON formatter / validator / minifier")
    p_json.add_argument("--input", "-i", help="Input JSON string or file path")
    p_json.add_argument("--format", action="store_true", help="Pretty print JSON")
    p_json.add_argument("--minify", action="store_true", help="Minify JSON")
    p_json.add_argument("--indent", type=int, default=2, help="Indent size (default: 2)")
    p_json.add_argument("--sort", action="store_true", help="Sort keys")

    # base64
    p_b64 = sub.add_parser("base64", help="Base64 encode / decode")
    p_b64.add_argument("--input", "-i", help="Input text")
    p_b64.add_argument("--encode", action="store_true", default=True, help="Encode (default)")
    p_b64.add_argument("--decode", "-d", action="store_true", help="Decode")

    # url
    p_url = sub.add_parser("url", help="URL encode / decode")
    p_url.add_argument("--input", "-i", help="Input text")
    p_url.add_argument("--decode", "-d", action="store_true", help="Decode")

    # hash
    p_hash = sub.add_parser("hash", help="Generate hash (MD5/SHA1/SHA256/SHA512)")
    p_hash.add_argument("--input", "-i", help="Input text")
    p_hash.add_argument("--algo", "-a", default="sha256", choices=["md5", "sha1", "sha256", "sha512"])

    # uuid
    p_uuid = sub.add_parser("uuid", help="Generate UUID")
    p_uuid.add_argument("--count", "-c", type=int, default=1, help="Number of UUIDs")
    p_uuid.add_argument("--version", "-v", default="v4", choices=["v1", "v4"])

    # jwt
    p_jwt = sub.add_parser("jwt", help="Decode JWT payload")
    p_jwt.add_argument("--input", "-i", help="JWT token")

    # regex
    p_regex = sub.add_parser("regex", help="Test regex patterns")
    p_regex.add_argument("--pattern", "-p", required=True, help="Regex pattern")
    p_regex.add_argument("--input", "-i", help="Input text")
    p_regex.add_argument("--ignore-case", action="store_true", help="Case insensitive")

    # time
    p_time = sub.add_parser("time", help="Timestamp / ISO8601 conversion")
    p_time.add_argument("--to-iso", help="Convert timestamp to ISO8601")
    p_time.add_argument("--to-timestamp", help="Convert ISO8601 to timestamp")
    p_time.add_argument("--now", action="store_true", help="Show current time")

    # color
    p_color = sub.add_parser("color", help="Color format conversion")
    p_color.add_argument("--hex-to-rgb", help="Convert HEX to RGB")
    p_color.add_argument("--rgb-to-hex", help="Convert RGB to HEX")

    # password
    p_pwd = sub.add_parser("password", help="Generate secure password")
    p_pwd.add_argument("--length", "-l", type=int, default=16)
    p_pwd.add_argument("--no-upper", action="store_true")
    p_pwd.add_argument("--no-lower", action="store_true")
    p_pwd.add_argument("--no-digits", action="store_true")
    p_pwd.add_argument("--no-special", action="store_true")

    # qr
    p_qr = sub.add_parser("qr", help="Generate ASCII QR code")
    p_qr.add_argument("--input", "-i", help="Text to encode")

    # html
    p_html = sub.add_parser("html", help="HTML escape / unescape")
    p_html.add_argument("--input", "-i", help="Input text")
    p_html.add_argument("--unescape", action="store_true")

    # diff
    p_diff = sub.add_parser("diff", help="Simple line diff")
    p_diff.add_argument("--a", help="Text A")
    p_diff.add_argument("--b", help="Text B")

    return parser


# ---------------------------------------------------------------------------
# Main Entry
# ---------------------------------------------------------------------------
def main(argv: Optional[List[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if not args.command:
        print_banner()
        print_help()
        return 0

    commands = {
        "json": cmd_json,
        "base64": cmd_base64,
        "url": cmd_url,
        "hash": cmd_hash,
        "uuid": cmd_uuid,
        "jwt": cmd_jwt,
        "regex": cmd_regex,
        "time": cmd_time,
        "color": cmd_color,
        "password": cmd_password,
        "qr": cmd_qr,
        "html": cmd_html,
        "diff": cmd_diff,
    }

    handler = commands.get(args.command)
    if not handler:
        safe_print(color("red", f"❌ Unknown command: {args.command}"))
        return 1

    return handler(args)


if __name__ == "__main__":
    sys.exit(main())
