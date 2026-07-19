<p align="center">
  <img src="assets/trump-groove-promo.png" alt="Trump Groove 的得意站姿、点赞、摊手和 Trump Dance" width="100%" />
</p>

<h1 align="center">Trump Groove</h1>

<p align="center">
  <strong>一只拥有丰富表情与魔性律动的 Codex Pet</strong><br/>
  多种动作 · Codex Pet V2 · 六拍 Trump Dance
</p>

<p align="center">
  <a href="README.md">English</a> | 简体中文
</p>

<p align="center">
  <a href="#特色">特色</a> •
  <a href="#安装">安装</a> •
  <a href="#仓库结构">仓库结构</a>
</p>

<p align="center">
  <a href="https://codex-pets.net/#/pets/trump-groove"><strong>在 Codex Pets 查看 Trump Groove →</strong></a>
</p>

---

## 🌟 特别鸣谢

<p align="center">
  <a href="https://linux.do">
    <img src="docs/images/linuxdo.png" alt="LINUX DO" width="420" />
  </a>
</p>
<p align="center"><b>学AI，上L站！祝小破站越来越好～</b></p>

---

## 特色

- **标志性 Trump Dance** — 手工调节双臂折叠舞步，作为活跃的 `running` 动画。
- **丰富的个性表达** — 包含得意站姿、点赞、摊手、评审、等待、成功/失败和方向移动状态。
- **支持 Codex Pet V2** — 使用 `spriteVersionNumber: 2` 和 `1536 × 2288` RGBA WebP 图集。
- **完整动画集合** — 包含九种标准 Codex 状态和十六个顺时针观察方向。
- **适合 Pet 尺寸** — 透明边缘平滑、轮廓紧凑、颜色醒目，在小尺寸下依然清晰。

## 安装

### 方式一：让 Codex 自动安装（推荐）

打开 Codex 并输入：

```text
Install this pet: npx codex-pets add trump-groove
```

Codex 会运行安装程序并自动完成 Trump Groove 的安装。

### 方式二：克隆仓库后让 Codex 安装

克隆此仓库：

```bash
git clone https://github.com/tomczhang/trump-groove-codex-pet.git
cd trump-groove-codex-pet
```

然后在 Codex 中打开克隆后的仓库并输入：

```text
帮我安装这个仓库中的 Trump Groove Pet。
```

使用 SSH 时也可以执行 `git clone git@github.com:tomczhang/trump-groove-codex-pet.git`。

> [!IMPORTANT]
> 安装完成后必须重启 Codex，Trump Groove 才会生效。

## 仓库结构

```text
.
├── README.md                   # 英文说明
├── README.zh-CN.md             # 简体中文说明
├── pet.json                    # Pet 标识和 V2 元数据
├── spritesheet.webp            # 8 × 11 Codex Pet V2 动画图集
├── assets/
│   ├── trump-groove-promo.png  # README 宣传图
│   ├── trump-dance.gif         # running 舞蹈预览源文件
│   └── emotes/                 # 宣传图使用的动作原图
└── scripts/
    └── build_promo.py          # 确定性宣传图合成脚本
```

## 免责声明

这是一个用于娱乐和戏仿的非官方人物漫画 Pet，与 Donald Trump、OpenAI 或 Codex Pets 网站均无关联，也未获得其认可或背书。
