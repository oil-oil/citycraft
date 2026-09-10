# 可选风格预览

用户尚未选风格且希望比较时，运行 Python 入口生成本地预览。Python 3.10+ 为必需依赖；没有 Python 时直接在对话中列出少量候选，不使用未转义的 sed 替换。只打开预览给用户选择，不自动点击代替用户选择。

```bash
python3 "<Skill绝对目录>/assets/scripts/run_preview.py" \
  --template "<Skill绝对目录>/assets/style-preview-template.html" \
  --output "<任务目录>/style-preview.html" --port 17433 --timeout 300 \
  "LANG=zh" "PRODUCT_NAME=<产品名>" "PRODUCT_HEADLINE=<短标题>"
```

使用宿主提供的结构化命令参数或正确的 shell 引号传递真实输入，不把用户文本当成 shell 代码。结果只来自当前会话的已提交 JSON；超时不是用户选择。

若结果为 `__AI_CHOOSE__`，说明选择理由并继续，不再次要求确认同一决定。布局细选使用 `assets/options-preview-template.html` 和新 output 路径，传入 CITY_NAME 与模板要求的颜色值。先运行 `assets/scripts/get_city_tokens.py <城市名> --json` 读取颜色对象，再以 KEY=VALUE 参数传递；不使用 eval。

Windows 可用 `assets/scripts/run_preview.ps1` 包装同一 Python 入口。结果文件使用随机任务路径；非空输出不会被覆盖。未收到提交时保留页面并提示用户在对话中选择。
