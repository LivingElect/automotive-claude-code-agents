# 单一事实来源 — 汽车软件 AI 辅助资源

面向汽车软件工程的 AI 辅助资源仓库，可与 **Claude Code**、**OpenCode** 等工具配合使用。

版本：1.0.2  
最后更新：2026-04-03

---

## 项目统计

### 内容清单

| 类别 | 数量 | 大小 | 路径 |
|------|------|------|------|
| 技能（Skills） | 80 | 约 1,984 KB | skills/ |
| 智能体（Agents） | 22 | 约 330 KB | agents/ |
| 命令（Commands） | 32 | - | commands/ |
| 工作流（Workflows） | 6 | - | workflows/ |
| 规则（Rules） | 10 | - | rules/ |
| 钩子（Hooks） | 17 | - | hooks/ |
| 知识库 | 20+ 篇 | 约 850 KB | knowledge-base/ |
| 交付物文档 | 27 | 约 506 KB | 仓库根目录 *.md |
| 仓库合计 | - | 约 56 MB | - |

### 代码语言占比

| 语言 | 行数（约） | 占比 | 典型用途 |
|------|------------|------|----------|
| C | 8,500 | 34% | 嵌入式 ECU、功能安全 |
| C++ | 7,200 | 29% | ADAS、AUTOSAR、动力总成 |
| Python | 6,800 | 27% | 工具、测试、ML/分析 |
| YAML/ARXML | 1,500 | 6% | AUTOSAR、配置 |
| SQL/JSON | 800 | 3% | 数据、API |
| Bash/Shell | 200 | 1% | 脚本、自动化 |
| **合计** | **25,000+** | **100%** | - |

---

## 领域覆盖

### 十三大领域

| 领域 | 技能数 | 智能体数 | 关键技术 |
|------|--------|----------|----------|
| ADAS / 自动驾驶 | 7 | 2 | 传感器融合、YOLO、卡尔曼、L0–L5 |
| AI-ECU / 边缘 AI | 5 | 2 | NPU、DMS、量化、ONNX |
| 功能安全 | 7 | 2 | ISO 26262、HARA、FMEA、ASIL-D |
| 网络安全 | 6 | 2 | ISO 21434、TARA、PKI、IDS |
| HPC 中央计算 | 5 | 2 | Hypervisor、AUTOSAR Adaptive |
| 区域架构 | 6 | 2 | 车载以太网 TSN、SOME/IP、E/E |
| SDV 平台 | 6 | 2 | OTA、容器、数字孪生 |
| V2X 通信 | 6 | 2 | DSRC、C-V2X、编队 |
| 整车 ECU | 9 | 2 | VCU、VGU、TCU、BCM、IVI、BMS 等 |
| 动力总成 / 底盘 | 7 | 2 | ECM、TCM、ESC、EPS、ABS |
| 诊断 | 8 | 1 | UDS、OBD-II、DoIP、刷写 |
| ML / 分析 | 7 | 2 | 预测、车队、异常检测 |
| 协议 | 1 | - | CAN、LIN、FlexRay、Ethernet |

**合计**：约 80 个技能包（按领域聚合）、22 个智能体（具体数量以仓库为准）。

---

## 标准覆盖

### 安全与网络安全

