# -*- coding: utf-8 -*-

def make_q(ar_q, en_q, fr_q, ar_opts, en_opts, fr_opts, ans, ar_exp, en_exp, fr_exp, diff="medium"):
    return {
        "difficulty": diff,
        "ar": {
            "question": ar_q,
            "options": ar_opts,
            "correctIndex": ans,
            "explanation": ar_exp
        },
        "en": {
            "question": en_q,
            "options": en_opts,
            "correctIndex": ans,
            "explanation": en_exp
        },
        "fr": {
            "question": fr_q,
            "options": fr_opts,
            "correctIndex": ans,
            "explanation": fr_exp
        }
    }
