"""争议可视化器 - 多角度观点对比分析"""


class DebateView:
    """争议可视化器，多角度观点对比分析工具。"""

    def __init__(self, topic: str):
        """初始化争议可视化器。

        Args:
            topic: 争议主题名称
        """
        self.topic = topic
        self.sides = {}
        self.evidence = []
        self.common_ground = []

    def add_side(self, name: str, stance: str, arguments: list, sources: list = None):
        """添加一方的观点立场及论据。

        Args:
            name: 立场名称，如"支持远程"
            stance: 核心主张描述
            arguments: 论点列表
            sources: 引用来源列表

        Returns:
            返回自身以支持链式调用
        """
        self.sides[name] = {
            "stance": stance,
            "arguments": arguments,
            "sources": sources or [],
        }
        return self

    def add_evidence(self, description: str, source: str = "", supports: str = ""):
        """添加客观证据。

        Args:
            description: 证据描述
            source: 证据来源
            supports: 支持哪一方立场

        Returns:
            返回自身以支持链式调用
        """
        self.evidence.append({
            "description": description,
            "source": source,
            "supports": supports,
        })
        return self

    def add_common_ground(self, point: str):
        """添加各方共识点。

        Args:
            point: 共识点描述

        Returns:
            返回自身以支持链式调用
        """
        self.common_ground.append(point)
        return self

    def visualize(self, fmt: str = "text"):
        """以指定格式输出争议可视化报告。

        Args:
            fmt: 输出格式，当前仅支持"text"

        Returns:
            格式化的争议分析文本
        """
        if fmt == "text":
            lines = [f"# 争议可视化: {self.topic}\n"]
            lines.append("## 各方观点\n")
            for name, data in self.sides.items():
                lines.append(f"### {name}")
                lines.append(f"立场: {data['stance']}\n")
                for i, arg in enumerate(data["arguments"], 1):
                    lines.append(f"{i}. {arg}")
                lines.append("")

            if self.common_ground:
                lines.append("## 共识点\n")
                for i, cg in enumerate(self.common_ground, 1):
                    lines.append(f"✓ {cg}")

            if self.evidence:
                lines.append("\n## 关键证据\n")
                for ev in self.evidence:
                    lines.append(f"- {ev['description']}")
                    if ev["source"]:
                        lines.append(f"  来源: {ev['source']}")

            return "\n".join(lines)
        return str(self.sides)


if __name__ == "__main__":
    dv = DebateView("远程办公 vs 办公室办公")
    dv \
        .add_side("支持远程", "远程办公效率更高",
                  ["通勤时间变为工作时间", "个人空间提升创造力",
                   "员工满意度提高30%"],
                  ["Stanford 2023研究", "Buffer 2024报告"]) \
        .add_side("支持办公室", "面对面协作不可替代",
                  ["即时沟通效率更高", "团队凝聚力更强",
                   "新人培养更快"],
                  ["Microsoft 2023研究"]) \
        .add_common_ground("混合办公是最佳方案") \
        .add_common_ground("工作性质决定办公模式")
    print(dv.visualize())
