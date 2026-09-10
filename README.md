# citycraft

基于城市风格库制作有明确视觉方向的完整落地页。

完整执行规则见 [SKILL.md](SKILL.md)。

## 配置、依赖与使用边界

基础创作无需账号。可选本地预览需要 Python 3.10+；Windows 包装入口也复用 Python 实现。网页中的字体和 GSAP CDN 会产生外部请求，离线需求应使用本地资源。

复用用户已经选择的产品与风格。预览只在本机提供页面；结果必须来自当前会话提交。模板评价、价格和客户 Logo 不是真实业务证据。

使用示例：

```text
用 citycraft 给我的记账产品做首尔风格落地页，产品名为简账，保留手机优先布局。
```

## GitHub 安装

把 [仓库地址](https://github.com/oil-oil/citycraft) 交给 Agent，要求按 README 安装；也可运行：

```bash
npx skills add oil-oil/citycraft
```

安装后由宿主重新加载 Skill。
