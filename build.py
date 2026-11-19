#!/usr/bin/env python3
"""把 src/ 里的页面拼成能直接打开的单文件：__AVATAR__ 换成内嵌头像，/*@SYNTH*/ 换成 src/synth.js。

src/thaw.html（「0 °C」）输出成 index.html，就是主页；仓库里只有这一页。
本地另外还有样稿（音源、窗和三版目录页），文件在的话顺带一起生成，不进仓库。
"""
import base64
import pathlib

root = pathlib.Path(__file__).parent
avatar = 'data:image/webp;base64,' + base64.b64encode((root / 'assets/avatar.webp').read_bytes()).decode()
synth_js = root / 'src/synth.js'
synth = synth_js.read_text().replace("if (typeof module !== 'undefined') module.exports = SYNTH;", '') if synth_js.exists() else ''

# 源文件 → 输出文件名。thaw.html 也照旧输出一份，给本地三版目录页（drafts.html）链接用
OUT = {'thaw.html': ['index.html', 'thaw.html'], 'index.html': ['drafts.html']}

for src in sorted((root / 'src').glob('*.html')):
    out = src.read_text().replace('__AVATAR__', avatar).replace('/*@SYNTH*/', synth)
    for name in OUT.get(src.name, [src.name]):
        (root / name).write_text(out)
        print('built', name, len(out))
