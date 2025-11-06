# 📄 VS Code 导出 Markdown 为 PDF 教程

## 方法1：使用 Markdown PDF 插件（推荐）

### 步骤1：安装插件

1. 打开VS Code
2. 点击左侧的**扩展**图标（或按 `Ctrl+Shift+X`）
3. 在搜索框中输入：`Markdown PDF`
4. 找到 **Markdown PDF** 插件（作者：yzane）
5. 点击**安装**按钮

### 步骤2：导出PDF

1. 在VS Code中打开 `exam_handbook_print.md` 文件
2. 右键点击编辑器区域
3. 选择 **Markdown PDF: Export (pdf)**
4. 等待几秒钟，PDF文件会自动生成在同一目录下

**快捷方式：**
- 也可以按 `Ctrl+Shift+P` 打开命令面板
- 输入 `Markdown PDF`
- 选择 `Markdown PDF: Export (pdf)`

### 步骤3：自定义设置（可选）

如果需要调整PDF样式，可以：

1. 按 `Ctrl+,` 打开设置
2. 搜索 `markdown-pdf`
3. 可以调整的选项：
   - **页边距**：`markdown-pdf.margin`
   - **页眉页脚**：`markdown-pdf.displayHeaderFooter`
   - **纸张大小**：`markdown-pdf.format`（默认A4）
   - **字体大小**：通过CSS自定义

---

## 方法2：使用 Markdown Preview Enhanced 插件

### 步骤1：安装插件

1. 打开VS Code扩展市场
2. 搜索：`Markdown Preview Enhanced`
3. 安装插件（作者：Yiyi Wang）

### 步骤2：导出PDF

1. 打开 `exam_handbook_print.md`
2. 按 `Ctrl+K` 然后按 `V`（或右键选择"打开侧边预览"）
3. 在预览窗口中右键
4. 选择 **Chrome (Puppeteer) -> PDF**
5. PDF会自动生成

**优点：**
- 预览效果更好
- 支持更多导出格式
- 可以自定义CSS样式

---

## 方法3：通过浏览器打印（无需插件）

### 步骤1：预览Markdown

1. 在VS Code中打开 `exam_handbook_print.md`
2. 按 `Ctrl+Shift+V` 打开Markdown预览
3. 在预览窗口右上角点击 **在浏览器中打开**图标

### 步骤2：浏览器打印

1. 在浏览器中按 `Ctrl+P`
2. 选择**目标打印机**为 **另存为PDF**
3. 调整设置：
   - 布局：纵向
   - 页边距：默认或自定义
   - 背景图形：建议勾选
4. 点击**保存**

---

## 方法4：使用在线工具

### 推荐工具

1. **Typora**（本地软件，免费试用）
   - 下载：https://typora.io/
   - 打开Markdown文件
   - 文件 -> 导出 -> PDF

2. **Markdown to PDF**（在线）
   - 网址：https://www.markdowntopdf.com/
   - 上传Markdown文件
   - 点击转换并下载

3. **Dillinger**（在线）
   - 网址：https://dillinger.io/
   - 粘贴Markdown内容
   - 导出为PDF

---

## 推荐配置（针对考场手册）

### Markdown PDF 插件设置

在VS Code设置中添加以下配置（`settings.json`）：

```json
{
  "markdown-pdf.format": "A4",
  "markdown-pdf.margin.top": "2cm",
  "markdown-pdf.margin.bottom": "2cm",
  "markdown-pdf.margin.left": "2cm",
  "markdown-pdf.margin.right": "2cm",
  "markdown-pdf.displayHeaderFooter": true,
  "markdown-pdf.headerTemplate": "<div style='font-size:9px; margin-left:1cm;'><span class='title'></span></div>",
  "markdown-pdf.footerTemplate": "<div style='font-size:9px; margin:0 auto;'><span class='pageNumber'></span> / <span class='totalPages'></span></div>",
  "markdown-pdf.scale": 0.9
}
```

### 自定义CSS样式（可选）

创建一个 `markdown-pdf.css` 文件：

```css
/* 标题样式 */
h1 {
  color: #2c3e50;
  border-bottom: 2px solid #3498db;
  padding-bottom: 10px;
  page-break-before: always;
}

h2 {
  color: #34495e;
  border-bottom: 1px solid #95a5a6;
  padding-bottom: 5px;
}

/* 代码块样式 */
code {
  background-color: #f4f4f4;
  padding: 2px 5px;
  border-radius: 3px;
  font-family: 'Consolas', 'Monaco', monospace;
}

pre {
  background-color: #f8f8f8;
  border: 1px solid #ddd;
  border-radius: 5px;
  padding: 10px;
  overflow-x: auto;
}

/* 表格样式 */
table {
  border-collapse: collapse;
  width: 100%;
  margin: 15px 0;
}

th {
  background-color: #3498db;
  color: white;
  padding: 10px;
  text-align: left;
}

td {
  border: 1px solid #ddd;
  padding: 8px;
}

tr:nth-child(even) {
  background-color: #f2f2f2;
}

/* 页面分隔 */
hr {
  page-break-after: always;
  border: none;
  margin: 0;
}
```

然后在设置中指定CSS文件：

```json
{
  "markdown-pdf.styles": ["d:/python_learn/markdown-pdf.css"]
}
```

---

## 常见问题

### Q1: PDF中中文显示乱码？

**解决方法：**
在 `settings.json` 中添加：

```json
{
  "markdown-pdf.executablePath": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
}
```

### Q2: 表格在PDF中显示不完整？

**解决方法：**
- 减小 `markdown-pdf.scale` 的值（如0.8）
- 或者调整表格内容，使用缩写

### Q3: 代码块被截断？

**解决方法：**
在CSS中添加：

```css
pre code {
  white-space: pre-wrap;
  word-wrap: break-word;
}
```

### Q4: 想要添加页码？

**解决方法：**
已在上面的推荐配置中包含，设置 `displayHeaderFooter` 为 `true`。

---

## 快速操作指南

### 最快速的方法（推荐）

1. **安装 Markdown PDF 插件**
2. **打开 `exam_handbook_print.md`**
3. **右键 -> Markdown PDF: Export (pdf)**
4. **完成！**

PDF文件会自动生成在同一目录下，文件名为 `exam_handbook_print.pdf`。

---

## 打印建议

生成PDF后，打印时建议：

- ✅ **双面打印**：节省纸张
- ✅ **黑白打印**：降低成本（除非需要彩色高亮）
- ✅ **装订**：使用订书机或活页夹
- ✅ **页码**：确保页码清晰可见
- ✅ **测试打印**：先打印1-2页测试效果

---

## 总结

| 方法 | 难度 | 效果 | 推荐度 |
|------|------|------|--------|
| Markdown PDF插件 | ⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Markdown Preview Enhanced | ⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| 浏览器打印 | ⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| 在线工具 | ⭐ | ⭐⭐⭐ | ⭐⭐ |

**最推荐：Markdown PDF 插件** - 简单快速，效果好！

祝你顺利导出PDF，考试加油！🎉