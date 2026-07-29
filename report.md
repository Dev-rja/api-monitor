# API Reliability Monitor — SLA Report

> Last updated: **2026-07-29 18:39 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **78.3%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 79.35% | 2223.2 | 10420.1 | 1000ms | 338/1637 |
| ❌ | `public_apis_list` | 0.0% | 99.76% | 125.2 | 4595.4 | 1500ms | 4/1637 |
| ❌ | `ipapi_check` | 69.76% | 99.94% | 150.3 | 4507.0 | 2500ms | 1/1637 |
| ❌ | `nasa_apod` | 77.89% | 54.49% | 2984.2 | 11152.5 | 2000ms | 745/1637 |
| ⚠️ | `dog_ceo_random` | 95.36% | 96.52% | 548.6 | 10244.1 | 2500ms | 57/1637 |
| ⚠️ | `open_meteo_weather` | 98.84% | 97.5% | 704.0 | 14877.1 | 2000ms | 41/1637 |
| ✅ | `rest_countries` | 99.08% | 98.78% | 296.6 | 10221.5 | 2500ms | 20/1637 |
| ✅ | `useless_fact` | 99.69% | 99.69% | 643.2 | 10229.6 | 2500ms | 5/1637 |
| ✅ | `catfact_random` | 99.82% | 99.45% | 257.0 | 10080.2 | 3000ms | 9/1637 |
| ✅ | `coingecko_bitcoin` | 99.82% | 99.94% | 96.1 | 4328.4 | 1500ms | 1/1637 |
| ✅ | `agify_name` | 99.88% | 99.76% | 388.9 | 16112.2 | 2000ms | 4/1637 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.88% | 200.4 | 3882.8 | 2000ms | 2/1637 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `nasa_apod` | 05:00 | 4220.5 | 60.0% |
| `nasa_apod` | 03:00 | 4134.2 | 67.86% |
| `numbers_trivia` | 03:00 | 3800.2 | 35.71% |
| `nasa_apod` | 09:00 | 3766.1 | 49.28% |
| `nasa_apod` | 17:00 | 3560.0 | 48.24% |
| `nasa_apod` | 12:00 | 3377.7 | 52.17% |
| `nasa_apod` | 01:00 | 3309.8 | 47.06% |
| `nasa_apod` | 11:00 | 3309.8 | 48.89% |
| `nasa_apod` | 18:00 | 3147.7 | 45.56% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
