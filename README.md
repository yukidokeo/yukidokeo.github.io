# 雪解け

˚‧₊· 雪がとけたら、なにになる？·₊‧˚
—— 春になる。

我的个人主页。简介中间横着一条 0 °C 线，跟着鼠标走：线上面在下雪，雪会积在字上；线下面雪化成水滴，草地一丛一丛开花。手机上用手指上下滑。

## 文件

- `index.html`：生成好的页面，直接打开就能看
- `src/thaw.html`：源码
- `assets/avatar.webp`：头像，生成时嵌进页面
- `build.py`：把源码和头像拼成 `index.html`

## 修改

改 `src/thaw.html`，然后运行：

```sh
python3 build.py
```

## 部署（Cloudflare Pages）

- 框架预设：无
- 构建命令：`python3 build.py && mkdir -p dist && cp index.html dist/`
- 构建输出目录：`dist`

## 找我

- X：[@yukidoke_o](https://x.com/yukidoke_o)
- GitHub：[yukidokeo](https://github.com/yukidokeo)
