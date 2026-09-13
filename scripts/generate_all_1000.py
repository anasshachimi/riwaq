#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Riwaq 1,000 Questions Generator
Produces exactly 100 questions for each of the 10 categories.
Total: 1,000 questions in Arabic, English, and French.
"""

import json
import os
import random

random.seed(42)  # Deterministic generation for consistency

def make_item(category_id, q_id, diff, ar_q, en_q, fr_q, ar_opts, en_opts, fr_opts, ans_idx, ar_exp, en_exp, fr_exp):
    # Rotate options so correct answers are distributed among 0, 1, 2, 3
    target_idx = q_id % 4
    if target_idx != ans_idx:
        # Swap options
        ar_opts = list(ar_opts)
        en_opts = list(en_opts)
        fr_opts = list(fr_opts)
        
        ar_opts[ans_idx], ar_opts[target_idx] = ar_opts[target_idx], ar_opts[ans_idx]
        en_opts[ans_idx], en_opts[target_idx] = en_opts[target_idx], en_opts[ans_idx]
        fr_opts[ans_idx], fr_opts[target_idx] = fr_opts[target_idx], fr_opts[ans_idx]
        ans_idx = target_idx
        
    return {
        "id": q_id,
        "categoryId": category_id,
        "difficulty": diff,
        "ar": {
            "question": ar_q,
            "options": ar_opts,
            "correctIndex": ans_idx,
            "explanation": ar_exp
        },
        "en": {
            "question": en_q,
            "options": en_opts,
            "correctIndex": ans_idx,
            "explanation": en_exp
        },
        "fr": {
            "question": fr_q,
            "options": fr_opts,
            "correctIndex": ans_idx,
            "explanation": fr_exp
        }
    }

print("Base generator helper defined.")

def generate_all():
    import sys
    sys.path.append(os.path.dirname(__file__))
    from gen_history import generate_history
    from gen_geography import generate_geography
    from gen_science import generate_science
    from gen_literature import generate_literature
    from gen_heritage import generate_heritage
    from gen_sports import generate_sports
    from gen_technology import generate_technology
    from gen_nature import generate_nature
    from gen_medicine import generate_medicine
    from gen_general import generate_general

    print("Generating questions for all 10 categories...")
    all_questions = []
    all_questions.extend(generate_history(1))
    all_questions.extend(generate_geography(101))
    all_questions.extend(generate_science(201))
    all_questions.extend(generate_literature(301))
    all_questions.extend(generate_heritage(401))
    all_questions.extend(generate_sports(501))
    all_questions.extend(generate_technology(601))
    all_questions.extend(generate_nature(701))
    all_questions.extend(generate_medicine(801))
    all_questions.extend(generate_general(901))

    assert len(all_questions) == 1000, f"Expected 1000 questions, got {len(all_questions)}"
    print(f"Successfully generated all {len(all_questions)} questions!")

    # Output paths
    os.makedirs("public/data", exist_ok=True)
    os.makedirs("src/data", exist_ok=True)

    with open("public/data/questions.json", "w", encoding="utf-8") as f:
        json.dump(all_questions, f, ensure_ascii=False, indent=2)

    with open("src/data/questions.json", "w", encoding="utf-8") as f:
        json.dump(all_questions, f, ensure_ascii=False, indent=2)

    print("Wrote questions.json to public/data/ and src/data/")

if __name__ == "__main__":
    generate_all()

