import json
import random
from dataclasses import dataclass, asdict
from typing import List

@dataclass
class AssetPrompt:
    category: str
    subject: str
    tags: List[str]
    prompt: str

FACE = ['清冷感东方女性', '阳光少年', '优雅中年男性', '甜美少女', '赛博朋克角色']
POSE = ['正面站姿', '侧身回眸', '坐姿阅读', '行走抓拍', '动态跳跃']
CLOTHING = ['简约白衬衫', '复古旗袍', '机能风外套', '学院风制服', '休闲卫衣']
STYLE = ['写实摄影', '二次元插画', '电影感', '时尚杂志', '水彩手绘']
LIGHT = ['柔和自然光', '棚拍柔光', '黄昏逆光', '冷色调霓虹', '窗边侧光']

def build_prompt(subject: str, clothing: str, pose: str, style: str, light: str) -> str:
    return f'中文AI作图素材：{subject}，穿着{clothing}，{pose}，{style}风格，{light}，高细节，构图干净。'

def generate_asset(category: str) -> AssetPrompt:
    subject = random.choice(FACE)
    clothing = random.choice(CLOTHING)
    pose = random.choice(POSE)
    style = random.choice(STYLE)
    light = random.choice(LIGHT)
    tags = [category, '中文素材', 'AI作图', style]
    prompt = build_prompt(subject, clothing, pose, style, light)
    return AssetPrompt(category, subject, tags, prompt)

def main() -> None:
    categories = ['脸', '姿势', '服装', '综合']
    assets = [generate_asset(random.choice(categories)) for _ in range(5)]
    print(json.dumps([asdict(a) for a in assets], ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
