# 10. Performance - 성능 최적화

> 💡 **핵심:**
> Python은 느릴 수 있지만, 올바른 패턴을 사용하면 충분히 빠릅니다.
> 프로파일링으로 병목을 찾고, 적절한 최적화를 적용하세요.

## 성능 최적화 원칙

```
┌─────────────────────────────────────────────────────────┐
│  Python 성능 최적화 순서                                 │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  1. 먼저 측정하라 (Profile first!)                      │
│  2. 알고리즘/자료구조 최적화                            │
│  3. 내장 함수 활용 (C로 구현됨)                         │
│  4. Comprehension > for loop                            │
│  5. 필요시 Cython, NumPy 활용                           │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

## 📚 예제 목록

| 파일 | 설명 | 난이도 |
|------|------|--------|
| 01_profiling.py | cProfile 사용법 | ⭐⭐ |
| 02_list_vs_generator.py | 메모리 효율 | ⭐⭐ |
| 03_dict_performance.py | dict 최적화 | ⭐⭐ |
| 04_string_concat.py | 문자열 연결 최적화 | ⭐ |

## 🚀 실행 방법

```bash
# 프로파일러 설치 (선택)
pip install line-profiler memory-profiler

# 프로파일링 실행
python -m cProfile -s tottime 01_profiling.py
```

