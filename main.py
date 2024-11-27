from fastapi import FastAPI
import logging
from pydantic import BaseModel
from typing import List, Dict
from fastapi.middleware.cors import CORSMiddleware
# ログの設定
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 全てのオリジンを許可 (必要に応じて特定のオリジンに制限)
    allow_credentials=True,
    allow_methods=["*"],  # 全てのHTTPメソッドを許可
    allow_headers=["*"],  # 全てのHTTPヘッダーを許可
)

# 設問データ
questions = [
    {"id": 1, "question": "どの作業が一番好きですか？", "options": ["コーディング", "テスト", "設計", "ドキュメント作成"]},
    {"id": 2, "question": "チームで一番大切なことは？", "options": ["コミュニケーション", "技術力", "計画性", "柔軟性"]},
    {"id": 3, "question": "新しい技術に対してどう感じますか？", "options": ["ワクワクする", "ちょっと不安", "興味がない", "学びたいけど時間がない"]},
    {"id": 4, "question": "プロジェクトが遅れているとき、何を優先しますか？", "options": ["進捗", "品質", "チームワーク", "予算"]},
    {"id": 5, "question": "好きなツールは？", "options": ["IDE", "タスク管理ツール", "デバッグツール", "CLI"]},
    {"id": 6, "question": "働く環境で重要なのは？", "options": ["自由度", "給料", "安定性", "挑戦的な環境"]},
    {"id": 7, "question": "同僚に求めるものは？", "options": ["協力性", "自主性", "技術力", "柔軟性"]},
    {"id": 8, "question": "納期が近いとき、あなたはどう動きますか？", "options": ["冷静に対処", "スピード重視", "周りをサポート", "徹夜で解決"]}
]

# 診断結果
result_mapping = {
    0: "バックエンドエンジニア",
    1: "フロントエンドエンジニア",
    2: "データベースエンジニア",
    3: "プロジェクトマネージャー"
}

class Answer(BaseModel):
    answers: List[int]

@app.get("/api/questions")
def get_questions():
    return {"questions": questions}

@app.post("/api/submit")
def submit_answers(answer: Answer):
    score = sum(answer.answers) % 4
    result = result_mapping[score]
    return {"result": result}