| 标准 | 版本 | 覆盖说明 | 对应技能路径 |
|------|------|----------|--------------|
| ISO 26262 | 2018 | 全生命周期 | safety/* |
| ISO 21434 | 2021 | 约 95% | cybersecurity/* |
| ISO 21448（SOTIF） | 2019 | 约 90% | adas/*、safety/* |
| UN R155/R156 | 2021 | 约 90% | cybersecurity/* |

### 通信与诊断协议

| 标准 | 覆盖说明 | 技能路径 |
|------|----------|----------|
| ISO 14229（UDS） | 全覆盖 | diagnostics/uds-* |
| ISO 13400（DoIP） | 全覆盖 | diagnostics/doip-* |
| SAE J1979（OBD-II） | 全覆盖 | diagnostics/obd-ii-* |
| SAE J2735（V2X） | 全覆盖 | v2x/v2x-protocols-* |
| IEEE 802.11p（DSRC） | 全覆盖 | v2x/* |
| IEEE 1609.2（安全） | 全覆盖 | v2x/v2x-security-* |

### AUTOSAR

| 平台 | 版本 | 覆盖说明 | 技能路径 |
|------|------|----------|----------|
| Classic | R4.x | 约 85% | vehicle-systems/*、powertrain/* |
| Adaptive | R22-11 | 约 90% | hpc/autosar-adaptive |

---

## 硬件平台

### 中央计算 / HPC

| 平台 | 厂商 | 算力 | 技能路径 |
|------|------|------|----------|
| DRIVE Orin | NVIDIA | 254 TOPS | hpc/vehicle-compute-platforms |
| DRIVE Thor | NVIDIA | 2000 TOPS | hpc/vehicle-compute-platforms |
| Snapdragon Ride | Qualcomm | 700 TOPS | hpc/vehicle-compute-platforms |
| S32G3 | NXP | 16K DMIPS | hpc/vehicle-compute-platforms |

### 边缘 AI / NPU

| 平台 | 厂商 | NPU | 技能路径 |
|------|------|-----|----------|
| i.MX 8M Plus | NXP | 2.3 TOPS | ai-ecu/edge-ai-deployment |
| RZ/V2M | Renesas | 8 TOPS | ai-ecu/neural-processing-units |
| CV5 | Ambarella | 8 TOPS | ai-ecu/neural-processing-units |
| NPU 5000 | Qualcomm | 15 TOPS | ai-ecu/neural-processing-units |

### 区域控制器

| 平台 | 厂商 | 用途 | 技能路径 |
|------|------|------|----------|
| S32K3 | NXP | 区域 ECU | zonal/zone-controller-development |
| RH850 | Renesas | 区域 ECU | zonal/zone-controller-development |
| AURIX TC3xx | Infineon | 功能安全相关 | zonal/zone-controller-development |

---

## 快速导航

### 按角色

| 角色 | 建议路径 |
|------|----------|
| 嵌入式工程师 | skills/automotive-ecu-systems/、skills/automotive-powertrain-chassis/；agents：vehicle-systems-engineer、powertrain-control-engineer |
| ADAS 开发 | skills/automotive-adas/、skills/automotive-ai-ecu/；agents：adas-perception-engineer、edge-ai-engineer |
| 功能安全 | skills/automotive-safety/；agents：safety-engineer、safety-assessor |
| 网络安全 | skills/automotive-cybersecurity/；agents：automotive-security-architect、penetration-tester |
| 系统架构 | skills/automotive-hpc/、automotive-zonal/、automotive-sdv/；agents：hpc-platform-architect、zonal-architect、sdv-platform-engineer |

### 按任务

| 任务 | 建议文档与路径 |
|------|----------------|
| ISO 26262 | FUNCTIONAL_SAFETY_DELIVERABLES.md、skills/automotive-safety/ |
| ISO 21434 | CYBERSECURITY_DELIVERABLES.md、skills/automotive-cybersecurity/ |
| ADAS L2–L5 | ADAS_DELIVERABLES.md、skills/automotive-adas/ |
| 区域架构 | ZONAL_DELIVERABLES.md、skills/automotive-zonal/ |
| OTA | SDV_DELIVERABLES.md、skills/automotive-sdv/ota-update-systems |
| UDS 诊断 | AUTOMOTIVE_DIAGNOSTICS_COMPLETE.md、skills/automotive-diagnostics/uds-iso14229-protocol |

---

## 开发提效（参考）

以下为行业常见对比量级，仅供参考。

| 任务 | 传统周期（约） | 使用本仓库辅助（约） | 时间节省 |
|------|----------------|----------------------|----------|
| ADAS 传感器融合 | 3–4 周 | 3–5 天 | 约 75–85% |
| ISO 26262 HARA | 2–3 周 | 2–3 天 | 约 85–90% |
| UDS 诊断客户端 | 2–3 周 | 1–2 天 | 约 90–95% |
| 区域架构 | 4–6 周 | 1–2 周 | 约 60–75% |
| 边缘 AI 部署 | 2–3 周 | 3–5 天 | 约 70–85% |
| OTA 体系 | 3–4 周 | 约 1 周 | 约 70–75% |

---

## 版本历史

### v1.0.2（2026-04-03）

- 技能 `SKILL.md` 中 **`description` 与正文**改为中文；文档中 OpenCode 使用说明统一为中文表述。

### v1.0.0（2026-03-19）— 初始发布

- 多领域技能、智能体、命令与工作流；知识库与交付物文档；测试与示例代码。
- 标准覆盖：ISO 26262、ISO 21434、AUTOSAR Classic/Adaptive、多种车载协议等。
- 许可：MIT，可商用。

---

## 重要文件

| 文件 | 说明 |
|------|------|
| README.md | 项目概览、安装与快速开始 |
| CLAUDE.md | Claude Code 集成说明 |
| QUICK_START.md | 入门教程 |
| CHANGELOG.md | 变更记录 |
| CONTRIBUTING.md | 贡献指南 |
| SECURITY.md | 安全策略 |
| ROADMAP.md | 路线图 |
| SOURCE_OF_TRUTH.md | 本文件：结构与导航总览 |
| opencode.json | OpenCode 项目配置（技能权限等） |

交付物类 Markdown（根目录，共 27 个左右）：如 ADAS_DELIVERABLES.md、FUNCTIONAL_SAFETY_DELIVERABLES.md、ZONAL_DELIVERABLES.md 等，详见仓库根目录列表。

---

## 关键目录

```
automotive-claude-code-agents/
├── skills/              # 按领域划分的技能素材（YAML 等）
├── agents/              # 智能体定义
├── commands/            # 自动化命令（shell）
├── workflows/           # 工作流（YAML）
├── rules/               # 编码 / 安全规范
├── hooks/               # Git 生命周期钩子
├── knowledge-base/      # 标准与协议参考
├── tools/               # Python 工具与适配
├── examples/            # 示例工程
├── tests/               # 测试
├── docs/                # 文档与教程
└── install.sh           # 安装脚本（Claude 与 OpenCode 技能路径）
```

---

## 安装

```bash
git clone https://github.com/LivingElect/automotive-claude-code-agents.git
cd automotive-claude-code-agents

./install.sh --dry-run   # 仅预览
./install.sh             # 安装到 ~/.claude，并同步 OpenCode 技能目录（见下节）
# 或仅针对某工程：
./install.sh --project /你的工程路径
```

验证与卸载：

```bash
./install.sh --status
./install.sh --uninstall
```

可选：统计技能文件、运行测试：

```bash
find skills/ -name "*.yaml" -not -path "*/_templates/*" | wc -l
pytest tests/ -v
```

---

## OpenCode 使用方法

安装脚本会按 [OpenCode Agent Skills](https://opencode.ai/docs/skills) 生成 **`SKILL.md`**（frontmatter 含 `name`、`description`、`license`、`compatibility`、`metadata`；**`description` 为中文**），并把技能安装到 OpenCode 可扫描的目录。

### 技能安装位置

| 场景 | OpenCode 技能目录 |
|------|-------------------|
| 默认执行 `./install.sh`（未加 `--project`） | `~/.config/opencode/skills/automotive-<领域>/` |
| 执行 `./install.sh --project /path/to/proj` | `/path/to/proj/.opencode/skills/automotive-<领域>/` |

每个目录内有 **`SKILL.md`** 与指向本仓库 `skills/<领域>/` 的 **`content/`** 链接，便于按需读取完整 YAML 库。

### 项目配置

仓库根目录的 **`opencode.json`** 为 `automotive-*` 技能声明加载权限。可选：在本仓库根使用 OpenCode；或将该文件复制到你的业务工程根目录并与现有 OpenCode 配置合并。

### 建议步骤

1. 安装 [OpenCode](https://opencode.ai/docs) 并配置模型与 API（如交互中执行 `/connect`）。  
2. 在本仓库或目标工程执行 **`./install.sh`**（工程场景可加 **`--project`**）。  
3. **`cd` 到含有 `opencode.json` 的目录**，执行 **`opencode`** 启动。  
4. 在对话中通过内置 **`skill`** 工具按名称加载技能（与目录名一致，例如 `automotive-v2x`、`automotive-adas`；以 `~/.config/opencode/skills/` 或项目下 `.opencode/skills/` 中实际文件夹名为准）。  
5. 需要细则时，让智能体读取该技能目录下 **`content/`** 中的 YAML。

### 与 Claude Code 的简要对照

- **Claude Code**：`claude` 命令、`/automotive …` 等，内容在 `~/.claude/`。  
- **OpenCode**：TUI 或 `opencode run` 等，通过 **`skill`** 按名加载；本仓库只提供规范 **`SKILL.md`** 与 **`content/`** 链接。

### 常见问题

- 列表里看不到技能：确认 **`SKILL.md` 全大写**、frontmatter 含 **`name` 与 `description`**、且 **`name` 与父目录名一致**。  
- 无法加载：检查 **`opencode.json`** 里 `permission.skill` 是否允许 `automotive-*`。  
- Windows 下 **`content/`** 链接失败：在开发者模式或管理员权限下用 **Git Bash / WSL** 执行 **`./install.sh`**。

---

## 使用示例（OpenCode）

在已安装技能且当前目录含 **`opencode.json`** 时，可先加载技能再提问，例如：

- 加载 **`automotive-adas`**：请说明「摄像头 + 毫米波雷达融合」的 L2 感知方案要点。  
- 加载 **`automotive-safety`**：请按 ISO 26262 ASIL-D 梳理线控制动 HARA 条目结构。

（具体交互以当前 OpenCode 版本与 **`skill`** 工具为准。若使用 **Claude Code**，可参见 **QUICK_START.md** 中的 `claude "..."` 示例。）

---

## 质量指标（参考）

| 指标 | 数值（约） |
|------|------------|
| 单技能平均字数 | 4,200 |
| 含生产级代码示例的技能占比 | 约 97% |
| 含硬件相关示例的技能占比 | 约 90% |

---

## 社区与支持

- 贡献方式见 **CONTRIBUTING.md**。  
- 许可证：**MIT**（可商用）。  

更完整的面向用户的说明见 **README.md** 与 **README_CN.md**；按领域交付物见根目录各 `*_DELIVERABLES.md` 文件。
