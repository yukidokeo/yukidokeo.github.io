# 雪解け

˚‧₊· 雪がとけたら、なにになる？·₊‧˚
—— 春になる。

我的个人主页：https://98543653.xyz

简介中间横着一条 0 °C 线，跟着鼠标走：线上面在下雪，雪会积在字上；线下面雪化成水滴，草地一丛一丛开花。手机上用手指上下滑。

## 文件

`public/` 就是整个网站，里面的文件原样上线：

- `public/index.html`：主页，直接改就行
- `public/avatar.webp`：头像
- 想加图片之类的文件，放进 `public/` 就能用 `/文件名` 访问

简介的文字画在 canvas 上，在 `index.html` 里搜 `function lines` 能找到；`<main class="sr">` 里还有一份给读屏软件读的，改的时候两处一起改。

## 本地预览

```sh
python3 -m http.server -d public
```

然后打开 http://localhost:8000 。

## 部署（Cloudflare Workers）

- 构建命令：留空
- 部署命令：`npx wrangler deploy`（按 `wrangler.jsonc` 把 `public/` 原样发上去）

推到 `main` 会自动重新部署。

## 找我

- X：[@yukidoke_o](https://x.com/yukidoke_o)
- GitHub：[yukidokeo](https://github.com/yukidokeo)
