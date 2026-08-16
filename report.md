# API Reliability Monitor — SLA Report

> Last updated: **2026-08-16 02:57 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **77.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 67.15% | 3420.1 | 10420.1 | 1000ms | 653/1988 |
| ❌ | `public_apis_list` | 0.0% | 99.55% | 136.2 | 5075.4 | 1500ms | 9/1988 |
| ❌ | `ipapi_check` | 59.41% | 99.95% | 146.2 | 4507.0 | 2500ms | 1/1988 |
| ❌ | `nasa_apod` | 77.67% | 53.57% | 3034.3 | 11152.5 | 2000ms | 923/1988 |
| ⚠️ | `dog_ceo_random` | 96.18% | 97.08% | 512.4 | 10244.1 | 2500ms | 58/1988 |
| ⚠️ | `open_meteo_weather` | 98.89% | 97.84% | 692.7 | 14877.1 | 2000ms | 43/1988 |
| ✅ | `rest_countries` | 99.25% | 98.94% | 281.5 | 10221.5 | 2500ms | 21/1988 |
| ✅ | `useless_fact` | 99.75% | 99.65% | 650.9 | 10229.6 | 2500ms | 7/1988 |
| ✅ | `catfact_random` | 99.75% | 99.4% | 264.2 | 10080.2 | 3000ms | 12/1988 |
| ✅ | `coingecko_bitcoin` | 99.8% | 99.95% | 96.1 | 4328.4 | 1500ms | 1/1988 |
| ✅ | `agify_name` | 99.9% | 99.75% | 392.1 | 16112.2 | 2000ms | 5/1988 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.9% | 192.4 | 3882.8 | 2000ms | 2/1988 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 5135.5 | 51.28% |
| `numbers_trivia` | 02:00 | 4528.0 | 42.86% |
| `nasa_apod` | 05:00 | 4347.0 | 61.22% |
| `numbers_trivia` | 10:00 | 4323.2 | 41.33% |
| `numbers_trivia` | 14:00 | 4043.7 | 39.33% |
| `nasa_apod` | 02:00 | 3934.2 | 57.14% |
| `nasa_apod` | 03:00 | 3922.3 | 58.97% |
| `numbers_trivia` | 05:00 | 3858.6 | 36.73% |
| `nasa_apod` | 09:00 | 3738.9 | 53.66% |
| `nasa_apod` | 17:00 | 3693.1 | 48.51% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
